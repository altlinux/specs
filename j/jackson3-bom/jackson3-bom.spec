%define _unpackaged_files_terminate_build 1

Name: jackson3-bom
Version: 3.3.0
Release: alt1

Summary: Bill of materials POM for Jackson projects
License: Apache-2.0
Group: Development/Java
URL: https://github.com/FasterXML/jackson-bom
VCS: https://github.com/FasterXML/jackson-bom.git

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml:oss-parent:pom:)
BuildRequires: mvn(org.junit:junit-bom:pom:)

BuildArch: noarch

%description
A bill of materials POM and shared build parent for Jackson dependencies.

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :central-publishing-maven-plugin base
%pom_remove_plugin :maven-enforcer-plugin base

%mvn_file :jackson-bom %name/jackson-bom
%mvn_file :jackson-base %name/jackson-base

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Sat Nov 14 2026 Ivan Khanas <xeno@altlinux.org> 3.3.0-alt1
- Initial build for ALT.
