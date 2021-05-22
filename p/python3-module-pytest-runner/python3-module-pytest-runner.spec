%def_with python3

%define oname pytest-runner

Name: python3-module-%oname
Version: 5.3.1
Release: alt1

Summary: Setup scripts can use pytest-runner to add setup.py test support for pytest runner
License: ISC
Group: Development/Python3

URL: https://pypi.python.org/pypi/pytest-runner

# setuptools-scm requires a pypi tarball and doesn't like github tarball
# Source-url: https://files.pythonhosted.org/packages/source/p/%oname/%oname-%version.tar.gz
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools python3-module-setuptools_scm
BuildRequires: python3-module-pytest

#py3_provides ptr

%description
Setup scripts can use pytest-runner to add setup.py test support for pytest
runner.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%python3_sitelibdir/*

%changelog
* Sat May 22 2021 Anton Midyukov <antohami@altlinux.org> 5.3.1-alt1
- new version (5.3.1) with rpmgs script

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.9-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 2.9-alt1
- New version 2.9
- srpm build

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 2.6.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt at altlinux.ru> 2.6.1-alt2
- remove hgtools from buildreq

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1
- Version 2.6.1

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus

