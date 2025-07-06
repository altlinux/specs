%define pypi_name pyerfa

Name:    python3-module-%pypi_name
Version: 2.0.1.5
Release: alt1

Summary: Python bindings for ERFA routines

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/pyerfa
VCS:     https://github.com/liberfa/pyerfa

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-numpy
BuildRequires: libnumpy-py3-devel
BuildRequires: liberfa-devel

Source: %name-%version.tar
Source1: %name-%version-liberfa-erfa.tar

%description
PyERFA is the Python wrapper for the ERFA library
(Essential Routines for Fundamental Astronomy), a C library containing
key algorithms for astronomy, which is based on the SOFA library published
by the International Astronomical Union (IAU). All C routines are wrapped
as Numpy universal functions, so that they can be called with scalar
or array inputs.

The project is a split of astropy._erfa module, developed in the context
of Astropy project, into a standalone package. It contains the ERFA C source code
as a git submodule. The wrapping is done with help of the Jinja2 template engine.

%prep
%setup -a1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PYERFA_USE_SYSTEM_LIBERFA=1
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/erfa
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jul 06 2025 Grigory Ustinov <grenka@altlinux.org> 2.0.1.5-alt1
- Initial build for Sisyphus.
