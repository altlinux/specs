BuildRequires: maven-plugin-plugin
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cxf
%define version 2.6.9
# vim: set ts=4 sw=4 sts=4 et:
%global tarname apache-%{name}-%{version}-src

Name:           cxf
Epoch:          1
Version:        2.6.9
Release:        alt2_1jpp7
Summary:        Apache CXF
License:        ASL 2.0
Group:          Development/Java
URL:            http://cxf.apache.org/

Source0:        http://archive.apache.org/dist/%{name}/%{version}/%{tarname}.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-archetype-packaging
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-shared-artifact-resolver
BuildRequires:  maven-shared-downloader
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-war-plugin
BuildRequires:  apache-commons-lang
BuildRequires:  apache-mina
BuildRequires:  aries-blueprint
BuildRequires:  asm2
BuildRequires:  batik
BuildRequires:  bouncycastle
BuildRequires:  cglib
BuildRequires:  cxf-build-utils
BuildRequires:  cxf-xjc-utils
BuildRequires:  ehcache-core
BuildRequires:  felix-osgi-core
BuildRequires:  geronimo-annotation
BuildRequires:  geronimo-saaj
BuildRequires:  glassfish-jaxb
BuildRequires:  glassfish-jaxb-api
BuildRequires:  glassfish-fastinfoset
BuildRequires:  javamail
BuildRequires:  jboss-connector-1.6-api
BuildRequires:  jboss-servlet-3.0-api
BuildRequires:  jboss-jaxws-2.2-api
BuildRequires:  jibx
BuildRequires:  jra
BuildRequires:  neethi
BuildRequires:  opensaml-java
BuildRequires:  opensaml-java-parent
BuildRequires:  springframework >= 3.1.1-9
BuildRequires:  springframework-aop
BuildRequires:  springframework-beans
BuildRequires:  springframework-context
BuildRequires:  springframework-jms
BuildRequires:  springframework-tx
BuildRequires:  springframework-web
BuildRequires:  springframework-webmvc
BuildRequires:  velocity
BuildRequires:  wsdl4j
BuildRequires:  wss4j >= 1.6
BuildRequires:  xml-commons-resolver
BuildRequires:  ws-xmlschema

Requires:       apache-commons-lang
Requires:       bouncycastle
Requires:       cxf-xjc-utils
Requires:       cglib
Requires:       ehcache-core
Requires:       geronimo-annotation
Requires:       glassfish-jaxb
Requires:       jboss-connector-1.6-api
Requires:       jboss-servlet-3.0-api
Requires:       jboss-jaxws-2.2-api
Requires:       jpackage-utils
Requires:       jra
Requires:       neethi
Requires:       opensaml-java
Requires:       ws-xmlschema
Requires:       wsdl4j
Requires:       wss4j >= 1.6
Source44: import.info

%description
Apache CXF is an open-source services framework that aids in
the development of services using front-end programming APIs,
like JAX-WS and JAX-RS.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package api
Summary:        Apache CXF API
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-common = %{epoch}:%{version}-%{release}
Provides:       %{name}-common = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-common < 2.4.9-4

%description api
Apache CXF API classes.

%package maven-plugins
Summary:        Apache CXF Maven Plugins
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-api = %{epoch}:%{version}-%{release}

%description maven-plugins
Maven plugins required for building or testing Apache CXF.


%package rt
Summary:        Apache CXF Runtime
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-api = %{epoch}:%{version}-%{release}
Requires:       %{name}-tools = %{epoch}:%{version}-%{release}
Requires:       apache-mina
Requires:       aries-blueprint
Requires:       asm2
Requires:       felix-osgi-core
Requires:       glassfish-fastinfoset
Requires:       javamail
Requires:       jibx
Requires:       springframework
Requires:       springframework-aop
Requires:       springframework-beans
Requires:       springframework-context
Requires:       springframework-jms
Requires:       springframework-tx
Requires:       springframework-web
Requires:       springframework-webmvc
Requires:       xml-commons-resolver

%description rt
This package contains core feature set of Apache CXF;
web service standards support, frontends, and protocols
support.

%package services
Summary:        Apache CXF Services
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-api = %{epoch}:%{version}-%{release}
Requires:       %{name}-rt = %{epoch}:%{version}-%{release}
Requires:       geronimo-jms
Requires:       felix-osgi-core
Requires:       aries-blueprint
#Requires:       activemq

%description services
This package contains Apache CXF WSN services.

%package tools
Summary:        Apache CXF Tools
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires(pre):  %{name}-rt = %{epoch}:%{version}-%{release}
Requires:       velocity

%description tools
Apache CXF Command Line Tools.

%prep

%setup -q -n %{tarname}

# Replace cglib-nodep with cglib
find . -name "pom.xml" -print | xargs sed -i "s|>cglib<|>net.sf.cglib<|"
find . -name "pom.xml" -print | xargs sed -i "s|cglib-nodep|cglib|"

# Replace bcprov-jdk15 with bcprov-jdk16
find . -name "pom.xml" -print | xargs sed -i "s|bcprov-jdk15|bcprov-jdk16|;s|bcprov-jdk16on|bcprov-jdk16|"

# Not necessary for javadoc generation
%pom_remove_plugin "org.apache.maven.plugins:maven-dependency-plugin" distribution/pom.xml

sed -i "s|<cxf.servlet-api.group>org.apache.geronimo.specs</cxf.servlet-api.group>|<cxf.servlet-api.group>org.jboss.spec.javax.servlet</cxf.servlet-api.group>|" parent/pom.xml
sed -i "s|<cxf.servlet-api.artifact>geronimo-servlet_3.0_spec</cxf.servlet-api.artifact>|<cxf.servlet-api.artifact>jboss-servlet-api_3.0_spec</cxf.servlet-api.artifact>|" parent/pom.xml

# Replace selected Geronimo APIs with other implementations
while read gid aid newgid newaid version
do

for f in $(grep "<artifactId>${aid}</artifactId>" --include "pom.xml" --exclude-dir "*samples*" -r | awk -F: '{ print $1 }' | uniq)
do

%pom_remove_dep "${gid}:${aid}" ${f}
%pom_xpath_inject "pom:dependencies" "<dependency><groupId>${newgid}</groupId><artifactId>${newaid}</artifactId></dependency>" ${f}

done

# Make sure we add the version requirements for just added APIs in parent pom.xml
%pom_xpath_inject "pom:dependencyManagement/pom:dependencies/pom:dependency[pom:artifactId='${newaid}']" "<version>${version}</version>" parent/pom.xml

done <<EOF
org.apache.geronimo.specs geronimo-j2ee-connector_1.5_spec org.jboss.spec.javax.resource jboss-connector-api_1.6_spec 1.0.1.Final
org.apache.geronimo.specs geronimo-jaxws_2.2_spec org.jboss.spec.javax.xml.ws jboss-jaxws-api_2.2_spec 2.0.2.Final
org.apache.geronimo.specs geronimo-javamail_1.4_spec javax.mail mail 1.4.3
EOF

# Disable main modules
%pom_disable_module "testutils"
%pom_disable_module "integration"
%pom_disable_module "osgi/karaf"
%pom_disable_module "osgi/bundle"
%pom_disable_module "systests"

# Disable common submodules
%pom_disable_module wstx-msv-validation common/pom.xml
%pom_disable_module xerces-xsd-validation common/pom.xml

# Disable Maven plugins submodules
# Requires jsr-339, jaxrs 2.0
%pom_disable_module "codegen-plugin" maven-plugins/pom.xml
# Requires jsr-339, jaxrs 2.0
%pom_disable_module "wadl2java-plugin" maven-plugins/pom.xml
%pom_disable_module "wsdl-validator-plugin" maven-plugins/pom.xml
%pom_disable_module "corba" maven-plugins/pom.xml
%pom_disable_module "archetypes" maven-plugins/pom.xml

# Disable rt submodules
%pom_disable_module "corba" rt/bindings/pom.xml
%pom_disable_module "databinding/xmlbeans" rt/pom.xml
%pom_disable_module "databinding/sdo" rt/pom.xml

# Requires jsr-339, jaxrs 2.0
%pom_disable_module "frontend/jaxrs" rt/pom.xml
%pom_disable_module "transports/http-jetty" rt/pom.xml
# Available in cxf 2.7.x
#%pom_disable_module "transports/http-hc" rt/pom.xml
%pom_disable_module "management-web" rt/pom.xml
%pom_disable_module "rs/extensions/providers" rt/pom.xml
%pom_disable_module "rs/extensions/search" rt/pom.xml

%pom_disable_module "rs/security/xml" rt/pom.xml
%pom_disable_module "rs/security/sso/saml" rt/pom.xml
%pom_disable_module "rs/security/oauth-parent" rt/pom.xml
%pom_disable_module "rs/security/cors" rt/pom.xml

%pom_disable_module "javascript-tests" rt/javascript/pom.xml

# Disable tools submodules
# Requires jsr-339, jaxrs 2.0
%pom_disable_module "wadlto" tools/pom.xml
%pom_disable_module "corba" tools/pom.xml
# Requires jsr-339, jaxrs 2.0
%pom_disable_module "frontend/javascript" tools/wsdlto/pom.xml
%pom_disable_module "test" tools/wsdlto/pom.xml
%pom_disable_module "misc" tools/wsdlto/pom.xml

#%pom_disable_module "sts" services/pom.xml
%pom_disable_module "wsn" services/pom.xml
# Available in cxf 2.7.x
#%pom_disable_module "ws-discovery" services/pom.xml
%pom_disable_module "systests" services/sts/pom.xml

%pom_remove_dep "org.springframework.ldap:spring-ldap-core" services/sts/sts-core/pom.xml
%pom_remove_dep "org.springframework.ldap:spring-ldap-core" services/sts/sts-war/pom.xml
%pom_remove_dep "com.hazelcast:hazelcast" services/sts/sts-core/pom.xml
%pom_remove_dep "com.hazelcast:hazelcast" services/sts/sts-war/pom.xml

# Remove test deps
for m in rt/frontend/simple rt/bindings/xml rt/frontend/jaxws rt/databinding/aegis tools/javato/ws rt/databinding/jibx rt/bindings/object rt/bindings/coloc rt/management rt/transports/jms rt/ws/rm; do
%pom_remove_dep "org.apache.cxf:cxf-testutils" ${m}/pom.xml
done

%pom_remove_dep "org.springframework:spring-test" rt/ws/policy/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-wstx-msv-validation" rt/databinding/aegis/pom.xml


%pom_remove_dep "org.apache.cxf:cxf-rt-transports-http-jetty" rt/databinding/aegis/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-rt-transports-http-jetty" tools/javato/ws/pom.xml
%pom_remove_dep "org.apache.cxf:cxf-rt-transports-http-jetty" rt/bindings/object/pom.xml

%pom_remove_dep "org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec" rt/transports/jms/pom.xml
%pom_remove_dep "org.apache.activemq:activemq-core" rt/transports/jms/pom.xml
%pom_remove_dep "org.apache.xbean:xbean-spring" rt/transports/jms/pom.xml

rm services/sts/sts-core/src/main/java/org/apache/cxf/sts/cache/HazelCastTokenStore.java
rm services/sts/sts-core/src/main/java/org/apache/cxf/sts/claims/LdapClaimsHandler.java

# Disable codegen plugin
%pom_remove_plugin "org.apache.cxf:cxf-codegen-plugin" rt/ws/policy/pom.xml
%pom_remove_plugin "org.apache.cxf:cxf-codegen-plugin" tools/javato/ws/pom.xml

# Disable checkstyle plugin
%pom_remove_plugin "org.apache.maven.plugins:maven-checkstyle-plugin" parent/pom.xml

# Disable pmd plugin
%pom_remove_plugin "org.apache.maven.plugins:maven-pmd-plugin" parent/pom.xml

# Disable remote-resources-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-remote-resources-plugin']" parent/pom.xml

# Disable xsdvalidation
%pom_remove_dep "org.apache.cxf:cxf-xerces-xsd-validation" rt/frontend/simple/pom.xml

# Fix java.lang.NoClassDefFoundError: org/w3c/dom/ElementTraversal
%pom_xpath_inject "pom:dependencies" "<dependency><groupId>org.apache.xmlgraphics</groupId><artifactId>batik-ext</artifactId><version>1.8</version><scope>runtime</scope></dependency>" tools/common/pom.xml

find . -name "*.jar" -delete
find . -name "*.class" -delete

iconv -f macintosh -t utf8 < licenses/cdd1-1.0.txt > cdd.txt
mv -f cdd.txt licenses/cdd1-1.0.txt

%build
# tests are disabled because of lots of missing dependencies
mvn-rpmbuild \
    -Pfastinstall \
    -Dmaven.test.skip=true \
    -Dmaven.local.depmap.file=%{_mavendepmapfragdir}/tomcat-tomcat-servlet-api \
    -Dproject.build.sourceEncoding=UTF-8 \
    package javadoc:aggregate


%install

install_pom_file ()
{
    local pom_file=${1}
    local module=${2}
    install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/${pom_file}
    %add_maven_depmap ${pom_file} -f ${module}
}

install_jar_file ()
{
    local pom_file=${1}
    local source=${2}
    local target=${3}
    local module=${4}

    install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/${pom_file}
    install -pm 644 ${source} %{buildroot}%{_javadir}/${target}
    %add_maven_depmap ${pom_file} ${target} -f ${module}
}

guess_jar_file_and_target ()
{
    jar_found=true
    jar_file=""
    jar_target=""
    local guess

    echo "target/%{name}-${module}-${aid_name}-%{version}.jar"

    guess=target/%{name}-${module}-${aid_name}-%{version}.jar
    if [ -f ${guess} ]; then
        jar_file=${guess}
        jar_target=%{name}/${module}-${aid_name}.jar
        return 0
    fi

    guess=target/%{name}-${module}-${aid_name}-%{version}.jar
    if [ -f ${guess} ]; then
        jar_file=${guess}
        jar_target=%{name}/${module}-${aid_name}.jar
        return 0
    fi

    guess=target/%{name}-${module}-%{version}.jar
    if [ -f ${guess} ]; then
        jar_file=${guess}
        jar_target=%{name}/${module}.jar
        return 0
    fi

    guess=target/%{name}-${aid_name}-%{version}.jar
    if [ -f ${guess} ]; then
        jar_file=${guess}
        jar_target=%{name}/${module}-${aid_name}.jar
        return 0
    fi

    jar_found=false
}

install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

while read module subdir nontemplate_name
do
    dir=${module}/${subdir}

    pushd $dir

    if [ "${subdir}" = "" ]; then
        aid_name=""
        pom_file=JPP.%{name}-${module}.pom
    else
        aid_name=${nontemplate_name:-$(echo ${subdir} | tr / -)}
        pom_file=JPP.%{name}-${module}-${aid_name}.pom
    fi

    guess_jar_file_and_target

    if $jar_found; then
        install_jar_file ${pom_file} ${jar_file} ${jar_target} ${module}
    else
        install_pom_file ${pom_file} ${module}
    fi

    popd

done <<EOM
api
maven-plugins
maven-plugins java2ws-plugin
rt
rt bindings
rt bindings/coloc
rt bindings/object
rt bindings/soap
rt bindings/xml
rt core
rt databinding/jaxb
rt databinding/aegis
rt databinding/jibx
rt frontend/simple
rt frontend/jaxws
rt frontend/js
rt features/clustering
rt javascript
rt management
rt transports/http
rt transports/jms
rt transports/local
rt ws/addr
rt ws/policy
rt ws/mex
rt ws/rm
rt ws/security
services
services sts
services sts/sts-core sts-core
tools
tools common
tools javato
tools validator
tools wsdlto
tools wsdlto/core
tools wsdlto/databinding/jaxb
tools wsdlto/frontend/jaxws
EOM
#services wsn
#services wsn/wsn-core wsn-core
#services wsn/wsn-api wsn-api
#services wsn/wsn-osgi wsn-osgi
#services ws-discovery
#services ws-discovery/ws-discovery-api ws-discovery-api
#services ws-discovery/ws-discovery-service ws-discovery-service


# Available in 2.7.0
#rt transports/udp


# parents
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-cxf.pom
install -pm 644 parent/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom

# special cases
install -pm 644 tools/javato/ws/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-tools-java2ws.pom
install -pm 644 tools/javato/ws/target/cxf-tools-java2ws-%{version}.jar %{buildroot}%{_javadir}/%{name}/tools-java2ws.jar
%add_maven_depmap JPP.%{name}-tools-java2ws.pom %{name}/tools-java2ws.jar -f tools

%add_maven_depmap JPP.%{name}-cxf.pom
%add_maven_depmap JPP.%{name}-parent.pom

# javadoc
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc README LICENSE NOTICE
%doc licenses
%{_mavenpomdir}/JPP.%{name}-cxf.pom
%{_mavenpomdir}/JPP.%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}
%dir %{_javadir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%doc licenses
%{_javadocdir}/%{name}

%files api
%{_mavenpomdir}/JPP.%{name}-api.pom
%{_mavendepmapfragdir}/%{name}-api
%{_javadir}/%{name}/api.jar

%files maven-plugins
%{_mavenpomdir}/JPP.%{name}-maven-plugins*
%{_mavendepmapfragdir}/%{name}-maven-plugins
%{_javadir}/%{name}/maven-plugins-*

%files rt
%{_mavenpomdir}/JPP.%{name}-rt*
%{_mavendepmapfragdir}/%{name}-rt
%{_javadir}/%{name}/rt-*

%files services
%{_mavenpomdir}/JPP.%{name}-services*
%{_mavendepmapfragdir}/%{name}-services
%{_javadir}/%{name}/services-*

%files tools
%{_mavenpomdir}/JPP.%{name}-tools*
%{_mavendepmapfragdir}/%{name}-tools
%{_javadir}/%{name}/tools-*


%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.6.9-alt2_1jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.6.9-alt1_1jpp7
- update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.9-alt1_2jpp7
- new version

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.8-alt1_5jpp7
- new version

