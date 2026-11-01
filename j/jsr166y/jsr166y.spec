%define _unpackaged_files_terminate_build 1

Name: jsr166y
Version: 1.7.0
Release: alt1

Summary: JSR-166y Fork/Join concurrency library
License: CC0-1.0
Group: Development/Java
Url: https://gee.cs.oswego.edu/dl/concurrency-interest/index.html
VCS: :pserver:anonymous@gee.cs.oswego.edu/home/jsr166/jsr166
BuildArch: noarch

Source0: %name-%version.orig.tar.gz
Source1: jsr166y-parent.pom
Source2: jsr166y.pom
Source3: extra166y.pom
Source4: CC0-1.0.txt
Source5: jsr166-20151014.orig.tar.gz
Source6: jsr166.pom

BuildRequires(pre): rpm-macros-java
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local

%description
JSR-166y provides a Fork/Join framework for Java. This package contains the
core jsr166y artifact; its extra166y companion is available in a subpackage.

%package extra
Summary: Extra parallel collections built on JSR-166y
Group: Development/Java

%description extra
Extra parallel array and collection classes built on the JSR-166y Fork/Join
framework.

%package main
Summary: JSR-166 concurrency classes for Java Flow APIs
License: CC0-1.0 and LicenseRef-Sun-JSR166
Group: Development/Java

%description main
The JSR-166 main source snapshot with Flow and SubmissionPublisher, published
as io.projectreactor:jsr166 for Java 8 consumers.

%package javadoc
Summary: API documentation for JSR-166y
Group: Documentation

%description javadoc
API documentation for the jsr166y and extra166y libraries.

%prep
%setup -q -n jsr166
cp %SOURCE1 pom.xml
cp %SOURCE4 CC0-1.0.txt
mkdir -p main-source maven-jsr166y maven-extra166y maven-jsr166
%__tar -xf %SOURCE5 -C main-source --strip-components=1
cp %SOURCE2 maven-jsr166y/pom.xml
cp %SOURCE3 maven-extra166y/pom.xml
cp %SOURCE6 maven-jsr166/pom.xml

%build
java8_javac="$(rpm -ql java-1.8.0-openjdk-devel | \
    grep '/java-1.8.0-openjdk-[^/]*/bin/javac$' | head -n 1)"
export JSR166_JAVAC8="$java8_javac"
export JSR166_JAVADOC8="${java8_javac%/*}/javadoc"
test -x "$JSR166_JAVAC8" -a -x "$JSR166_JAVADOC8"
%mvn_build -s -j
mkdir -p target/javadoc
"$JSR166_JAVADOC8" -quiet -Xdoclint:none -source 8 \
    -d target/javadoc -sourcepath src jsr166y extra166y

%install
%mvn_package org.codehaus.jsr166-mirror:jsr166y jsr166y
%mvn_package org.codehaus.jsr166-mirror:extra166y jsr166y-extra
%mvn_package org.codehaus.jsr166-mirror:jsr166y-parent jsr166y
%mvn_package io.projectreactor:jsr166 jsr166y-main
%mvn_install
cat .mfiles-jsr166y-parent >> .mfiles-jsr166y
install -d -m 0755 %buildroot%_javadocdir/jsr166y
cp -a target/javadoc/. %buildroot%_javadocdir/jsr166y/

%files -f .mfiles-jsr166y
%doc CC0-1.0.txt

%files extra -f .mfiles-extra166y
%doc CC0-1.0.txt

%files main -f .mfiles-jsr166
%doc CC0-1.0.txt main-source/src/main/readme

%files javadoc
%_javadocdir/jsr166y
%doc CC0-1.0.txt

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 1.7.0-alt1
- Initial build for ALT.
