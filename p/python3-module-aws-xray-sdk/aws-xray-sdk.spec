%define _unpackaged_files_terminate_build 1

%define oname aws-xray-sdk
%define modname aws_xray_sdk

# TODO: turn on some tests
%def_with check

Name: python3-module-%oname
Version: 2.12.0
Release: alt1
Summary: AWS X-Ray SDK for the Python programming language
Group: Development/Python3
License: Apache-2.0
URL: https://github.com/aws/aws-xray-sdk-python

BuildArch: noarch

# https://github.com/aws/aws-xray-sdk-python.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-wrapt
BuildRequires: python3-module-botocore
BuildRequires: python3-module-coverage
%endif

%add_python3_req_skip aiobotocore.client flask_sqlalchemy.model
%add_python3_self_prov_path  %buildroot%python3_sitelibdir/%modname/ext

%description
The AWS X-Ray SDK for Python (the SDK) enables Python developers
to record and emit information from within their applications
to the AWS X-Ray service.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/ext/flask_sqlalchemy/test_query.py
# https://github.com/aws/aws-xray-sdk-python/issues/359
%tox_check_pyproject

%files
%doc LICENSE *.md *.rst
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version.dist-info

%changelog
* Wed Sep 13 2023 Grigory Ustinov <grenka@altlinux.org> 2.12.0-alt1
- Automatically updated to 2.12.0.

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.8.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Aug 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.0-alt1
- Updated to upstream version 2.8.0.
- Enabled tests.

* Wed Sep 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Initial build for ALT.
