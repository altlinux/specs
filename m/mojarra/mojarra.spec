Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          mojarra
Version:       2.2.13
Release:       alt1_1jpp8
Summary:       JSF Reference Implementation
License:       CDDL or GPLv2 with exceptions
URL:           http://javaserverfaces.java.net
Source0:       https://github.com/javaserverfaces/mojarra/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       http://repo1.maven.org/maven2/com/sun/faces/jsf-api/%{version}/jsf-api-%{version}.pom
Source2:       http://repo1.maven.org/maven2/com/sun/faces/jsf-impl/%{version}/jsf-impl-%{version}.pom

# Don't use the installer builder as it requires additional dependences and it
# is only used to build installers, which we don't use:
Patch0:        %{name}-2.2.13-remove-installer-builder.patch

# Fix the classpath for maven ant tasks to include all the needed jar files:
Patch1:        %{name}-2.2.13-fix-maven-ant-tasks-classpath.patch

# Don't try to download dependencies:
Patch2:        %{name}-2.2.13-dont-download-dependencies.patch

# Use "Oracle Corporation" as the name of the Java vendor, otherwise the
# profile that adds tools.jar to the classpath is not activated:
Patch3:        %{name}-2.2.13-jdk7.patch

# The classpaths were calculated using the maven ant tasks, but we removed
# that, so we need to build fix them:
Patch4:        %{name}-2.2.13-fix-classpaths.patch

# Don't compres JavaScript using YUI compressor, as we don't have it available
# in the distribution:
Patch5:        %{name}-2.2.13-dont-use-yuicompressor.patch

# Don't build the Tomcat 6, Jetty and Glassfish injection providers:
Patch6:        %{name}-2.2.13-dont-build-injection-providers.patch

# Don't bundle the API inside the implementation:
Patch7:        %{name}-2.2.13-dont-bundle-api.patch

# Don't use the namespace-alias XLST element in the stylesheet
# that merges the jsf-ri-runtime.xml file:
Patch8:        %{name}-dont-use-namespace-alias.patch

# Adapt the source to the Servlet 3.1 specification:
Patch9:        %{name}-servlet-3.1.patch

# Disable references to com.sun.faces.spi.InjectionProvider class in API code, otherwise jsf-api can't compile.
# this package is not shipping jsf-impl jar and a class in jsf-api jar that is depending on that specific implementation.
Patch10:       %{name}-2.2.13-disable-references-to-com.sun.faces.spi.InjectionProvider.patch

BuildArch: noarch

BuildRequires: ant
BuildRequires: ant-contrib
BuildRequires: apache-commons-digester
BuildRequires: aqute-bnd
BuildRequires: atinject
BuildRequires: cdi-api
BuildRequires: bean-validation-api
BuildRequires: glassfish-annotation-api
BuildRequires: glassfish-ejb-api
BuildRequires: glassfish-el-api
BuildRequires: glassfish-jsp-api
BuildRequires: glassfish-servlet-api
BuildRequires: groovy
BuildRequires: hibernate-jpa-2.1-api
BuildRequires: java-devel
BuildRequires: jboss-jstl-1.2-api
BuildRequires: maven-install-plugin
BuildRequires: maven-local

Requires:      apache-commons-digester
Requires:      atinject
Requires:      bean-validation-api
Requires:      cdi-api
Requires:      glassfish-annotation-api
Requires:      glassfish-ejb-api
Requires:      glassfish-el-api
Requires:      glassfish-jsp-api
Requires:      glassfish-servlet-api
Requires:      hibernate-jpa-2.1-api
Requires:      jboss-jstl-1.2-api
Source44: import.info


%description
JvaServer(TM) Faces technology simplifies building user interfaces for
JavaServer applications. Developers of various skill levels can quickly build
web applications by: assembling reusable UI components in a page; connecting
these components to an application data source; and wiring client-generated
events to server-side event handlers. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
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


sed -i "s|-f @{pomFile}|-o -f @{pomFile}|" common/ant/maven.xml common/ant/maven-pre-maven-rename.xml


# Remove binaries
find . -name '*.class' -print -delete
find . -name '*.jar' -print -delete

# Convert the license file to UTF-8:
mv LICENSE LICENSE.tmp
iconv -f ISO-8859-1 -t UTF-8 LICENSE.tmp > LICENSE

native2ascii -encoding UTF8 jsf-api/src/main/java/javax/faces/component/UIComponent.java \
 jsf-api/src/main/java/javax/faces/component/UIComponent.java

# Fix the ant group id, it should be org.apache.ant instead of just ant:
%pom_change_dep :ant org.apache.ant: jsf-tools

cp -p %{SOURCE1} jsf-api.pom
cp -p %{SOURCE2} jsf-impl.pom
for a in jsf-api.pom jsf-impl.pom; do
 %pom_change_dep javax.servlet.jsp.jstl:jstl-api org.jboss.spec.javax.servlet.jstl:jboss-jstl-api_1.2_spec:1.0.3.Final ${a}
done

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
  ln -s `build-classpath ${name}` lib/$(basename ${name}).jar
done

# Create links for the jars used for compilation:
mkdir -p lib/compile
names='
atinject
bean-validation-api
cdi-api
glassfish-annotation-api
glassfish-ejb-api
glassfish-el-api
glassfish-jsp-api
glassfish-servlet-api
groovy/groovy-all
hibernate-jpa-2.1-api
jboss-jstl-1.2-api
'
for name in ${names}
do
  ln -s `build-classpath ${name}` lib/compile/$(basename ${name}).jar
done

mkdir -p common/lib
ln -s `build-classpath aqute-bnd/biz.aQute.bnd` common/lib/bnd.jar
ln -s `build-classpath aqute-bnd/biz.aQute.bndlib` common/lib/bndlib.jar


# Build the binaries:
ant \
  -Dbuild.sysclasspath=last \
  -Djsf.build.home=$PWD \
  -Dcontainer.name=tomcat7 \
  -Dmvn.cmd=xmvn

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

# Associate POM files with artifacts:
%mvn_artifact jsf-api.pom jsf-api/build/lib/jsf-api-intermediate.jar
%mvn_artifact jsf-impl.pom jsf-ri/build/lib/javax.faces.jar

%mvn_alias com.sun.faces:jsf-api javax.faces:javax.faces-api
%mvn_alias com.sun.faces:jsf-impl org.glassfish:javax.faces

%install

# Install artifacts:
%mvn_install

# Install the Javadoc:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}/jsf-api
cp -rp jsf-api/build/javadocs/* %{buildroot}%{_javadocdir}/%{name}/jsf-api/.
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}/jsf-impl
cp -rp jsf-ri/build/javadocs/* %{buildroot}%{_javadocdir}/%{name}/jsf-impl/.

%files -f .mfiles
%doc LICENSE
%doc docs/index.html
%doc docs/releasenotes.html
%doc docs/community.html
%doc docs/jsf-2_1-changelog.html

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.7-alt2_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.7-alt2_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.7-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.7-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.7-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.7-alt1_4jpp7
- new version

