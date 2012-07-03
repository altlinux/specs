%define oname z3c.amf
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: Zope support for Flash messages (AMF)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.amf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%add_python_req_skip Globals Products ZPublisher pyamf

%description
This package allows you to query Zope 2 from a flash using Flex with
Actionscript 2 or Actionscript 3 throught AMF0 or AMF3.

We are just providing here the Zope layer. The lower layer has been done
using the PyAMF package (see http://pyamf.org).

%package tests
Summary: Tests for Zope support for Flash messages (AMF)
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package allows you to query Zope 2 from a flash using Flex with
Actionscript 2 or Actionscript 3 throught AMF0 or AMF3.

We are just providing here the Zope layer. The lower layer has been done
using the PyAMF package (see http://pyamf.org).

This package contains tests for Zope support for Flash messages (AMF).

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jul 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

