# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-eclipse-plugin
Version:        2.9
Release:        alt4_2jpp7
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e "s|3.3.0-v20070604|3.7.100.v20110510-0712|g" pom.xml
sed -i -e '/<version>0.0.145<.version>/d' pom.xml


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
        install javadoc:aggregate

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

