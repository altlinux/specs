BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-specs-parent
%define version 1.0.0
%global namedreltag .Beta2
%global namedversion %{version}%{?namedreltag}

Name:             jboss-specs-parent
Version:          1.0.0
Release:          alt2_0.5.Beta2jpp7
Summary:          JBoss Specification API Parent POM
Group:            Development/Java
# The license is not included because it's not a part of this tag. License file
# was pushed to trunk and no new tag will be created for this change.
# http://anonsvn.jboss.org/repos/jbossas/projects/specs/trunk/jboss-specs-parent/LICENSE-2.0.txt
License:          ASL 2.0
Url:              http://www.jboss.org/

# svn export http://anonsvn.jboss.org/repos/jbossas/projects/specs/tags/jboss-specs-parent-1.0.0.Beta2/
# tar czf jboss-specs-parent-1.0.0.Beta2-src-svn.tar.gz jboss-specs-parent-1.0.0.Beta2
Source0:          %{name}-%{namedversion}-src-svn.tar.gz

BuildRequires:    jpackage-utils

Requires:         jboss-parent
Requires:         maven-compiler-plugin
Requires:         maven-release-plugin
Requires:         jpackage-utils
BuildArch:        noarch
Source44: import.info

%description
Parent POM that allows building all specification projects at once.

%prep
%setup -q -n %{name}-%{namedversion}

%build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jboss-%{name}.pom

%add_maven_depmap JPP.jboss-%{name}.pom

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.5.Beta2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Beta2jpp7
- new release

