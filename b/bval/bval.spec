# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name bval
%define version 0.5
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
# disable guice module for now
%global with_guice 0
Name:          bval
Version:       0.5
Release:       alt1_4jpp7
Summary:       Apache Bean Validation
Group:         Development/Java
License:       ASL 2.0
Url:           http://bval.apache.org/
Source0:       http://www.apache.org/dist/%{name}/%{namedversion}/%{name}-parent-%{namedversion}-source-release.zip

Patch0:        %{name}-0.3-incubating-core-FeaturesCapable.patch
# change org.codehaus.mojo jaxb2-maven-plugin with maven-jaxb22-plugin
# change org.apache.geronimo.specs geronimo-jpa_2.0_spec 1.1 with org.hibernate.javax.persistence hibernate-jpa-2.0-api 1.0.1.Final
Patch1:        %{name}-0.4-jsr303-pom.patch
# fix jaxb 2.2 apis
Patch2:        %{name}-0.4-jsr303-fix-jaxb-apis.patch

BuildRequires: jpackage-utils

BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-lang3
BuildRequires: bean-validation-api
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
Requires:      aopalliance
Requires:      atinject
Requires:      google-guice
%endif

Requires:      apache-commons-beanutils
Requires:      apache-commons-lang3
Requires:      bean-validation-api
Requires:      freemarker
Requires:      geronimo-validation
Requires:      glassfish-jaxb
Requires:      glassfish-jaxb-api
Requires:      hibernate-jpa-2.0-api
Requires:      slf4j
Requires:      xstream

# test deps
BuildRequires: geronimo-osgi-support
BuildRequires: junit
BuildRequires: mockito

BuildRequires: apache-rat-plugin
BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jaxb2-plugin
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Apache BVal delivers an implementation of the Bean Validation
Specification (JSR303), which is TCK compliant and
works on Java SE 5 or later. The initial codebase for the
project was donated to the ASF by a SGA from Agimatec GmbH.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-parent-%{namedversion}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p0
%patch1 -p0
%patch2 -p0

# Don't use buildnumber-plugin, because jna is required and currently broken in f17
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin bval-xstream
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin org.codehaus.mojo:jdepend-maven-plugin


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

# unavailable deps
# org.hibernate.jsr303.tck jsr303-tck 1.0.6.GA
# org.jboss.test-harness jboss-test-harness-jboss-as-51 1.0.0
%pom_disable_module bval-tck

%pom_disable_module bundle

# fix non ASCII chars
for s in bval-extras/src/main/java/org/apache/bval/extras/constraints/net/DomainValidator.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%build

mvn-rpmbuild -Dri -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

# bundle guice tck
mkdir -p %{buildroot}%{_javadir}/%{name}
for m in core \
  extras \
  json \
  jsr303 \
  xstream;do
    install -m 644 %{name}-${m}/target/%{name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
    install -pm 644 %{name}-${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc CHANGES.txt LICENSE NOTICE README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4jpp7
- new release

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1jpp7
- new fc release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_3jpp7
- fc version

