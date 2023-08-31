%def_enable snapshot

%define pypi_name rawkit
%def_enable check

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt3

Summary: CTypes based LibRaw bindings
Group: Development/Python3
License: MIT
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/photoshell/rawkit.git

%if_disabled snapshot
Source: https://pypi.io/packages/source/r/%pypi_name/%pypi_name-%version.tar.gz
%else
Source: %pypi_name-%version.tar
%endif

BuildArch: noarch

Requires: libraw

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(tox) python3(pytest)
BuildRequires: python3(coverage) python3(mock) python3(numpy) python3(flake8)}

%description
rawkit (pronounced `rocket`) is a ctypes-based LibRaw_ binding for Python 3
inspired by the Wand_ API.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
py.test-3 tests
#%%tox_check

%files
%python3_sitelibdir_noarch/libraw/
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%doc README.rst


%changelog
* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt3
- updated to v0.6.0-28-g1e99fc9
- ported to %%pyproject* macros

* Thu Aug 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt2
- python3-only build

* Mon Jul 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus


