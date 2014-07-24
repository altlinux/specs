%define oname z3c.schema2xml

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt3
Summary: Convert schema-described Zope 3 objects to XML and back
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.schema2xml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires lxml grokcore.component zc.sourcefactory

%description
This package can convert objects described by Zope 3 schema to simple
XML structures. It's also able to convert this XML back into objects.
The export and import processes are completely schema-driven; any
attribute not described in the schema is not seen by this system at all.

This system can be used to create export and import systems for Zope 3
applications. It could also be used to provide XML representations of
objects for other purposes, such as XSLT transformations, or even just
to get a full-text representation for index purposes.

%package -n python3-module-%oname
Summary: Convert schema-described Zope 3 objects to XML and back
Group: Development/Python3
%py3_requires lxml grokcore.component zc.sourcefactory

%description -n python3-module-%oname
This package can convert objects described by Zope 3 schema to simple
XML structures. It's also able to convert this XML back into objects.
The export and import processes are completely schema-driven; any
attribute not described in the schema is not seen by this system at all.

This system can be used to create export and import systems for Zope 3
applications. It could also be used to provide XML representations of
objects for other purposes, such as XSLT transformations, or even just
to get a full-text representation for index purposes.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.schema2xml
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package can convert objects described by Zope 3 schema to simple
XML structures. It's also able to convert this XML back into objects.
The export and import processes are completely schema-driven; any
attribute not described in the schema is not seen by this system at all.

This system can be used to create export and import systems for Zope 3
applications. It could also be used to provide XML representations of
objects for other purposes, such as XSLT transformations, or even just
to get a full-text representation for index purposes.

This package contains tests for z3c.schema2xml.

%package tests
Summary: Tests for z3c.schema2xml
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package can convert objects described by Zope 3 schema to simple
XML structures. It's also able to convert this XML back into objects.
The export and import processes are completely schema-driven; any
attribute not described in the schema is not seen by this system at all.

This system can be used to create export and import systems for Zope 3
applications. It could also be used to provide XML representations of
objects for other purposes, such as XSLT transformations, or even just
to get a full-text representation for index purposes.

This package contains tests for z3c.schema2xml.

%prep
%setup

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
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

