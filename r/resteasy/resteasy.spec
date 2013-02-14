BuildRequires: weld-parent
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name resteasy
%define version 2.3.2
%global namedreltag .Final
%global namedversion %{version}%{namedreltag}

Name: resteasy
Version: 2.3.2
Release: alt3_9jpp7
Summary: Framework for RESTful Web services and Java applications
Group: Development/Java
License: ASL 2.0 and CDDL
URL: http://www.jboss.org/resteasy

# git clone git://github.com/resteasy/Resteasy.git
# cd Resteasy
# git archive --prefix=resteasy-2.3.2.Final/ --output=resteasy-2.3.2.Final.tgz RESTEASY_JAXRS_2_3_2_FINAL
Source0: %{name}-%{namedversion}.tgz
Source33: resteasy-2.3.2-jpp-depmap.xml

Patch0: %{name}-%{namedversion}-remove-dependenciesA.patch
Patch1: %{name}-%{namedversion}-fix-tests.patch
Patch2: %{name}-%{namedversion}-remove-currently-unbuilt-modules.patch
Patch3: %{name}-%{namedversion}-fix-javadoc.patch
# Support for mime4j 0.7.2
Patch4: %{name}-%{namedversion}-mime4j-0.7.2.patch

BuildArch: noarch

BuildRequires: apache-commons-lang
BuildRequires: apache-commons-cli
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-collections
BuildRequires: apache-mime4j >= 0:0.7.2-2
BuildRequires: apache-james-project

BuildRequires: bea-stax
BuildRequires: bouncycastle
BuildRequires: bouncycastle-mail
BuildRequires: cglib
BuildRequires: codehaus-parent
BuildRequires: dnsjava
BuildRequires: geronimo-annotation
BuildRequires: glassfish-jaxb >= 0:2.2.5-2
BuildRequires: glassfish-jaxb-api
BuildRequires: google-guice
# BuildRequires: hibernate3-ejb3-persistence-3.0-api
# BuildRequires: hibernate-validator
BuildRequires: httpcomponents-client
BuildRequires: httpcomponents-core
BuildRequires: hsqldb
BuildRequires: httpunit
BuildRequires: jackson
BuildRequires: jakarta-commons-httpclient
BuildRequires: javamail
BuildRequires: javassist
BuildRequires: jandex >= 1.0.3-4
# BuildRequires: jboss-ejb3-ext-api
# BuildRequires: jbosscache-core
# BuildRequires: jboss-web
BuildRequires: jcip-annotations
BuildRequires: jettison
BuildRequires: jetty
BuildRequires: junit4
# BuildRequires: jyaml
# BuildRequires: liblog4j-java

# BuildRequires: oauth
BuildRequires: scannotation
BuildRequires: slf4j
BuildRequires: snakeyaml
#BuildRequires: spring3-core
#BuildRequires: spring3-test
#BuildRequires: spring3-web-servlet
BuildRequires: glassfish-fastinfoset
#BuildRequires: sun-sjsxp
BuildRequires: tomcat-el-2.2-api
BuildRequires: tomcat-servlet-3.0-api
BuildRequires: tomcat6-servlet-2.5-api
#BuildRequires: tomcat6
#BuildRequires: tomcat6-lib
BuildRequires: cdi-api
BuildRequires: xerces-j2

#BuildRequires: findbugs-maven-plugin
BuildRequires: jetty-version-maven-plugin
BuildRequires: maven
BuildRequires: maven-checkstyle-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-deploy-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jaxb2-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-pmd-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: maven-surefire-provider-junit4

BuildRequires: jboss-annotations-1.1-api

BuildRequires: jpackage-utils


# A:
Requires: apache-commons-cli
Requires: apache-commons-codec
Requires: apache-commons-collections
Requires: apache-commons-lang
Requires: apache-commons-logging
Requires: apache-mime4j >= 0:0.7.2-2

# B:
Requires: bea-stax
Requires: bouncycastle
Requires: bouncycastle-mail

# C:
Requires: cglib
Requires: cdi-api

# D:
Requires: dnsjava

# G:
Requires: geronimo-annotation
Requires: glassfish-fastinfoset
Requires: glassfish-jaxb >= 0:2.2.5-2
Requires: glassfish-jaxb-api
Requires: google-guice

# H:
Requires: httpcomponents-client
Requires: httpcomponents-core
Requires: httpunit

# J:
Requires: jackson
Requires: jakarta-commons-httpclient
Requires: javamail
Requires: javassist
Requires: jcip-annotations
Requires: jettison
Requires: jpackage-utils

# S:
Requires: scannotation
Requires: slf4j
Requires: snakeyaml

# T:
#Requires: tomcat6
#Requires: tomcat6-lib
Requires: tomcat-el-2.2-api
Requires: tomcat6-servlet-2.5-api
Requires: tomcat-servlet-3.0-api
Requires: ws-jaxme
Requires: xerces-j2
Source44: import.info

%description
RESTEasy contains a JBoss project that provides frameworks to help
build RESTful Web Services and RESTful Java applications. It is a fully
certified and portable implementation of the JAX-RS specification. 

%package javadoc
Summary: Javadocs for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1 -b .p0
%patch1 -p1 -b .p1
%patch2 -p1 -b .p2
%patch3 -p1
%patch4 -p1

%build
mvn-rpmbuild -Dmaven.local.depmap.file=%{SOURCE33} \
 -Dmaven.test.skip=true -e install javadoc:aggregate

%install

# Create the directories for jars and maven files:
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_mavendepmapfragdir}

# Install jars, poms and dependencies maps:
while read module_path artifact_id additional_aid_gid
do
  base_name=${module_path}/target/${artifact_id}-%{namedversion}
  jar_file=${base_name}.jar
  jandex_file=${base_name}-jandex.jar
  pom_file=${module_path}/pom.xml
  install -pm 644 ${pom_file} %{buildroot}%{_mavenpomdir}/JPP.%{name}-${artifact_id}.pom
  if [ -f ${jar_file} ]
  then
    install -pm 644 ${jar_file} %{buildroot}%{_javadir}/%{name}/${artifact_id}.jar

    # Create also the Jandex index files
    # Required by JBoss AS7
    java -cp $(build-classpath jandex) org.jboss.jandex.Main -j ${jar_file}
    install -pm 644 ${jandex_file} %{buildroot}%{_javadir}/%{name}/${artifact_id}-jandex.jar

    if [ -z "${additional_aid_gid}" ]
    then
      %add_maven_depmap JPP.%{name}-${artifact_id}.pom %{name}/${artifact_id}.jar
    else
      %add_maven_depmap JPP.%{name}-${artifact_id}.pom %{name}/${artifact_id}.jar -a ${additional_aid_gid}
    fi
  else
    %add_maven_depmap JPP.%{name}-${artifact_id}.pom
  fi
done <<'.'
. jaxrs-all
async-http-servlet-3.0 asynch-http-servlet-3.0
async-http-servlet-3.0/async-http-servlet-3.0 async-http-servlet-3.0
jaxrs-api jaxrs-api org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_1.1_spec
providers providers
providers/fastinfoset resteasy-fastinfoset-provider
providers/jackson resteasy-jackson-provider
providers/jaxb resteasy-jaxb-provider
providers/jettison resteasy-jettison-provider
providers/resteasy-atom resteasy-atom-provider
providers/resteasy-html resteasy-html
providers/multipart resteasy-multipart-provider
providers/yaml resteasy-yaml-provider
resteasy-bom resteasy-bom
resteasy-guice resteasy-guice
resteasy-jaxrs resteasy-jaxrs
resteasy-jsapi resteasy-jsapi
resteasy-cdi resteasy-cdi
tjws tjws
.

# To be added to the list above when dependencies are added to fedora to
# allow jars to be built:

# async-http-jbossweb/async-http-jbossweb-jar async-http-jbossweb
# async-http-tomcat/asynch-http-tomcat-jar async-http-tomcat6
# eagledns eagledns-fork
# providers/resteasy-hibernatevalidator-provider resteasy-hibernatevalidator-provider
# resteasy-cache/resteasy-cache-core resteasy-cache-core
# resteasy-links resteasy-links
# resteasy-spring resteasy-spring
# resteasy-crypto resteasy-crypto
# security/resteasy-oauth resteasy-oauth

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc License.html README.html

%files javadoc
%{_javadocdir}/%{name}
%doc License.html

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt3_9jpp7
- fixed build with new cdc - added BR: weld-parent

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_9jpp7
- fixed build

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_9jpp7
- new version

