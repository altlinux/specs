%define pypi_name chalice

%def_with check

Name:    python3-module-%pypi_name
Version: 1.32.0
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
BuildRequires: python3-module-yaml
BuildRequires: python3-module-six
BuildRequires: python3-module-jmespath
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
    --deselect=tests/functional/cli/test_cli.py::test_can_generate_pipeline_for_all \
    --deselect=tests/functional/test_deployer.py::test_no_error_message_printed_on_empty_reqs_file

%files
%doc *.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 30 2025 Alexander Burmatov <thatman@altlinux.org> 1.32.0-alt1
- New 1.32.0 version.

* Fri Aug 01 2025 Alexandr Shashkin <dutyrok@altlinux.org> 1.31.2-alt2
- Built with Hypothesis supplied without numerous redundant dependencies.

* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 1.31.2-alt1
- Initial build for Sisyphus.
