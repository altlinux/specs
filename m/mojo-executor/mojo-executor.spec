Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Testing note: this package relies on an old version of mockito.  Compilation
# of the tests fails with the version of mockito currently in Fedora.  Porting
# to the new version is needed.

Name:           mojo-executor
Version:        2.3.1
Release:        alt1_8jpp11
Summary:        Execute other plugins within a maven plugin

License:        ASL 2.0
URL:            http://timmoore.github.io/mojo-executor/
Source0:        https://github.com/TimMoore/%{name}/archive/%{name}-parent-%{version}.tar.gz
# Convert from commons-lang to commons-lang3
# https://pagure.io/java-maint-sig/issue/4
Patch0:         %{name}-commons-lang3.patch
# Remove dependency on ant-contrib, which no longer builds successfully
Patch1:         %{name}-ant-contrib.patch

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
Source44: import.info

%description
The Mojo Executor provides a way to to execute other Mojos (plugins)
within a Maven plugin, allowing you to easily create Maven plugins that
are composed of other plugins.

%package parent
Group: Development/Java
Summary:        Parent POM for mojo-executor

%description parent
%{summary}.

%package maven-plugin
Group: Development/Java
Summary:        Maven plugin for mojo-executor

%description maven-plugin
%{summary}.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{name}-parent-%{version}
%patch0 -p1
%patch1 -p1


# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# We do not need jacoco since we do not run the tests
%pom_remove_plugin :jacoco-maven-plugin

# maven-release is not needed
%pom_remove_plugin :maven-release-plugin

# Modernize the junit dependency
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-no-plugin-version/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-null-maven-project/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-quiet/pom.xml

%build
%mvn_build -s -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-%{name}
%doc --no-dereference LICENSE.txt
%doc README.md

%files parent -f .mfiles-%{name}-parent

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.3.1-alt1_8jpp11
- update

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 2.3.1-alt1_5jpp11
- fixed build

* Thu Nov 12 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_4jpp8
- new version

