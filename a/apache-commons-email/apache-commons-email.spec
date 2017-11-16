Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global short_name      commons-email

Name:             apache-%{short_name}
Version:          1.5
Release:          alt1_1jpp8
Summary:          Apache Commons Email Package
License:          ASL 2.0
URL:              http://commons.apache.org/proper/%{short_name}/
BuildArch:        noarch

Source0:          http://archive.apache.org/dist/commons/email/source/%{short_name}-%{version}-src.tar.gz

# Disable tests that require Internet access
Patch0:           disable-internet-tests.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(com.sun.mail:javax.mail)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.powermock:powermock-api-easymock)
BuildRequires:  mvn(org.powermock:powermock-module-junit4)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)
BuildRequires:  mvn(org.subethamail:subethasmtp)
Source44: import.info

%description
Commons-Email aims to provide an API for sending email. It is built on top of 
the JavaMail API, which it aims to simplify.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src
%patch0

# Compatibility links
%mvn_alias "org.apache.commons:commons-email" "commons-email:commons-email"
%mvn_file :commons-email %{short_name} %{name}

# Javascript in Javadoc mis-detection
sed -i -e '/<script>/s/</&lt;/' src/main/java/org/apache/commons/mail/ImageHtmlEmail.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp7
- new version

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_4jpp6
- fixed build (added jansi BR:)

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp6
- fixed symlinks

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp6
- added osgi manifest

