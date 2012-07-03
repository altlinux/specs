%define oname zc.relation
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Index intransitive and transitive n-ary relationships
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.relation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

