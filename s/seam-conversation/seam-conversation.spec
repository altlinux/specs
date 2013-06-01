# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name seam-conversation
%define version 3.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:          seam-conversation
Version:       3.1.0
Release:       alt1_4jpp7
Summary:       Conversation management logic
Group:         Development/Java
License:       LGPLv2+
URL:           http://www.seamframework.org/
# git clone git://github.com/seam/conversation seam-conversation-3.1.0.Final
# (cd seam-conversation-3.1.0.Final/ && git archive --format=tar --prefix=seam-conversation-3.1.0.Final/ 3.1.0.Final | xz > ../seam-conversation-3.1.0.Final.tar.xz)
Source0:       %{name}-%{namedversion}.tar.xz
# force use jboss-servlet-3.0-api apis
Source1:       %{name}-%{namedversion}-depmap

BuildRequires: geronimo-parent-poms
BuildRequires: httpcomponents-project

BuildRequires: jpackage-utils
#BuildRequires: seam-parent
BuildRequires: weld-parent

BuildRequires: cdi-api
BuildRequires: jboss-jsf-2.1-api
BuildRequires: jboss-servlet-3.0-api
BuildRequires: tomcat-lib
BuildRequires: weld-api
BuildRequires: weld-core

%if 0
# test deps
BuildRequires: junit
BuildRequires: slf4j
BuildRequires: mvn(org.apache.openwebbeans:openwebbeans-resource)
BuildRequires: mvn(org.apache.openwebbeans:openwebbeans-tomcat6)
BuildRequires: mvn(org.apache.openwebbeans:openwebbeans-web)
#BuildRequires: mvn(org.apache.tomcat:catalina)
BuildRequires: mvn(org.glassfish.web:el-impl)
BuildRequires: mvn(org.jboss.arquillian.container:arquillian-tomcat-embedded-6)
BuildRequires: mvn(org.jboss.arquillian.junit:arquillian-junit-container)
BuildRequires: mvn(org.jboss.weld.servlet:weld-servlet-core)
BuildRequires: mvn(org.jboss.weld.servlet:weld-servlet-test-base)
%endif

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin

Requires:      cdi-api
Requires:      jboss-jsf-2.1-api
Requires:      jboss-servlet-3.0-api
Requires:      tomcat-lib
Requires:      weld-api
Requires:      weld-core

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
This is where different CDI impls should abstract its 
conversation management logic until that is part of the CDI spec.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
# seam-parent org.jboss.seam 19
%pom_remove_parent
sed -i 's|<version>${junit.version}|<version>any|' pom.xml
sed -i 's|<version>${slf4j.version}|<version>any|' pom.xml

%pom_remove_dep com.caucho:resin
%pom_remove_dep com.caucho:resin-javaee
%pom_disable_module candi
# TODO require openwebbeans (work in progress...)
%pom_remove_dep org.apache.openwebbeans:openwebbeans-impl
%pom_remove_dep org.apache.openwebbeans:openwebbeans-spi
%pom_disable_module owb

%pom_remove_dep org.apache.tomcat:coyote
%pom_remove_dep org.apache.tomcat:coyote weld
%pom_remove_dep org.jboss.arquillian.container:arquillian-tomcat-embedded-6 weld
sed -i "s|<artifactId>jasper|<artifactId>tomcat-jasper|" pom.xml
sed -i "s|<artifactId>catalina|<artifactId>tomcat-catalina|" pom.xml

%pom_remove_dep org.apache.tomcat:catalina weld
%pom_xpath_inject "pom:project/pom:dependencies" "
<dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-catalina</artifactId>
    <scope>test</scope>
</dependency>" weld
%pom_remove_dep org.apache.tomcat:jasper weld
%pom_xpath_inject "pom:project/pom:dependencies" "
<dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-jasper</artifactId>
    <scope>provided</scope>
      <exclusions>
        <exclusion>
          <groupId>org.apache.tomcat</groupId>
          <artifactId>el-api</artifactId>
        </exclusion>
        <exclusion>
          <groupId>org.apache.tomcat</groupId>
          <artifactId>tomcat-api</artifactId>
        </exclusion>
        <exclusion>
          <groupId>org.apache.tomcat</groupId>
          <artifactId>tomcat-util</artifactId>
        </exclusion>
        <exclusion>
          <groupId>org.eclipse.jdt.core.compiler</groupId>
          <artifactId>ecj</artifactId>
        </exclusion>
      </exclusions>
</dependency>" weld

%pom_remove_dep org.glassfish.web:el-impl
%pom_remove_dep org.glassfish.web:el-impl weld
%pom_xpath_inject "pom:project/pom:dependencies" "
      <dependency>
         <groupId>org.apache.tomcat</groupId>
         <artifactId>tomcat-jasper-el</artifactId>
         <scope>test</scope>
      </dependency>" weld
# see https://bugzilla.redhat.com/show_bug.cgi?id=825355
%pom_remove_dep org.jboss.weld:weld-core weld
%pom_xpath_inject "pom:project/pom:dependencies" "
<dependency>
    <groupId>org.jboss.weld</groupId>
    <artifactId>weld-core</artifactId>
    <scope>provided</scope>
      <exclusions>
        <exclusion>
          <groupId>org.jboss.weld</groupId>
          <artifactId>weld-build-config</artifactId>
        </exclusion>
      </exclusions>
</dependency>" weld

%build
# unavailable test deps
# org.jboss.weld.servlet weld-servlet-test-base
mvn-rpmbuild \
  -Dmaven.local.depmap.file="%{SOURCE1}" \
  -Dproject.build.sourceEncoding=UTF-8 \
  -Dmaven.test.skip=true \
  package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

mkdir -p %{buildroot}%{_javadir}
# candi
# owb
for m in spi \
      weld; do
    install -m 644 ${m}/target/%{name}-${m}.jar %{buildroot}%{_javadir}/%{name}-${m}.jar
    install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-${m}.pom
%add_maven_depmap JPP-%{name}-${m}.pom %{name}-${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-*.jar
%{_mavenpomdir}/JPP-%{name}*.pom
%{_mavendepmapfragdir}/%{name}
%doc README

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_4jpp7
- new release

