%define majver 2.9

Name: jatha
License: LGPL v2.1
Group: Development/Java
Summary: Java library that implements a fairly large subset of Common LISP
Version: %majver.0
Release: alt3.cvs20100623_jpp7
Url: http://jatha.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -z3 -d:pserver:anonymous@jatha.cvs.sourceforge.net:/cvsroot/jatha co -P jatha
Source: %name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-java
BuildPreReq: ant

%description
Jatha is a Java library that implements a large subset 
of Common LISP, including most of the datatypes 
(e.g. packages, bignums).  The API allows access to 
LISP from Java.  Jatha is useful as a fast, embedded 
LISP language, as a set of dynamically-typed data types,
or as a standalone LISP.

%package doc
Summary: Documentation for Jatha
Group: Development/Documentation
Requires: %name-javadoc = %version-%release

%description doc
Jatha is a Java library that implements a large subset 
of Common LISP, including most of the datatypes 
(e.g. packages, bignums).  The API allows access to 
LISP from Java.  Jatha is useful as a fast, embedded 
LISP language, as a set of dynamically-typed data types,
or as a standalone LISP.

This package contains documentation for Jatha.

%package javadoc
Summary: Java API documentation for Jatha
Group: Development/Documentation

%description javadoc
Jatha is a Java library that implements a large subset 
of Common LISP, including most of the datatypes 
(e.g. packages, bignums).  The API allows access to 
LISP from Java.  Jatha is useful as a fast, embedded 
LISP language, as a set of dynamically-typed data types,
or as a standalone LISP.

This package contains Java API documentation for Jatha.

%prep
%setup

%build
export LANG=en_US.ISO8859-1
export JATHA_HOME=$PWD
pushd src
%ant
popd
%ant jar
pushd build/lib
mv %name.jar %name-%majver.jar
popd

%install
install -d %buildroot%_javadir
install -m644 build/lib/*.jar %buildroot%_javadir
ln -s %name-%majver.jar %buildroot%_javadir/%name.jar

install -d %buildroot%_javadocdir/%name
mv www/doc/api/* %buildroot%_javadocdir/%name/
rmdir www/doc/api

install -d %buildroot%_docdir/%name
cp -fR www/* %buildroot%_docdir/%name/
ln -s %_javadocdir/%name %buildroot%_docdir/%name/doc/api

%files
%doc README.txt
%_javadir/*.jar

%files doc
%_docdir/%name

%files javadoc
%_javadocdir/%name

%changelog
* Mon Mar 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt3.cvs20100623_jpp7
- Fixed build with java7 (thnx viy@)

* Wed Jun 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt2.cvs20100623_jpp5
- New snapshot

* Tue May 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt1
- Initial build for Sisyphus
