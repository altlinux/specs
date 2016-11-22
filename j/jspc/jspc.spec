# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jspc
%define version 2.0
%global namedreltag  -alpha-3
%global namedversion %{version}%{?namedreltag}
%global dotreltag    %(echo %{namedreltag} | tr - .)

Name:          jspc
Version:       2.0
Release:       alt1_0.18.alpha.3jpp8
Summary:       Compile JSPs under Maven
Group:         Development/Other
License:       ASL 2.0
Url:           http://mojo.codehaus.org/jspc/
# svn export https://svn.codehaus.org/mojo/tags/jspc-2.0-alpha-3 jspc
# tar czf jspc-2.0-alpha-3-src-svn.tar.gz jspc
Source0:       %{name}-%{namedversion}-src-svn.tar.gz
Source1:       %{name}-mp-plugin.xml
Patch0:        %{name}-ant-groovyc.patch

BuildRequires: maven-local

BuildRequires: apache-resource-bundles
BuildRequires: ant
BuildRequires: antlr3-tool
BuildRequires: fusesource-pom
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(org.apache.maven.shared:file-management)
BuildRequires: plexus-containers-container-default
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: mvn(org.glassfish.web:javax.servlet.jsp)

BuildRequires: maven-antrun-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-install-plugin

BuildRequires: groovy18
Requires: groovy18

BuildArch:     noarch
Source44: import.info

%description
The Codehaus is a collaborative environment for building open source
projects with a strong emphasis on modern languages, focused on
quality components that meet real world needs.

Provides support to precompile your JSPs and have them included into
your WAR file. Version 2 of the JSP compilation support includes a
pluggable JSP compiler implementation, which currently allows different
versions of the Tomcat Jasper compiler to be used as needed.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}

for d in LICENSE ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

# fix up gmaven removal in src
sed -i 's|import org.codehaus.groovy.maven.mojo.GroovyMojo|import org.apache.maven.plugin.AbstractMojo|' \
  jspc-maven-plugin/src/main/groovy/org/codehaus/mojo/jspc/CompilationMojoSupport.groovy
sed -i 's|extends GroovyMojo|extends AbstractMojo|' \
  jspc-maven-plugin/src/main/groovy/org/codehaus/mojo/jspc/CompilationMojoSupport.groovy

# plexus-maven-plugin superceded by plexus-containers-component-metadata
sed -i 's|<artifactId>plexus-maven-plugin</artifactId>|<artifactId>plexus-component-metadata</artifactId>|' pom.xml

# no tomcat5
%pom_disable_module jspc-compiler-tomcat5 jspc-compilers/pom.xml

# switch tomcat-jasper for glassfish-jsp
%pom_remove_dep org.apache.tomcat:juli jspc-compilers/jspc-compiler-tomcat6/pom.xml
%pom_remove_dep org.apache.tomcat:servlet-api jspc-compilers/jspc-compiler-tomcat6/pom.xml
%pom_remove_dep org.apache.tomcat:jsp-api jspc-compilers/jspc-compiler-tomcat6/pom.xml
%pom_remove_dep org.apache.tomcat:el-api jspc-compilers/jspc-compiler-tomcat6/pom.xml
%pom_remove_dep org.apache.tomcat:jasper-jdt jspc-compilers/jspc-compiler-tomcat6/pom.xml
%pom_remove_dep org.apache.tomcat:annotations-api jspc-compilers/jspc-compiler-tomcat6/pom.xml
%pom_remove_dep org.apache.tomcat:jasper jspc-compilers/jspc-compiler-tomcat6/pom.xml
%pom_remove_dep org.apache.tomcat:jasper-el jspc-compilers/jspc-compiler-tomcat6/pom.xml

# we need servlet 3.0 and jsp 2.2+ in this order
%pom_add_dep org.apache.tomcat:tomcat-servlet-api jspc-compilers/jspc-compiler-tomcat6/pom.xml
%pom_add_dep org.glassfish.web:javax.servlet.jsp jspc-compilers/jspc-compiler-tomcat6/pom.xml

# drop plexus-maven-plugin and add plexus-component-metadata and appropriate config
%pom_remove_plugin org.codehaus.plexus:plexus-maven-plugin jspc-compilers/pom.xml
%pom_add_plugin org.codehaus.plexus:plexus-component-metadata jspc-compilers/pom.xml "
                <configuration>
                  <descriptors>
                    <descriptor>target/classes/META-INF/plexus/components.xml</descriptor>
                  </descriptors>
                </configuration>
                <executions>
                    <execution>
                        <id>create-component-descriptor</id>
                        <phase>generate-resources</phase>
                        <goals>
                            <goal>generate-metadata</goal>
                        </goals>
                    </execution>
                </executions>
"

# fix up source, target config in compiler plugin
%pom_remove_plugin org.apache.maven.plugins:maven-compiler-plugin pom.xml
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin pom.xml "
                <configuration>
                    <source>1.7</source>
                    <target>1.7</target>
                </configuration>
"

# fix up source config in javadoc plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin pom.xml
%pom_add_plugin org.apache.maven.plugins:maven-javadoc-plugin pom.xml "
                <configuration>
                    <source>1.7</source>
                </configuration>
"

# remove wagon-webdav
%pom_xpath_remove "pom:build/pom:extensions"

# get rid of gmaven...
%pom_remove_dep org.codehaus.groovy.maven:gmaven-mojo pom.xml
%pom_remove_plugin org.codehaus.groovy.maven:gmaven-plugin pom.xml
%pom_add_dep org.apache.ant:ant jspc-compilers/jspc-compiler-tomcat6/pom.xml

#...replace with ant groovyc task
# have to patch due to some $ substitution problems
%patch0 -p2

# ant property now needs AntBuilder()
sed -i '/Make directories if needed/a def ant = new AntBuilder()' jspc-maven-plugin/src/main/groovy/org/codehaus/mojo/jspc/CompilationMojoSupport.groovy

%build
%mvn_build

# http://jira.codehaus.org/browse/GMAVEN-68
# gmaven-runtime 1.8 doesn't generate plugin descriptor
# files from javadoc, so we have to load in an existing
# one derived from mvn and g-r 1.6
mkdir -p META-INF/maven/
cp %{SOURCE1} META-INF/maven/plugin.xml
jar uf  %{name}-maven-plugin/target/%{name}-maven-plugin-2.0-alpha-3.jar META-INF/maven/plugin.xml

%install
%mvn_install

%files -f .mfiles
%{_javadir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_0.18.alpha.3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_0.17.alpha.3jpp8
- new version

