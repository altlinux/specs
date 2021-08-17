Epoch: 0
Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

Name:           plexus-containers
Version:        2.1.0
Release:        alt1_7jpp11
Summary:        Containers for Plexus
# Most of the files are either under ASL 2.0 or MIT
# The following files are under xpp:
# plexus-component-metadata/src/main/java/org/codehaus/plexus/metadata/merge/Driver.java
# plexus-component-metadata/src/main/java/org/codehaus/plexus/metadata/merge/MXParser.java
License:        ASL 2.0 and MIT and xpp
URL:            https://github.com/codehaus-plexus/plexus-containers
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        LICENSE.MIT

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.xbean:xbean-reflect)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package component-metadata
Group: Development/Java
Summary:        Component metadata from %{name}

%description component-metadata
%{summary}.

%package component-annotations
Group: Development/Java
Summary:        Component API from %{name}

%description -n %{?module_prefix}%{name}-component-annotations
%{summary}.

%package container-default
Group: Development/Java
Summary:        Default Container from %{name}

%description container-default
%{summary}.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{name}-%{version}

cp %{SOURCE1} .
cp %{SOURCE2} .

%pom_remove_plugin -r :maven-site-plugin

%pom_change_dep -r :google-collections com.google.guava:guava

# Generate OSGI info
%pom_xpath_inject "pom:project" "
    <packaging>bundle</packaging>
    <build>
      <plugins>
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <_nouses>true</_nouses>
              <Export-Package>org.codehaus.plexus.component.annotations.*</Export-Package>
            </instructions>
          </configuration>
        </plugin>
      </plugins>
    </build>" plexus-component-annotations

# plexus-component-api has been merged into plexus-container-default
%mvn_alias ":plexus-container-default" "org.codehaus.plexus:containers-component-api"

# keep compat symlink for maven's sake
%mvn_file ":plexus-component-annotations" %{name}/plexus-component-annotations plexus/containers-component-annotations

# remove some broken tests
rm plexus-component-metadata/src/test/java/org/codehaus/plexus/metadata/merge/ComponentsXmlMergerTest.java
rm plexus-component-metadata/src/test/java/org/codehaus/plexus/metadata/DefaultComponentDescriptorWriterTest.java

%build
%mvn_build -s -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

# plexus-containers pom goes into main package
%files -f .mfiles-plexus-containers
%doc --no-dereference LICENSE-2.0.txt LICENSE.MIT

%files component-annotations -f .mfiles-plexus-component-annotations
%doc --no-dereference LICENSE-2.0.txt LICENSE.MIT

%files container-default -f .mfiles-plexus-container-default
%doc --no-dereference LICENSE-2.0.txt LICENSE.MIT

%files component-metadata -f .mfiles-plexus-component-metadata
%doc --no-dereference LICENSE-2.0.txt LICENSE.MIT

%changelog
* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:2.1.0-alt1_7jpp11
- update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.1.0-alt1_2jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_1jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_9jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_6jpp8
- java fc28+ update

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_5jpp8
- use guava 20

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_6jpp8
- new fc release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_5jpp8
- added osgi provides

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_5jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp8
- added osgi provides

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt8_13jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt8_11jpp7
- new release

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt8_6jpp7
- more symlinks

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt7_6jpp7
- added another compat symlink

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt6_6jpp7
- added compat symlink

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt5_6jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt4_6jpp7
- fixed build

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt3_6jpp7
- fixed deps

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt2_6jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt2_5jpp7
- applied repocop patches

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_5jpp7
- fc build

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_1jpp6
- new version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.1.a34.5jpp6
- fixed build

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.1.a34.5jpp6
- fixed build

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.1.a34.5jpp6
- fixed build

* Thu Sep 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.1.a34.5jpp6
- new release a34

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a32.3jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a30.1jpp5
- converted from JPackage by jppimport script

