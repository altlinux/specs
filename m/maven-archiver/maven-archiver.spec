Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-archiver
Version:        2.5
Release:        alt2_8jpp7
Epoch:          0
Summary:        Maven Archiver
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-archiver/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-shared-jar
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-archiver >= 2.1-1
BuildRequires:  plexus-utils
BuildRequires:  apache-commons-parent

Provides:       maven-shared-archiver = %{version}-%{release}
Obsoletes:      maven-shared-archiver < %{version}-%{release}
Source44: import.info

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%pom_add_dep org.apache.maven:maven-core
# tests don't compile with maven 2.2.1
rm -fr src/test/java/org/apache/maven/archiver/*.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_3jpp7
- rebuild with maven-local

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_3jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

