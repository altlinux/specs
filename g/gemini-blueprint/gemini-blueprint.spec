Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name gemini-blueprint
%define version 1.0.2
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
%global dotname gemini.blueprint
Name:          gemini-blueprint
Version:       1.0.2
Release:       alt1_10jpp8
Summary:       Reference Implementation of the OSGi Blueprint Service
# BSD file - test-support/src/main/java/org/eclipse/gemini/blueprint/test/internal/util/DependencyVisitor.java,
License:       ASL 2.0 and BSD and EPL
URL:           http://www.eclipse.org/gemini/
# https://github.com/glyn/Gemini-Blueprint
Source0:       https://github.com/eclipse/gemini.blueprint/archive/%{namedversion}.tar.gz
# add maven-{bundle,jar}-plugin configuration
Patch0:        %{name}-%{namedversion}-add-osgi-manifests.patch

BuildRequires: aopalliance
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: log4j12
BuildRequires: springframework
BuildRequires: springframework-aop
BuildRequires: springframework-beans
BuildRequires: springframework-context
BuildRequires: springframework-context-support
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle

# test deps
BuildRequires: easymock3
BuildRequires: junit
BuildRequires: multithreadedtc
# BuildRequires: springframework-test

BuildArch:     noarch
Source44: import.info

%description
Eclipse Gemini Blueprint project makes it
easy to build Java applications that run
in an OSGi framework. 
By using Gemini Blueprint, applications
benefit from using a better separation of
modules, the ability to dynamically add,
remove, and update modules in a running system,
the ability to deploy multiple versions of a
module simultaneously (and have clients
automatically bind to the appropriate one),
and a dynamic service model.

NOTE: Eclipse Gemini Blueprint can be considered the
successor of Spring DM (OSGi) 2.x (http://www.springsource.org/osgi).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{dotname}-%{namedversion}
%patch0 -p1

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-bundle-plugin']/pom:configuration/pom:instructions" "
<Bundle-Activator>org.eclipse.gemini.blueprint.extender.internal.boot.ChainActivator</Bundle-Activator>" extender

find . -name "*.class" -delete
find . -name "*.jar" -type f -delete

%pom_remove_plugin com.springsource.bundlor:com.springsource.bundlor.maven
%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin

# remove org.springframework.build.aws.maven
%pom_xpath_remove pom:extensions
# remove clover knopflerfish profiles (todo remove also eclipse/equinox and org.apache.felix profiles)
%pom_xpath_remove pom:profiles

# TODO require:
# org.springframework spring-test
# org.knopflerfish framework
# org.apache.felix org.apache.felix.main
# org.eclipse.osgi org.eclipse.osgi
%pom_disable_module test-support
%pom_remove_dep org.eclipse.gemini.blueprint:gemini-blueprint-test

# build deps
%pom_remove_dep org.springframework:spring-test
%pom_remove_dep org.springframework:spring-test core
# require org.springframework:org.springframework.test*
rm -r core/src/test/java/org/eclipse/gemini/blueprint/internal/util/BeanFactoryUtilsTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/DictionaryEditorTest.java

%pom_remove_dep log4j:log4j
%pom_remove_dep org.apache.log4j:com.springsource.org.apache.log4j
%pom_add_dep log4j:log4j:1.2.17
%pom_remove_dep org.junit:com.springsource.org.junit
%pom_add_dep junit:junit:4.11:test

%pom_remove_dep org.aopalliance: core
%pom_add_dep aopalliance:aopalliance::provided core

%pom_remove_dep org.aopalliance: extender
%pom_add_dep aopalliance:aopalliance::test extender

%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId = 'multithreadedtc' ]/pom:groupId" edu.umd.cs core

%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:version = '1.0.0' ]/pom:artifactId" aopalliance
%pom_xpath_set "pom:project/pom:dependencyManagement/pom:dependencies/pom:dependency[pom:version = '1.0.0' ]/pom:groupId" aopalliance

# migrate from easymock 1 to easymock 3
%pom_remove_dep easymock:
%pom_add_dep org.easymock:easymock:3.2:test
rm -r mock/src/test/java/org/eclipse/gemini/blueprint/mock/MockServiceRegistrationTest.java \
 extender/src/test/java/org/eclipse/gemini/blueprint/extender/internal/ContextLoaderListenerTest.java \
 io/src/test/java/org/eclipse/gemini/blueprint/io/OsgiBundleResourceLoaderTest.java \
 io/src/test/java/org/eclipse/gemini/blueprint/io/OsgiBundleResourceTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/config/internal/OsgiServiceLifecycleListenerAdapterTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/config/internal/OsgiServiceRegistrationListenerAdapterTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/config/BundleFactoryBeanParserTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/context/support/AbstractBundleXmlApplicationContextTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/context/support/AbstractRefreshableOsgiBundleApplicationContextTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/context/support/BundleContextAwareProcessorTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/util/BundleDelegatingClassLoaderTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/service/OsgiServiceReferenceUtilsTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/service/importer/OsgiSingleServiceProxyFactoryBeanTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/service/importer/OsgiServiceCollectionProxyFactoryBeanTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/service/OsgiServiceUtilsTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/service/exporter/support/internal/support/ServiceRegistrationWrapperTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/service/exporter/support/OsgiServiceFactoryBeanTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/service/exporter/BeanNameServicePropertiesResolverTest.java \
 core/src/test/java/org/eclipse/gemini/blueprint/compendium/internal/cm/ConfigurationAdminManagerTest.java

# Fix CRLF
sed 's/\r//' -i changelog.txt license-apache.txt readme-building.txt readme.txt

rm -r core/src/test/java/org/eclipse/gemini/blueprint/blueprint/ReflectionTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/ComponentElementTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/ComponentSubElementTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/ConstructorInjectionTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/MixedRfc124BeansTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/NestedElementsTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/SchemaWithLocationTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/SpringDmRfc124Test.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/SpringRootConfigTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/config/TypeConverterTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/container/BlueprintFieldsTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/container/CycleTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/container/GenericsTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/container/LazyExporterTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/container/TestBlueprintBuiltinConvertersTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/container/TestLazyBeansTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/metadata/BundleContextApiTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/metadata/ImporterMetadataTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/metadata/BeanComponentMetadataTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/metadata/DefaultsTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/metadata/ExporterMetadataTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/metadata/ImporterCollectionsMetadataTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/blueprint/reflect/NestedDefinitionMetadataTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/compendium/config/CmConfigAndCtxPropertiesConfigurationTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/compendium/config/ConfigPropertiesHandlerTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/compendium/config/ManagedPropertiesTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/compendium/config/ManagedServiceFactoryTest.java \

%build

# some test fails for unavailable build deps*
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc about.html changelog.txt readme-building.txt readme.txt
%doc epl-v10.html license-apache.txt notice.html 

%files javadoc -f .mfiles-javadoc
%doc epl-v10.html license-apache.txt notice.html

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_10jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_9jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new release

