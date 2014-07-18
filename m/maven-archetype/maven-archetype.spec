BuildRequires: maven-plugin-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: xpp3-minimal
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-archetype
Version:        2.1
Release:        alt4_7jpp7
Summary:        Maven project templating toolkit

Group:          Development/Java
License:        ASL 2.0
URL:            https://maven.apache.org/archetype/
Source0:        http://search.maven.org/remotecontent?filepath=org/apache/maven/archetype/%{name}/%{version}/%{name}-%{version}-source-release.zip

# custom depmap needed to resolve ant-antlr which doesn't have pom/depmap
Source1:        %{name}.depmap

Patch0:         0001-Use-component-metadata-instead-of-maven-plugin.patch
Patch1:         0002-Use-generics.patch
Patch2:         0003-Add-Maven-3-compatibility.patch
Patch3:         %{name}-fix-jetty-namespace.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
# we added test dep skipping there
BuildRequires:  maven > 3.0.3-13
BuildRequires:  maven-war-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  jchardet
BuildRequires:  plexus-containers-component-metadata

Requires:       jpackage-utils
Requires:       maven
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
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.

%package catalog
Summary:        Maven Archetype Catalog model
Group:          Development/Java
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       maven-archetype = %{?epoch:%epoch:}%{version}-%{release}

%description catalog
%{summary}.

%package descriptor
Summary:        Maven Archetype Descriptor model
Group:          Development/Java
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       maven-archetype = %{?epoch:%epoch:}%{version}-%{release}

%description descriptor
%{summary}.

%package registry
Summary:        Maven Archetype Registry model
Group:          Development/Java
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       maven-archetype = %{?epoch:%epoch:}%{version}-%{release}

%description registry
%{summary}.

%package common
Summary:        Maven Archetype common classes
Group:          Development/Java
Requires:       maven-archetype = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-catalog = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-descriptor = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-registry = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       jchardet
Requires:       dom4j
Requires:       jdom
Requires:       maven-project
Requires:       plexus-containers-container-default
Requires:       apache-commons-io
Requires:       plexus-velocity

%description common
%{summary}.

%package packaging
Summary:        Maven Archetype packaging configuration for archetypes
Group:          Development/Java
Requires:       jpackage-utils
Requires:       maven-archetype = %{?epoch:%epoch:}%{version}-%{release}

%description packaging
%{summary}.

%package -n %{name}-plugin
Summary:        Maven Plugin for using archetypes
Group:          Development/Java
Requires:       jpackage-utils
Requires:       plexus-utils
Requires:       apache-commons-collections
Requires:       maven-archetype = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-catalog = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-descriptor = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-registry = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{name}-plugin
%{summary}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3

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


%build
# we don't have cargo so skip tests for now
mvn-rpmbuild -X -Dmaven.test.skip=true \
             -Dmaven.local.depmap.file=%{SOURCE1} \
             install javadoc:aggregate

%install
# parent pom
install -Dpm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

for module in common packaging; do
    pushd archetype-$module
    install -Dpm 644 target/archetype-$module-%{version}.jar \
                     %{buildroot}%{_javadir}/%{name}/$module.jar
    install -Dpm 644 pom.xml \
            %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom

    %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar -f $module
    popd
done

pushd archetype-models
     install -Dpm 644 pom.xml \
                     %{buildroot}%{_mavenpomdir}/JPP-%{name}-models.pom

     %add_maven_depmap JPP-%{name}-models.pom

     for module in catalog descriptor registry;do
         pushd archetype-$module
         install -Dpm 644 target/archetype-$module-%{version}.jar \
                      %{buildroot}%{_javadir}/%{name}/$module.jar
         install -Dpm 644 pom.xml \
                      %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom

         %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar -f $module
         popd
     done
popd

pushd %{name}-plugin
install -Dpm 644 target/%{name}-plugin-%{version}.jar \
                 %{buildroot}%{_javadir}/%{name}/plugin.jar
install -Dpm 644 pom.xml \
        %{buildroot}%{_mavenpomdir}/JPP.%{name}-plugin.pom
%add_maven_depmap JPP.%{name}-plugin.pom %{name}/plugin.jar -f plugin
popd

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/



%files
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-models.pom
%{_mavendepmapfragdir}/%{name}
%dir %{_javadir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}
%exclude %{_javadocdir}/%{name}/javadoc.sh

%files catalog
%{_mavendepmapfragdir}/%{name}-catalog
%{_mavenpomdir}/JPP.%{name}-catalog.pom
%{_javadir}/%{name}/catalog.jar

%files descriptor
%{_mavendepmapfragdir}/%{name}-descriptor
%{_mavenpomdir}/JPP.%{name}-descriptor.pom
%{_javadir}/%{name}/descriptor.jar

%files registry
%{_mavendepmapfragdir}/%{name}-registry
%{_mavenpomdir}/JPP.%{name}-registry.pom
%{_javadir}/%{name}/registry.jar

%files common
%{_mavendepmapfragdir}/%{name}-common
%{_mavenpomdir}/JPP.%{name}-common.pom
%{_javadir}/%{name}/common.jar

%files packaging
%{_mavendepmapfragdir}/%{name}-packaging
%{_mavenpomdir}/JPP.%{name}-packaging.pom
%{_javadir}/%{name}/packaging.jar

%files -n %{name}-plugin
%{_mavendepmapfragdir}/%{name}-plugin
%{_mavenpomdir}/JPP.%{name}-plugin.pom
%{_javadir}/%{name}/plugin.jar

%changelog
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

