%define _unpackaged_files_terminate_build 1

Name: checkt
Version: 0.1.0
Release: alt1

Summary: Compile-time checked type tokens and containers
License: Apache-2.0
Group: Development/Java
URL: https://github.com/veithen/checkt
VCS: https://github.com/veithen/checkt.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: LICENSE

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(com.google.auto.service:auto-service)
BuildRequires: mvn(com.google.auto.service:auto-service-annotations)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)

%description
Annotations and an annotation processor generate checked casts and typed
containers for Java type-token APIs.

%javadoc_package

%prep
%setup
cp %SOURCE1 LICENSE
# The unavailable parent supplies build conventions, not production code.
%pom_remove_parent
%pom_remove_plugin org.codehaus.mojo:license-maven-plugin
%mvn_package :test __noinstall
%mvn_package :* %name

%build
%mvn_build -s -- -Dmaven.compiler.source=8 -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 0.1.0-alt1
- Initial build for ALT.
