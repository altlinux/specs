%define pypi_name chalice

%def_with check

Name:    python3-module-%pypi_name
Version: 1.31.2
Release: alt1

Summary: Python Serverless Microframework for AWS
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/aws/chalice

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-botocore
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-click
BuildRequires: python3-module-websockets
BuildRequires: python3-module-inquirer
BuildRequires: python3-module-pip
%endif

%add_python3_req_skip app
%add_python3_req_skip aws_cdk
%add_python3_req_skip stacks.chaliceapp
%add_python3_req_skip botocore.vendored
%add_python3_req_skip botocore.vendored.requests
%add_python3_req_skip botocore.vendored.requests.exceptions

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Chalice is a framework for writing serverless apps in python. It allows you to
quickly create and deploy applications that use AWS Lambda.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
# Skip tests requiring Internet access or deal with packaging
%pyproject_run_pytest --ignore=chalice/templates \
    --ignore=docs \
    --ignore=tests/aws/test_features.py \
    --ignore=tests/aws/test_websockets.py \
    --ignore=tests/unit/deploy/test_packager.py \
    --ignore=tests/integration/test_package.py \
    --ignore=tests/functional/test_awsclient.py \
    --deselect=tests/functional/cli/test_cli.py::test_can_generate_pipeline_for_all

%files
%doc *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 1.31.2-alt1
- Initial build for Sisyphus.
