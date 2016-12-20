Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name wildfly-common
%define version 1.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:          wildfly-common
Version:       1.1.0
Release:       alt1_2jpp8
Summary:       WildFly common utilities project
License:       ASL 2.0
URL:           http://wildfly.org/
Source0:       https://github.com/wildfly/wildfly-common/archive/%{namedversion}.tar.gz

BuildRequires: graphviz libgraphviz
BuildRequires: maven-local
BuildRequires: mvn(com.intellij:annotations)
BuildRequires: mvn(jdepend:jdepend)
# jboss-parent:16
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
# jboss-logging-{annotations,processor}:1.2.0.Final
BuildRequires: mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)

BuildArch:     noarch
Source44: import.info

%description
The WildFly Common project is a repository of shared utilities
which do not have a more specific categorization.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Build fails
# [ERROR] An error has occurred in JavaDocs report generation
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:configuration" '
<sourceFileExcludes>
  <exclude>**/CommonMessages_*.java</exclude>
  <exclude>**/Log_*.java</exclude>
</sourceFileExcludes>'

%mvn_file org.wildfly.common:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp8
- new version

