%define _unpackaged_files_terminate_build 1

Name: jackson-dataformat-xml
Version: 2.22.1
Release: alt1

Summary: Jackson XML dataformat module
License: Apache-2.0
Group: Development/Java
Url: https://github.com/FasterXML/jackson-dataformat-xml
Vcs: https://github.com/FasterXML/jackson-dataformat-xml.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: jpackage-default

BuildRequires: jackson-bom
BuildRequires: moditect-maven-plugin
BuildRequires: jackson-core
BuildRequires: jackson-annotations
BuildRequires: jackson-databind
BuildRequires: stax2-api
BuildRequires: woodstox-core
BuildRequires: replacer

%description
Data format extension for Jackson to serialize Java objects as XML and
deserialize XML as Java objects.

%javadoc_package

%prep
%setup

%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Tue Aug 11 2026 Evgeniy Serov <scala@altlinux.org> 2.22.1-alt1
- Updated to 2.22.1.
- Enabled javadoc.

* Mon Apr 13 2026 Ivan Khanas <xeno@altlinux.org> 2.20.1-alt1
- First build for ALT.
