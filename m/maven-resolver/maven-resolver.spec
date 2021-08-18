Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           maven-resolver
Epoch:          1
Version:        1.6.1
Release:        alt1_5jpp11
License:        ASL 2.0
Summary:        Apache Maven Artifact Resolver library
URL:            https://maven.apache.org/resolver/
Source0:        https://archive.apache.org/dist/maven/resolver/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice::no_aop:)
%endif

Provides:       maven-resolver-api = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-spi = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-impl = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-util = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-connector-basic = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-wagon = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-http = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-file = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-classpath = %{epoch}:%{version}-%{release}

Obsoletes:      maven-resolver-api < 1:1.4.2-6
Obsoletes:      maven-resolver-spi < 1:1.4.2-6
Obsoletes:      maven-resolver-impl < 1:1.4.2-6
Obsoletes:      maven-resolver-util < 1:1.4.2-6
Obsoletes:      maven-resolver-connector-basic < 1:1.4.2-6
Obsoletes:      maven-resolver-transport-wagon < 1:1.4.2-6
Obsoletes:      maven-resolver-transport-http < 1:1.4.2-6
Obsoletes:      maven-resolver-transport-file < 1:1.4.2-6
Obsoletes:      maven-resolver-transport-classpath < 1:1.4.2-6
Obsoletes:      maven-resolver-test-util < 1:1.4.2-6
Source44: import.info

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%{?javadoc_package}

%prep
%setup -q

%pom_remove_plugin -r :bnd-maven-plugin

%pom_disable_module maven-resolver-demos
%pom_disable_module maven-resolver-synccontext-global
%pom_disable_module maven-resolver-synccontext-redisson
%pom_disable_module maven-resolver-transport-classpath
%pom_disable_module maven-resolver-transport-file
%pom_disable_module maven-resolver-transport-http
%mvn_package :maven-resolver-test-util __noinstall

# generate OSGi manifests
for pom in $(find -mindepth 2 -name pom.xml) ; do
  %pom_add_plugin "org.apache.felix:maven-bundle-plugin" $pom \
  "<configuration>
    <instructions>
      <Bundle-SymbolicName>\${project.groupId}$(sed 's:./maven-resolver::;s:/pom.xml::;s:-:.:g' <<< $pom)</Bundle-SymbolicName>
      <Export-Package>!org.eclipse.aether.internal*,org.eclipse.aether*</Export-Package>
      <_nouses>true</_nouses>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>"
done
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%mvn_alias 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%mvn_file ':maven-resolver{*}' %{name}/maven-resolver@1 aether/aether@1

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed Aug 18 2021 Igor Vlasenko <viy@altlinux.org> 1:1.6.1-alt1_5jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:1.4.2-alt1_5jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:1.4.2-alt1_3jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 1:1.4.1-alt1_2jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.3.3-alt1_2jpp8
- new version

* Wed Jul 10 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_2jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.1.1-alt1_2jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_1jpp8
- new version

* Sun Nov 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.3-alt1_7jpp8
- new version

