%define _unpackaged_files_terminate_build 1
%define oname colormath

Name: python3-module-%oname
Version: 2.1.1
Release: alt2

Summary: Python module that abstracts common color math operations
License: GPLv3
Group: Development/Python
Url: http://pypi.python.org/pypi/colormath

BuildArch: noarch

# https://github.com/gtaylor/python-colormath.git
Source0: https://pypi.python.org/packages/f5/f0/1358c821de66e5f3fc107b8a1afbea100a3bbaa0f7024f990b5d1911a055/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
This module implements a large number of different color operations such
as color space conversions, Delta E, and density to spectral.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt PKG-INFO README.rst examples
%python3_sitelibdir/*


%changelog
* Mon Mar 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.1.1-alt2
- Build for python2 disabled.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.2-alt1.git20140701.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.git20140701
- Version 2.0.2

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20130430
- New snapshot

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.8-alt2.git20121128.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20121128
- New snapshot

* Sat May 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2.git20110928
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1.git20110928
- Initial build for Sisyphus

