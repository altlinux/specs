Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           jakarta-annotations
Version:        1.3.5
Release:        alt1_11jpp11
Summary:        Jakarta Annotations
License:        EPL-2.0 or GPLv2 with exceptions
URL:            https://github.com/eclipse-ee4j/common-annotations-api
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/common-annotations-api/archive/%{version}/common-annotations-api-%{version}.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

Provides:       glassfish-annotation-api = %{version}-%{release}
Source44: import.info

%description
Jakarta Annotations defines a collection of annotations representing
common semantic concepts that enable a declarative style of programming
that applies across a variety of Java technologies.

%{?javadoc_package}

%prep
%setup -q -n common-annotations-api-%{version}

# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent

# disable spec submodule: it's not needed, and
# it has missing dependencies (jruby, asciidoctor-maven-plugin, ...)
%pom_disable_module spec

# remove plugins not needed for RPM builds
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :findbugs-maven-plugin api

# Remove use of spec-version-maven-plugin
%pom_remove_plugin :spec-version-maven-plugin api
%pom_xpath_set pom:Bundle-Version '${project.version}' api
%pom_xpath_set pom:Bundle-SymbolicName '${project.artifactId}' api
%pom_xpath_set pom:Extension-Name '${extension.name}' api
%pom_xpath_set pom:Implementation-Version '${project.version}' api
%pom_xpath_set pom:Specification-Version '${spec.version}' api

# provide aliases for the old artifact coordinates
%mvn_alias jakarta.annotation:jakarta.annotation-api \
  javax.annotation:javax.annotation-api \
  javax.annotation:jsr250-api

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%changelog
* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1.3.5-alt1_11jpp11
- update

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1.3.5-alt1_6jpp11
- new version

