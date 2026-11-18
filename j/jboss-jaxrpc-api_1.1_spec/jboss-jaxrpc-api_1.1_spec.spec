%define _unpackaged_files_terminate_build 1

Name: jboss-jaxrpc-api_1.1_spec
Version: 1.0.2
Release: alt1

Summary: Java API for XML-based RPC 1.1
License: GPL-2.0-only WITH Classpath-exception-2.0
Group: Development/Java
URL: https://github.com/jboss/jboss-jaxrpc-api_spec
VCS: https://github.com/jboss/jboss-jaxrpc-api_spec.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-system.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires: mvn(jakarta.xml.soap:jakarta.xml.soap-api:1.4.2)

%description
The complete JBoss implementation of the Java API for XML-based RPC 1.1,
including handlers, encoding, holders, SOAP and servlet endpoint interfaces.

%package javadoc
Summary: API documentation for %name
Group: Development/Documentation

%description javadoc
API documentation for %name.

%prep
%setup
%patch0 -p1
%pom_remove_parent
%pom_remove_plugin :maven-source-plugin
%mvn_file : %name

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
