%define _unpackaged_files_terminate_build 1

%define oname setuptools_cython

Name: python3-module-%oname
Version: 0.2.1
Release: alt3
Summary: Cython setuptools integration
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/setuptools_cython/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython

%py3_provides %oname
%py3_requires setuptools Cython

%description
Allows compiling Cython extensions in setuptools by putting
setuptools_cython in your setup_requires.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*

%changelog
* Wed May 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.1-alt3
- Drop python2 support.

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.1-alt2
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

