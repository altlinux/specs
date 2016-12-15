Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           plexus-containers
Version:        1.6
Release:        alt3_5jpp8
Summary:        Containers for Plexus
License:        ASL 2.0 and MIT
URL:            https://github.com/codehaus-plexus/plexus-containers
BuildArch:      noarch

Source0:        https://github.com/sonatype/%{name}/archive/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  maven-invoker-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shared-invoker
BuildRequires:  maven-release
BuildRequires:  maven-plugin-plugin
BuildRequires:  plexus-classworlds >= 2.5
BuildRequires:  plexus-utils
BuildRequires:  plexus-cli
BuildRequires:  xbean >= 3.14
BuildRequires:  guava
BuildRequires:  objectweb-asm >= 5.0.2
BuildRequires:  qdox >= 2.0
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

%package component-javadoc
Group: Development/Java
Summary:        Javadoc component from %{name}

%description component-javadoc
%{summary}.

%package component-annotations
Group: Development/Java
Summary:        Component API from %{name}

%description component-annotations
%{summary}.

%package container-default
Group: Development/Java
Summary:        Default Container from %{name}
Obsoletes:      plexus-container-default < 1.0-1
Provides:       plexus-containers-component-api = %{version}-%{release}

%description container-default
%{summary}.

%package javadoc
Summary:        API documentation for all plexus-containers packages
Group:          Development/Java
Provides:       %{name}-component-annotations-javadoc = %{version}-%{release}
Obsoletes:      %{name}-component-annotations-javadoc < %{version}-%{release}
Provides:       %{name}-component-javadoc-javadoc = %{version}-%{release}
Obsoletes:      %{name}-component-javadoc-javadoc < %{version}-%{release}
Provides:       %{name}-component-metadata-javadoc = %{version}-%{release}
Obsoletes:      %{name}-component-metadata-javadoc < %{version}-%{release}
Provides:       %{name}-container-default-javadoc = %{version}-%{release}
Obsoletes:      %{name}-container-default-javadoc < %{version}-%{release}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# For Maven 3 compat
%pom_add_dep org.apache.maven:maven-core plexus-component-metadata

# ASM dependency was changed to "provided" in XBean 4.x, so we need to provide ASM
%pom_add_dep org.ow2.asm:asm:5.0.3:runtime plexus-container-default
%pom_add_dep org.ow2.asm:asm-commons:5.0.3:runtime plexus-container-default

%pom_remove_dep com.sun:tools plexus-component-javadoc
%pom_add_dep com.sun:tools plexus-component-javadoc

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

# to prevent ant from failing
mkdir -p plexus-component-annotations/src/test/java

# integration tests fix
sed -i "s|<version>2.3</version>|<version> %{javadoc_plugin_version}</version>|" plexus-component-javadoc/src/it/basic/pom.xml

# plexus-component-api has been merged into plexus-container-default
%mvn_alias ":plexus-container-default" "org.codehaus.plexus:containers-component-api"

# keep compat symlink for maven's sake
%mvn_file ":plexus-component-annotations" %{name}/plexus-component-annotations plexus/containers-component-annotations

%build
%mvn_build -f -s

%install
%mvn_install


# plexus-containers pom goes into main package
%files -f .mfiles-plexus-containers
%files component-annotations -f .mfiles-plexus-component-annotations
%files container-default -f .mfiles-plexus-container-default
%files component-metadata -f .mfiles-plexus-component-metadata
%files component-javadoc -f .mfiles-plexus-component-javadoc

%files javadoc -f .mfiles-javadoc

%changelog
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

