Name: closure-compiler
Version: 20150218
Release: alt1jpp7
Summary: A JavaScript checker and optimizer
License: ASLv2.0
Group: Development/Java
Url: https://developers.google.com/closure/compiler/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/google/closure-compiler.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-java
BuildPreReq: java-devel-default ant

%description
The Closure Compiler is a tool for making JavaScript download and run
faster. It is a true compiler for JavaScript. Instead of compiling from
a source language to machine code, it compiles from JavaScript to better
JavaScript. It parses your JavaScript, analyzes it, removes dead code
and rewrites and minimizes what's left. It also checks syntax, variable
references, and types, and warns about common JavaScript pitfalls.

%package javadoc
Summary: Javadoc for %name
Group: Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %name.

%prep
%setup

%build
ant jar
ant javadoc

%install
install -d %buildroot%_javadir
install -m644 build/compiler.jar %buildroot%_javadir/closure.jar
install -m644 build/*.zip %buildroot%_javadir/

install -d %buildroot%_javadocdir/%name-%version
cp -fR build/javadoc/* %buildroot%_javadocdir/%name-%version/
ln -s %name-%version %buildroot%_javadocdir/%name

%files
%doc CONTRIBUTORS *.md
%_javadir/*

%files javadoc
%_javadocdir/*

%changelog
* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20150218-alt1jpp7
- Initial build for Sisyphus

