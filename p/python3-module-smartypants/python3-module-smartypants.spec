%def_disable snapshot
%define pypi_name smartypants
%def_enable check


Name: python3-module-%pypi_name
Version: 2.0.2
Release: alt1

Summary: Python with the SmartyPants
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/%pypi_name

Vcs: https://github.com/leohemsted/smartypants.py.git

%if_disabled snapshot
Source: http://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest) python3(docutils) python3(Pygments)}

%description
Python module to translate plain ASCII punctuation characters into
"smart" typographic punctuation HTML entities.

%pypi_name is a Python fork of SmartyPants (http://daringfireball.net/projects/smartypants/)

%prep
%setup -n %pypi_name-%version
%python3_fix_shebang %pypi_name tests/*.py

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test-3

%files
%_bindir/%pypi_name
%python3_sitelibdir_noarch/%pypi_name.py
%python3_sitelibdir_noarch/__pycache__/*
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%doc README*

%changelog
* Tue Jun 17 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Fri Mar 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- first build for Sisyphus (v2.0.1-4-gc46d26c)




