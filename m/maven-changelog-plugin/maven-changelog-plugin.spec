Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-changelog-plugin
Version:        2.3
Release:        alt1_2jpp8
Summary:        Produce SCM changelog reports

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-changelog-plugin/
Source0:        http://archive.apache.org/dist/maven/plugins/maven-changelog-plugin-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: maven-local
BuildRequires: maven-scm
Source44: import.info

%description
The Maven Changelog Plugin generates reports regarding the recent changes 
in your Software Configuration Management or SCM. These reports include 
the changelog report, developer activity report and the file activity report.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 

# No netbeans-cvsclient support in fedora
%pom_remove_dep :maven-scm-provider-cvsjava

# Fix deps for maven 3
%pom_remove_dep org.apache.maven:maven-project
%pom_remove_dep org.apache.maven:maven-model
%pom_remove_dep org.apache.maven:maven-settings
%pom_add_dep org.apache.maven:maven-artifact
%pom_add_dep org.apache.maven:maven-compat

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_2jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt4_17jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt4_16jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt4_10jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_10jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_10jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_10jpp7
- new fc release

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_9jpp7
- new version

