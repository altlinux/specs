%define oname resampy

# The 'parallel' target is not currently supported on 32 bit hardware
%ifarch armh
%def_without check
%else
%def_with check
%endif

Name:    python3-module-%oname
Version: 0.3.1
Release: alt1

Summary: Efficient signal resampling.

License: MIT
Group:   Development/Python3
URL:     https://github.com/bmcfee/resampy

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-scipy
BuildRequires: python3-module-numba
%endif

BuildArch: noarch

Source:  %name-%version.tar

Patch: 0001-Support-for-32bit-architectures.patch

%description
%summary

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Jul 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt1
- Build new version.

* Sun Oct 04 2020 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus.
