%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname DateTime

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 4.1.1
Release: alt1
Summary: Encapsulation of date/time values
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/DateTime/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/DateTime.git
Source0: https://pypi.python.org/packages/80/67/37467b2725462859366d35bfe30e1e217e6f49ca391ecbe54ae2f09da191/%{oname}-%{version}.zip
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
%endif

%description
This package provides a DateTime data type, as known from Zope 2. Unless
you need to communicate with Zope 2 APIs, you're probably better off
using Python's built-in datetime module.

%if_with python3
%package -n python3-module-%oname
Summary: Encapsulation of date/time values (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This package provides a DateTime data type, as known from Zope 2. Unless
you need to communicate with Zope 2 APIs, you're probably better off
using Python's built-in datetime module.

%package -n python3-module-%oname-tests
Summary: Tests for DateTime (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package provides a DateTime data type, as known from Zope 2. Unless
you need to communicate with Zope 2 APIs, you're probably better off
using Python's built-in datetime module.

This package contains tests for DateTime.
%endif

%package tests
Summary: Tests for DateTime
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides a DateTime data type, as known from Zope 2. Unless
you need to communicate with Zope 2 APIs, you're probably better off
using Python's built-in datetime module.

This package contains tests for DateTime.

%prep
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.0.2-alt1.dev.git20150614.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1:4.0.2-alt1.dev.git20150614.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.2-alt1.dev.git20150614
- New snapshot

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.2-alt1.dev.git20140324
- Version 4.0.2dev

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.1-alt1
- Version 4.0.1

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0-alt1
- Version 4.0

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1:3.0.3-alt1.1
- Rebuild with Python-3.3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.3-alt1
- Version 3.0.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0rel-alt2
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0rel-alt1
- Version 3.0 (release)

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0b3-alt1
- Version 3.0b3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0b1-alt1.1
- Rebuild with Python-2.7

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0b1-alt1
- Initial build for Sisyphus

