Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
%define oldname neethi
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           ws-commons-neethi
Version:        3.0.1
Release:        alt2_4jpp7
Summary:        Web Services Policy framework

Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/neethi/
# svn export https://svn.apache.org/repos/asf/webservices/commons/tags/neethi/neethi-3.0.1/ neethi-3.0.1
# tar cJf neethi-3.0.1.tar.xz neethi-3.0.1
Source0:        %{oldname}-%{version}.tar.xz
Patch0:         %{oldname}-disable-rat.patch
BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: wsdl4j
BuildRequires: ws-commons-axiom
Requires:      jpackage-utils
Requires:      wsdl4j
Requires:      ws-commons-axiom
Source44: import.info
Provides: neethi = %version

%description
Apache Neethi provides general framework for the programmers to
use WS Policy. It is compliant with latest WS Policy specification
which was published in March 2006. This framework is specifically
written to enable the Apache Web services stack to use WS Policy as
a way of expressing it's requirements and capabilities.

%package javadoc
Summary:      API documentation for %{oldname}
Group:        Development/Java
Requires:     jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{oldname}.

%prep
%setup -q -n %{oldname}-%{version}
%patch0 -p1

%build
# skip tests due to requirement for old wstx
mvn-rpmbuild -D maven.test.skip=true install javadoc:javadoc

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{oldname}-%{version}.jar %{buildroot}%{_javadir}/%{oldname}.jar

install -d -m 755 %{buildroot}%{_mavenpomdir}
cp pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{oldname}.pom
%add_maven_depmap JPP-%{oldname}.pom %{oldname}.jar

install -d -m 755 %{buildroot}%{_javadocdir}/%{oldname}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{oldname}

%files
%doc README.txt RELEASE-NOTE.txt
%{_javadir}/%{oldname}.jar
%{_mavenpomdir}/JPP-%{oldname}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{oldname}


%changelog
* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt2_4jpp7
- new release

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt2_2jpp7
- added compat Provides:

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_2jpp7
- new version

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt4_2jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt3_2jpp6
- new jpp relase

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt3_1jpp6
- build with velocity 15

* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_1jpp6
- build with wstx 3.2.8

* Wed Sep 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_1jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt4_4jpp5
- new jpp release

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt4_3jpp5
- fixed build

* Sun Feb 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt3_3jpp5
- fixed build with maven 2.0.7

* Mon Oct 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt3_2jpp5
- fixed build with velocity

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt2_2jpp5
- rebuild with velocity14

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

