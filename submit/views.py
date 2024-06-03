from pathlib import Path
import subprocess
from sys import path
import uuid
from django.shortcuts import render
from submit.forms import SubmissionForm
from django.conf import settings
# from pathlib import path
# Create your views here.
def submit(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            print(submission.language)
            print(submission.code)
            print(submission.input_data)
            output_data = run_code(submission.language, submission.code, submission.input_data)
            submission.output_data = output_data
            submission.save()
            context = {
                'submission': submission
            }
        return render(request, "result.html", context)
    else:
        form = SubmissionForm()
        context = {
            'form': form,
        }
    return render(request, "index.html", context)

def run_code(language, code, input_data):
    project_path=Path(settings.BASE_DIR)    

    directories= ['codes','inputs', 'outputs']

    for directory in directories:
        directory_path = project_path / directory
        if not directory_path.exists():
            directory_path.mkdir(parents=True, exist_ok=True)
            
    codes_dir = project_path / "codes"
    inputs_dir = project_path / "inputs"
    outputs_dir = project_path / "outputs"

    unique = str(uuid.uuid4())

    code_file_name = f"{unique}.{language}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = inputs_dir / input_file_name
    output_file_path = outputs_dir / output_file_name

    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    with open(input_file_path, "w") as input_file:
        input_file.write(input_data)

    with open(output_file_path, "w") as output_file:
        pass  # This will create an empty file

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    subprocess.run(
                        [str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                    )
    elif language == "py":
        # Code for executing Python script
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    ["python3", str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )

    # Read the output from the output file
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()

    return output_data