Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.0.1
%global namedreltag -b08
%global namedversion %{version}%{?namedreltag}

Name:          glassfish-el
Version:       3.0.1
Release:       alt1_0.6.b08jpp8
Summary:       J2EE Expression Language Implementation
License:       CDDL-1.1 or GPLv2 with exceptions
URL:           http://uel.java.net
# svn export https://svn.java.net/svn/uel~svn/tags/javax.el-3.0.1-b08/ glassfish-el-3.0.1-b08
# rm -r glassfish-el-3.0.1-b08/fonts
# rm -r glassfish-el-3.0.1-b08/parent-pom
# rm -r glassfish-el-3.0.1-b08/repo
# rm -r glassfish-el-3.0.1-b08/spec
# rm -r glassfish-el-3.0.1-b08/uel
# rm -r glassfish-el-3.0.1-b08/www
# tar cJf glassfish-el-3.0.1-b08.tar.xz glassfish-el-3.0.1-b08
Source0:       %{name}-%{namedversion}-clean.tar.xz
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.surefire:surefire-junit47)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.glassfish:legal)

BuildArch:     noarch
Source44: import.info

%description
This project provides an implementation of the Expression Language (EL).
The main goals are:
 * Improves current implementation: bug fixes and performance improvements
 * Provides API for use by other tools, such as Netbeans

%package api
Group: Development/Java
Summary:       Expression Language 3.0 API
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0

%description api
Expression Language 3.0 API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

cp -p %{SOURCE1} .

%pom_remove_plugin -r :findbugs-maven-plugin
%pom_remove_plugin -r :findbugs-maven-plugin api
%pom_remove_plugin -r :glassfish-copyright-maven-plugin

# Useless tasks
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-release-plugin api
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-source-plugin api

# Fix javadoc task
%pom_xpath_remove "pom:plugin[pom:artifactId ='maven-javadoc-plugin']/pom:executions/pom:execution/pom:goals"
%pom_xpath_remove "pom:plugin[pom:artifactId ='maven-javadoc-plugin']/pom:executions/pom:execution/pom:goals" api
%pom_xpath_remove "pom:plugin[pom:artifactId ='maven-javadoc-plugin']/pom:executions/pom:execution/pom:configuration/pom:sourcepath"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions/pom:execution/pom:configuration" "<additionalparam>-Xdoclint:none</additionalparam>"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions/pom:execution/pom:configuration" "<additionalparam>-Xdoclint:none</additionalparam>" api

# Fix apis version
%pom_xpath_set "pom:project/pom:version" %{namedversion} api
# Add missing build dep
%pom_add_dep javax.el:javax.el-api:'${project.version}'

# Move code without build-helper plugin in the proper folder
%pom_remove_plugin -r :build-helper-maven-plugin
mv impl/src/main src

# Do not use ant
%pom_add_plugin org.codehaus.mojo:javacc-maven-plugin:2.6 . "
<executions>
    <execution>
        <id>jjtree-javacc</id>
        <goals>
            <goal>jjtree-javacc</goal>
        </goals>
        <configuration>
            <sourceDirectory>src/main/java/com/sun/el/parser</sourceDirectory>
            <outputDirectory>src/main/java/com/sun/el/parser</outputDirectory>
        </configuration>
    </execution>
</executions>"

# Fix impl resources path
%pom_xpath_remove "pom:build/pom:resources/pom:resource"
%pom_xpath_inject "pom:build/pom:resources" "
    <resource>
        <directory>src/main/java</directory>
        <includes>
            <include>**/*.properties</include>
            <include>**/*.xml</include>
        </includes>
    </resource>"

# This is a dummy POM added just to ease building in the RPM platforms
cat > pom-parent.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <modelVersion>4.0.0</modelVersion>
  <groupId>org.glassfish.web</groupId>
  <artifactId>javax.el-root</artifactId>
  <version>%{namedversion}</version>
  <packaging>pom</packaging>
  <name>%{name} Parent</name>
  <modules>
    <module>api</module>
    <module>pom.xml</module>
  </modules>
</project>
EOF

%mvn_file javax.el:javax.el-api %{name}-api
%mvn_alias javax.el:javax.el-api "javax.el:el-api" "org.glassfish:javax.el-api"

%mvn_file org.glassfish:javax.el %{name}
%mvn_alias org.glassfish:javax.el "org.eclipse.jetty.orbit:com.sun.el" "org.glassfish.web:javax.el" "org.glassfish:javax.el-impl"

%mvn_package :javax.el-root __noinstall

%build

%mvn_build -s -- -f pom-parent.xml

%install
%mvn_install

cp -p api/target/classes/META-INF/LICENSE.txt .
cp -p api/src/main/javadoc/doc-files/*-spec-license.html .

%files -f .mfiles-javax.el
%files api -f .mfiles-javax.el-api
%doc LICENSE.txt LICENSE-2.0.txt *-spec-license.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_0.6.b08jpp8
- new fc release

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_0.5.b08jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_0.4.b08jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_0.3.b08jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_6jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_5jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.5-alt1_2jpp7
- new release

