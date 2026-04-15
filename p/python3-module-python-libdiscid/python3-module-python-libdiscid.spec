%define pypi_name python-libdiscid

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.3
Release: alt1

Summary: Python bindings for libdiscid
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/python-libdiscid
VCS: https://github.com/sebastinas/python-libdiscid

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-pkgconfig
BuildRequires: libdiscid-devel
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
cd /tmp && py.test-3 --pyargs libdiscid

%files
%doc *.md
%python3_sitelibdir/libdiscid
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 15 2026 Anton Vyatkin <toni@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus.
