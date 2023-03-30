%define pypi_name soxr
%ifarch ppc64le
%def_disable check
%else
%def_enable check
%endif

Name: python3-module-%pypi_name
Version: 0.3.3
Release: alt1

Summary: Python-SoXR is a Python wrapper of libsoxr
Group: Development/Python3
License: LGPL-2.1-or-later
Url: https://pypi.org/project/soxr

Vcs: https://github.com/dofuuz/python-soxr.git
Source: https://pypi.io/packages/source/s/%pypi_name/%pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel
BuildRequires: libsoxr-devel libnumpy-py3-devel python3-module-numpy python3-module-Cython
%{?_enable_check:BuildRequires: /proc python3-module-pytest}

%description
This package provides Python 3 wrappers for the SoX Resampler library.

%prep
%setup -n %pypi_name-%version
rm -rf libsoxr

%build
%python3_build --use-system-libsoxr

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%_bindir/py.test3

%files
%python3_sitelibdir/%pypi_name/
#%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/%pypi_name-%version-*.egg-info/
%doc README*

%changelog
* Wed Feb 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- first build for Sisyphus

