Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 5.0.6
%global namedreltag .CR1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-naming
Version:          5.0.6
Release:          alt2_0.15.CR1jpp8
Summary:          JBoss Naming
License:          LGPLv2+
URL:              http://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/naming/tags/5.0.6.CR1/ jboss-naming-5.0.6.CR1
# tar cafJ jboss-naming-5.0.6.CR1.tar.xz jboss-naming-5.0.6.CR1
Source0:          %{name}-%{namedversion}.tar.xz

Patch0:           %{name}-%{namedversion}-pom.patch

BuildArch:        noarch

BuildRequires:    java-devel
BuildRequires:    jboss-common-core
BuildRequires:    jboss-logging
BuildRequires:    jboss-parent
BuildRequires:    jpackage-utils
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
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.15.CR1jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.14.CR1jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.0.6-alt2_0.13.CR1jpp8
- new jpp release

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

