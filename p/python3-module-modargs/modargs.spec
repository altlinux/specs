%define modulename modargs

Name: python3-module-%modulename
Version: 1.7
Release: alt3

Summary: Simple command line argument parsing library
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-modargs
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
modargs is a simple command line argument parsing library that infers
arguments from functions in a module.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.7-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.7-alt2.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7-alt2.1
- NMU: Use buildreq for BR.

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt2
- Added module for Python 3

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1
- Version 1.7

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

