%define _unpackaged_files_terminate_build 1

Name: felix-resolver
Version: 2.0.4
Release: alt1

Summary: Apache Felix OSGi Resolver
License: Apache-2.0
Group: Development/Java
URL: https://felix.apache.org/
VCS: https://github.com/apache/felix-dev.git

Source0: org.apache.felix.resolver-%version-source-release.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:felix-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.osgi:osgi.annotation)
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires: mvn(org.mockito:mockito-core)

%description
The Apache Felix Resolver implements the OSGi resolver service.

%package javadoc
Summary: Javadoc for %name
Group: Development/Java

%description javadoc
Javadoc for the Apache Felix Resolver API.

%prep
%setup -q -n org.apache.felix.resolver-%version
%pom_change_dep org.mockito:mockito-all org.mockito:mockito-core
%pom_remove_plugin org.apache.rat:apache-rat-plugin

%build
%mvn_build -- -Dfelix.java.version=11

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 2.0.4-alt1
- Initial build for ALT.
