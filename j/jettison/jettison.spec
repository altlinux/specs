Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jettison
Version:        1.3.7
Release:        alt1_3jpp8
Summary:        A JSON StAX implementation
License:        ASL 2.0
URL:            http://jettison.codehaus.org/
BuildArch:      noarch

Source0:        https://github.com/codehaus/jettison/archive/%{name}-%{version}.tar.gz

# Change the POM to use the version of woodstox that we have available:
Patch0: %{name}-update-woodstox-version.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.codehaus:codehaus-parent:pom:)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(stax:stax-api)
Source44: import.info

%description
Jettison is a collection of Java APIs (like STaX and DOM) which read
and write JSON. This allows nearly transparent enablement of JSON based
web services in services frameworks like CXF or XML serialization
frameworks like XStream.

%package javadoc
Group: Development/Java
Summary:           Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
# We don't need wagon-webdav
%pom_xpath_remove pom:build/pom:extensions

# Confuses maven-bundle-plugin
%pom_xpath_remove pom:Private-Package

%build
# Disable the tests until BZ#796739 is fixed:
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/META-INF/LICENSE

%files javadoc -f .mfiles-javadoc
%doc src/main/resources/META-INF/LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.7-alt1_3jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.7-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt1_5jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.3-alt1_1jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_5jpp7
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.rc2.1jpp5
- jpp5 build

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.rc1.1jpp1.7
- added dependency on new excalibur

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.rc1.1jpp1.7
- converted from JPackage by jppimport script

