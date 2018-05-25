Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-project-info-reports-plugin
Version:        2.8.1
Release:        alt1_3jpp8
Summary:        Maven Project Info Reports Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-project-info-reports-plugin/
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Port-to-Maven-3-API.patch
Patch1:         0002-Port-to-latest-doxia.patch
Patch2:	maven-project-info-reports-plugin-2.8.1-buildfix.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-validator:commons-validator)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-logging-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xhtml)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jarsigner-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-api)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-manager-plexus)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-cvs-commons)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-cvsexe)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-git-commons)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-gitexe)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-hg)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-perforce)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-starteam)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-svn-commons)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-svnexe)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree) >= 3.0
BuildRequires:  mvn(org.apache.maven.shared:maven-doxia-tools)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-jar)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-lightweight)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-ssh)
BuildRequires:  mvn(org.codehaus.mojo:keytool-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
The Maven Project Info Reports Plugin is a plugin 
that generates standard reports for the specified project.
  

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -c
mv %{name}-%{version}/* .
%patch0 -p1
%patch1 -p1
%patch2 -p1
# removed cvsjava provider since we don't support it anymore
%pom_remove_dep :maven-scm-provider-cvsjava
# Port to latest keytool-maven-plugin
%pom_xpath_set "pom:goal[text()='genkey']" generateKeyPair
sed -i -e s,generateKeyPair,genkey, pom.xml

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_3jpp8
- java update

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_2jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_1jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1_5jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt5_7jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt4_7jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt3_7jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_7jpp7
- new release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_5jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

