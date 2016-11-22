Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-reporting-exec
Version:        1.2
Release:        alt1_4jpp8
BuildArch:      noarch
Summary:        Classes to manage report plugin executions with Maven 3

License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-reporting-exec/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/reporting/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-embedder)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-lightweight)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(velocity:velocity)

Patch0001:      0001-Port-to-Maven-3.1.0-Eclipse-Aether-and-Eclipse-Sisu.patch

Source44: import.info

%description
Classes to manage report plugin executions with Maven 3. Contains classes for
managing and configuring reports and their execution.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
The API documentation of %{name}.



%prep
%setup -qn %{name}-%{version}
%patch0001 -p1

# convert CR+LF to LF
sed -i 's/\r//g' pom.xml src/main/java/org/apache/maven/reporting/exec/*

%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

# Build against Maven 3.x, Eclipse Aether and Eclipse Sisu
%pom_remove_dep org.sonatype.aether:aether-api
%pom_remove_dep org.sonatype.aether:aether-util
%pom_change_dep org.sonatype.aether:aether-connector-wagon org.eclipse.aether:aether-transport-wagon
%pom_change_dep org.sonatype.sisu:sisu-inject-plexus org.eclipse.sisu:org.eclipse.sisu.plexus

%build
# Test are skipped because there are errors with PlexusLogger
# More info possibly here:
# https://docs.sonatype.org/display/AETHER/Using+Aether+in+Maven+Plugins?focusedCommentId=10485782#comment-10485782
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE



%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_2jpp7
- rebuild with maven-local

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new release

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

