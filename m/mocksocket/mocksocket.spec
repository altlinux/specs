%define _unpackaged_files_terminate_build 1

Name: mocksocket
Version: 1.2
Release: alt1

Summary: Privileged socket wrappers for Java tests
License: Apache-2.0
Group: Development/Java
URL: https://github.com/elastic/mocksocket
VCS: https://github.com/elastic/mocksocket.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-11-openjdk-devel
BuildRequires: maven-local

%description
MockSocket provides socket, server socket, HTTP server and socket channel
wrappers for code running with Java security restrictions.

%prep
%setup
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin

%build
%mvn_build -s -j

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 1.2-alt1
- Initial build for ALT.
