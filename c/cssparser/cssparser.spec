Epoch: 0
Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           cssparser
Version:        0.9.15
Release:        alt1_4jpp8
Summary:        CSS Parser
License:        LGPLv2+ 
URL:            http://cssparser.sourceforge.net/
# sh ./fetch-cssparser.sh
Source0:        cssparser-%{version}.tar.xz
Source1:        fetch-cssparser.sh

BuildArch: noarch

BuildRequires: mvn(org.w3c.css:sac) >= 1.3
BuildRequires: mvn(junit:junit)
BuildRequires: javacc-maven-plugin >= 2.6
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-reporting-impl
BuildRequires: replacer
Source44: import.info

%description
A CSS parser which implements SAC (the Simple API for CSS).

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%pom_remove_plugin :maven-checkstyle-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc doc/license.html doc/readme.html
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.15-alt1_4jpp8
- java 8 mass update

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.7-alt1_1jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.6-alt1_3jpp7
- new version

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt3_1jpp5
- fixed build with javacc 5

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_1jpp5
- fixed build with javacc 5

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_1jpp5
- fixed build with new maven 2.0.8

* Mon Feb 09 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_1jpp5
- new version

