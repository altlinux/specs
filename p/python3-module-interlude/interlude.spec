%define oname interlude

Name: python3-module-%oname
Version: 1.3.1
Release: alt2
Summary: Interlude for Doctests provides an Interactive Console
License: LGPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/interlude/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Provides an interactive shell aka console inside your doctest case.

The console looks exact like in a doctest-case and you can copy and
paste code from the shell into your doctest. It feels as you are in the
test case itself. Its not pdb, it's a python shell.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.1.1-alt2.1
- Rebuild with Python-3.3

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

