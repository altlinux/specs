Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             glassfish-saaj
Version:          1.3.19
Release:          alt2_10jpp8
Summary:          JSR-67 implementation
License:          CDDL and GPLv2 with exceptions
URL:              http://java.net/projects/saaj

# svn export https://svn.java.net/svn/saaj~svn/tags/saaj-impl-1.3.19 glassfish-saaj-1.3.19
# find glassfish-saaj-1.3.19/ -name '*.jar' -delete
# find glassfish-saaj-1.3.19/ -name '*.zip' -delete
# tar cafJ glassfish-saaj-1.3.19.tar.xz glassfish-saaj-1.3.19
Source0:          glassfish-saaj-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    java-devel
BuildRequires:    maven-local
BuildRequires:    mvn(net.java:jvnet-parent:pom:)
BuildRequires:    mvn(javax.xml.soap:saaj-api)
BuildRequires:    mvn(net.java:jvnet-parent:pom:)
BuildRequires:    mvn(org.jvnet.mimepull:mimepull)
Source44: import.info

%description
Open source Reference Implementation of JSR-67: SOAP with Attachments
API for Java (SAAJ MR: 1.3)

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# Useless tasks
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc license.html

%files javadoc -f .mfiles-javadoc
%doc license.html

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_10jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_9jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_8jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_3jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt2_1jpp7
- fixed maven1 dependency

* Tue Jan 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.19-alt1_1jpp7
- initial build

