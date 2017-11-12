Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  hsqldb

Name:           velocity
Version:        1.7
Release:        alt3_21jpp8
Epoch:          1
Summary:        Java-based template engine
License:        ASL 2.0
URL:            http://velocity.apache.org/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/%{name}/engine/%{version}/%{name}-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}.pom

Patch0:         0001-Remove-avalon-logkit.patch
Patch1:         0004-Use-log4j-1.2.17.patch
Patch2:         0003-Use-system-jars.patch
Patch3:         0004-JDBC-41-compat.patch
Patch4:         0001-Don-t-use-Werken-XPath.patch
Patch5:         0006-Skip-Java-8-incompatible-test.patch
Patch6:         velocity-1.7-doclint.patch
Patch7:         velocity-1.7-osgi.patch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  antlr-tool
BuildRequires:  junit
BuildRequires:  ant-junit
%if %{with hsqldb}
BuildRequires:  hsqldb-lib
%endif
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-lang
BuildRequires:  glassfish-servlet-api
BuildRequires:  jakarta-oro
BuildRequires:  jaxen
BuildRequires:  jdom
BuildRequires:  bcel
BuildRequires:  log4j12
BuildRequires:  apache-parent

# It fails one of the arithmetic test cases with gcj
BuildRequires:  java-devel >= 1.6.0
Source44: import.info

%description
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%package        manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description    manual
Documentation for %{name}.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        demo
Group: Development/Java
Summary:        Demo for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q

# remove bundled libs/classes (except those used for testing)
find . -name '*.jar' ! -name 'test*.jar' -print -delete
find . -name '*.class' ! -name 'Foo.class' -print -delete

# Remove dependency on avalon-logkit
rm -f src/java/org/apache/velocity/runtime/log/AvalonLogChute.java
rm -f src/java/org/apache/velocity/runtime/log/AvalonLogSystem.java
rm -f src/java/org/apache/velocity/runtime/log/VelocityFormatter.java

# need porting to new servlet API. We would just add a lot of empty functions
rm  src/test/org/apache/velocity/test/VelocityServletTestCase.java

# This test doesn't work with new hsqldb
rm src/test/org/apache/velocity/test/sql/DataSourceResourceLoaderTestCase.java

cp %{SOURCE1} ./pom.xml

# remove rest of avalon logkit refences
%patch0 -p1

# Use log4j 1.2.17
%patch1 -p1

# Use system jar files instead of downloading from net
%patch2 -p1

%patch3 -p1

# Use jdom instead of werken-xpath
%patch4 -p1
%pom_remove_dep werken-xpath:

# Skip Java 8 incompatible test
%patch5 -p1

# Disable Java8 doclint
%patch6 -p1

# Remove werken-xpath Import/Export refences in OSGi manifest file
%patch7 -p1

%if %{without hsqldb}
rm -r src/test/org/apache/velocity/test/sql
%endif

# -----------------------------------------------------------------------------

%build

export CLASSPATH=$(build-classpath \
antlr \
apache-commons-collections \
commons-lang \
commons-logging \
glassfish-servlet-api \
junit \
jakarta-oro \
log4j:log4j:1.2.17 \
jaxen \
jdom \
bcel \
hsqldb \
junit)
ant \
  -buildfile build/build.xml \
  -Dbuild.sysclasspath=first \
  -Djavac.target=1.6 \
  -Djavac.source=1.6 \
  jar javadocs test

# fix line-endings in generated files
sed -i 's/\r//' docs/api/stylesheet.css docs/api/package-list

# -----------------------------------------------------------------------------

%install
%mvn_file : %{name}
%mvn_alias : %{name}:%{name}
%mvn_artifact pom.xml bin/%{name}-%{version}.jar
%mvn_install -J docs/api

# zero-length file
rm -r test/issues/velocity-537/compare/velocity537.vm.cmp
# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -pr examples test %{buildroot}%{_datadir}/%{name}


%files -f .mfiles
%doc README.txt
%doc LICENSE NOTICE

%files manual
%doc LICENSE NOTICE
%doc docs/*

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%files demo
%doc LICENSE NOTICE
%{_datadir}/%{name}

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_21jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_20jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_19jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_18jpp8
- unbootstrap build

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_7jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_6jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_5jpp7
- new version

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt3_1jpp6
- fixed build

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt2_1jpp6
- added velocity:velocity jppmap

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_1jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt2_4jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_3jpp5
- converted from JPackage by jppimport script

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_2jpp1.7
- pom fixes

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_1jpp1.7
- updated to new jpackage release

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_6jpp1.7
- import from jpackage;set epoch 1; overrides unstable version

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.3
- rebuild with excalibur-avalon-logkit

* Fri Dec 02 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.2
- nightly build 20051125053934 

* Sat May 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.1
- 1.5-dev
- svn snapshot 20050507

* Fri May 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Initial build for ALT Linux Sisyphus

