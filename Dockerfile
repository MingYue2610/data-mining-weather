# Use the official AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.8

# Copy the function code and requirements.txt to the container
COPY src ${LAMBDA_TASK_ROOT}/src
COPY requirements.txt ${LAMBDA_TASK_ROOT}/requirements.txt

# Install dependencies using pip
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (filename.handler-function)
CMD ["data_mining_weather.lambda_handler"]