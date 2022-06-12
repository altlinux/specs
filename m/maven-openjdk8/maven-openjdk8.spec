BuildRequires(pre): rpm-macros-java
%define shortver 8
%define jdkver 1.8.0
Name: maven-openjdk%{shortver}
Version: 0.01
Summary: openjdk%{shortver} binding for Maven
License: X-ALT-PublicDomain
Packager: Igor Vlasenko <viy@altlinux.org>
Group: Development/Java
Release: alt1
BuildArch: noarch

Provides: maven-jdk-binding = %EVR
Requires: maven
Requires: java-%{jdkver}-openjdk-devel
Conflicts: maven-jdk-binding

%description
Maven is a software project management and comprehension tool. Based on the
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

This package configures Maven to run with OpenJDK %{shortver}.

%prep

%build

%install
mkdir -p %buildroot%_javaconfdir/
echo JAVA_HOME=%_jvmlibdir/java-%{jdkver}-openjdk >%buildroot%_javaconfdir/maven.conf

%files
%_javaconfdir/maven.conf

%changelog
* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 0.01-alt1
- first build
