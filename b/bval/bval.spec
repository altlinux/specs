BuildRequires: xpp3-minimal
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name bval
%define version 0.4
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
# disable guice module for now
%global with_guice 0
Name:          bval
Version:       0.4
Release:       alt1_3jpp7
Summary:       Apache Bean Validation
Group:         Development/Java
License:       ASL 2.0
Url:           http://bval.apache.org/
Source0:       http://www.apache.org/dist/%{name}/%{namedversion}/%{name}-parent-%{namedversion}-source-release.zip

# remove 
#    findbugs-maven-plugin
#    ianal-maven-plugin
#    jdepend-maven-plugin
# change org.apache.geronimo.specs geronimo-jpa_2.0_spec 1.1 with org.hibernate.javax.persistence hibernate-jpa-2.0-api 1.0.1.Final
Patch0:        %{name}-%{namedversion}-parent-pom.patch
Patch1:        %{name}-0.3-incubating-core-FeaturesCapable.patch
# change org.codehaus.mojo jaxb2-maven-plugin with maven-jaxb22-plugin
# change org.apache.geronimo.specs geronimo-jpa_2.0_spec 1.1 with org.hibernate.javax.persistence hibernate-jpa-2.0-api 1.0.1.Final
Patch2:        %{name}-%{namedversion}-jsr303-pom.patch
# fix jaxb 2.2 apis
Patch3:        %{name}-%{namedversion}-jsr303-fix-jaxb-apis.patch

# replace bundle with core and jsr303
Patch4:        %{name}-%{namedversion}-guice-pom.patch
# build failure bval-guice/src/main/java/org/apache/bval/guice/ValidationModule.java:[61,12] error: cannot find symbol
Patch5:        %{name}-%{namedversion}-disable-guice.patch

# replace bundle with core and jsr303
Patch6:        %{name}-%{namedversion}-extras-pom.patch
# fix koji build problems missing org.apache.geronimo.osgi.locator.ProviderLocator
Patch7:        %{name}-%{namedversion}-jsr303-osgi-locator.patch

BuildRequires: jpackage-utils

BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-lang3
BuildRequires: bean-validation-api
BuildRequires: freemarker
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
%patch3 -p0
%if %with_guice
%patch4 -p0
%else
%patch5 -p0
%endif
%patch6 -p0
%patch7 -p0

# unavailable deps
# org.hibernate.jsr303.tck jsr303-tck 1.0.6.GA
# org.jboss.test-harness jboss-test-harness-jboss-as-51 1.0.0
sed -i "s|<module>bval-tck</module>|<!--module>bval-tck</module-->|" pom.xml

sed -i "s|<module>bundle</module>|<!--module>bundle</module-->|" pom.xml

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
    install -m 644 bval-${m}/target/bval-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
    install -pm 644 bval-${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
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
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_3jpp7
- fc version

