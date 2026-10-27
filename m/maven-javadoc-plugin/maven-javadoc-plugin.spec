%define _unpackaged_files_terminate_build 1

Name: maven-javadoc-plugin
Version: 3.12.0
Release: alt1

Summary: Maven plugin for generating Java API documentation
License: Apache-2.0
Group: Development/Java
Url: https://maven.apache.org/plugins/maven-javadoc-plugin/
VCS: https://github.com/apache/maven-javadoc-plugin.git

ExcludeArch: %ix86

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel

# Parent POM and plugins executed during the upstream Maven build.
BuildRequires: mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires: mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)

# Direct compile/provided dependencies from the upstream 3.12.0 POM.
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-settings)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires: mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires: mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires: mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires: mvn(org.apache.maven:maven-archiver)
BuildRequires: mvn(org.apache.maven.shared:maven-invoker)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires: mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires: mvn(org.apache.maven.doxia:doxia-integration-tools)
BuildRequires: mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.commons:commons-text)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.httpcomponents:httpcore)
BuildRequires: mvn(com.thoughtworks.qdox:qdox)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-java)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)
BuildRequires: mvn(org.codehaus.plexus:plexus-io)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires: mvn(commons-io:commons-io)

%description
The Apache Maven Javadoc Plugin uses the javadoc tool to generate
Java API documentation, including Javadoc JAR archives.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
API documentation for %name.

%prep
%setup

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE README.md

%changelog
* Mon Oct 26 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.12.0-alt1
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_3jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 3.1.1-alt2_3jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 3.1.1-alt1_0jpp11
- bootstrap

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_3jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_4jpp8
- java fc28+ update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_2jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_4jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.10.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_2jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.9.1-alt1_1.1jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt2_2jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_2jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

