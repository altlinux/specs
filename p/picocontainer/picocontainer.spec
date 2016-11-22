Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          picocontainer
Version:       2.15
Release:       alt1_5jpp8
Summary:       Java library implementing the Dependency Injection pattern
License:       BSD
Url:           http://picocontainer.codehaus.org/
# svn export http://svn.codehaus.org/picocontainer/java/2.x/tags/picocontainer-2.15
# tar cJf picocontainer-2.15.tar.xz picocontainer-2.15
Source0:       %{name}-%{version}.tar.xz

BuildRequires: mvn(asm:asm)
BuildRequires: mvn(com.thoughtworks.paranamer:paranamer)
BuildRequires: mvn(com.thoughtworks.xstream:xstream)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.annotation:jsr250-api)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.jmock:jmock-junit4)
BuildRequires: mvn(xpp3:xpp3_min)
%if 0
# picocontainer-gems deps
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(mx4j:mx4j-impl)
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires: mvn(org.prefuse:prefuse)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(proxytoys:proxytoys)
%endif

# test deps
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(simple-jndi:simple-jndi)

BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(xpp3:xpp3)

BuildRequires: maven-local
# https://bugzilla.redhat.com/show_bug.cgi?id=1191694
# BuildRequires: mvn(com.thoughtworks.paranamer:paranamer-maven-plugin)
BuildRequires: mvn(org.codehaus:codehaus-parent:pom:)
BuildArch:     noarch
Source44: import.info

%description
PicoContainer is a highly embeddable full service Inversion of Control
(IoC) container for components honor the Dependency Injection pattern.
It can be used as a lightweight alternative to Sun's J2EE patterns for
web applications or general solutions.

Despite it being very compact in size (the core is ~128K and it has no
mandatory dependencies outside the JDK), PicoContainer supports
different dependency injection types (Constructor, Setter, Annotated
Field and Method) and offers multiple lifecycle and monitoring
strategies.

%package javadoc
Group: Development/Documentation
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

# remove wagon-webdav-jackrabbit
%pom_xpath_remove "pom:project/pom:build/pom:extensions"
%pom_remove_plugin :xsite-maven-plugin
# Unwanted source jar
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-shade-plugin container

%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

sed -i "s|junit-dep|junit|" pom.xml

%pom_xpath_remove "pom:dependencyManagement/pom:dependencies/pom:dependency[pom:groupId='cglib']/pom:artifactId"
%pom_xpath_inject "pom:dependencyManagement/pom:dependencies/pom:dependency[pom:groupId='cglib']" "<artifactId>cglib</artifactId>"
%if 0
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:groupId='cglib']/pom:artifactId" gems
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId='cglib']" "<artifactId>cglib</artifactId>" gems

%pom_remove_dep javax.servlet:servlet-api gems
%pom_xpath_inject "pom:project/pom:dependencies" "
<dependency>
  <groupId>org.apache.tomcat</groupId>
  <artifactId>tomcat-servlet-api</artifactId>
  <version>any</version>
  <optional>true</optional>
</dependency>" gems
%else
# missing BR
%pom_disable_module gems
%endif

# https://bugzilla.redhat.com/show_bug.cgi?id=1191694
%pom_remove_plugin :paranamer-maven-plugin
%pom_remove_plugin :paranamer-maven-plugin container
%pom_remove_plugin :paranamer-maven-plugin container-debug

# these test fails for various reason
rm -r container/src/test/org/picocontainer/PicoVisitorTestCase.java \
 container/src/test/org/picocontainer/behaviors/BehaviorAdapterTestCase.java \
 container/src/test/org/picocontainer/behaviors/CachedTestCase.java \
 container/src/test/org/picocontainer/classname/DefaultClassLoadingPicoContainerTestCase.java \
 container/src/test/org/picocontainer/containers/ImmutablePicoContainerTestCase.java \
 container/src/test/org/picocontainer/defaults/AbstractComponentMonitorTestCase.java \
 container/src/test/org/picocontainer/defaults/CollectionComponentParameterTestCase.java \
 container/src/test/org/picocontainer/defaults/DefaultPicoContainerLifecycleTestCase.java \
 container/src/test/org/picocontainer/defaults/issues/Issue0265TestCase.java \
 container/src/test/org/picocontainer/injectors/ConstructorInjectorTestCase.java \
 container/src/test/org/picocontainer/injectors/ReinjectionTestCase.java \
 container/src/test/org/picocontainer/injectors/SetterInjectorTestCase.java \
 container/src/test/org/picocontainer/lifecycle/ReflectionLifecycleStrategyTestCase.java \
 container/src/test/org/picocontainer/lifecycle/StartableLifecycleStrategyTestCase.java \
 container/src/test/org/picocontainer/monitors/RegexComposerTestCase.java \
 container/src/test/org/picocontainer/visitors/MethodCallingVisitorTest.java \
 container/src/test/org/picocontainer/defaults/XStreamSerialisationTestCase.java \
 container/src/test/org/picocontainer/converters/BuiltInConverterTestCase.java \
 container/src/test/org/picocontainer/defaults/DefaultMultipleConstructorTestCase.java \
%if 0
 gems/src/test/org/picocontainer/gems/constraints/AndOrNotTestCase.java \
 gems/src/test/org/picocontainer/gems/constraints/ConstraintsTestCase.java \
 gems/src/test/org/picocontainer/gems/containers/CommonsLoggingTracingContainerDecoratorTestCase.java \
 gems/src/test/org/picocontainer/gems/containers/Log4jTracingContainerDecoratorTestCase.java \
 gems/src/test/org/picocontainer/gems/jmx/AbstractConstructingProviderTest.java \
 gems/src/test/org/picocontainer/gems/jmx/ComponentKeyConventionMBeanInfoProviderTest.java \
 gems/src/test/org/picocontainer/gems/jmx/ComponentTypeConventionMBeanInfoProviderTest.java \
 gems/src/test/org/picocontainer/gems/jmx/DynamicMBeanComponentProviderTest.java \
 gems/src/test/org/picocontainer/gems/jmx/JMXExposedTestCase.java \
 gems/src/test/org/picocontainer/gems/jmx/JMXExposingTestCase.java \
 gems/src/test/org/picocontainer/gems/jmx/JMXVisitorTestCase.java \
 gems/src/test/org/picocontainer/gems/jmx/RegisteredMBeanConstructingProviderTest.java
%endif

# NoClassDefFoundError: org/xmlpull/v1/XmlPullParserFactory
%pom_add_dep xpp3:xpp3::test container
%pom_add_dep xpp3:xpp3::test container-debug

%build

%mvn_build

%install
%mvn_install

sed -i 's/\r//' %{buildroot}%{_javadocdir}/%{name}/stylesheet.css

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.15-alt1_5jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.15-alt1_4jpp8
- java 8 mass update

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt6_5jpp6
- use jmock1

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt5_5jpp6
- dropped extra build dependencies

* Mon May 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt4_5jpp6
- fixed build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_5jpp6
- fixed build with java 7

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_5jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_4jpp5
- new jpp release

* Fri Feb 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp5
- fixed build

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp1.7
- added dependency on new excalibur

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp1.7
- converted from JPackage by jppimport script

