Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global with_maven 0
Name:           logback
Version:        1.0.9
Release:        alt1_2jpp7
Summary:        A Java logging library

Group:          Development/Java
License:        LGPLv2 or EPL
URL:            http://logback.qos.ch/
Source0:        http://logback.qos.ch/dist/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-00-build.xml
Source2:        %{name}-%{version}-core-osgi.bnd
Source3:        %{name}-%{version}-classic-osgi.bnd
Source4:        %{name}-%{version}-access-osgi.bnd

# Java dependencies
BuildRequires: jpackage-utils

# Required libraries
BuildRequires: geronimo-jms
# require groovy 2.0.0
BuildRequires: groovy
BuildRequires: janino
# require jansi 1.8
BuildRequires: jansi
BuildRequires: javamail
BuildRequires: jetty
BuildRequires: log4j
BuildRequires: slf4j
BuildRequires: tomcat-lib
BuildRequires: tomcat-servlet-3.0-api

# groovy-all embedded libraries
BuildRequires: antlr-tool
BuildRequires: apache-commons-cli
BuildRequires: objectweb-asm

# Build tools -- build with ant for now because of circular dependencies
%if %with_maven
# antrun plugin deps
BuildRequires: ant-junit
BuildRequires: felix-main
BuildRequires: junit

BuildRequires: gmaven
BuildRequires: maven
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
%else
BuildRequires: ant
BuildRequires: aqute-bnd
%endif

# Java runtime dependencies
Requires:      jpackage-utils
# Java library dependencies
Requires:      geronimo-jms
Requires:      groovy
Requires:      janino
Requires:      jansi
Requires:      javamail

Requires:      slf4j
Requires:      tomcat-lib
Requires:      tomcat-servlet-3.0-api

BuildArch:     noarch
Source44: import.info

%description
Logback is intended as a successor to the popular log4j project. At present
time, logback is divided into three modules, logback-core, logback-classic
and logback-access.

The logback-core module lays the groundwork for the other two modules. The
logback-classic module can be assimilated to a significantly improved
version of log4j. Moreover, logback-classic natively implements the SLF4J
API so that you can readily switch back and forth between logback and other
logging frameworks such as log4j or java.util.logging (JUL).

The logback-access module integrates with Servlet containers, such as
Tomcat and Jetty, to provide HTTP-access log functionality. Note that you
could easily build your own module on top of logback-core.

%package javadoc
Summary:       Javadoc for %{name}
Group:         Development/Java
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for the Logback library

%package access
Summary:       Logback-access module for Servlet integration
Group:         Development/Java
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:      janino
Requires:      javamail
Requires:      jetty
Requires:      tomcat-lib
Requires:      tomcat-servlet-3.0-api

%description access
The logback-access module integrates with Servlet containers, such as Tomcat
and Jetty, to provide HTTP-access log functionality. Note that you could
easily build your own module on top of logback-core. 

%package examples
Summary:       Logback Examples Module
Group:         Development/Java
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:      %{name}-access = %{?epoch:%epoch:}%{version}-%{release}
Requires:      log4j
Requires:      slf4j
Requires:      tomcat-servlet-3.0-api

%description examples
logback-examples module.

%prep
%setup -q
%if !%with_maven
cp -p %{SOURCE4} osgi-access.bnd
%endif

%pom_remove_plugin org.scala-tools:maven-scala-plugin %{name}-core

find . -name "*.class" -delete
find . -name "*.cmd" -delete
find . -name "*.jar" -delete

# Clean up the documentation
sed -i 's/\r//' LICENSE.txt README.txt docs/*.* docs/*/*.* docs/*/*/*.*
sed -i 's#"apidocs#"%{_javadocdir}/%{name}#g' docs/*.html
rm -rf docs/apidocs docs/project-reports docs/testapidocs docs/project-reports.html
rm -f docs/manual/.htaccess docs/css/site.css # Zero-length file

sed -i 's#<artifactId>groovy-all</artifactId#<artifactId>groovy</artifactId#' $(find . -name "pom.xml")

# disable for now
#om_disable_module logback-site
sed -i 's#<module>logback-site</module>#<!--module>logback-site</module-->#' pom.xml

%build

%if %with_maven
# unavailable test dep maven-scala-plugin
# slf4jJAR and org.apache.felix.main are required by logback-examples modules for maven-antrun-plugin
mvn-rpmbuild -Dmaven.test.skip=true \
  -Dslf4jJAR=$(build-classpath slf4j/api) \
  -Dorg.apache.felix:org.apache.felix.main:jar=$(build-classpath felix/org.apache.felix.main) \
  package javadoc:aggregate
%else
cp -p %{SOURCE1} build.xml
cp -p %{SOURCE2} osgi-core.bnd
cp -p %{SOURCE3} osgi-classic.bnd
ant dist javadoc
%endif

%install

install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

install -d -m 755 %{buildroot}%{_javadir}/%{name}
# main
for sub in classic core; do
  install -m 644 %{name}-$sub/target/%{name}-$sub-%{version}.jar \
      %{buildroot}%{_javadir}/%{name}/%{name}-$sub.jar
  install -pm 644 %{name}-$sub/pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}-%{name}-$sub.pom
%add_maven_depmap JPP.%{name}-%{name}-$sub.pom %{name}/%{name}-$sub.jar
done

# optionals
for sub in access examples; do
  install -m 644 %{name}-$sub/target/%{name}-$sub-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}/%{name}-$sub.jar
  install -pm 644 %{name}-$sub/pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}-%{name}-$sub.pom
%add_maven_depmap JPP.%{name}-%{name}-$sub.pom %{name}/%{name}-$sub.jar -f $sub
done

install -d -m 755 p %{buildroot}%{_javadocdir}/%{name}
# copy only apis docs
cp -r target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

install -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}/examples
cp -r %{name}-examples/pom.xml %{name}-examples/src %{buildroot}%{_datadir}/%{name}-%{version}/examples

%files
%doc LICENSE.txt README.txt docs/*
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-classic.jar
%{_javadir}/%{name}/%{name}-core.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-classic.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%files access
%doc LICENSE.txt
%{_javadir}/%{name}/%{name}-access.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-access.pom
%{_mavendepmapfragdir}/%{name}-access

%files examples
%doc LICENSE.txt
%{_datadir}/%{name}-%{version}
%{_javadir}/%{name}/%{name}-examples.jar
%{_mavendepmapfragdir}/%{name}-examples
%{_mavenpomdir}/JPP.%{name}-%{name}-examples.pom

%changelog
* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_2jpp7
- fc update

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.6-alt1_3jpp7
- new version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.27-alt1_1jpp6
- new version

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt2_2jpp6
- build with compat slf4j15

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt1_2jpp6
- new version

