%def_without javadoc

Name:    jnr-a64asm
Version: 1.0.0
Release: alt1
Summary: AArch64 assembler for the Java Native Runtime

License: Apache-2.0
Group:   Development/Java
URL:     https://github.com/jnr/jnr-a64asm
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)

BuildArch: noarch
Requires: java

%description
%summary.

%prep
%setup

%pom_remove_parent
%pom_remove_plugin ":maven-javadoc-plugin"

%pom_xpath_replace "pom:maven.compiler.source" \
"<maven.compiler.source>1.8</maven.compiler.source>"

%pom_xpath_replace "pom:maven.compiler.target" \
"<maven.compiler.target>1.8</maven.compiler.target>"

%build
%mvn_build

%install
%mvn_install
install -Dpm 644 pom.xml %buildroot%_mavenpomdir/JPP-%name.pom

%files -f .mfiles
%doc *.md
%_mavenpomdir/*

%changelog
* Fri Sep 25 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
