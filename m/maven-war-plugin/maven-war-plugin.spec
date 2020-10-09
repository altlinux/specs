Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Requires: xpp3-minimal
BuildRequires: xpp3-minimal
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Allow building with minimal dependency set
%bcond_with jp_minimal

Name:           maven-war-plugin
Version:        3.2.2
Release:        alt1_5jpp8
Summary:        Maven WAR Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-war-plugin/
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Patch out reliance on xstream for minimal build
Patch0: 0001-Patch-out-reliance-on-xstream.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-filtering)
BuildRequires:  mvn(org.apache.maven.shared:maven-mapping)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%if %{without jp_minimal}
BuildRequires:  mvn(com.thoughtworks.xstream:xstream)
%endif
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

%if %{with jp_minimal}
# Patch out reliance on xstream for minimal build
%patch0 -p1
%pom_remove_dep com.thoughtworks.xstream:xstream
%endif

%pom_remove_plugin :maven-enforcer-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 3.2.2-alt1_5jpp8
- update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.2-alt1_3jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_4jpp8
- fc27 update

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

