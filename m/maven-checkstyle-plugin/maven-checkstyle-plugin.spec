# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             maven-checkstyle-plugin
Version:          2.12
Release:          alt1_2jpp8
Summary:          Plugin that generates a report regarding the code style used by the developers
Group:            Development/Other
License:          ASL 2.0
URL:              http://maven.apache.org/plugins/%{name}

Source0:          http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:           %{name}-maven-core-dep.patch

BuildArch:        noarch

BuildRequires:    java-devel >= 1.6.0
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-plugin-plugin >= 2.5.1
BuildRequires:    plexus-containers-component-metadata >= 1.5.1
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-compiler-plugin >= 2.0.2
BuildRequires:    maven-jar-plugin >= 2.2
BuildRequires:    maven-install-plugin >= 2.2
BuildRequires:    checkstyle >= 5.6
BuildRequires:    plexus-cli >= 1.2
BuildRequires:    maven-artifact-manager
BuildRequires:    plexus-resources
BuildRequires:    maven-doxia-sitetools
BuildRequires:    maven-doxia-sink-api

Provides:         maven2-plugin-checkstyle = %{version}-%{release}
Obsoletes:        maven2-plugin-checkstyle <= 0:2.0.8
Source44: import.info

%description
Generates a report on violations of code style and optionally fails the build
if violations are detected.

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 

%build
%mvn_build -f -- -DmavenVersion=3.2.1

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt4_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_2jpp7
- new version

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_2jpp7
- complete build

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

