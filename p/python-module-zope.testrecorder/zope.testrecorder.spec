%define oname zope.testrecorder
Name: python-module-%oname
Version: 0.4
Release: alt2.1
Summary: Test recorder for functional tests
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.testrecorder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%add_python_req_skip App OFS Products

%py_requires zope

%description
The testrecorder is a browser-based tool to support the rapid
development of functional tests for Web-based systems and applications.
The idea is to "record" tests by exercising whatever is to be tested
within the browser. The test recorder will turn a recorded session into
a functional test.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

