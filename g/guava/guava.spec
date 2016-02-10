Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          guava
Version:       18.0
Release:       alt2_4jpp8
Summary:       Google Core Libraries for Java
License:       ASL 2.0
URL:           https://github.com/google/guava

Source0:       https://github.com/google/guava/archive/v%{version}.tar.gz
Patch0:        %{name}-java8.patch

BuildRequires: maven-local

BuildRequires: mvn(com.google.code.findbugs:jsr305) >= 0
BuildRequires: ant
BuildRequires: apache-ivy

BuildArch:     noarch

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}
Source44: import.info

%description
Guava is a suite of core and expanded libraries that include
utility classes, Googlea.'s collections, io classes, and much
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
find . -name '*.jar' -delete

%pom_disable_module guava-gwt
%pom_disable_module guava-testlib
%pom_disable_module guava-tests
%pom_remove_plugin :animal-sniffer-maven-plugin guava
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_dep jdk:srczip guava

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin :maven-javadoc-plugin guava

%pom_xpath_inject /pom:project/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:instructions "<_nouses>true</_nouses>" guava/pom.xml

%build

%mvn_file :%{name} %{name}
%mvn_alias :%{name} com.google.collections:google-collections com.google.guava:guava-jdk5
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS CONTRIBUTORS README*
%doc COPYING

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_4jpp8
- added osgi provides

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt1_4jpp8
- unbootsrap build

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_3jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_1jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

