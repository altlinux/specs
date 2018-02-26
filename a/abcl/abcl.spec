Name: abcl
Version: 1.1.0
Release: alt1.svn20111205_jpp6.1

Summary: Armed Bear Common Lisp is an implementation of ANSI Common Lisp for JVM
License: GPLv2 with exceptions
Group: Development/Java
Packager: Eugeny A. Rostovtsev (REAL) <real@altlinux.org>

Url: http://common-lisp.net/project/armedbear/
# fragment from .git/config :
#[svn-remote "svn"]
#  url = svn://common-lisp.net/project/armedbear/svn/trunk/abcl
#  fetch = :refs/remotes/git-svn
Source: %name-src-%version.tar.gz

BuildRequires(pre): rpm-build-java jpackage-utils
BuildPreReq: java-devel-default ant dos2unix ant-nodeps
BuildArch: noarch

%description
Armed Bear Common Lisp (ABCL) is an implementation of ANSI Common Lisp that runs
in a Java virtual machine. It provides a runtime system, a compiler that
compiles Lisp source to JVM bytecode, and an interactive REPL for program
development.

ABCL is distributed under the terms of the GNU General Public License, with a
special linking exception. If you link ABCL with your own program, then you do
not need to release the source code for that program. However, any changes that
you make to ABCL itself must be released in accordance with the terms of the
GPL. The license is the same as used by GNU Classpath and J2SE (Java).

ABCL runs on platforms that support Java 1.5 (or later), including Linux,
Windows, and Mac OS X.

ABCL is free software and comes with ABSOLUTELY NO WARRANTY.

%package javadoc
Summary: Javadoc for abcl
Group: Development/Documentation

%description javadoc
Javadoc for abcl.

%prep
%setup -n %name-src-%version

%build
cp customizations.lisp.in customizations.lisp
sed -i 's|/home/peter/sun/jdk1.5.0_16/|%_javadir|' customizations.lisp
sed -i -e 's/\${abcl.version}/%version/g' build.xml
pushd src
javadoc org.armedbear.lisp -d api
popd

%install
%ant -find build.xml %name.wrapper
#dos2unix %name
install -d %buildroot%_bindir
#install -m755 %name %buildroot%_bindir
install -d %buildroot%_javadir/%name
mv dist/%name.jar dist/%name-%version.jar
install -m644 dist/%name-%version.jar %buildroot%_javadir/%name
pushd %buildroot%_javadir
ln -s %name/%name-%version.jar %name.jar
popd

cat <<EOF >%buildroot%_bindir/%name
#!/bin/sh

java -jar %_javadir/%name.jar $1
EOF
chmod +x %buildroot%_bindir/%name

install -d -m755 %buildroot%_javadocdir/%name-%version
cp -pr src/api %buildroot%_javadocdir/%name-%version
ln -s %name-%version %buildroot%_javadocdir/%name

%files
%doc COPYING README
%_javadir/%name.jar
%_javadir/%name
%_bindir/%name

%files javadoc
%doc %_javadocdir/%name-%version
%doc %_javadocdir/%name

%changelog
* Sun Dec 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.svn20111205_jpp6.1
- Version 1.1.0

* Tue Aug 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.27.0-alt1.svn20110816_jpp6.1
- Version 0.27.0

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.25.0-alt1.svn20110507_jpp6
- Version 0.25.0

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1.svn20101111_jpp6
- Version 0.23.0

* Wed Jun 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20.0-alt1.svn20100621_jpp5
- Version 0.20.0

* Sun Mar 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1.svn20090325_jpp5
- version 0.14.0

* Wed Jan 07 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 0.12.0-alt1jpp5
- Initial build for Sisyphus

