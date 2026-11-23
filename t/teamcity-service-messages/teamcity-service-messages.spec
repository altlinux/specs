%define _unpackaged_files_terminate_build 1

Name: teamcity-service-messages
Version: 2024.07
Release: alt1

Summary: JetBrains TeamCity service message protocol library
License: Apache-2.0
Group: Development/Java
URL: https://www.jetbrains.com/teamcity/

Source: %name-%version.tar
Source1: teamcity-service-messages-pom.xml

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)

%description
The TeamCity service message library provides Java classes for parsing and
constructing TeamCity build, test, and progress messages.

%package javadoc
Summary: API documentation for TeamCity service messages
Group: Development/Documentation

%description javadoc
API documentation for the TeamCity service message protocol library.

%prep
%setup -q
cp %SOURCE1 pom.xml
%mvn_file :serviceMessages teamcity/service-messages

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-serviceMessages
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2024.07-alt1
- Initial build for ALT.
