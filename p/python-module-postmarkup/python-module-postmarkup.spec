%define version 1.2.0
%define release alt2
%setup_python_module postmarkup

%def_with python3

Name: %packagename
Version: %version
Release: alt2.1

Summary: Generates XHTML snippets from BBCode

License: BSD
Group: Development/Python
BuildArch: noarch
Url: http://code.google.com/p/postmarkup

Source: %modulename-%version.tar

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Generates XHTML snippets from BBCode.

%package -n python3-module-%modulename
Summary: Generates XHTML snippets from BBCode
Group: Development/Python3

%description -n python3-module-%modulename
Generates XHTML snippets from BBCode.

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Added module for Python 3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt2.1.1
- Rebuild with Python-2.7

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt2.1
- Rebuilt with python 2.6

* Sun Feb 01 2009 Denis Klimov <zver@altlinux.org> 1.1.4-alt2
- more improve using setup_python_module macros
- use optimize and record options for install
- add BuildArch: noarch

* Fri Jan 30 2009 Denis Klimov <zver@altlinux.org> 1.1.4-alt1
- Initial build for ALT Linux

