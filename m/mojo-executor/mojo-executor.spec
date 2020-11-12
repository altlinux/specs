Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Testing note: this package relies on an old version of mockito.  Compilation
# of the tests fails with the version of mockito currently in Fedora.  Porting
# to the new version is needed.

Name:           mojo-executor
Version:        2.3.1
Release:        alt1_4jpp8
Summary:        Execute other plugins within a maven plugin

License:        ASL 2.0
URL:            https://github.com/TimMoore/%{name}
Source0:        %{url}/archive/%{name}-parent-%{version}.tar.gz
# Convert from commons-lang to commons-lang3
# https://pagure.io/java-maint-sig/issue/4
Patch0:         %{name}-commons-lang3.patch

BuildArch:      noarch
BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
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


# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

# maven-release is not needed
%pom_remove_plugin :maven-release-plugin

# Modernize the junit dependency
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-no-plugin-version/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-null-maven-project/pom.xml
%pom_change_dep :junit-dep :junit mojo-executor-maven-plugin/src/it/mojo-executor-test-project-quiet/pom.xml

# ant-contrib has no POM
%pom_remove_dep ant-contrib: mojo-executor-maven-plugin/src/it/mojo-executor-test-project-with-dependencies/pom.xml
sed -i 's,classpath.*,classpath="%{_javadir}/ant-contrib/ant-contrib.jar" />,' \
  mojo-executor-maven-plugin/src/it/mojo-executor-test-project-with-dependencies/pom.xml

%build
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-%{name}
%doc --no-dereference LICENSE.txt
%doc README.md

%files parent -f .mfiles-%{name}-parent

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 12 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_4jpp8
- new version

