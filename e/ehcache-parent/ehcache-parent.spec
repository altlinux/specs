Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          ehcache-parent
Version:       2.3
Release:       alt2_11jpp8
Summary:       Ehcache Parent
License:       ASL 2.0
URL:           http://www.terracotta.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/ehcache-parent-2.3
# tar czf ehcache-parent-2.3-src-svn.tar.gz ehcache-parent-2.3
Source0:       ehcache-parent-2.3-src-svn.tar.gz
BuildRequires: maven-local
BuildArch: noarch
Source44: import.info
Obsoletes: ehcache1-parent < 2.0

%description
Ehcache is a widely used, pure Java, in-process, distributed cache.

%prep
%setup -q -n ehcache-parent-%{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_11jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_5jpp7
- new release

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

