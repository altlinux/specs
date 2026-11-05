%define _unpackaged_files_terminate_build 1

Name: mustache-java
Version: 0.9.14
Release: alt1

Summary: Mustache template engine for Java
License: Apache-2.0 AND MIT
Group: Development/Java
URL: https://github.com/spullara/mustache.java
VCS: https://github.com/spullara/mustache.java.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-plugin-plugin
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-compiler-api)

%description
Mustache.java implements logic-less templates with partials, inheritance,
reflection-based object handling and concurrent evaluation.

%package parent
Summary: Maven parent POMs for Mustache.java
Group: Development/Java

%description parent
Shared upstream Maven metadata for Mustache.java and Scala extensions.

%package maven-plugin
Summary: Maven plugin for Mustache templates
Group: Development/Java

%description maven-plugin
Maven plugin for compiling and rendering templates with Mustache.java.

%package javadoc
Summary: API documentation for Mustache.java
Group: Development/Documentation

%description javadoc
Generated Java API documentation for Mustache.java.

%prep
%setup

# The benchmark reactor is a separate development-only SNAPSHOT project.
%pom_disable_module benchmarks
# The optional Scala ABI needs a compiler unavailable in Sisyphus i586.
%pom_disable_module scala-extensions
%pom_remove_plugin :maven-release-plugin
# The ordinary library has no runtime dependencies to bundle.
%pom_remove_plugin :maven-assembly-plugin compiler

%mvn_package :compiler %name
%mvn_package :mustache.java parent
%mvn_package :mustache-maven-plugin maven-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%files parent -f .mfiles-parent

%files maven-plugin -f .mfiles-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.9.14-alt1
- Initial build for ALT.
