Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-naming
%define version 5.0.6
%global namedreltag .CR1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-naming
Version:          5.0.6
Release:          alt2_0.12.CR1jpp8
Summary:          JBoss Naming
License:          LGPLv2+
URL:              http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/naming/tags/5.0.6.CR1/ jboss-naming-5.0.6.CR1
# tar cafJ jboss-naming-5.0.6.CR1.tar.xz jboss-naming-5.0.6.CR1
Source0:          %{name}-%{namedversion}.tar.xz

Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    jboss-common-core
BuildRequires:    jboss-logging
BuildRequires:    jboss-parent
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
BuildRequires:    maven-antrun-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    rmic-maven-plugin
Source44: import.info

%description
The JBoss JNDI name server implementation

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

%mvn_file ':jnp-{client,server}' %{name}-@1

%build
# No jboss-test and jboss-kernel packages
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc JBossORG-EULA.txt

%files javadoc -f .mfiles-javadoc
%doc JBossORG-EULA.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.12.CR1jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.11.CR1jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.6.CR1jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.4.CR1jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt1_0.4.CR1jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt1_3jpp6
- new version

