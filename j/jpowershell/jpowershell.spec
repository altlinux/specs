%define _unpackaged_files_terminate_build 1

Name: jpowershell
Version: 1.0.1
Release: alt1

Summary: Java API for using PowerShell
License: Apache-2.0
Group: Development/Java
URL: https://github.com/pandalxb/jPowerShell
VCS: https://github.com/pandalxb/jPowerShell.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(junit:junit)

%description
jPowerShell provides a Java API for executing PowerShell commands and scripts.

%javadoc_package

%prep
%setup -q
%pom_change_dep junit:junit:4.12 junit:junit:4.13.2

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
