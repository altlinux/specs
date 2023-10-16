%define _unpackaged_files_terminate_build 1
%define oname schedule

Name: python3-module-%oname
Version: 1.2.1
Release: alt1

Summary: Python job scheduling

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/schedule/

# https://github.com/dbader/schedule
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

%description
Python job scheduling for humans. Run Python functions (or any other callable)
periodically using a friendly syntax.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/schedule/__pycache__

%changelog
* Fri Oct 13 2023 Slava Aseev <ptrnine@altlinux.org> 1.2.1-alt1
- Initial build for ALT
