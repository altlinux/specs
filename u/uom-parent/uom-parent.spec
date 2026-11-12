%define _unpackaged_files_terminate_build 1

Name: uom-parent
Version: 2.2.5
Release: alt1

Summary: Parent POM for Units of Measurement projects
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/unitsofmeasurement/uom-parent
VCS: https://github.com/unitsofmeasurement/uom-parent.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: javapackages-local
BuildRequires: java-17-openjdk-devel

%description
The original parent POM shared by Units of Measurement Java projects.

%prep
%setup
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin

%install
%mvn_artifact pom.xml
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 2.2.5-alt1
- New version.

* Tue Oct 08 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp8
- new version

