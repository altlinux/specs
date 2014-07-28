# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jilter
Version:        1.2
Release:        alt1_6jpp7
Summary:        Sendmail milter protocol for Java

Group:          Development/Java
License:        Sendmail
URL:            http://sendmail-jilter.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sendmail-jilter/%{version}/jilter-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant-junit
BuildRequires:  log4j
BuildRequires:  junit

Requires:       jpackage-utils
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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_6jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_5jpp7
- new version

