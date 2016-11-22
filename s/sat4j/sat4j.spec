Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# should be consistent across one release
%global build_date 20130405

Name:           sat4j
Version:        2.3.5
Release:        alt1_8jpp8
Summary:        A library of SAT solvers written in Java

License:        EPL or LGPLv2
URL:            http://www.sat4j.org/
# Created by sh sat4j-fetch.sh
Source0:        sat4j-%{version}.tar.xz
Source1:        sat4j-fetch.sh
Patch0:         sat4j-classpath.patch

BuildRequires:  ant
BuildRequires:  javapackages-local

BuildArch:      noarch
Source44: import.info

%description
The aim of the SAT4J library is to provide an efficient library of SAT
solvers in Java. The SAT4J library targets first users of SAT "black
boxes", those willing to embed SAT technologies into their application
without worrying about the details.

%prep
%setup -q -n sat4j-%{version}
%patch0

%build
ant -Dbuild.compiler=modern -Drelease=%{version} \
 -Dtarget=1.5 -DBUILD_DATE=%{build_date} p2 

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -rp dist/%{version}/org.sat4j.core.jar \
 $RPM_BUILD_ROOT%{_javadir}
cp -rp dist/%{version}/org.sat4j.pb.jar \
 $RPM_BUILD_ROOT%{_javadir}

%files
# No %%doc files as the about.html is in the jar
%{_javadir}/org.sat4j*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_1jpp7
- new version

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_4jpp7
- update to new release by jppimport

* Thu Sep 08 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_2jpp6
- update to new release by jppimport

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp6
- new version

* Mon Oct 04 2010 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_2jpp6
- new version; for eclipse 2.5.2

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_1jpp6
- new version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_7jpp6
- rebuild with eclipse 3.4.1

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_7jpp5
- new version

