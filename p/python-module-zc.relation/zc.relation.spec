%define oname zc.relation

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt3.1
Summary: Index intransitive and transitive n-ary relationships
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.relation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc ZODB3 zope.interface

%description
The relation catalog can be used to optimize intransitive and transitive
searches for N-ary relations of finite, preset dimensions.

For example, you can index simple two-way relations, like employee to
supervisor; RDF-style triples of subject-predicate-object; and more
complex relations such as subject-predicate-object with context and
state. These can be searched with variable definitions of transitive
behavior.

The catalog can be used in the ZODB or standalone. It is a generic,
relatively policy-free tool.

It is expected to be used usually as an engine for more specialized and
constrained tools and APIs. Three such tools are zc.relationship
containers, plone.relations containers, and zc.vault. The documents in
the package, including this one, describe other possible uses.

%package -n python3-module-%oname
Summary: Index intransitive and transitive n-ary relationships
Group: Development/Python3
%py3_requires zc ZODB3 zope.interface

%description -n python3-module-%oname
The relation catalog can be used to optimize intransitive and transitive
searches for N-ary relations of finite, preset dimensions.

For example, you can index simple two-way relations, like employee to
supervisor; RDF-style triples of subject-predicate-object; and more
complex relations such as subject-predicate-object with context and
state. These can be searched with variable definitions of transitive
behavior.

The catalog can be used in the ZODB or standalone. It is a generic,
relatively policy-free tool.

It is expected to be used usually as an engine for more specialized and
constrained tools and APIs. Three such tools are zc.relationship
containers, plone.relations containers, and zc.vault. The documents in
the package, including this one, describe other possible uses.

%package -n python3-module-%oname-tests
Summary: Tests for zc.relation
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zc.relationship

%description -n python3-module-%oname-tests
The relation catalog can be used to optimize intransitive and transitive
searches for N-ary relations of finite, preset dimensions.

For example, you can index simple two-way relations, like employee to
supervisor; RDF-style triples of subject-predicate-object; and more
complex relations such as subject-predicate-object with context and
state. These can be searched with variable definitions of transitive
behavior.

The catalog can be used in the ZODB or standalone. It is a generic,
relatively policy-free tool.

It is expected to be used usually as an engine for more specialized and
constrained tools and APIs. Three such tools are zc.relationship
containers, plone.relations containers, and zc.vault. The documents in
the package, including this one, describe other possible uses.

This package contains tests for zc.relation.

%package tests
Summary: Tests for zc.relation
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.relationship

%description tests
The relation catalog can be used to optimize intransitive and transitive
searches for N-ary relations of finite, preset dimensions.

For example, you can index simple two-way relations, like employee to
supervisor; RDF-style triples of subject-predicate-object; and more
complex relations such as subject-predicate-object with context and
state. These can be searched with variable definitions of transitive
behavior.

The catalog can be used in the ZODB or standalone. It is a generic,
relatively policy-free tool.

It is expected to be used usually as an engine for more specialized and
constrained tools and APIs. Three such tools are zc.relationship
containers, plone.relations containers, and zc.vault. The documents in
the package, including this one, describe other possible uses.

This package contains tests for zc.relation.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

