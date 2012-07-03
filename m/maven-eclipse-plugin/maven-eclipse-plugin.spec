# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-eclipse-plugin
Version:        2.8
Release:        alt1_8jpp7
Summary:        Maven Eclipse Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-eclipse-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         add_compat.patch
Patch1:         reduced_exception.patch
Patch2:         kill-bsh.patch

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%else
BuildArch: noarch
%endif

# Basic stuff
BuildRequires: jpackage-utils

# Maven and its dependencies
BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-doxia
BuildRequires: maven-doxia-tools
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-archiver
BuildRequires: maven-shared-osgi
BuildRequires: maven-antrun-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-shared-invoker
# Others
BuildRequires: apache-commons-io
BuildRequires: easymock
BuildRequires: xmlunit
BuildRequires: eclipse-platform
BuildRequires: plexus-resources
BuildRequires: bsf
BuildRequires: jaxen
BuildRequires: dom4j
BuildRequires: xom
BuildRequires: saxpath


Requires: maven
Requires: apache-commons-io
Requires: plexus-resources
Requires: jpackage-utils
Requires: jsch
Requires: jtidy

Provides:       maven2-plugin-eclipse = 0:%{version}-%{release}
Obsoletes:      maven2-plugin-eclipse <= 0:2.0.8
Source44: import.info

%description
The Eclipse Plugin is used to generate Eclipse IDE files (.project, .classpath 
and the .settings folder) from a POM.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0
%patch1
%patch2
sed -i -e "s|3.3.0-v20070604|3.7.100.v20110510-0712|g" pom.xml

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository

CORE_FAKE_VERSION="3.7.100.v20110510-0712"
CORE_PLUGIN_DIR=$MAVEN_REPO_LOCAL/org/eclipse/core/resources/$CORE_FAKE_VERSION

mkdir -p $CORE_PLUGIN_DIR
plugin_file=`ls %{_libdir}/eclipse/plugins/org.eclipse.core.resources_*jar`

ln -s "$plugin_file" $CORE_PLUGIN_DIR/resources-$CORE_FAKE_VERSION.jar

mvn-rpmbuild -e \
        -Dmaven.test.skip=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_8jpp7
- new version

