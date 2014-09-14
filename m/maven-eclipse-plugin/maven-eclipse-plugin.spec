# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Eclipse does not yet export virtual maven provides, so filter out the requires


Name:           maven-eclipse-plugin
Version:        2.9
Release:        alt5_9jpp7
Summary:        Maven Eclipse Plugin

Group:          Development/Java
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

# Basic stuff
BuildRequires: jpackage-utils

# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven-test-tools
BuildRequires: maven-plugin-testing-tools
# Others
BuildRequires: apache-commons-io
BuildRequires: xmlunit
BuildRequires: eclipse-platform
BuildRequires: plexus-resources
BuildRequires: bsf
BuildRequires: jaxen
BuildRequires: dom4j
BuildRequires: xom
BuildRequires: saxpath

Provides:       maven2-plugin-eclipse = 0:%{version}-%{release}
Obsoletes:      maven2-plugin-eclipse <= 0:2.0.8
Source44: import.info
%filter_from_requires /mvn.org.eclipse.core:resources./d

%description
The Eclipse Plugin is used to generate Eclipse IDE files (.project, .classpath 
and the .settings folder) from a POM.

%package javadoc
Group:          Development/Java
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

# Remove easymock dependency (tests are skipped)
%pom_remove_dep easymock:

%build
# Create a local repo for the eclipse dependency because eclipse
# does not yet export virtual mvn provides or ship pom files
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
CORE_FAKE_VERSION="3.7.100.v20110510-0712"
CORE_PLUGIN_DIR=$MAVEN_REPO_LOCAL/org/eclipse/core/resources/$CORE_FAKE_VERSION

mkdir -p $CORE_PLUGIN_DIR
plugin_file=`ls /usr/lib{,64}/eclipse/plugins/org.eclipse.core.resources_*jar || :`

ln -s "$plugin_file" $CORE_PLUGIN_DIR/resources-$CORE_FAKE_VERSION.jar

# Skip tests because they do not compile
%mvn_build -- -Dmaven.test.skip=true -Dmaven.repo.local=$MAVEN_REPO_LOCAL

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES README-testing.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

