%def_disable snapshot
%define pypi_name asciimatics
%def_disable check

Name: python3-module-%pypi_name
Version: 1.15.0
Release: alt1

Summary: Python library like curses
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/%pypi_name

%if_disabled snapshot
Source: https://pypi.io/packages/source/a/%pypi_name/%pypi_name-%version.tar.gz
%else
Vcs: https://github.com/peterbrittain/asciimatics.git
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools_scm)
%{?_enable_check:BuildRequires: python3(pytest)...}

%description
Asciimatics is a package to help people create full-screen text UIs
(from interactive forms to ASCII animations) on any platform.

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
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc CHANGES* README*

%changelog
* Wed Dec 13 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- first build for Sisyphus

