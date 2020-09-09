%define _unpackaged_files_terminate_build 1

%define oname aws-xray-sdk
%define modname aws_xray_sdk

Name: python3-module-%oname
Version: 2.6.0
Release: alt1
Summary: AWS X-Ray SDK for the Python programming language
Group: Development/Python3
License: Apache-2.0
URL: https://github.com/aws/aws-xray-sdk-python

BuildArch: noarch

# https://github.com/aws/aws-xray-sdk-python.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(botocore)
BuildRequires: python3(future)
BuildRequires: python3(jsonpickle)
BuildRequires: python3(wrapt)

%add_python3_req_skip aiobotocore.client flask_sqlalchemy.model

%description
The AWS X-Ray SDK for Python (the SDK) enables Python developers
to record and emit information from within their applications
to the AWS X-Ray service.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc *.md *.rst
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version-py*.egg-info

%changelog
* Wed Sep 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Initial build for ALT.
