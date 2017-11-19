BuildRequires: javapackages-local jboss-parent maven-compiler-plugin maven-release-plugin
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.0
%global namedreltag .Beta2
%global namedversion %{version}%{?namedreltag}

Name:             jboss-specs-parent
Version:          1.0.0
Release:          alt3_0.14.Beta2jpp8
Summary:          JBoss Specification API Parent POM
Group:            Development/Other
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

%files -f .mfiles

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_0.14.Beta2jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.14.Beta2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.13.Beta2jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.12.Beta2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.7.Beta2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.6.Beta2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_0.5.Beta2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Beta2jpp7
- new release

