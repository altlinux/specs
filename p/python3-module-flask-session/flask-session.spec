%define _unpackaged_files_terminate_build 1
%define oname flask-session

Name: python3-module-%oname
Version: 0.4.0
Release: alt1

Summary: Server side session extension for Flask

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/Flask-Session/

# https://github.com/fengsp/flask-session
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

%description
Flask-Session is an extension for Flask that adds support for Server-side
Session to your application.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/flask_session/__pycache__

%changelog
* Wed Apr 19 2023 Slava Aseev <ptrnine@altlinux.org> 0.4.0-alt1
- Initial build for ALT

