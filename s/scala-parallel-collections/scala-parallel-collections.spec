%define _unpackaged_files_terminate_build 1

Name: scala-parallel-collections
Version: 1.3.0
Release: alt1

Summary: Parallel collections for Scala 2.13
License: Apache-2.0
Group: Development/Java
URL: https://github.com/scala/scala-parallel-collections
VCS: https://github.com/scala/scala-parallel-collections.git
BuildArch: noarch

Source: %name-%version.tar
Source1: upstream.pom
Source2: build.sh

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: scala
BuildRequires: scala-library
BuildRequires: scala-reflect
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.scalacheck:scalacheck_2.13)

%description
Parallel arrays, ranges, vectors, sets and maps for Scala 2.13.
This standard Scala module provides scala.collection.parallel and
converters between sequential and parallel collections.

%prep
%setup
cp %SOURCE1 pom.xml
cp %SOURCE2 build.sh
%mvn_file : %name/%name

%build
bash build.sh %_jvmdir/java-17-openjdk
%mvn_artifact pom.xml target/%name.jar

%install
%mvn_install

%check
bash build.sh %_jvmdir/java-17-openjdk check

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 1.3.0-alt1
- Initial build for ALT.
