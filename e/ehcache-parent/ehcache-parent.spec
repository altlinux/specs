Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          ehcache-parent
Version:       2.3
Release:       alt2_4jpp7
Summary:       Ehcache Parent
Group:         Development/Java
License:       ASL 2.0
URL:           http://www.terracotta.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/ehcache-parent-2.3
# tar czf ehcache-parent-2.3-src-svn.tar.gz ehcache-parent-2.3
Source0:       ehcache-parent-2.3-src-svn.tar.gz
BuildRequires: jpackage-utils
BuildRequires: maven-compiler-plugin
BuildRequires: maven-gpg-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-pmd-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-surefire-plugin
Requires: jpackage-utils
BuildArch: noarch
Source44: import.info
Provides: ehcache1-parent = %version
Obsoletes: ehcache1-parent < 2.0


%description
Ehcache is a widely used, pure Java, in-process, distributed cache.

%prep

%setup -q -n ehcache-parent-%{version}

%build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_3jpp7
- new version

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt3_2jpp6
- new version

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_2jpp6
- resolved conflict with ehcache1

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_2jpp6
- fixed requires on modello plugin

