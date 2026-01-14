Name:    sparsebitset
Version: 1.3
Release: alt1
Summary: An efficient sparse bit set implementation for Java

License: Apache-2.0
Group:   Development/Java
URL:     https://github.com/brettwooldridge/SparseBitSet
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)

BuildArch: noarch
Requires: java

%description
%summary

%prep
%setup
%pom_remove_parent
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -j -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Mon Jan 12 2026 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Initial build for Sisyphus.
