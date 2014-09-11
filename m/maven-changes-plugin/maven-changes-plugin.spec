# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-changes-plugin
Version:        2.8
Release:        alt1_6jpp7
Summary:        Plugin to support reporting of changes between releases

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         0001-Remove-dependency-on-velocity-tools.patch

BuildArch:      noarch

BuildRequires: apache-commons-collections
BuildRequires: jakarta-commons-httpclient
BuildRequires: apache-commons-io
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-logging
BuildRequires: maven-local
BuildRequires: maven-project
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-shared-filtering
BuildRequires: maven-shared-reporting-api
BuildRequires: maven-shared-reporting-impl
BuildRequires: modello
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-containers-component-metadata
BuildRequires: plexus-mail-sender
BuildRequires: plexus-i18n
BuildRequires: plexus-interpolation
BuildRequires: plexus-utils
BuildRequires: plexus-velocity
BuildRequires: xmlrpc3-client
BuildRequires: xmlrpc3-common
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis
BuildRequires: velocity

Obsoletes: maven2-plugin-changes <= 0:2.0.8
Provides: maven2-plugin-changes = 1:%{version}-%{release}
Source44: import.info

%description
This plugin is used to inform your users of the changes that have
occurred between different releases of your project. The plugin can
extract these changes, either from a changes.xml file or from the JIRA
issue management system, and present them as a report. You also have
the option of creating a release announcement and even sending this
via email to your users.


%package javadoc
Group:    Development/Java
Summary:  Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q

# remove dependency on velocity-tools
%patch0 -p1
%pom_remove_dep :velocity-tools

# Javamail is provided by JDK
%pom_remove_dep :geronimo-javamail_1.4_mail
%pom_remove_dep :geronimo-javamail_1.4_provider
%pom_remove_dep :geronimo-javamail_1.4_spec

# Fix Maven 3 compatibility
%pom_add_dep org.apache.maven:maven-compat

# Disable github module as we don't have dependencies
rm -rf src/main/java/org/apache/maven/plugin/github
%pom_remove_dep org.apache.httpcomponents:
%pom_remove_dep org.eclipse.mylyn.github:

%build
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_4jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt4_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt3_2jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt2_2jpp7
- fixed deps

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_2jpp7
- new version

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_2jpp7
- new version

