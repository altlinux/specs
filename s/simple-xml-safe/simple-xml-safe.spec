%define _unpackaged_files_terminate_build 1

Name: simple-xml-safe
Version: 2.7.1
Release: alt1

Summary: XML serialization library with web-safe defaults
License: Apache-2.0
Group: Development/Java
URL: https://github.com/carrotsearch/simplexml-safe
VCS: https://github.com/carrotsearch/simplexml-safe.git
BuildArch: noarch

Source0: %name-%version.tar.gz
Source1: simple-xml-safe.pom

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core)

%description
Simple XML Safe is a Java framework for XML serialization and deserialization.
It is a maintained fork with deterministic collection ordering and secure
defaults that disable entity expansion and external entity resolution.

%package javadoc
Summary: Javadoc for Simple XML Safe
Group: Development/Java

%description javadoc
API documentation for the Simple XML Safe library.

%prep
%setup -q
cp %SOURCE1 pom.xml

%mvn_file :simple-xml-safe simple-xml-safe

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles-simple-xml-safe
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 2.7.1-alt1
- Initial build for ALT.
