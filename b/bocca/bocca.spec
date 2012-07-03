%define python_noarch %_libexecdir/python%_python_version/site-packages
Name: bocca
Version: 0.5.7
Release: alt1.1
Summary: Component and Application Generator for CCA
License: LGPL
Group: Development/Tools
Url: http://www.cca-forum.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: python-module-%name = %version-%release

BuildRequires(pre): rpm-build-python rpm-build-java
BuildPreReq: java-devel-default python-devel cca-spec-babel
BuildPreReq: ccaffeine babel cca-tutorial-chasm-examples

%description
Bocca is a command line tool for creating and maintaining CCA components and
applications. Bocca makes creating ports and components as easy giving them a
name. Bocca also provides a scaffolding for building, testing and maintaining
components. While Bocca provides a "best practices" source tree, the resulting
infrastructure uses only standard development tools (e.g. autotools) and is in
no way dependent on Bocca itself. Bocca generates the source tree only, and lets
the user decide when and if they wish to abandon the Bocca way of doing things.
Bocca has enjoyed early success and is now the basis of the CCA tutorial.

%package docs
Summary: Documentation for Bocca
Group: Development/Documentation
BuildArch: noarch

%description docs
Bocca is a command line tool for creating and maintaining CCA components and
applications. Bocca makes creating ports and components as easy giving them a
name. Bocca also provides a scaffolding for building, testing and maintaining
components. While Bocca provides a "best practices" source tree, the resulting
infrastructure uses only standard development tools (e.g. autotools) and is in
no way dependent on Bocca itself. Bocca generates the source tree only, and lets
the user decide when and if they wish to abandon the Bocca way of doing things.
Bocca has enjoyed early success and is now the basis of the CCA tutorial.

This package contains documentation for Bocca.

%package -n python-module-%name
Summary: Python module of Bocca
Group: Development/Python
%py_provides ASE splicers

%description -n python-module-%name
Bocca is a command line tool for creating and maintaining CCA components and
applications. Bocca makes creating ports and components as easy giving them a
name. Bocca also provides a scaffolding for building, testing and maintaining
components. While Bocca provides a "best practices" source tree, the resulting
infrastructure uses only standard development tools (e.g. autotools) and is in
no way dependent on Bocca itself. Bocca generates the source tree only, and lets
the user decide when and if they wish to abandon the Bocca way of doing things.
Bocca has enjoyed early success and is now the basis of the CCA tutorial.

This package contains python module of Bocca.

%prep
%setup

%build
%configure \
	--with-ccafe-config=%_bindir/ccafe-config \
	--with-cca-spec-babel-config=%_bindir/cca-spec-babel-config \
	--with-babel-config=%_bindir/babel-config \
	--with-python=%_bindir/python \
	--with-java=%_libexecdir/jvm/java/bin/java
%make_build checklocal build

# TODO: make check with cca-tutorial,
# inregrate with cca-tutorial-chasm-examples

%install
%make install INSTALL_OPTS='--skip-build --root=%buildroot --optimize=2'

install -d %buildroot%_docdir/%name
cp -fR doc/* %buildroot%_docdir/%name 

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_noarch/* %buildroot%python_sitelibdir/
%endif

%files
%_bindir/*

%files -n python-module-%name
%python_sitelibdir/*

%files docs
%_docdir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.7-alt1.1
- Rebuild with Python-2.7

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt1
- Version 0.5.7

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt2.svn20090721.3
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt2.svn20090721.2
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt2.svn20090721.1
- Rebuilt with python 2.6

* Thu Sep 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt2.svn20090721
- Snapshot 20090721
- Fix path to lsattr
- Rebuilt with cca-spec-babel & fixed babel

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1
- Initial build for Sisyphus

