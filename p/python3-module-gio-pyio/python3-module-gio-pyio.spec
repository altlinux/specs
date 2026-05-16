%define _name gio-pyio
%define pypi_name gio_pyio

%def_enable check

Name: python3-module-%_name
Version: 0.0.6
Release: alt1

Summary: Python like IO for gio
Group: Development/Python3
License: GPL-3.0-only
Url: https://pypi.org/project/gio-pyio

Vcs: https://github.com/cmkohnen/gio_pyio.git
# no test data in tarball from pypi.io
#Source: https://pypi.io/packages/source/g/%pypi_name/%pypi_name-%version.tar.gz
Source: https://github.com/cmkohnen/gio_pyio/archive/%version/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3(wheel) python3(setuptools_scm)
%{?_enable_check:BuildRequires: python3(pytest) python3(gi)}

%description
This library provides python like IO for Gio. It is intended to bridge
the gap between Gtk apps using GFile for file handling and python
libraries that expect files in the form of file objects
(https://docs.python.org/3/glossary.html#term-file-object).


%prep
%setup -n %_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Sat May 16 2026 Yuri N. Sedunov <aris@altlinux.org> 0.0.6-alt1
- first build for Sisyphus

