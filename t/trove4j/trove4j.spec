%define _unpackaged_files_terminate_build 1

%define oname trove

Name:    trove4j
Version: 3.0.3
Release: alt1
Summary: High performance collections for java
Group:   Development/Java
License: LGPLv2.1
Url:     http://trove4j.sourceforge.net/

BuildArch: noarch

Source: %name-%version.tar

Source1: trove4j-3.0.3.pom

Patch1: 01_build_target_5_0.patch
Patch2: do-not-copy-junit.jar.patch

BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: java-devel
BuildRequires: ant
BuildRequires: javapackages-local
BuildRequires: maven-local

%description
GNU Trove is a fast, lightweight  implementations of the java.util
Collections API. These implementations are designed to be pluggable
replacements for their JDK equivalents.

Whenever possible, GNU Trove provide the same collections support for
primitive types. This gap in the JDK is often addressed by using the
"wrapper" classes (java.lang.Integer, java.lang.Float, etc.) with
Object-based collections. For most applications, however, collections
which store primitives directly will require less space and yield
significant performance gains.

%prep
%setup
%patch1 -p1
%patch2 -p1

find -name '*.jar' -delete
find -name '*.orig' -delete
rm -rf docs/api

%build
ant -Dversion.number=%version

%install
%mvn_artifact %{SOURCE1} output/lib/%{oname}-%version.jar
%mvn_install -J docs/api/

%files -f .mfiles
%doc AUTHORS.txt CHANGES.txt README*.txt
%doc LICENSE.txt
%dir %{_javadir}/%{name}

%changelog
* Fri Nov 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.3-alt1
- Initial build for ALT.
