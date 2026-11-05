%define _unpackaged_files_terminate_build 1

Name: software-and-algorithms
Version: 1.0.0
Release: alt2

Summary: Neat algorithm implementations in Java
License: MIT
Group: Development/Java
URL: https://github.com/KevinStern/software-and-algorithms
VCS: https://github.com/KevinStern/software-and-algorithms.git

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: junit
BuildRequires: maven-source-plugin

%description
%summary.

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -j -- \
  -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt2
- Restore the published Maven Central 1.0 source snapshot.

* Mon Nov 24 2025 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt1
- Fist build for ALT.
