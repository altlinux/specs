Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-archetype
Version:        3.2.0
Release:        alt1_4jpp11
Summary:        Maven project templating toolkit

# Most of the code is under ASL 2.0, but some bundled jdom sources are
# under ASL 1.1
License:        ASL 2.0 and ASL 1.1
URL:            https://maven.apache.org/archetype/
Source0:        http://archive.apache.org/dist/maven/archetype/%{name}-%{version}-source-release.zip

# We only use groovy for running a post generation script,
# removing this continues the old behaviour of ignoring it
Patch1: 0001-Avoid-reliance-on-groovy.patch

# Taken from https://github.com/apache/maven-archetype/commit/e4eed30d1c0c6eabf45c49194ff6f0d8a4e4d5a7
Patch2: 0002-declare-dependencies.patch

# Port to commons-lang3
Patch3: 0003-Port-to-commons-lang3.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(net.sourceforge.jchardet:jchardet)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.jdom:jdom)
Source44: import.info
Provides: maven-archetype2 = %version
Obsoletes: maven-archetype2 < %version



%description
Archetype is a Maven project templating toolkit. An archetype is
defined as an original pattern or model from which all other things of
the same kind are made. The names fits as we are trying to provide a
system that provides a consistent means of generating Maven
projects. Archetype will help authors create Maven project templates
for users, and provides users with the means to generate parameterized
versions of those project templates.

Using archetypes provides a great way to enable developers quickly in
a way consistent with best practices employed by your project or
organization. Within the Maven project we use archetypes to try and
get our users up and running as quickly as possible by providing a
sample project that demonstrates many of the features of Maven while
introducing new users to the best practices employed by Maven. In a
matter of seconds a new user can have a working Maven project to use
as a jumping board for investigating more of the features in Maven. We
have also tried to make the Archetype mechanism additive and by that
we mean allowing portions of a project to be captured in an archetype
so that pieces or aspects of a project can be added to existing
projects. A good example of this is the Maven site archetype. If, for
example, you have used the quick start archetype to generate a working
project you can then quickly create a site for that project by using
the site archetype within that existing project. You can do anything
like this with archetypes.

You may want to standardize J2EE development within your organization
so you may want to provide archetypes for EJBs, or WARs, or for your
web services. Once these archetypes are created and deployed in your
organization's repository they are available for use by all developers
within your organization.


%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%package catalog
Group: Development/Java
Summary: Maven Archetype Catalog model

%description catalog
%{summary}.

%package descriptor
Group: Development/Java
Summary: Maven Archetype Descriptor model

%description descriptor
%{summary}.

%package common
Group: Development/Java
Summary: Maven Archetype common classes
# Registry module was obsoleted and removed by upstream F31
Obsoletes: %{name}-registry <= 3.1.1-1

%description common
%{summary}.

%package packaging
Group: Development/Java
Summary: Maven Archetype packaging configuration for archetypes

%description packaging
%{summary}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Not needed for RPM builds
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# Add OSGI info to catalog and descriptor jars
pushd archetype-models/archetype-catalog
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.catalog.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd
pushd archetype-models/archetype-descriptor
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.metadata.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd

# Remove ivy as a runtime dep
%pom_remove_dep org.apache.ivy:ivy archetype-common

# Disable processing of test resources using ant
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin archetype-common

# Don't build the maven-plugin
%pom_disable_module maven-archetype-plugin

%build
%mvn_package :archetype-models maven-archetype
# Tests are skipped due to missing test dependencies
%mvn_build -f -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8 -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

%files -f .mfiles-maven-archetype
%doc --no-dereference LICENSE NOTICE

%files catalog -f .mfiles-archetype-catalog

%files descriptor -f .mfiles-archetype-descriptor

%files common -f .mfiles-archetype-common
%doc --no-dereference LICENSE NOTICE

%files packaging -f .mfiles-archetype-packaging

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.0-alt1_4jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.0-alt1_1jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:3.1.2-alt1_3jpp11
- fixed build

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_10jpp8
- fc update & java 8 build

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_3jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1jpp7
- new release

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt5_7jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_7jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_7jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_7jpp7
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_7jpp7
- new version

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

