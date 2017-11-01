Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
Requires: xpp3-minimal
BuildRequires: xpp3-minimal
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-war-plugin
Version:        3.0.0
Release:        alt1_3jpp8
Summary:        Maven WAR Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-war-plugin/
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(com.thoughtworks.xstream:xstream)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-filtering)
BuildRequires:  mvn(org.apache.maven.shared:maven-mapping)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Builds a Web Application Archive (WAR) file from the project output and its 
dependencies.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_4jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_1jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_5jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2jpp7
- new release

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_5jpp7
- fixed build with xpp3

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_5jpp7
- new version

