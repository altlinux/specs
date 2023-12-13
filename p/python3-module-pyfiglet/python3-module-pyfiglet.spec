%def_disable snapshot
%define pypi_name pyfiglet
%def_disable check

Name: python3-module-%pypi_name
Version: 1.0.2
Release: alt1

Summary: Python port of FIGlet
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/%pypi_name

%if_disabled snapshot
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/peterbrittain/asciimatics.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest)...}

%description
pyfiglet is a full port of FIGlet (http://www.figlet.org/) into pure
python. It takes ASCII text and renders it in ASCII art fonts.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Wed Dec 13 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- first build for Sisyphus

