%define _unpackaged_files_terminate_build 1

Name: openjdk-asmtools
Version: 9.1
Release: alt1

Summary: To develop tools create proper & improper Java '.class' files
License: GPLv2+
Group: Development/Java
Url: https://github.com/openjdk/asmtools
Vcs: https://github.com/openjdk/asmtools

BuildArch: noarch

Source0: %name-%version.tar
Source1: openjdk-asmtools.in
Source2: openjdk-asmtools.1

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: java-17-openjdk-devel

%description
AsmTools helps develop tools to create proper and improper
Java '.class' files. Aids various Java .class based testing
and OpenJDK development applications. Asmtools supports latest class
file formats, in lock-step with JDK development. AsmTools consist of
a set of (Java class file) assembler/dis-assemblers:

Jasm/Jdis:
An assembler language to provide Java-like declaration of member
signatures, providing Java VM specification compliant mnemonics for
byte-code instructions.

JCod/JDec:
An assembler language to provide byte-code containers of class-file
constructs.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for the %name.

%prep
%setup
sed -i '1s|#!.*|#!/bin/sh|' %SOURCE1

%build
cd maven
sed -i "s|ln -sv|cp -r|g" mvngen.sh
sh mvngen.sh
%mvn_build -- -Dmaven.compiler.source=17 -Dmaven.compiler.target=17 -Dmaven.compiler.release=17

%install
cd maven
%mvn_install
cd ..

install -d -m 755 %buildroot%_bindir
install -d -m 755 %buildroot%_mandir/man1

for launcher in "" "-jasm" "-jdis" "-jcoder" "-jdec" "-jcdec"; do
    switch=$(echo $launcher | sed "s/-//")
    sed "s/@SCD@/$switch/" %SOURCE1 > %buildroot%_bindir/%name$launcher
    chmod 755 %buildroot%_bindir/%name$launcher
done

install -m 644 %SOURCE2 %buildroot%_mandir/man1/

%files -f maven/.mfiles
%doc README.md
%doc --no-dereference LICENSE
%_bindir/*
%_mandir/man1/openjdk-asmtools.1*

%files javadoc -f maven/.mfiles-javadoc

%changelog
* Wed Aug 06 2026 Timofei Fedotov <sovtouch@altlinux.org> 9.1-alt1
- Updated to 9.1.
- Removed Java 8 cross-compilation flags.

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 7.0.b10-alt1_0.1.20210122.git7eadbbfjpp11
- new version
