%define pypi_name js2py

Name: python3-module-%pypi_name
Version: 0.74.1
Release: alt1

Summary: Translates JavaScript to Python code
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/Js2Py-3.13

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Translates JavaScript to Python code. Js2Py is able to translate and
execute virtually any JavaScript code.

Js2Py is written in pure python and does not have any dependencies.
Basically an implementation of JavaScript core in pure python.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Mon Jun 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.74.1-alt1
- Initial build for ALT Linux.

