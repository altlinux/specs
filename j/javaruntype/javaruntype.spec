%define _unpackaged_files_terminate_build 1

%def_with check

Name: javaruntype
Version: 2.0.0
Release: alt1

Summary: A runtime representation of the Java type system
License: Apache-2.0
Group: Development/Java
Url: https://github.com/arxila/javaruntype
Vcs: https://github.com/arxila/javaruntype

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(io.arxila.atomichash:atomichash)
BuildRequires: mvn(org.antlr:antlr-runtime)
%if_with check
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
%endif

%description
javaRuntype is a compact library offering a runtime objectual
representation of the Java type system. It provides a way to work
with generic types at runtime, including parameterized types,
wildcard types, type variables and arrays.

%package javadoc
Summary: API documentation for javaruntype
Group: Development/Java

%description javadoc
API documentation for the javaruntype library.

%prep
%setup
# Remove parent POM (oss.sonatype requires network)
%pom_remove_parent

# Set Java 17 compiler - required for sealed classes and pattern matching
%pom_xpath_inject "pom:properties" "<maven.compiler.source>17</maven.compiler.source><maven.compiler.target>17</maven.compiler.target><maven.compiler.release>17</maven.compiler.release>"

# Replace junit-jupiter managed by parent BOM with explicit version
%pom_change_dep org.junit.jupiter:junit-jupiter: org.junit.jupiter:junit-jupiter:5.10.2:test

# Fix atomichash version (was managed by parent)
%pom_change_dep io.arxila.atomichash:atomichash: io.arxila.atomichash:atomichash:1.0.1

# Fix antlr-runtime version (was managed by parent)
%pom_change_dep org.antlr:antlr-runtime: org.antlr:antlr-runtime:3.5.3

%build
%mvn_build %{?_without_check:-f}

%install
%mvn_install

%check
%mvn_build -s

%files -f .mfiles
%doc README.md LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jun 11 2026 Timofei Fedotov <sovtouch@altlinux.org> 2.0.0-alt1
- Initial build for ALT Sisyphus.
