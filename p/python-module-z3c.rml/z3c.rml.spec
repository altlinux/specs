%define oname z3c.rml

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.8.1
Release: alt1.dev0.git20150202.1.1
Summary: An alternative implementation of RML
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.rml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/z3c.rml.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Pygments python-module-lxml
#BuildPreReq: python-module-PyPDF2 python-module-Reportlab
#BuildPreReq: python-module-svg2rlg python-module-zope.interface
#BuildPreReq: python-module-zope.schema python-module-zope.pagetemplate
#BuildPreReq: python-module-Pillow python-module-coverage
#BuildPreReq: python-module-zope.testrunner
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Pygments python3-module-lxml
#BuildPreReq: python3-module-PyPDF2 python3-module-Reportlab
#BuildPreReq: python3-module-zope.interface
#BuildPreReq: python3-module-zope.schema python3-module-zope.pagetemplate
#BuildPreReq: python3-module-Pillow python3-module-coverage
#BuildPreReq: python3-module-zope.testrunner
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires z3c lxml pyPdf reportlab zope.interface zope.schema
%py_requires zope.pagetemplate

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-Reportlab python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-mimeparse python-module-numpy python-module-pbr python-module-persistent python-module-pyasn1 python-module-pytz python-module-serial python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-transaction python-module-twisted-core python-module-unittest2 python-module-zope.browser python-module-zope.component python-module-zope.configuration python-module-zope.contenttype python-module-zope.event python-module-zope.exceptions python-module-zope.hookable python-module-zope.i18n python-module-zope.i18nmessageid python-module-zope.interface python-module-zope.location python-module-zope.proxy python-module-zope.publisher python-module-zope.schema python-module-zope.security python-module-zope.tal python-module-zope.tales python-module-zope.testing python-module-zope.traversing python-module-zope.untrustedpython python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-Reportlab python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-genshi python3-module-jinja2 python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-transaction python3-module-unittest2 python3-module-zope python3-module-zope.browser python3-module-zope.component python3-module-zope.configuration python3-module-zope.contenttype python3-module-zope.event python3-module-zope.exceptions python3-module-zope.i18n python3-module-zope.i18nmessageid python3-module-zope.interface python3-module-zope.location python3-module-zope.proxy python3-module-zope.publisher python3-module-zope.schema python3-module-zope.security python3-module-zope.tal python3-module-zope.tales python3-module-zope.testing python3-module-zope.traversing
BuildRequires: python-module-PyPDF2 python-module-coverage python-module-docutils python-module-html5lib python-module-pytest python-module-svg2rlg python-module-zope.pagetemplate python-module-zope.testrunner python3-module-PyPDF2 python3-module-coverage python3-module-html5lib python3-module-pytest python3-module-sphinx python3-module-zope.pagetemplate python3-module-zope.testrunner rpm-build-python3 time

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.1-alt1.dev0.git20150202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.8.1-alt1.dev0.git20150202.1
- NMU: Use buildreq for BR.

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

