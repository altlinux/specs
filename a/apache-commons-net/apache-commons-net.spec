Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
Provides: osgi(org.apache.commons.net) = 2.0.0
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat

%global base_name    net
%global short_name   commons-%{base_name}

Name:           apache-%{short_name}
Version:        3.2
Release:        alt2_1jpp7
Summary:        Internet protocol suite Java library
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-plugin-build-helper
BuildRequires:  apache-commons-parent

Requires:       jpackage-utils

Provides:       jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < 0:2.0-3
Source44: import.info


%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

%package javadoc
Summary:    API documentation for %{name}
Group:      Development/Java
Requires:   jpackage-utils

Obsoletes:  jakarta-%{short_name}-javadoc < 0:2.0-3
BuildArch: noarch

%description javadoc
%%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' NOTICE.txt LICENSE.txt


%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
# test.failure.ignore added because package would not build on koji
# with TimeTCPClientTest failing
mvn-rpmbuild -Dmaven.test.failure.ignore=true \
    install javadoc:aggregate

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.apache.commons:%{short_name}"

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# jakarta compat
ln -s %{short_name}.jar %buildroot%_javadir/jakarta-%{short_name}.jar



%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%changelog
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
