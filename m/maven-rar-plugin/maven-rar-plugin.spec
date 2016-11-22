Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-rar-plugin
Version:        2.4
Release:        alt1_2jpp8
Summary:        Plugin to create Resource Adapter Archive which can be deployed to a J2EE server

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-rar-plugin/
Source0:        http://archive.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip

Patch0:         fix-tests.patch

BuildArch: noarch

BuildRequires: maven-local
Source44: import.info

%description
A resource adapter is a system-level software driver that 
a Java application to connect to an enterprise 
information system (EIS).The RAR plugin has the capability 
to store these resource adapters to an archive 
(Resource Adapter Archive or RAR) which can be deployed to
 a J2EE server.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%patch0

# Fix deps to build against maven 3
%pom_remove_dep org.apache.maven:maven-project
%pom_add_dep org.apache.maven:maven-compat
%pom_add_dep org.apache.maven:maven-core
%pom_add_dep junit:junit::test

# To make tests work
%pom_remove_dep org.apache.maven:maven-artifact
%pom_add_dep org.apache.maven:maven-artifact

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_2jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_10jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_8jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_8jpp7
- new fc release

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_7jpp7
- complete build

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

