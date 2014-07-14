BuildRequires: /proc
BuildRequires: jpackage-compat
Name: mojarra
Version: 2.1.7
Release: alt2_4jpp7
Summary: JSF Reference Implementation

Group: Development/Java
License: CDDL or GPLv2 with exceptions
URL: http://javaserverfaces.java.net

# svn export https://svn.java.net/svn/mojarra~svn/tags/2.1.7/ mojarra-2.1.7
# find mojarra-2.1.7/ -name '*.class' -delete
# find mojarra-2.1.7/ -name '*.jar' -delete
# tar czf mojarra-2.1.7.tgz mojarra-2.1.7
Source0: %{name}-%{version}.tgz
Source1: http://repo1.maven.org/maven2/com/sun/faces/jsf-api/2.1.7/jsf-api-2.1.7.pom
Source2: http://repo1.maven.org/maven2/com/sun/faces/jsf-impl/2.1.7/jsf-impl-2.1.7.pom

# Don't use the installer builder as it requires additional dependences and it
# is only used to build installers, which we don't use:
Patch0: %{name}-remove-installer-builder.patch

# Fix the classpath for maven ant tasks to include all the needed jar files:
Patch1: %{name}-fix-maven-ant-tasks-classpath.patch

# Add the target to deploy test dependencies to the Tomcat 7 container
# configuration:
Patch2: %{name}-add-tomcat7-deploy-test-dependencies-target.patch

# Don't try to download dependencies:
Patch3: %{name}-dont-download-dependencies.patch

# Fix the ant group id, it should be org.apache.ant instead of just ant:
Patch4: %{name}-fix-ant-gid.patch

# Use "Oracle Corporation" as the name of the Java vendor, otherwise the
# profile that adds tools.jar to the classpath is not activated:
Patch5: %{name}-jdk7.patch

# The classpaths were calculated using the maven ant tasks, but we removed
# that, so we need to build fix them:
Patch6: %{name}-fix-classpaths.patch

# Don't compres JavaScript using YUI compressor, as we don't have it available
# in the distribution:
Patch7: %{name}-dont-use-yuicompressor.patch

# Don't build the Tomcat 6, Jetty and Glassfish injection providers:
Patch8: %{name}-dont-build-injection-providers.patch

# Don't bundle the API inside the implementation:
Patch9: %{name}-dont-bundle-api.patch

# Don't use the namespace-alias XLST element in the stylesheet
# that merges the jsf-ri-runtime.xml file:
Patch10: %{name}-dont-use-namespace-alias.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: ant-contrib
BuildRequires: maven
BuildRequires: groovy
BuildRequires: aqute-bnd
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: tomcat-el-2.2-api
BuildRequires: tomcat-jsp-2.2-api
BuildRequires: geronimo-annotation
BuildRequires: geronimo-validation

Requires: jpackage-utils
Requires: tomcat-servlet-3.0-api
Requires: tomcat-el-2.2-api
Requires: tomcat-jsp-2.2-api
Requires: geronimo-annotation
Requires: geronimo-validation
Source44: import.info


%description
JvaServer(TM) Faces technology simplifies building user interfaces for
JavaServer applications. Developers of various skill levels can quickly build
web applications by: assembling reusable UI components in a page; connecting
these components to an application data source; and wiring client-generated
events to server-side event handlers. 


%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.

%prep

# Unpack and patch the original sources:
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# Remove binaries (I know this is already mentinoned in the instructions to
# build the source tarball above, but it doesn't hurt):
find . -name '*.class' -delete
find . -name '*.jar' -delete

# Convert the license file to UTF-8:
mv LICENSE LICENSE.tmp
iconv -f ISO-8859-1 -t UTF-8 LICENSE.tmp > LICENSE


%build

# Create links for the apache commons jars:
mkdir -p lib
names='
apache-commons-collections
apache-commons-digester
apache-commons-beanutils
apache-commons-logging
'
for name in ${names}
do
  ln -s `build-classpath ${name}` lib/${name}.jar
done

# Create links for the jars used for compilation:
mkdir -p lib/compile
names='
taglibs-core
tomcat-servlet-3.0-api
tomcat-el-2.2-api
tomcat-jsp-2.2-api
geronimo-annotation
geronimo-validation
groovy
'
for name in ${names}
do
  ln -s `build-classpath ${name}` lib/compile/${name}.jar
done

# Some other jars that require specific version number in the names:
mkdir -p common/lib
ln -s `build-classpath aqute-bnd` common/lib/bnd-0.0.249.jar

export OPT_JAR_LIST="ant-contrib"
# Build it the binaries:
ant \
  -Dbuild.sysclasspath=last \
  -Djsf.build.home=$PWD \
  -Dcontainer.name=tomcat7 \
  -Dmvn.cmd=`which mvn-rpmbuild`

# Generate the javadocs:
ant \
  -Dbuild.sysclasspath=last \
  -Djsf.build.home=$PWD \
  -Dcontainer.name=tomcat7 \
  -f jsf-api/build.xml \
  javadocs

ant \
  -Dbuild.sysclasspath=last \
  -Djsf.build.home=$PWD \
  -Dcontainer.name=tomcat7 \
  -f jsf-ri/build.xml \
  javadocs


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -m 644 jsf-api/build/lib/jsf-api-intermediate.jar %{buildroot}%{_javadir}/%{name}/jsf-api.jar
install -m 644 jsf-ri/build/lib/javax.faces.jar %{buildroot}%{_javadir}/%{name}/jsf-impl.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP.%{name}-jsf-api.pom
install -m 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/JPP.%{name}-jsf-impl.pom

# API javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}/jsf-api
cp -rp jsf-api/build/javadocs/* %{buildroot}%{_javadocdir}/%{name}/jsf-api/.
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}/jsf-impl
cp -rp jsf-api/build/javadocs/* %{buildroot}%{_javadocdir}/%{name}/jsf-impl/.

# Dependencies map:
%add_maven_depmap JPP.%{name}-jsf-api.pom %{name}/jsf-api.jar
%add_maven_depmap JPP.%{name}-jsf-impl.pom %{name}/jsf-impl.jar


%files
%{_javadir}/%{name}
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE
%doc docs/index.html
%doc docs/releasenotes.html
%doc docs/community.html
%doc docs/jsf-2_1-changelog.html


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.7-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.7-alt1_4jpp7
- new version

