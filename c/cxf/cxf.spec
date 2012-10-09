BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cxf
%define version 2.4.9
# vim: set ts=4 sw=4 sts=4 et:
%global tarname apache-%{name}-%{version}-src

Name:           cxf
Version:        2.4.9
Release:        alt1_2jpp7
Summary:        Apache CXF
License:        ASL 2.0
Group:          Development/Java
URL:            http://cxf.apache.org/

Source0:        http://archive.apache.org/dist/%{name}/%{version}/%{tarname}.tar.gz

Patch0:         0001-replace-geronimo-j2ee-connector.patch
Patch1:         0002-replace-cglib-nodep-with-cglib.patch
Patch2:         0003-disable-common-submodules.patch
Patch3:         0004-disable-maven-plugins-submodules.patch
Patch4:         0005-disable-modules.patch
Patch5:         0006-disable-rt-submodules.patch
Patch6:         0007-disable-tools-submodules.patch
Patch7:         0008-disable-plugin-for-ws-policy.patch
Patch8:         0009-replace-geronimo-javamail.patch
Patch9:         0010-disable-maven-remote-resources-plugin.patch
Patch10:        0011-disable-optional-xsd-validation.patch
Patch11:        0012-enable-http-jms-related-modules.patch
Patch12:        0013-enable-databindings-modules.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
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
BuildRequires:  jibx
BuildRequires:  jra
BuildRequires:  neethi
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
BuildRequires:  wss4j
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
Requires:       jpackage-utils
Requires:       jra
Requires:       neethi
Requires:       ws-xmlschema
Requires:       wsdl4j
Requires:       wss4j
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
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description api
Apache CXF API classes.


%package common
Summary:        Apache CXF Common
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       glassfish-jaxb-api
Requires:       geronimo-saaj

%description common
This package contains Apache CXF Common classes (including
Apache CXF Common Utilities).

%package maven-plugins
Summary:        Apache CXF Maven Plugins
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-api = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

%description maven-plugins
Maven plugins required for building or testing Apache CXF.


%package rt
Summary:        Apache CXF Runtime
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-api = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-tools = %{version}-%{release}
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


%package tools
Summary:        Apache CXF Tools
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires(pre):  %{name}-rt = %{version}-%{release}
Requires:       velocity

%description tools
Apache CXF Command Line Tools.

%prep

%setup -q -n %{tarname}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

find . -name "*.jar" -delete
find . -name "*.class" -delete

iconv -f macintosh -t utf8 < licenses/cdd1-1.0.txt > cdd.txt
mv -f cdd.txt licenses/cdd1-1.0.txt

%build
# tests are disabled because of lots of missing dependencies
mvn-rpmbuild \
    -Pfastinstall \
    -Dmaven.test.skip=true \
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
maven-plugins codegen-plugin
common
common common utilities
rt
rt bindings
rt bindings/coloc
rt bindings/http
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
rt management
rt transports/common
rt transports/http
rt transports/jms
rt transports/local
rt ws/addr
rt ws/policy
rt ws/rm
tools
tools common
tools javato
tools validator
tools wsdlto
tools wsdlto/core
tools wsdlto/databinding/jaxb
tools wsdlto/frontend/jaxws
EOM

# parents
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-cxf.pom
install -pm 644 parent/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom

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

%files common
%{_mavenpomdir}/JPP.%{name}-common*
%{_mavendepmapfragdir}/%{name}-common
%{_javadir}/%{name}/common-*

%files maven-plugins
%{_mavenpomdir}/JPP.%{name}-maven-plugins*
%{_mavendepmapfragdir}/%{name}-maven-plugins
%{_javadir}/%{name}/maven-plugins-*

%files rt
%{_mavenpomdir}/JPP.%{name}-rt*
%{_mavendepmapfragdir}/%{name}-rt
%{_javadir}/%{name}/rt-*

%files tools
%{_mavenpomdir}/JPP.%{name}-tools*
%{_mavendepmapfragdir}/%{name}-tools
%{_javadir}/%{name}/tools-*


%changelog
* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.9-alt1_2jpp7
- new version

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.8-alt1_5jpp7
- new version

