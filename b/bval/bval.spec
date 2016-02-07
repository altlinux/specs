Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name bval
%define version 0.5
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
# disable guice module for now
%global with_guice 0
Name:          bval
Version:       0.5
Release:       alt1_11jpp8
Summary:       Apache Bean Validation
License:       ASL 2.0
Url:           http://bval.apache.org/
Source0:       http://www.apache.org/dist/%{name}/%{namedversion}/%{name}-parent-%{namedversion}-source-release.zip
# add JSR303 full support
Source1:       %{name}-0.5-depmap
Patch0:        %{name}-0.3-incubating-core-FeaturesCapable.patch
# fix jaxb 2.2 apis
Patch1:        %{name}-0.4-jsr303-fix-jaxb-apis.patch
# https://issues.apache.org/jira/browse/BVAL-127
Patch2:        bval-0.5-java8.patch

BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-lang3
#BuildRequires: bean-validation-api provides incopatible JSR349 APIs
BuildRequires: freemarker
BuildRequires: geronimo-parent-poms
BuildRequires: geronimo-validation
BuildRequires: glassfish-jaxb
BuildRequires: glassfish-jaxb-api
BuildRequires: hibernate-jpa-2.0-api
BuildRequires: slf4j
BuildRequires: xstream

%if %with_guice
BuildRequires: aopalliance
BuildRequires: atinject
BuildRequires: google-guice
%endif

# test deps
BuildRequires: geronimo-osgi-support
BuildRequires: junit
BuildRequires: mockito
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:slf4j-simple)

#BuildRequires: apache-rat-plugin
#BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: jaxb2-maven-plugin
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-surefire-provider-junit
# force JSR303 apis
Requires:      geronimo-validation
BuildArch:     noarch
Source44: import.info

%description
Apache BVal delivers an implementation of the Bean Validation
Specification (JSR303), which is TCK compliant and
works on Java SE 5 or later. The initial codebase for the
project was donated to the ASF by a SGA from Agimatec GmbH.

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

%patch0 -p0
%patch1 -p0
%patch2 -p1

# Don't use buildnumber-plugin, because jna is required and currently broken in f17
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin bval-xstream
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin
%pom_remove_plugin :maven-source-plugin


%pom_remove_dep org.apache.geronimo.specs:geronimo-jpa_2.0_spec
%pom_xpath_inject "pom:project/pom:dependencyManagement/pom:dependencies" "
  <dependency>
    <groupId>org.hibernate.javax.persistence</groupId>
    <artifactId>hibernate-jpa-2.0-api</artifactId>
    <version>1.0.1.Final</version>
  </dependency>"

%if %with_guice
# require guice with aop support
# build failure bval-guice/src/main/java/org/apache/bval/guice/ValidationModule.java:[61,12] error: cannot find symbol
%pom_remove_dep org.apache.bval:org.apache.bval.bundle bval-guice
%pom_xpath_inject "pom:project/pom:dependencies" '
  <dependency>
    <groupId>org.apache.bval</groupId>
    <artifactId>bval-core</artifactId>
    <version>${project.version}</version>
  </dependency>
  <dependency>
    <groupId>org.apache.bval</groupId>
    <artifactId>bval-jsr303</artifactId>
    <version>${project.version}</version>
  </dependency>' bval-guice
%else
%pom_disable_module bval-guice
%endif
%pom_remove_dep org.apache.bval:org.apache.bval.bundle bval-extras
%pom_xpath_inject "pom:project/pom:dependencies" '
  <dependency>
    <groupId>org.apache.bval</groupId>
    <artifactId>bval-core</artifactId>
    <version>${project.version}</version>
  </dependency>' bval-extras
%pom_xpath_inject "pom:project/pom:dependencies" '
  <dependency>
    <groupId>org.apache.bval</groupId>
    <artifactId>bval-jsr303</artifactId>
    <version>${project.version}</version>
  </dependency>' bval-extras

# fix koji build problems missing org.apache.geronimo.osgi.locator.ProviderLocator
%pom_xpath_inject "pom:project/pom:dependencies" '
  <dependency>
    <groupId>org.apache.geronimo.specs</groupId>
    <artifactId>geronimo-osgi-locator</artifactId>
    <version>1.0</version>
    <scope>test</scope>
  </dependency>' bval-jsr303

%pom_remove_dep :geronimo-jpa_2.0_spec bval-jsr303
%pom_xpath_inject "pom:project/pom:dependencies" '
  <dependency>
    <groupId>org.hibernate.javax.persistence</groupId>
    <artifactId>hibernate-jpa-2.0-api</artifactId>
    <scope>provided</scope>
    <optional>true</optional>
  </dependency>' bval-jsr303
  
# unavailable deps
# org.hibernate.jsr303.tck jsr303-tck 1.0.6.GA
# org.jboss.test-harness jboss-test-harness-jboss-as-51 1.0.0
%pom_disable_module bval-tck

%pom_disable_module bundle

# fix non ASCII chars
for s in bval-extras/src/main/java/org/apache/bval/extras/constraints/net/DomainValidator.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

# Break build
%pom_remove_plugin org.apache.rat:apache-rat-plugin
rm -r bval-xstream/src/test/java/org/apache/bval/xml/BeanValidatorTest.java \
 bval-xstream/src/test/java/org/apache/bval/xml/XMLMetaBeanInfosTest.java \
 bval-xstream/src/test/java/org/apache/bval/xml/XMLMetaBeanManagerTest.java \
 bval-json/src/test/java/org/apache/bval/json/JSONGeneratorTest.java \
 bval-jsr303/src/test/java/org/apache/bval/jsr303/ValidationTest.java

sed -i "s|<groupId>javax.validation</groupId>|<groupId>org.apache.geronimo.specs</groupId>|" \
 bval-jsr303/pom.xml bval-extras/pom.xml
sed -i "s|<artifactId>validation-api</artifactId>|<artifactId>geronimo-validation_1.0_spec</artifactId>|" \
 bval-jsr303/pom.xml bval-extras/pom.xml

%build

%mvn_file :%{name}-core %{name}/core
%mvn_file :%{name}-extras %{name}/extras
%mvn_file :%{name}-json %{name}/json
%mvn_file :%{name}-jsr303 %{name}/jsr303
%mvn_file :%{name}-xstream %{name}/xstream

%mvn_build -- -Dri -Dproject.build.sourceEncoding=UTF-8 \
 -Dmaven.local.depmap.file="%{SOURCE1}"

%install
%mvn_install 

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc CHANGES.txt README.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

