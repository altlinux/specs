BuildRequires: maven-plugin-plugin
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          gmaven
Version:       1.4
Release:       alt3_1jpp7
Summary:       Integration of Groovy into Maven
Group:         Development/Java
License:       ASL 2.0
Url:           http://gmaven.codehaus.org/
# MOVED TO GITHUB 2012-08-02 https://github.com/groovy/gmaven
# svn export http://svn.codehaus.org/gmaven/tags/gmaven-1.4
# tar czf gmaven-1.4-src-svn.tar.gz gmaven-1.4
Source0:       %{name}-%{version}-src-svn.tar.gz
# depend on groovy 2.x
Patch0:        %{name}-%{version}-disable-runtime20.patch
# build fix for gshell 2.6.x
Patch1:        %{name}-%{version}-gshell-io.patch
# set source to 1.5
Patch2:        %{name}-%{version}-javadoc.patch
# build fix for gossip >= 1.7
Patch3:        %{name}-%{version}-gossip.patch
# use plexus component-metadata instead of maven-plugin
Patch4:        %{name}-%{version}-component-metadata.patch
# remove maven-enforcer-plugin wagon-webdav-jackrabbit requireMavenVersion
Patch5:        %{name}-%{version}-pom.patch
# add maven 3.x core as dep
Patch6:        %{name}-%{version}-runtime-loader.patch

# fix build with maven3.x apis
Patch7:        %{name}-%{version}-plugin-maven3-apis-changed.patch

# change groovy aId
# vs 1.6 1.7 1.8 2.x groovy-all groovy
# vs 1.5 groovy-all-minimal groovy
# remove runtime-1.5 runtime-1.6 runtime-1.7

# for some maven metadata files require groovy and gmaven runtime 1.6
# change packaging for filter-plugin examples

# set source/target to 1.5 in compiler-plugin conf

# configure gmvane-plugin for filter-plugin gmaven-mojo-support groovy-maven-plugin

Patch8:        %{name}-%{version}-default-runtime.patch

BuildRequires: codehaus-parent
BuildRequires: fusesource-pom
# BuildRequires: forge-parent
BuildRequires: jpackage-utils

BuildRequires: ant
# groovy-all rebundle libraries
BuildRequires: antlr
BuildRequires: apache-commons-cli
BuildRequires: objectweb-asm

BuildRequires: apache-commons-lang
BuildRequires: apache-resource-bundles apache-jar-resource-bundle
BuildRequires: groovy
BuildRequires: gshell
BuildRequires: jline2
BuildRequires: maven
BuildRequires: maven-artifact-manager
BuildRequires: maven-monitor
BuildRequires: maven-plugin-descriptor
BuildRequires: maven-project
BuildRequires: maven-shared-file-management
BuildRequires: maven-shared-filtering
BuildRequires: maven-shared-reporting-api
BuildRequires: maven-shared-reporting-impl
BuildRequires: maven-wagon
BuildRequires: plexus-classworlds
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-digest
BuildRequires: plexus-utils
BuildRequires: qdox
BuildRequires: slf4j
BuildRequires: sonatype-gossip

# test deps
BuildRequires: junit

BuildRequires: maven-archetype-common
BuildRequires: maven-archetype-packaging
BuildRequires: maven-archetype-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-plugin
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-surefire-report-plugin
BuildRequires: plexus-containers-component-metadata

Requires:      ant
Requires:      antlr
Requires:      apache-commons-cli
Requires:      apache-commons-lang
Requires:      groovy
Requires:      gshell
Requires:      jline2
Requires:      maven
Requires:      maven-monitor
Requires:      maven-plugin-descriptor
Requires:      maven-project
Requires:      maven-shared-file-management
Requires:      maven-shared-filtering
Requires:      maven-shared-reporting-api
Requires:      maven-shared-reporting-impl
Requires:      maven-wagon
Requires:      objectweb-asm
Requires:      plexus-classworlds
Requires:      plexus-containers-container-default
Requires:      plexus-digest
Requires:      plexus-utils
Requires:      qdox
Requires:      slf4j
Requires:      sonatype-gossip

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
GMaven provides integration of the Groovy language into Maven.
With GMaven you can:
* Build Groovy Projects
* Execute Groovy Code
* Run Groovy Tools
* Implement Maven Plugins
Advanced:
* Groovy Runtime
* Advanced Configuration

%package archetypes
Group:         Development/Java
Summary:       GMaven Archetypes
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description archetypes
Integration of Groovy into Maven.

%package -n groovy-maven-plugin
Group:         Development/Java
Summary:       Groovy Maven Plugin
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n groovy-maven-plugin
Adapts the latest Groovy Maven Plugin to the
legacy 'org.codehaus.mojo:groovy-maven-plugin'
location.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package examples
Group:         Development/Java
Summary:       GMaven Examples
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:      maven
Requires:      maven-artifact-manager
Requires:      maven-shared-file-management
Requires:      plexus-digest

%description examples
Provides some example plugins implemented in Groovy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p1

# https://jira.codehaus.org/browse/GMAVEN-98
sed -i "s|return new Version(1, 8, 5);|return new Version(1, 8, 7);|" gmaven-runtime/gmaven-runtime-1.8/src/main/java/org/codehaus/gmaven/runtime/v1_8/ProviderImpl.java


%build

# runtime profile
mvn-rpmbuild -Pjava7 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_mavenpomdir}

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom

install -pm 644 %{name}-archetypes/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-archetypes.pom
%add_maven_depmap -f archetypes JPP.%{name}-%{name}-archetypes.pom
for m in %{name}-archetype-basic %{name}-archetype-mojo; do
  install -m 644 %{name}-archetypes/${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
  install -pm 644 %{name}-archetypes/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap -f archetypes JPP.%{name}-${m}.pom %{name}/${m}.jar
done

install -pm 644 %{name}-examples/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-examples.pom
%add_maven_depmap -f examples JPP.%{name}-%{name}-examples.pom
for m in clean-maven-plugin install-maven-plugin; do
  install -m 644 %{name}-examples/${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
  install -pm 644 %{name}-examples/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap -f examples JPP.%{name}-${m}.pom %{name}/${m}.jar
done

install -pm 644 %{name}-feature/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-feature.pom
%add_maven_depmap JPP.%{name}-%{name}-feature.pom
for m in %{name}-feature-api gmaven-feature-support; do
  install -m 644 %{name}-feature/${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
  install -pm 644 %{name}-feature/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

install -pm 644 %{name}-runtime/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-runtime.pom
%add_maven_depmap JPP.%{name}-%{name}-runtime.pom

for m in %{name}-runtime-api %{name}-runtime-loader %{name}-runtime-support %{name}-runtime-1.8; do
  install -m 644 %{name}-runtime/${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
  install -pm 644 %{name}-runtime/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

for m in %{name}-mojo %{name}-mojo-support %{name}-packaging %{name}-plugin; do
  install -m 644 ${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
  install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

install -pm 644 %{name}-support/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-support.pom
%add_maven_depmap JPP.%{name}-%{name}-support.pom
install -m 644 %{name}-support/filter-plugin/target/filter-plugin-%{version}.jar %{buildroot}%{_javadir}/%{name}/filter-plugin.jar
install -pm 644 %{name}-support/filter-plugin/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-filter-plugin.pom
%add_maven_depmap JPP.%{name}-filter-plugin.pom %{name}/filter-plugin.jar

install -m 644 groovy-maven-plugin/target/groovy-maven-plugin-%{version}.jar %{buildroot}%{_javadir}/%{name}/groovy-maven-plugin.jar
install -pm 644 groovy-maven-plugin/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-groovy-maven-plugin.pom
%add_maven_depmap JPP.%{name}-groovy-maven-plugin.pom %{name}/groovy-maven-plugin.jar -f groovy-maven-plugin
mv %{buildroot}%{_mavendepmapfragdir}/%{name}-groovy-maven-plugin %{buildroot}%{_mavendepmapfragdir}/groovy-maven-plugin

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/filter-plugin.jar
%{_javadir}/%{name}/%{name}-feature-api.jar
%{_javadir}/%{name}/%{name}-feature-support.jar
%{_javadir}/%{name}/%{name}-mojo-support.jar
%{_javadir}/%{name}/%{name}-mojo.jar
%{_javadir}/%{name}/%{name}-packaging.jar
%{_javadir}/%{name}/%{name}-plugin.jar
%{_javadir}/%{name}/%{name}-runtime-1.8.jar
%{_javadir}/%{name}/%{name}-runtime-api.jar
%{_javadir}/%{name}/%{name}-runtime-loader.jar
%{_javadir}/%{name}/%{name}-runtime-support.jar
%{_mavenpomdir}/JPP.%{name}-filter-plugin.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-feature-api.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-feature-support.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-feature.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-mojo-support.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-mojo.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-packaging.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-plugin.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-runtime-1.8.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-runtime-api.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-runtime-loader.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-runtime-support.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-runtime.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-support.pom
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt README.txt

%files archetypes
%{_javadir}/%{name}/%{name}-archetype-basic.jar
%{_javadir}/%{name}/%{name}-archetype-mojo.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-archetype-basic.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-archetype-mojo.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-archetypes.pom
%{_mavendepmapfragdir}/%{name}-archetypes
%doc LICENSE.txt

%files -n groovy-maven-plugin
%{_javadir}/%{name}/groovy-maven-plugin.jar
%{_mavenpomdir}/JPP.%{name}-groovy-maven-plugin.pom
%{_mavendepmapfragdir}/groovy-maven-plugin
%doc LICENSE.txt

%files examples
%{_javadir}/%{name}/clean-maven-plugin.jar
%{_javadir}/%{name}/install-maven-plugin.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-examples.pom
%{_mavenpomdir}/JPP.%{name}-clean-maven-plugin.pom
%{_mavenpomdir}/JPP.%{name}-install-maven-plugin.pom
%{_mavendepmapfragdir}/%{name}-examples
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_1jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_1jpp7
- rebuild with new apache-resource-bundles

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- new version

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt5jpp
- added gmaven-runtime-1.5 dep

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt4jpp
- bootstrap jar pack to restore broken gmaven jars

