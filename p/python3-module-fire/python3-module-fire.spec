%def_enable snapshot

%define pypi_name fire

%def_enable check

Name: python3-module-%pypi_name
Version: 0.7.0
Release: alt1

Summary: A Python library for automatically generating command line interfaces
Group: Development/Python3
License: Apache-2.0
Url: https://pypi.python.org/pypi/%name

Vcs: https://github.com/google/python-fire.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/f/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest) python3(hypothesis) python3(mock)
BuildRequires: python3(termcolor) python3(Levenshtein)}

%description
Python Fire is a library for automatically generating command line
interfaces (CLIs) with a single line of code.

It will turn any Python module, class, object, function, etc. (any
Python component will work!) into a CLI. It's called Fire because when
you call Fire(), it fires off your command.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir_noarch
%__python3 -m unittest

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Wed Feb 12 2025 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- v0.7.0-7-g6cf45c6

* Wed Jan 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus (v0.5.0-12-gffb8121)



