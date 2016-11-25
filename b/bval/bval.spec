Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name bval
%define version 1.1.1
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}

%if 0%{?fedora}
# https://bugzilla.redhat.com/show_bug.cgi?id=1289726
# https://issues.apache.org/jira/browse/BVAL-142
# https://issues.apache.org/jira/browse/WEAVER-10
#def_with commons-weaver
%bcond_with commons-weaver
%endif

Name:          bval
Version:       1.1.1
Release:       alt1_1jpp8
Summary:       Apache Bean Validation
License:       ASL 2.0
Url:           http://bval.apache.org/
Source0:       http://www.apache.org/dist/bval/%{namedversion}/%{name}-parent-%{namedversion}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(com.thoughtworks.xstream:xstream)
BuildRequires: mvn(commons-beanutils:commons-beanutils-core)
BuildRequires: mvn(javax.annotation:javax.annotation-api)
BuildRequires: mvn(javax.el:javax.el-api)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.validation:validation-api)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.commons:commons-lang3)
%if %{with commons-weaver}
BuildRequires: mvn(org.apache.commons:commons-weaver-privilizer)
BuildRequires: mvn(org.apache.commons:commons-weaver-privilizer-api)
BuildRequires: mvn(org.apache.commons:commons-weaver-processor)
BuildRequires: mvn(org.apache.commons:commons-weaver-maven-plugin)
%endif
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-interceptor_3.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.rat:apache-rat-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:jaxb2-maven-plugin)
BuildRequires: mvn(org.freemarker:freemarker)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(xpp3:xpp3)

BuildArch:     noarch
Source44: import.info

%description
Apache BVal delivers an implementation of the Bean Validation
Specification (JSR-303 and JSR-346), which is TCK compliant and
works on Java SE 5 or later. The initial codebase for the
project was donated to the ASF by a SGA from Agimatec GmbH.

%package extras
Group: Development/Java
Summary:       Apache BVal :: Extras

%description extras
BVal - non-JSR303 routines and constraints.

%package json
Group: Development/Java
Summary:       Apache BVal :: JSON

%description json
BVal - Optional JSON Component.

%package jsr
Group: Development/Java
Summary:       Apache BVal :: JSR 349

%description jsr
Implementation specific classes for JSR 349 Bean Validation 1.1.

%package parent
Group: Development/Java
Summary:       Apache BVal :: Parent POM

%description parent
Apache BVal Parent POM.

%package xstream
Group: Development/Java
Summary:       Apache BVal :: XStream

%description xstream
BVal XML Metadata with XStream.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-parent-%{namedversion}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%pom_disable_module bval-tck
# org.hibernate.beanvalidation.tck:beanvalidation-tck-tests:1.1.3.Final
%pom_disable_module bval-tck11
%pom_disable_module bundle

%pom_xpath_remove pom:Embed-Dependency bundle

%pom_remove_plugin -r :findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin -r :maven-source-plugin

# NoClassDefFoundError: org/xmlpull/v1/XmlPullParserFactory
%pom_add_dep xpp3:xpp3:1.1.4c:test %{name}-json
%pom_add_dep xpp3:xpp3:1.1.4c:test %{name}-xstream

%if %{without commons-weaver}
# Remove commons-weaver support
%pom_remove_plugin -r :commons-weaver-maven-plugin
%pom_remove_dep -r :commons-weaver-privilizer-api
sed -i '/Privilizing/d' \
 bval-core/src/main/java/org/apache/bval/model/MetaBean.java \
 bval-core/src/main/java/org/apache/bval/util/BValVersion.java \
 bval-core/src/main/java/org/apache/bval/util/FieldAccess.java \
 bval-core/src/main/java/org/apache/bval/util/MethodAccess.java \
 bval-core/src/main/java/org/apache/bval/util/reflection/Reflection.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/AnnotationConstraintBuilder.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/AnnotationProcessor.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/ApacheFactoryContext.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/ApacheValidatorFactory.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/BeanDescriptorImpl.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/ClassValidator.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/ConfigurationImpl.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/ConstraintAnnotationAttributes.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/ConstraintDefaults.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/DefaultMessageInterpolator.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/DefaultValidationProviderResolver.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/JsrMetaBeanFactory.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/resolver/DefaultTraversableResolver.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/xml/AnnotationProxyBuilder.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/xml/ValidationMappingParser.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/xml/ValidationParser.java \
 bval-xstream/src/main/java/org/apache/bval/xml/XMLMetaBeanManager.java
sed -i '/Privileged/d' \
 bval-jsr/src/main/java/org/apache/bval/jsr/AnnotationConstraintBuilder.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/ApacheValidatorFactory.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/ConfigurationImpl.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/xml/AnnotationProxyBuilder.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/xml/ValidationMappingParser.java \
 bval-jsr/src/main/java/org/apache/bval/jsr/xml/ValidationParser.java
%endif

%pom_change_dep -r :geronimo-annotation_1.2_spec javax.annotation:javax.annotation-api:1.2
%pom_change_dep -r :geronimo-atinject_1.0_spec javax.inject:javax.inject:1
%pom_change_dep -r :geronimo-interceptor_1.2_spec :geronimo-interceptor_3.0_spec
# https://bugzilla.redhat.com/show_bug.cgi?id=1276632
%pom_change_dep -r :geronimo-jcdi_1.1_spec javax.enterprise:cdi-api:1.1
%pom_change_dep -r :geronimo-jpa_2.0_spec org.hibernate.javax.persistence:hibernate-jpa-2.1-api:1.0.0.Draft-16

%pom_change_dep -r :tomcat-el-api javax.el:javax.el-api:3.0.0

%mvn_alias :bval-jsr :bval-jsr303
%mvn_package ":{*}::tests:" @1

%build

%mvn_build -s -- -Dri -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install 

%files -f .mfiles-%{name}-core
%doc CHANGES.txt README.txt RELEASE-NOTES.adoc
%doc LICENSE NOTICE

%files extras -f .mfiles-%{name}-extras
%files json -f .mfiles-%{name}-json
%files jsr -f .mfiles-%{name}-jsr
%files parent -f .mfiles-%{name}-parent
%doc LICENSE NOTICE
%files xstream -f .mfiles-%{name}-xstream

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_11jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4jpp7
- new release

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1jpp7
- new fc release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_3jpp7
- fc version

