AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global eclipse_base %{_libdir}/eclipse
# We want the version to match that shipped in Eclipse's Orbit project
%global qualifier 20100429

Name:           sat4j
Version:        2.3.0
Release:        alt1_2jpp6
Summary:        A library of SAT solvers written in Java

Group:          Development/Java
License:        EPL or LGPLv2
URL:            http://www.sat4j.org/
# Created by sh %{name}-fetch.sh
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-fetch.sh
Patch0:         %{name}-classpath.patch

BuildRequires:  ant
BuildRequires:  ecj
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
The aim of the SAT4J library is to provide an efficient library of SAT
solvers in Java. The SAT4J library targets first users of SAT "black
boxes", those willing to embed SAT technologies into their application
without worrying about the details.

%prep
%setup -q
%patch0

# Only used for the tests
rm lib/commons-cli.jar

%build
ant -Dbuild.compiler=modern -Drelease=%{version} -DBUILD_DATE=%{qualifier} -Dtarget=1.5 p2 

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

