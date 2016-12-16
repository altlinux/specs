Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat

%global base_name    net
%global short_name   commons-%{base_name}

Name:           apache-%{short_name}
Version:        3.5
Release:        alt1_1jpp8
Summary:        Internet protocol suite Java library
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
Source44: import.info


%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

%package javadoc
Group: Development/Java
Summary:    API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

# This test fails with "Connection timed out"
rm src/test/java/org/apache/commons/net/time/TimeTCPClientTest.java
# Fails in Koji with "Address already in use"
rm src/test/java/org/apache/commons/net/tftp/TFTPServerPathTest.java

%mvn_file  : %{short_name} %{name}
%mvn_alias : org.apache.commons:%{short_name}

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_3jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_6jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_1jpp7
- rebuild with maven-local

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_1jpp7
- fc update

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_2jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt9_6jpp6
- build without clirr plugin

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt8_6jpp6
- fixed build with maven3

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt7_6jpp6
- added compat osgi provides

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt6_6jpp6
- rebuild with new osgi.prov

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt5_6jpp6
- added osgi manifest

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_6jpp6
- added osgi provides

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_6jpp6
- renamed to apache-commons-net

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_2jpp6
- really added OSGi provides

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_2jpp6
- added OSGi provides

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_2jpp6
- new version

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_4jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_4jpp5
- converted from JPackage by jppimport script

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_3jpp1.7
- rebuilt with maven1

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Tue Jun 07 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0-alt1
- New upstream release

* Thu Dec 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.0-alt1
- New upstream release
- Use rpm-build-java macros
- Updated Patch0

* Sat Jun 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.2-alt1
- New upstream release

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.1-alt1
- New upstream release

* Tue May 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.0-alt1
- New upstream release

* Sun Feb 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.0-alt1
- Adapted for Sisyphus from the JPackage project
