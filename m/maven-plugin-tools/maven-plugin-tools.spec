# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-plugin-tools
Version:        2.7
Release:        alt1_4jpp7
Epoch:          0
Summary:        Maven Plugin Tools

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-tools/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}-source-release.zip

# this patch should be upstreamed (together with updated pom.xml
# dependency version on jtidy 8.0)
Patch0:         0001-fix-for-new-jtidy.patch
Patch1:         0002-maven3-compat.patch
Patch2:         0003-missing-com.sun-in-1.6.0-and-higher.patch

BuildArch: noarch

BuildRequires: maven
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-doxia-tools
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-shared-reporting-impl
BuildRequires: maven-test-tools
BuildRequires: maven-plugin-testing-harness
BuildRequires: modello
Requires: maven
Requires:       jpackage-utils
Source44: import.info

%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven Plugins in a variety of languages.

%package javadocs
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadocs
API documentation for %{name}.

%package ant
Summary: Maven Plugin Tool for Ant
Group: Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-api
Obsoletes: maven-shared-plugin-tools-ant < 0:%{version}-%{release}
Provides: maven-shared-plugin-tools-ant = 0:%{version}-%{release}

%description ant
Descriptor extractor for plugins written in Ant.

%package api
Summary: Maven Plugin Tools APIs
Group: Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Obsoletes: maven-shared-plugin-tools-api < 0:%{version}-%{release}
Provides: maven-shared-plugin-tools-api = 0:%{version}-%{release}

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%package beanshell
Summary: Maven Plugin Tool for Beanshell
Group: Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-api
Requires: bsh
Obsoletes: maven-shared-plugin-tools-beanshell < 0:%{version}-%{release}
Provides: maven-shared-plugin-tools-beanshell = 0:%{version}-%{release}

%description beanshell
Descriptor extractor for plugins written in Beanshell.

%package java
Summary: Maven Plugin Tool for Java
Group: Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-api
Obsoletes: maven-shared-plugin-tools-java < 0:%{version}-%{release}
Provides: maven-shared-plugin-tools-java = 0:%{version}-%{release}

%description java
Descriptor extractor for plugins written in Java.

%package javadoc
Summary: Maven Plugin Tools Javadoc
Group: Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-java
BuildArch: noarch

%description javadoc
The Maven Plugin Tools Javadoc provides several Javadoc taglets to be used when generating Javadoc.

%package model
Summary: Maven Plugin Metadata Model
Group: Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-java
Obsoletes: maven-shared-plugin-tools-model < 0:%{version}-%{release}
Provides: maven-shared-plugin-tools-model = 0:%{version}-%{release}

%description model
The Maven Plugin Metadata Model provides an API to play with the Metadata model.

%package -n maven-plugin-plugin
Summary: Maven Plugin Plugin
Group: Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-java
Requires: %{name}-model
Requires: %{name}-beanshell
Requires: maven-doxia-sitetools
Requires: maven-shared-reporting-impl
Obsoletes: maven2-plugin-plugin < 0:%{version}-%{release}
Provides: maven2-plugin-plugin = 0:%{version}-%{release}

%description -n maven-plugin-plugin
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's found in the source tree,
to include in the JAR. It is also used to generate Xdoc files for the Mojos as well as for updating the
plugin registry, the artifact metadata and a generic help goal.

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-rpmbuild package javadoc:aggregate

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}

install -pm 644 maven-plugin-tools-ant/target/maven-plugin-tools-ant-%{version}.jar \
                %{buildroot}%{_javadir}/maven-plugin-tools/ant.jar
install -pm 644 maven-plugin-tools-api/target/maven-plugin-tools-api-%{version}.jar \
                %{buildroot}%{_javadir}/maven-plugin-tools/api.jar
install -pm 644 maven-plugin-tools-beanshell/target/maven-plugin-tools-beanshell-%{version}.jar \
                %{buildroot}%{_javadir}/maven-plugin-tools/beanshell.jar
install -pm 644 maven-plugin-tools-java/target/maven-plugin-tools-java-%{version}.jar \
                %{buildroot}%{_javadir}/maven-plugin-tools/java.jar
install -pm 644 maven-plugin-tools-javadoc/target/maven-plugin-tools-javadoc-%{version}.jar \
                %{buildroot}%{_javadir}/maven-plugin-tools/javadoc.jar
install -pm 644 maven-plugin-tools-model/target/maven-plugin-tools-model-%{version}.jar \
                %{buildroot}%{_javadir}/maven-plugin-tools/model.jar
install -pm 644 maven-plugin-plugin/target/maven-plugin-plugin-%{version}.jar \
                %{buildroot}%{_javadir}/maven-plugin-tools/plugin.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 pom.xml \
                %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom

install -pm 644 %{name}-ant/pom.xml \
                %{buildroot}%{_mavenpomdir}/JPP.%{name}-ant.pom
%add_maven_depmap -f ant JPP.%{name}-ant.pom %{name}/ant.jar

install -pm 644 %{name}-api/pom.xml \
                %{buildroot}%{_mavenpomdir}/JPP.%{name}-api.pom
%add_maven_depmap -f api JPP.%{name}-api.pom %{name}/api.jar

install -pm 644 %{name}-beanshell/pom.xml \
                %{buildroot}%{_mavenpomdir}/JPP.%{name}-beanshell.pom
%add_maven_depmap -f beanshell JPP.%{name}-beanshell.pom %{name}/beanshell.jar

install -pm 644 %{name}-java/pom.xml \
                %{buildroot}%{_mavenpomdir}/JPP.%{name}-java.pom
%add_maven_depmap -f java JPP.%{name}-java.pom %{name}/java.jar

install -pm 644 %{name}-javadoc/pom.xml \
                %{buildroot}%{_mavenpomdir}/JPP.%{name}-javadoc.pom
%add_maven_depmap -f javadoc JPP.%{name}-javadoc.pom %{name}/javadoc.jar

install -pm 644 %{name}-model/pom.xml \
                %{buildroot}%{_mavenpomdir}/JPP.%{name}-model.pom
%add_maven_depmap -f model JPP.%{name}-model.pom %{name}/model.jar

install -pm 644 maven-plugin-plugin/pom.xml \
                %{buildroot}%{_mavenpomdir}/JPP.%{name}-plugin.pom
%add_maven_depmap -f plugin JPP.%{name}-plugin.pom %{name}/plugin.jar
# add_maven_depmap macro supports name suffixes only, renaming ...
mv -f %{buildroot}%{_mavendepmapfragdir}/%{name}-plugin %{buildroot}%{_mavendepmapfragdir}/maven-plugin-plugin

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadocs
%{_javadocdir}/%{name}

%files ant
%{_javadir}/%{name}/ant.jar
%{_mavenpomdir}/JPP.%{name}-ant.pom
%{_mavendepmapfragdir}/%{name}-ant

%files api
%{_javadir}/%{name}/api.jar
%{_mavenpomdir}/JPP.%{name}-api.pom
%{_mavendepmapfragdir}/%{name}-api

%files beanshell
%{_javadir}/%{name}/beanshell.jar
%{_mavenpomdir}/JPP.%{name}-beanshell.pom
%{_mavendepmapfragdir}/%{name}-beanshell

%files java
%{_javadir}/%{name}/java.jar
%{_mavenpomdir}/JPP.%{name}-java.pom
%{_mavendepmapfragdir}/%{name}-java

%files javadoc
%{_javadir}/%{name}/javadoc.jar
%{_mavenpomdir}/JPP.%{name}-javadoc.pom
%{_mavendepmapfragdir}/%{name}-javadoc

%files model
%{_javadir}/%{name}/model.jar
%{_mavenpomdir}/JPP.%{name}-model.pom
%{_mavendepmapfragdir}/%{name}-model

%files -n maven-plugin-plugin
%{_javadir}/%{name}/plugin*
%{_mavenpomdir}/JPP.%{name}-plugin.pom
%{_mavendepmapfragdir}/maven-plugin-plugin

%changelog
* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_4jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

