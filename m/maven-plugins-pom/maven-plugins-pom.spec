Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name maven-plugins

Name:           %{short_name}-pom
Version:        28
Release:        alt1_4jpp8
Summary:        Maven Plugins POM
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/
BuildArch:      noarch

Source:         http://repo.maven.apache.org/maven2/org/apache/maven/plugins/%{short_name}/%{version}/%{short_name}-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
Source44: import.info

%description
This package provides Maven Plugins parent POM used by different
Apache Maven plugins.

%prep
%setup -q -n %{short_name}-%{version}
# Enforcer plugin is used to ban plexus-component-api.
%pom_remove_plugin :maven-enforcer-plugin
# maven-scm-publish-plugin is not usable in Fedora.
%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :maven-site-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 28-alt1_4jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 28-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 27-alt1_3jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 27-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 23-alt3_7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 23-alt3_6jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 23-alt3_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 23-alt2_2jpp7
- fixed build

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 23-alt1_2jpp7
- new version

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 23-alt1_0jpp7
- intermediate build

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 23-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

