%define oname z3c.rml

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.8.1
Release: alt1.dev0.git20150202
Summary: An alternative implementation of RML
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.rml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/z3c.rml.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Pygments python-module-lxml
BuildPreReq: python-module-PyPDF2 python-module-Reportlab
BuildPreReq: python-module-svg2rlg python-module-zope.interface
BuildPreReq: python-module-zope.schema python-module-zope.pagetemplate
BuildPreReq: python-module-Pillow python-module-coverage
BuildPreReq: python-module-zope.testrunner
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Pygments python3-module-lxml
BuildPreReq: python3-module-PyPDF2 python3-module-Reportlab
BuildPreReq: python3-module-zope.interface
BuildPreReq: python3-module-zope.schema python3-module-zope.pagetemplate
BuildPreReq: python3-module-Pillow python3-module-coverage
BuildPreReq: python3-module-zope.testrunner
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires z3c lxml pyPdf reportlab zope.interface zope.schema
%py_requires zope.pagetemplate

%description
This is an alternative implementation of ReportLab's RML PDF generation
XML format. Like the original implementation, it is based on ReportLab's
reportlab library.

You can read all about z3c.rml and see many examples on how to use it,
see the "RML Reference":
http://svn.zope.org/z3c.rml/trunk/src/z3c/rml/rml-reference.pdf?view=auto

%package -n python3-module-%oname
Summary: An alternative implementation of RML
Group: Development/Python3
%py3_provides %oname
%py3_requires z3c lxml pyPdf reportlab zope.interface zope.schema
%py3_requires zope.pagetemplate

%description -n python3-module-%oname
This is an alternative implementation of ReportLab's RML PDF generation
XML format. Like the original implementation, it is based on ReportLab's
reportlab library.

You can read all about z3c.rml and see many examples on how to use it,
see the "RML Reference":
http://svn.zope.org/z3c.rml/trunk/src/z3c/rml/rml-reference.pdf?view=auto

%package -n python3-module-%oname-tests
Summary: Tests for alternative implementation of RML
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.pagetemplate zope.testing

%description -n python3-module-%oname-tests
This is an alternative implementation of ReportLab's RML PDF generation
XML format. Like the original implementation, it is based on ReportLab's
reportlab library.

You can read all about z3c.rml and see many examples on how to use it,
see the "RML Reference":
http://svn.zope.org/z3c.rml/trunk/src/z3c/rml/rml-reference.pdf?view=auto

This package contains tests for alternative implementation of RML.

%package tests
Summary: Tests for alternative implementation of RML
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.pagetemplate zope.testing

%description tests
This is an alternative implementation of ReportLab's RML PDF generation
XML format. Like the original implementation, it is based on ReportLab's
reportlab library.

You can read all about z3c.rml and see many examples on how to use it,
see the "RML Reference":
http://svn.zope.org/z3c.rml/trunk/src/z3c/rml/rml-reference.pdf?view=auto

This package contains tests for alternative implementation of RML.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt1.dev0.git20150202
- Version 2.8.1.dev0

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.3-alt1.dev0.git20141028
- Version 2.7.3.dev0

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1
- Version 2.5.0
- Added module for Python 3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus

