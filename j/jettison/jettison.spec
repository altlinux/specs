%define _unpackaged_files_terminate_build 1
%def_with check

Name: jettison
Version: 1.5.4
Release: alt1

Summary: A StAX implementation for JSON
Group: Development/Java
License: Apache-2.0
Url: https://github.com/jettison-json/jettison
Vcs: https://github.com/jettison-json/jettison
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-deploy-plugin
BuildRequires: maven-source-plugin
%if_with check
BuildRequires: woodstox-core
BuildRequires: junit
%endif

%description
Jettison is a Java library for converting XML to JSON and vice-versa with
the help of StAX. It implements  XMLStreamWriter and XMLStreamReader and
supports Mapped and BadgerFish conventions. For example, with a Mapped
convention, JAXB processes JAXB beans and emits XMLStreamWriter events
which are processed by Jettison with the XML data being converted to JSON.
Likewise, when it reads JSON, it reports XMLStreamReader events for JAXB
to populate JAXB beans.

%{?javadoc_package}

%prep
%setup
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%if_with check
%mvn_build
%else
%mvn_build -f
%endif

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Mar 24 2026 Arseniy Kostevich <faux@altlinux.org> 1.5.4-alt1
- Initial build for ALT.
