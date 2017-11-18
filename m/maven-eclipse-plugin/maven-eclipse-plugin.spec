Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Eclipse does not yet export virtual maven provides, so filter out the requires


Name:           maven-eclipse-plugin
Version:        2.9
Release:        alt6_18jpp8
Summary:        Maven Eclipse Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-eclipse-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         %{name}-compat.patch
Patch1:         %{name}-exception.patch
Patch2:         %{name}-ioexception.patch

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%else
BuildArch: noarch
%endif

# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugins-pom
BuildRequires: maven-test-tools
BuildRequires: maven-plugin-testing-tools
BuildRequires: maven-osgi
# Others
BuildRequires: apache-commons-io
BuildRequires: xmlunit
BuildRequires: eclipse-equinox-servlet
BuildRequires: plexus-resources
BuildRequires: plexus-interactivity-jline
BuildRequires: bsf
BuildRequires: jaxen
BuildRequires: jdom
BuildRequires: dom4j
BuildRequires: xom
BuildRequires: saxpath
Source44: import.info
%filter_from_requires /mvn\\(org\\.eclipse\\.core:resources\\)/d

%description
The Eclipse Plugin is used to generate Eclipse IDE files (.project, .classpath 
and the .settings folder) from a POM.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e "s|3.3.0-v20070604|3.7.100.v20110510-0712|g" pom.xml

sed -i 's/aQute\.lib\.osgi/aQute.bnd.osgi/g' src/main/java/org/apache/maven/plugin/eclipse/EclipseToMavenMojo.java

# Remove easymock dependency (tests are skipped)
%pom_remove_dep easymock:

%build
# Create a local repo for the eclipse dependency because eclipse
# does not yet export virtual mvn provides or ship pom files
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
CORE_FAKE_VERSION="3.7.100.v20110510-0712"
CORE_PLUGIN_DIR=$MAVEN_REPO_LOCAL/org/eclipse/core/resources/$CORE_FAKE_VERSION

mkdir -p $CORE_PLUGIN_DIR
#plugin_file=`ls /usr/lib{,64}/eclipse/plugins/org.eclipse.core.resources_*jar || :`
plugin_file=`ls /usr/share/java/eclipse/core.resources.jar || :`

ln -s "$plugin_file" $CORE_PLUGIN_DIR/resources-$CORE_FAKE_VERSION.jar

%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId[text()='org.eclipse.core']]" "<scope>provided</scope>"

# Skip tests because they do not compile
%mvn_build -- -Dmaven.test.skip=true -Dmaven.repo.local=$MAVEN_REPO_LOCAL

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES README-testing.txt
%dir %{_javadir}/maven-eclipse-plugin
%dir %{_mavenpomdir}/maven-eclipse-plugin

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.9-alt6_18jpp8
- fixed build

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.9-alt6_15jpp8
- fixed build

* Wed Feb 24 2016 Igor Vlasenko <viy@altlinux.ru> 2.9-alt5_15jpp8
- jpp8 update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.9-alt5_9jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.9-alt5_5jpp7
- new release

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.9-alt5_2jpp7
- added maven-local BR:

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.9-alt4_2jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.9-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.9-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.9-alt1_2jpp7
- new version

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_8jpp7
- new version

