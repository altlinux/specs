Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname neethi
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           ws-commons-neethi
Version:        3.0.1
Release:        alt2_6jpp7
Summary:        Web Services Policy framework

Group:          Development/Java
License:        ASL 2.0
URL:            http://ws.apache.org/neethi/
Source0:        http://archive.apache.org/dist/ws/neethi/%{version}/neethi-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: wsdl4j
BuildRequires: ws-commons-axiom
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
BuildArch: noarch

%description javadoc
API documentation for %{oldname}.

%prep
%setup -q -n %{oldname}-%{version}

# This check always fails
%pom_remove_plugin org.apache.rat:apache-rat-plugin

%mvn_file : %{oldname}

%build
# skip tests due to requirement for old wstx
%mvn_build -- -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles
%doc NOTICE LICENSE README.txt RELEASE-NOTE.txt

%files javadoc -f .mfiles-javadoc
%doc NOTICE LICENSE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt2_6jpp7
- new release

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

