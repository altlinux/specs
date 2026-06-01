%define pypi_name cloudscraper

Name: python3-module-%pypi_name
Version: 3.0.0
Release: alt1

Summary: A Python module to bypass Cloudflare's anti-bot page
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/cloudscraper
Vcs: https://github.com/venomous/cloudscraper

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup
#switch js2py to js2py-3.13
sed -i 's/js2py/js2py_/g' setup.py
sed -i 's/js2py/js2py_/g' pyproject.toml
sed -i 's/js2py/js2py_/g' requirements.txt
sed -i 's/js2py/js2py_/g' cloudscraper/__init__.py
sed -i 's/js2py/js2py_/g' cloudscraper/interpreters/js2py.py
sed -i 's/js2py/js2py_/g' cloudscraper/interpreters/js2py_interpreter.py

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 01 2026 Aleksandr Shamaraev <shad@altlinux.org> 3.0.0-alt1
- Initial build for ALT Linux.

