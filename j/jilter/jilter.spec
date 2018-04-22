# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jilter
Version:        1.2
Release:        alt1_14jpp8
Summary:        Sendmail milter protocol for Java

Group:          Development/Other
License:        Sendmail
URL:            http://sendmail-jilter.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sendmail-jilter/%{version}/jilter-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel
BuildRequires:  ant-junit
BuildRequires:  log4j
BuildRequires:  junit

Requires:       jpackage-utils
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%else
Requires:       java
%endif
Requires:       log4j
Source44: import.info

%description
Sendmail-Jilter is an Open Source implementation of the Sendmail milter
protocol, for implementing milters in Java that can interface with the
Sendmail MTA. 


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
mkdir -p External
build-jar-repository -s -p External log4j junit


%build
ant all docs


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/dist/lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/
cp -rp build/doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}



%files
%doc LICENSE.txt
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_14jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_13jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_6jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_5jpp7
- new version

