%define antsuffix 17
ExclusiveArch: x86_64

# TODO: jbossas-4.2.3-jarmap
%def_without cglib21
%if_with cglib21
%define cglibsuffix 21
%else
%define cglibsuffix %nil
%endif

Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-core
%define version 4.2.3
%define name jbossas
%define jbhomedir %{_datadir}/%{name}
%define jbossdir %{_var}/lib/%{name}
%define logdir   %{_var}/log
%define tmpdir   %{_var}/cache

%define tmp_build_file_dir %{_builddir}/jboss-%{jbver}-src/temp_build_file_dir
%define tpcsfile %{tmp_build_file_dir}/tpchecksumsfile
%define rlibcsfile %{tmp_build_file_dir}/repolibchecksumsfile
%define jbossarchivecsfile %{tmp_build_file_dir}/jbossarchivechecksumsfile

# Build specific macros
%define version_major 4
%define version_minor 2
%define version_revision 3
%define version_tag GA

%define jbver %{version_major}.%{version_minor}.%{version_revision}.%{version_tag}
%define taggedversion %{jbver}

Name:           jbossas
Version:        %{version_major}.%{version_minor}.%{version_revision}
Release:        alt22_24jpp6
Epoch:          0
Summary:        JBoss Application Server
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# mkdir -p jboss-4.2.3.GA-src/4.2.3.GA
# svn export http://anonsvn.jboss.org/repos/jbossas/tags/JBoss_4_2_3_GA/ jboss-4.2.3.GA-src/4.2.3.GA/jboss-4.2.x/
# tar cjf jboss-4.2.3.GA-src.tar.bz2 jboss-4.2.3.GA-src
Source0:        jboss-%{taggedversion}-src.tar.bz2
Source1:        %{name}.catalog
Source2:        %{name}.conf
Source3:        %{name}.init
Source4:        %{name}-%{taggedversion}-tp.tar.bz2
Source5:        %{name}-%{taggedversion}-tp-licenses.tar.bz2
Source7:        %{name}-%{version}-jarmap
Source8:        %{name}-webconsole-context.xml
# Script for computing jar signatures at build time
Source99:       %{name}-%{version}-compute_jar_signature
# alt build hack
Source44: build-thirdparty.xml

Patch0:         %{name}-buildziponly.patch
Patch1:         %{name}-4.2.3-ant17.patch
Patch2:         %{name}-4.2.3-no-pluggable-instrumentor.patch
Patch3:         %{name}-4.2.3-no-faces-logger.patch
Patch4:         %{name}-4.2.3-glassfish.patch
Patch5:         %{name}-4.2.3-thirdparty-versions.patch
Patch6:         %{name}-4.2.3-version-release-maxmemory.patch
Requires: antlr >= 0:2.7.6
#Requires: bcel >= 0:5.1
Requires: /bin/netstat
Requires: bsf >= 0:2.3.0
Requires: bsh >= 0:1.3.0
Requires: cglib%{cglibsuffix} >= 0:2.1.3
Requires: codehaus-stax11-api >= 0:1.1.2
Requires: concurrent >= 0:1.3.4
Requires: dom4j >= 0:1.6.1
Requires: excalibur-avalon-framework >= 1:4.3.1
Requires: gawk
Requires: glassfish-jaf = 0:1.1.0
Requires: glassfish-javamail = 0:1.4.0
Requires: glassfish-jaxb >= 0:2.1.4
Requires: glassfish-jaxws >= 0:2.1.1
Requires: glassfish-jsf >= 0:1.2_08
Requires: glassfish-jstl = 0:1.2.0
Requires: gnu-getopt >= 0:1.0.12
Requires: gnu-trove >= 0:1.0.2
Requires: grep
Requires: hibernate32 >= 0:3.2.4-1.SP1_CP01
Requires: hibernate32-annotations >= 0:3.2.1
Requires: hibernate3-ejb-persistence-3.0-api >= 0:3.2.1
Requires: hibernate32-entitymanager >= 0:3.2.1
Requires: hsqldb >= 1:1.8.0.8-2.patch01
Requires: jacorb >= 0:2.3.0-1jpp.ep1.4
Requires: jakarta-commons-codec >= 0:1.3
Requires: jakarta-commons-collections >= 0:3.1
Requires: jakarta-commons-httpclient >= 1:3.0.1
Requires: jakarta-commons-logging-jboss >= 0:1.1
Requires: javassist >= 0:3.8.0
Requires: jaxbintros >= 0:1.0.0
Requires: jaxen >= 0:1.1
Requires: jboss-aop >= 0:1.5.6-1
Requires: jboss-cache >= 0:1.4.1-4.SP9
Requires: jboss-common >= 0:1.2.1
Requires: jboss-jaxr >= 0:1.2.0-1.SP1
Requires: jboss-microcontainer >= 1:1.0.2
Requires: jboss-remoting >= 0:2.2.2-3.SP8
Requires: jboss-serialization >= 0:1.0.3
Requires: jbossts >= 1:4.2.3-0.SP7
Requires: jboss-vfs >= 0:1.0.0
Requires: jbossweb20 >= 0:2.0.1-1.GA
Requires: jbossws-common >= 0:1.0.0
Requires: jbossws-framework >= 0:2.0.1
Requires: jbossws-native >= 0:3.0.1
Requires: jbossws-spi >= 0:1.0.0
Requires: jbossxb >= 1:1.0.0-3
Requires: jettison >= 0:1.0.1
Requires: jfreechart >= 0:1.0.9
Requires: jgroups24 >= 1:2.4.1-1.SP4
Requires: joesnmp >= 0:0.3.4
Requires: jpackage-utils >= 0:1.7.3
Requires: log4j >= 0:1.2.14
Requires: quartz >= 0:1.5.2
Requires: snmptrapappender >= 0:1.2.8
Requires: sun-fi >= 0:1.2.2
Requires: ws-commons-policy = 0:1.0
Requires: wsdl4j16 >= 0:1.6.2
Requires: ws-scout0 >= 0:0.7
#Requires: wstx >= 0:3.1.1
Requires: xalan-j2 >= 0:2.7.1
Requires: xerces-j2 >= 0:2.9.1
Requires: xml-security >= 0:1.3.0
BuildRequires: ant%{antsuffix}
BuildRequires: ant%{antsuffix}-junit ant%{antsuffix}-antlr
BuildRequires: antlr >= 0:2.7.6
BuildRequires: antlr-repolib >= 0:2.7.6
BuildRequires: ant%{antsuffix}-nodeps
BuildRequires: asm >= 0:1.5.3
BuildRequires: asm-repolib = 0:1.5.3
#BuildRequires: bcel >= 0:5.1
BuildRequires: bcel-repolib = 1:5.1
BuildRequires: bsf >= 0:2.3.0
BuildRequires: bsf-repolib >= 0:2.3.0
BuildRequires: bsh >= 0:1.3.0
BuildRequires: bsh-repolib = 0:1.3.0
BuildRequires: buildmagic
BuildRequires: cglib%{cglibsuffix} >= 0:2.1.3
BuildRequires: cglib%{cglibsuffix}-repolib >= 0:2.1.3
BuildRequires: codehaus-stax11-api >= 0:1.1.2
BuildRequires: codehaus-stax11-repolib >= 0:1.1.2
BuildRequires: concurrent >= 0:1.3.4
BuildRequires: concurrent-repolib = 0:1.3.4
BuildRequires: dom4j >= 0:1.6.1
BuildRequires: dom4j-repolib = 0:1.6.1
BuildRequires: dom4j-jarjar >= 0:1.6.1
BuildRequires: dom4j-jarjar-repolib >= 0:1.6.1
BuildRequires: dtdparser >= 0:1.21
BuildRequires: dtdparser-repolib = 0:1.21
BuildRequires: excalibur-avalon-framework >= 1:4.3.1
BuildRequires: excalibur-avalon-framework-repolib = 1:4.3.1
BuildRequires: excalibur-avalon-logkit >= 1:2.2.1
BuildRequires: excalibur-avalon-logkit-repolib = 1:2.2.1
BuildRequires: findutils
BuildRequires: gawk
BuildRequires: glassfish-jaf = 0:1.1.0
BuildRequires: glassfish-jaf-repolib = 0:1.1.0
BuildRequires: glassfish-javamail = 0:1.4.0
BuildRequires: glassfish-javamail-repolib = 0:1.4.0
BuildRequires: glassfish-jaxb >= 0:2.1.4
BuildRequires: glassfish-jaxb-repolib >= 0:2.1.4
BuildRequires: glassfish-jaxws >= 0:2.1.1
BuildRequires: glassfish-jaxws-repolib >= 0:2.1.1
BuildRequires: glassfish-jsf >= 0:1.2_08
BuildRequires: glassfish-jsf-repolib >= 0:1.2_08
BuildRequires: glassfish-jstl = 0:1.2.0
BuildRequires: glassfish-jstl-repolib = 0:1.2.0
BuildRequires: gnu-getopt >= 0:1.0.12
BuildRequires: gnu-getopt-repolib >= 0:1.0.12
BuildRequires: gnu-trove >= 0:1.0.2
BuildRequires: gnu-trove-repolib = 0:1.0.2
BuildRequires: hibernate32 >= 0:3.2.4-1.SP1_CP01
BuildRequires: hibernate32-annotations >= 0:3.2.1
BuildRequires: hibernate32-annotations-repolib = 0:3.2.1
BuildRequires: hibernate3-ejb-persistence-3.0-api >= 0:3.2.1
BuildRequires: hibernate32-entitymanager >= 0:3.2.1
BuildRequires: hibernate32-entitymanager-repolib = 0:3.2.1
BuildRequires: hibernate32-repolib >= 0:3.2.4-1.SP1_CP01
BuildRequires: hsqldb >= 1:1.8.0.8-2.patch01
BuildRequires: hsqldb-repolib >= 1:1.8.0.8-2.patch01
BuildRequires: jacorb >= 0:2.3.0-1jpp.ep1.4
BuildRequires: jacorb-repolib >= 0:2.3.0-1jpp.ep1.4
BuildRequires: jakarta-commons-beanutils >= 0:1.7.0
BuildRequires: jakarta-commons-beanutils-repolib >= 0:1.7.0
BuildRequires: jakarta-commons-codec >= 0:1.3
BuildRequires: jakarta-commons-codec-repolib >= 0:1.3
BuildRequires: jakarta-commons-collections >= 0:3.1
BuildRequires: jakarta-commons-collections-repolib >= 0:3.1
BuildRequires: jakarta-commons-digester >= 0:1.7
BuildRequires: jakarta-commons-digester-repolib >= 0:1.7
BuildRequires: jakarta-commons-discovery >= 1:0.4
BuildRequires: jakarta-commons-discovery-repolib >= 1:0.4
BuildRequires: jakarta-commons-fileupload >= 0:1.1.1
BuildRequires: jakarta-commons-fileupload-repolib >= 0:1.1.1
BuildRequires: jakarta-commons-httpclient >= 0:3.0.1
BuildRequires: jakarta-commons-httpclient-repolib >= 0:3.0.1
BuildRequires: jakarta-commons-lang >= 0:2.1
BuildRequires: jakarta-commons-lang-repolib >= 0:2.1
BuildRequires: jakarta-commons-logging-jboss >= 0:1.1
BuildRequires: jakarta-commons-logging-jboss-repolib >= 0:1.1
BuildRequires: jakarta-slide-webdavclient >= 0:2.1
BuildRequires: jakarta-slide-webdavclient-repolib >= 0:2.1
BuildRequires: javacc3 = 0:3.2
BuildRequires: javacc3-repolib = 0:3.2
BuildRequires: javassist >= 0:3.8.0
BuildRequires: javassist-repolib >= 0:3.8.0
BuildRequires: jaxbintros >= 0:1.0.0
BuildRequires: jaxbintros-repolib >= 0:1.0.0
BuildRequires: jaxen >= 0:1.1
BuildRequires: jaxen-repolib >= 0:1.1
BuildRequires: jboss-aop >= 0:1.5.6-1
BuildRequires: jboss-aop-repolib >= 0:1.5.6-1
BuildRequires: jbossbuild
BuildRequires: jboss-cache >= 0:1.4.1-4.SP9
BuildRequires: jboss-cache-repolib >= 0:1.4.1-4.SP9
BuildRequires: jboss-common >= 0:1.2.1
BuildRequires: jboss-common-repolib = 0:1.2.1
BuildRequires: jboss-jaxr >= 0:1.2.0-1.SP1
BuildRequires: jboss-jaxr-repolib >= 0:1.2.0-1.SP1
BuildRequires: jboss-jbpm-bpel >= 0:1.1.0
BuildRequires: jboss-jbpm-bpel-repolib = 0:1.1.0
BuildRequires: jboss-jbpm-jpdl >= 0:3.2.0
BuildRequires: jboss-jbpm-jpdl-repolib = 0:3.2.0
BuildRequires: jboss-microcontainer >= 1:1.0.2
BuildRequires: jboss-microcontainer-repolib >= 1:1.0.2
BuildRequires: jboss-profiler >= 0:1.0
BuildRequires: jboss-profiler-jvmti-repolib >= 0:1.0
BuildRequires: jboss-remoting >= 0:2.2.2-3.SP8
BuildRequires: jboss-remoting-repolib >= 0:2.2.2-3.SP8
BuildRequires: jboss-serialization >= 0:1.0.3
BuildRequires: jboss-serialization-repolib = 0:1.0.3
BuildRequires: jbossts >= 1:4.2.3-1.SP7
BuildRequires: jbossts-repolib >= 1:4.2.3-1.SP7
BuildRequires: jboss-vfs >= 0:1.0.0
BuildRequires: jboss-vfs-repolib >= 0:1.0.0
BuildRequires: jbossweb20 >= 0:2.0.1-0.GA
BuildRequires: jbossweb20-repolib >= 0:2.0.1-0.GA
BuildRequires: jbossws-common >= 0:1.0.4
BuildRequires: jbossws-common-repolib >= 0:1.0.4
BuildRequires: jbossws-framework >= 0:3.0.1
BuildRequires: jbossws-framework-repolib >= 0:3.0.1
BuildRequires: jbossws-native >= 0:3.0.1
BuildRequires: jbossws-native-repolib >= 0:3.0.1
BuildRequires: jbossws-repolib >= 0:2.0.1-3.SP2
BuildRequires: jbossws-spi >= 0:1.0.2
BuildRequires: jbossws-spi-repolib >= 0:1.0.2
BuildRequires: jbossxb >= 1:1.0.0-3
BuildRequires: jbossxb-repolib >= 1:1.0.0-3
BuildRequires: jcommon >= 0:1.0.12
BuildRequires: jcommon-repolib >= 0:1.0.12
BuildRequires: jettison >= 0:1.0.1
BuildRequires: jettison-repolib >= 0:1.0.1
BuildRequires: jfreechart >= 0:1.0.9
BuildRequires: jfreechart-repolib >= 0:1.0.9
BuildRequires: jgroups24 >= 1:2.4.1-1.SP4
BuildRequires: jgroups24-repolib >= 1:2.4.1-1.SP4
BuildRequires: joesnmp >= 0:0.3.4
BuildRequires: joesnmp-repolib = 0:0.3.4
BuildRequires: joramtests >= 0:1.1
BuildRequires: joramtests-repolib >= 0:1.1
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: juddi >= 0:0.9-0.rc4
BuildRequires: juddi-repolib >= 0:0.9-0.rc4
BuildRequires: junit >= 0:3.8.2
BuildRequires: junit-repolib = 1:3.8.2
BuildRequires: log4j >= 0:1.2.14
BuildRequires: log4j-repolib >= 0:1.2.14
BuildRequires: odmg >= 0:3.0
BuildRequires: odmg-repolib = 0:3.0
BuildRequires: qdox >= 0:1.6.1
BuildRequires: qdox-repolib = 1:1.6.1
BuildRequires: quartz >= 0:1.5.2
BuildRequires: quartz-repolib = 0:1.5.2
BuildRequires: sed
BuildRequires: servletapi6 >= 0:6.0.18
BuildRequires: servletapi6-repolib >= 0:6.0.18
BuildRequires: snmptrapappender >= 0:1.2.8
BuildRequires: snmptrapappender-repolib >= 0:1.2.8
BuildRequires: sun-fi >= 0:1.2.2
BuildRequires: sun-fi-repolib >= 0:1.2.2
BuildRequires: unzip
BuildRequires: velocity-jboss >= 0:1.4
BuildRequires: velocity-jboss-repolib = 0:1.4
BuildRequires: ws-commons-policy = 0:1.0
BuildRequires: ws-commons-policy-repolib = 0:1.0
BuildRequires: wsdl4j16 >= 0:1.6.2
BuildRequires: wsdl4j16-repolib = 0:1.6.2
BuildRequires: ws-jaxme-jboss >= 0:0.2
BuildRequires: ws-jaxme-jboss-repolib >= 0:0.2
BuildRequires: ws-scout0 >= 0:0.7
BuildRequires: ws-scout0-repolib >= 0:0.7
BuildRequires: wstx >= 0:3.1.1
BuildRequires: wstx-repolib >= 0:3.1.1
BuildRequires: xalan-j2 >= 0:2.7.1
BuildRequires: xalan-j2-repolib >= 0:2.7.1
BuildRequires: xdoclet >= 0:1.2.3
BuildRequires: xdoclet-repolib = 0:1.2.3
BuildRequires: xjavadoc >= 0:1.1
BuildRequires: xjavadoc-repolib = 0:1.1
BuildRequires: xerces-j2 >= 0:2.9.1
BuildRequires: xerces-j2-repolib >= 0:2.9.1
BuildRequires: xml-security >= 0:1.3.0
BuildRequires: xml-security-repolib >= 0:1.3.0
BuildRequires: xml-commons >= 0:1.3.04
BuildRequires: xml-commons-repolib = 0:1.3.04
Provides:       %{name}-ejb3 = %{epoch}:1.0.0-0.2.rc10
Obsoletes:      %{name}-ejb3 < 0:1.0.0-0.2.rc10
Provides:       %{name}-core = %{epoch}:%{version}-%{release} 
Obsoletes:      %{name}-core <= 0:4.0.5
BuildArch:      noarch

%description
JBoss Application Server is the #1 most widely used Java application server 
on the market. A J2EE certified platform for developing and deploying
enterprise Java applications, Web applications, and Portals, 
JBoss Application Server provides the full range of J2EE 1.4 features as 
well as extended enterprise services including clustering, caching, and 
persistence.

%prep
%setup -q -n jboss-%{jbver}-src
# ant 1.8 support hack
for i in `find . -name buildmagic.ent`; do sed -i 's,fail unless="buildmagic.ant.compatible",fail if="never",' $i; done

for jar in `find . -type f -name '*.jar' -a ! -name 'jbossbuild.jar'`; do rm -v ${jar}; done
#for jar in `find . -type f -name '*.jar'`; do rm -v ${jar}; done
ln -s $(build-classpath ant%{antsuffix}) 4.2.3.GA/jboss-4.2.x/tools/lib/ant.jar
ln -s $(build-classpath ant%{antsuffix}/ant%{antsuffix}-junit) 4.2.3.GA/jboss-4.2.x/tools/lib/ant-junit.jar
ln -s $(build-classpath jboss-common/jboss-common) 4.2.3.GA/jboss-4.2.x/tools/lib/jboss-common.jar
ln -s $(build-classpath buildmagic-tasks) 4.2.3.GA/jboss-4.2.x/tools/lib/buildmagic-tasks.jar
#ln -s $(build-classpath jbossbuild) 4.2.3.GA/jboss-4.2.x/tools/lib/jbossbuild.jar
%setup -q -T -D -a 4 -n jboss-%{jbver}-src
%setup -q -T -D -a 5 -n jboss-%{jbver}-src/%{jbver}/jboss-%{version_major}.%{version_minor}.x/thirdparty
%setup -q -T -D -n jboss-%{jbver}-src
cp -p %{jbver}/jboss-%{version_major}.%{version_minor}.x/build/build-release.xml .
%patch0 -p0
pushd %{jbver}/jboss-%{version_major}.%{version_minor}.x
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
popd

mkdir %{tmp_build_file_dir}

echo "release.version.major=%{version_major}" > release.properties
echo "release.version.minor=%{version_minor}" >> release.properties
echo "release.version.revision=%{version_revision}" >> release.properties
echo "release.version.tag=%{version_tag}" >> release.properties
echo "version.cvstag=JBoss_%{version_major}_%{version_minor}_%{version_revision}_%{version_tag}" >> release.properties

# Compute checksums of jars in tp (note: our 'compute' consists of stripping meta 
# info and computing only classes)
(cd thirdpartyrepo
    rm -f %{tpcsfile}
    for i in `find \`pwd\` -type f -name "*ar" | sort`; do
       /bin/sh %{SOURCE99} $i >> %{tpcsfile}
    done
)

# Grab remaining thirdparty jars...
rm -f %{rlibcsfile}
touch %{rlibcsfile}
for item in %{_javadir}/repository.jboss.com/*; do
    cp -pr $item/ thirdpartyrepo/

    # Add the checksums from that jar into the checksum file
    for i in `find $item -type f -name "*ar" | sort`; do
        /bin/sh %{SOURCE99} $i >> %{rlibcsfile}
    done
done

# Sed out the task that requires going online (we package licenses directly)
sed -i -e s:'<visit-componentref-graph componentVisitor="org.jboss.ant.util.graph.ComponentRefGraphLicenseVisitor"/>'::g  %{jbver}/jboss-%{version_major}.%{version_minor}.x/build/build-thirdparty.xml

# alt build hack
cp %{SOURCE44}  4.2.3.GA/jboss-4.2.x/build/build-thirdparty.xml

%build
export CLASSPATH=
export OPT_JAR_LIST="ant%{antsuffix}/ant%{antsuffix}-nodeps"
export ANT_OPTS="-Xms500m -Xmx1500m -Xss1m"
# FIXME: (dwalluck): Work around <https://issues.apache.org/bugzilla/show_bug.cgi?id=42263>
ant%{antsuffix} -f build-release.xml \
    -Dversion.major=%{version_major} \
    -Dversion.minor=%{version_minor} \
    -Dversion.revision=%{version_revision} \
    -Dversion.tag=%{version_tag} \
    -Djbossbuild.repository=file://`pwd`/thirdpartyrepo \
    -Dant.version="`%{_bindir}/ant%{antsuffix} -version`" \
    build-dist release 2>&1 | tee %{tmp_build_file_dir}/build.log

%install

# FIXME: class-path-in-manifest /var/lib/jbossas/bin/shutdown.jar
# FIXME: class-path-in-manifest /var/lib/jbossas/bin/run.jar
# FIXME: log-files-without-logrotate /var/log/jbossas

# Extract the "distribution" so that we can patch appropriate files 
# and install from it
rm -rf jboss-as-4.2
mkdir jboss-as-4.2

# Extract the .zip
unzip -d jboss-as-4.2 -qq %{jbver}/dist/jboss-%{jbver}.zip

# Go into the distribution dir
pushd jboss-as-4.2/jboss-%{jbver}

# Remove the empty docs/tests dir (JBPAPP-114)
rmdir docs/tests

# Set up a specific context for web-console, so that links are allowed for it
cp -p %{SOURCE8} server/all/deploy/management/console-mgr.sar/web-console.war/WEB-INF/context.xml
cp -p %{SOURCE8} server/default/deploy/management/console-mgr.sar/web-console.war/WEB-INF/context.xml

# Set jboss.dist to a direct path, since relative paths don't work due 
# to the symlink setup
sed -i -e s:'<property name="jboss.dist" value="../../../.."/>':'<property name="jboss.dist" value="/var/lib/jbossas"/>': docs/examples/jms/standalone/build.xml

# Copy DTD catalog into place
install -p -m 644 %{SOURCE1} docs/dtd/catalog

# Global configuration file
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
cat > jbossas.conf << EOT
# System-wide configuration file for jbossas services
# This will be sourced by jbossas and any secondary service
# Values will be overridden by service-specific configuration
# files in /etc/sysconfig
# Use this one to change default values for all services
# Change the service specific ones to affect only one service
# (see, for instance, /etc/sysconfig/jbossas)
#
# To change a setting, uncomment the line and set the value for what you want
# The values in the comments are the default values, shown here for convenience
#
EOT
cat %{SOURCE2} >> jbossas.conf
install -m 644 jbossas.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
rm jbossas.conf
# Service-specific configuration file
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
cat > jbossas << EOT
# Service-specific configuration file for jbossas services
# This will be sourced by the SysV service script after the global
# configuration file /etc/jbossas/jbossas.conf, thus allowing values
# to be overridden on a per-service way
#
# NEVER change the init script itself:
# To change values for all services make your changes in
# /etc/jbossas/jbossas.conf
# To change values for a specific service, change it here
# To create a new service, create a link from /etc/init.d/<you new service> to
# /etc/init.d/jbossas (do not copy the init script) and make a copy of the
# /etc/sysconfig/jbossas file to /etc/sysconfig/<you new service> and change
# the property values so the two services won't conflict
# Register the new service in the system as usual (see chkconfig and similars)
#
# To change a setting, uncomment the line and set the value for what you want
# The values in the comments are the default values, shown here for convenience
#
EOT
cat %{SOURCE2} >> jbossas

install -m 644 jbossas $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
rm jbossas
# Configuration file used when run.sh is used
install -m 644 bin/run.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_initrddir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{jbossdir}

install -d -m 755 $RPM_BUILD_ROOT%{jbhomedir}/client
cp -pr client/* $RPM_BUILD_ROOT%{jbhomedir}/client
install -d -m 755 $RPM_BUILD_ROOT%{jbhomedir}/lib
cp -pr lib/* $RPM_BUILD_ROOT%{jbhomedir}/lib
cp -pr server $RPM_BUILD_ROOT%{jbossdir}

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{jbossdir}/bin
for script in classpath probe run shutdown twiddle wstools wsconsume wsrunclient wsprovide; do
  install -m 0755 bin/${script}.sh $RPM_BUILD_ROOT%{jbossdir}/bin/${script}.sh
  ln -sf %{jbossdir}/bin/${script}.sh $RPM_BUILD_ROOT%{_bindir}/jbossas-${script}
done
install -m 644 bin/*.jar $RPM_BUILD_ROOT%{jbossdir}/bin
pushd $RPM_BUILD_ROOT%{jbossdir}/bin
ln -sf %{_sysconfdir}/%{name}/run.conf .
popd

install -m 644 copyright.txt $RPM_BUILD_ROOT%{jbossdir}
install -m 644 jar-versions.xml $RPM_BUILD_ROOT%{jbossdir}
install -m 644 lgpl.html $RPM_BUILD_ROOT%{jbossdir}
install -m 644 JBossORG-EULA.txt $RPM_BUILD_ROOT%{jbossdir}

ln -s %{jbhomedir}/client $RPM_BUILD_ROOT%{jbossdir}/client
ln -s %{jbhomedir}/lib $RPM_BUILD_ROOT%{jbossdir}/lib
cp -pr docs/ $RPM_BUILD_ROOT%{jbossdir}/

ln -s %{jbossdir}/bin $RPM_BUILD_ROOT%{jbhomedir}/bin
ln -s %{jbossdir}/docs $RPM_BUILD_ROOT%{jbhomedir}/docs
ln -s %{jbossdir}/server $RPM_BUILD_ROOT%{jbhomedir}/server

for server in all default minimal; do
  mv $RPM_BUILD_ROOT%{jbossdir}/server/$server/conf \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/$server
  ln -sf %{_sysconfdir}/%{name}/$server \
	$RPM_BUILD_ROOT%{jbossdir}/server/$server/conf
  install -d -m 755 $RPM_BUILD_ROOT%{logdir}/%{name}/$server
# avoid these symlinks for now
# install -d -m 755 $RPM_BUILD_ROOT%{tmpdir}/%{name}/temp/$server
# install -d -m 755 $RPM_BUILD_ROOT%{tmpdir}/%{name}/work/$server
# and replace them by straight dirs
  install -d -m 755 $RPM_BUILD_ROOT%{jbossdir}/server/$server/tmp
  install -d -m 755 $RPM_BUILD_ROOT%{jbossdir}/server/$server/work
#
  install -d -m 755 $RPM_BUILD_ROOT%{jbossdir}/server/$server/data
  ln -s %{logdir}/%{name}/$server \
    $RPM_BUILD_ROOT%{jbossdir}/server/$server/log
# avoid these symlinks for now
# ln -s %{tmpdir}/%{name}/temp/$server \
#   $RPM_BUILD_ROOT%{jbossdir}/server/$server/tmp
# ln -s %{tmpdir}/%{name}/work/$server \
#   $RPM_BUILD_ROOT%{jbossdir}/server/$server/work
done
#cleanup
find $RPM_BUILD_ROOT -name "*.sav" -exec rm -f {} \;

popd

# Compute signatures for all archives in the install dirs
rm -f %{jbossarchivecsfile} 
for i in `find $RPM_BUILD_ROOT%{jbhomedir} $RPM_BUILD_ROOT%{jbossdir} -type f -name "*ar" | sort`; do
    /bin/sh %{SOURCE99} $i >> %{jbossarchivecsfile}
done

# We now have checksums of
# 1. Files from thirdparty
# 2. Files from repolib (brew)
# 3. Files in /usr/share/jbossas and /var/lib/jbossas
#
# Files from thirdparty will be copied/unversioned
# Files from repolib will be linked
# Remaining files will be copied/versioned

OLD_IFS=$IFS
IFS='
'

rm -f %{tmp_build_file_dir}/tpfiles %{tmp_build_file_dir}/rlibfiles 
rm -f %{tmp_build_file_dir}/builtfiles

# Identify files in thirdparty
for i in `cat %{jbossarchivecsfile}`; do
    checksum=`echo $i | awk '{print $1}'`
    file=`echo $i | awk '{print $2}' | sed -e s:$RPM_BUILD_ROOT::g`

    found=`grep $checksum %{tpcsfile} || :`

    if [ ! -z "$found" ]; then
        echo $file >> %{tmp_build_file_dir}/tpfiles
    fi
done

# Identify files from brew
for i in `cat %{jbossarchivecsfile}`; do
    checksum=`echo $i | awk '{print $1}'`
    file=`echo $i | awk '{print $2}' | sed -e s:$RPM_BUILD_ROOT::g`

    found=`grep $checksum %{rlibcsfile} || :`

    if [ ! -z "$found" ]; then
        echo $file >> %{tmp_build_file_dir}/rlibfiles
    fi
done

# Identify files from neither
for i in `cat %{jbossarchivecsfile}`; do
    checksum=`echo $i | awk '{print $1}'`
    file=`echo $i | awk '{print $2}' | sed -e s:$RPM_BUILD_ROOT::g`

    found=`grep $checksum %{tpcsfile} || :`
    found=$found`grep $checksum %{rlibcsfile} || :`

    if [ -z "$found" ]; then
        echo $file >> %{tmp_build_file_dir}/builtfiles
    fi
done

# We created a list in %%prep with existing jar/ear/war files.. other than those, we install everything

install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}/rars
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}/sars
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}/wars

# Files to copy and version to /usr/share/java/jbossas (all built files)
while read archive; do

    archiveonsystem=$archive
    archive="$RPM_BUILD_ROOT$archive"

    # rar's go in the rar/ subdir, and wars go into the war/ dir
    dir=""
    extension=${archive##*.}

    if [ $extension == "rar" ]; then
        dir=%{_javadir}/%{name}/rars
    elif [ $extension == "sar" ]; then
        dir=%{_javadir}/%{name}/sars
    elif [ $extension == "war" ]; then
        dir=%{_javadir}/%{name}/wars
    else
        dir=%{_javadir}/%{name}
    fi

    buildrootjavadir="$RPM_BUILD_ROOT$dir"
    versionedname=`basename $archive | sed -e s:\\\\\(\\\..ar\\\\\):-%{version}\\\1:`

    # Does file already exist in /usr/share/java/jbossas? make sure the signature matches
    if [ -f $buildrootjavadir/$versionedname ]; then
        sig1=`/bin/sh %{SOURCE99} $archive | awk '{print $1}'`
        sig2=`/bin/sh %{SOURCE99} $buildrootjavadir/$versionedname | awk '{print $1}'`

        if [ "$sig1" != "$sig2" ]; then
            echo "Signatures do not match for $archive and $buildrootjavadir/$versionedname"
            exit 1
        fi
    else
        install -m 644 $archive $buildrootjavadir/$versionedname
        ln -s $versionedname $buildrootjavadir/`basename $archive`
    fi

    # Remove archive from $JBOSS_HOME and link it
   rm -f $archive
   ln -s $dir/`basename $archive` $archive

done < %{tmp_build_file_dir}/builtfiles

# Third party files to copy to /usr/share/java/jbossas/thirdparty (non brew built)
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}/thirdparty
while read archive; do

    archiveonsystem=$archive
    archive="$RPM_BUILD_ROOT$archive"

    # rar's go in the rar/ subdir, and wars go into the war/ dir
    dir=%{_javadir}/%{name}/thirdparty
    buildrootjavadir="$RPM_BUILD_ROOT$dir"
    filename=`basename $archive`

    # Does file already exist in /usr/share/java/jbossas? make sure the signature matches
    if [ -f $buildrootjavadir/$filename ]; then
        sig1=`/bin/sh %{SOURCE99} $archive | awk '{print $1}'`
        sig2=`/bin/sh %{SOURCE99} $buildrootjavadir/$filename | awk '{print $1}'`

        if [ "$sig1" != "$sig2" ]; then
            echo "Signatures do not match for $archive and $buildrootjavadir/$filename"
            exit 1
        fi
    else
        install -m 644 $archive $buildrootjavadir/$filename
    fi

    # Remove archive from $JBOSS_HOME and link it
    rm -f $archive
    ln -s $dir/$filename $archive

done < %{tmp_build_file_dir}/tpfiles

# Finally, link brew built jars...
while read archive; do

    archive=$RPM_BUILD_ROOT$archive

    tosearch=`basename $archive`
    jarname=`grep -E "^$tosearch " %{SOURCE7} | awk '{print $2}' || :`
    jarfile=$(build-classpath $jarname) || :

    if [ -z "$jarname" ] || [ ! -r "$jarfile" ]; then
        echo "Incorrect/missing archive mapping for $archive"
        exit 1
    fi

    rm -f $archive
    ln -s $jarfile $archive

done < %{tmp_build_file_dir}/rlibfiles

# Temporary workaround for JBAS-3433.
# See: http://jira.jboss.org/jira/browse/JBAS-3433
for file in $RPM_BUILD_ROOT%{jbossdir}/bin/*.jar; do
    filebasename=`basename $file`
    rm -f $RPM_BUILD_ROOT%{jbossdir}/bin/$filebasename
    /bin/cp -f $RPM_BUILD_ROOT/%{_javadir}/%{name}/$filebasename $RPM_BUILD_ROOT%{jbossdir}/bin/
done

# Mark files status for jars, .xml's, .properties, etc. based on their extention
serverfileslist=%{tmp_build_file_dir}/jbossas-server-files.list
rm -f $serverfileslist
for file in `find $RPM_BUILD_ROOT%{jbossdir}/server`; do

    actualfile=`echo $file | sed -e s:^$RPM_BUILD_ROOT::g -e s:/var/lib/jbossas:%%{jbossdir}:g`

    # .xml/.properties => config file
    if [ "${actualfile##*.}" == "xml" ] || [ "${actualfile##*.}" == "properties" ]; then
       echo "%attr(-,jboss,jboss)  %config(noreplace) $actualfile" >> $serverfileslist
    elif [ -d "$file" ]; then
       # directory
       echo "%attr(-,jboss,jboss) %dir $actualfile" >> $serverfileslist
    else
       # Not a config file, not a directory => normal
       echo "%attr(-,jboss,jboss) $actualfile" >> $serverfileslist
    fi

done

# (dwalluck): Fix file eol
pushd %{jbver}/jboss-%{version_major}.%{version_minor}.x/build
%{__perl} -pi -e 's/\r$//g' \
output/jboss-%{jbver}/JBossORG-EULA.txt \
output/jboss-%{jbver}/docs/dtd/jboss-service_4_2.dtd \
output/jboss-%{jbver}/docs/dtd/jboss_4_2.dtd \
output/jboss-%{jbver}/docs/dtd/jboss-client_4_2.dtd \
output/jboss-%{jbver}/docs/dtd/jboss-app_4_2.dtd \
output/jboss-%{jbver}/docs/examples/jmx/persistent-service.sar/META-INF/MANIFEST.MF \
output/jboss-%{jbver}/docs/examples/jms/db2-jdbc2-service.xml \
output/jboss-%{jbver}/docs/dtd/jbosscmp-jdbc_4_2.dtd \
output/jboss-%{jbver}/docs/licenses/cddl.txt \
output/jboss-%{jbver}/docs/dtd/jboss-web_4_2.dtd \
output/jboss-%{jbver}/docs/schema/persistence_1_0.xsd \
output/jboss-%{jbver}/docs/schema/orm_1_0.xsd \
output/jboss-%{jbver}/docs/schema/ejb-jar_3_0.xsd
%{__perl} -pi -e 's/\r$//g' $RPM_BUILD_ROOT%{jbossdir}/JBossORG-EULA.txt

# (dwalluck): Fix file encoding
%{_bindir}/iconv -f iso-8859-1 -t utf-8 < $RPM_BUILD_ROOT%{jbossdir}/copyright.txt > $RPM_BUILD_ROOT%{jbossdir}/copyright.txt.utf8
%{__mv} -f $RPM_BUILD_ROOT%{jbossdir}/copyright.txt.utf8 $RPM_BUILD_ROOT%{jbossdir}/copyright.txt
%{_bindir}/iconv -f iso-8859-1 -t utf-8 < $RPM_BUILD_ROOT%{jbossdir}/JBossORG-EULA.txt > $RPM_BUILD_ROOT%{jbossdir}/JBossORG-EULA.txt.utf8
%{__mv} -f $RPM_BUILD_ROOT%{jbossdir}/JBossORG-EULA.txt.utf8 $RPM_BUILD_ROOT%{jbossdir}/JBossORG-EULA.txt

%{_bindir}/iconv -f iso-8859-1 -t utf-8 < docs/copyright.txt > docs/copyright.txt.utf8
%{__mv} -f docs/copyright.txt.utf8 docs/copyright.txt
%{_bindir}/iconv -f iso-8859-1 -t utf-8 < output/jboss-%{jbver}/docs/dtd/connector_1_0.dtd > output/jboss-%{jbver}/docs/dtd/connector_1_0.dtd.utf8
%{__mv} -f output/jboss-%{jbver}/docs/dtd/connector_1_0.dtd.utf8 output/jboss-%{jbver}/docs/dtd/connector_1_0.dtd
popd

mkdir -p %{buildroot}%{_sysconfdir}/sgml
/bin/touch $RPM_BUILD_ROOT%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat

%pre
JBOSS_SHELL=/sbin/nologin
%{_sbindir}/groupadd -r jboss 2>/dev/null || :
%{_sbindir}/useradd -c JBossAS -r -s $JBOSS_SHELL -d /usr/share/%{name} -g jboss jboss 2>/dev/null || :
if [ "$1" = 2 ]; then
  # stop server before upgrade
  %{_initrddir}/%{name} stop >/dev/null 2>&1 || :
fi

%post
/bin/touch %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat 2>/dev/null || :
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{jbossdir}/docs/dtd/catalog > /dev/null 2>&1 || :
fi
[ -x /sbin/chkconfig ] && /sbin/chkconfig --add %{name} || :

%preun
# remove service
if [ "$1" = 0 ]; then
  # on erase
  %{_initrddir}/%{name} stop > /dev/null 2>&1 || :
  [ -x /sbin/chkconfig ] && /sbin/chkconfig --del %{name}
fi

%postun
# We NEVER, EVER remove users and groups from the system after they are added!
#if [ "$1" = 0 ]; then
#  # on erase
#  userdel jboss > /dev/null 2>&1 || :
#  groupdel jboss > /dev/null 2>&1 || :
#fi
# Note that we're using versioned catalog, so this is always ok.
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{jbossdir}/docs/dtd/catalog > /dev/null 2>&1 || :
fi

%files -f temp_build_file_dir/jbossas-server-files.list
%defattr(0644,jboss,jboss,0755)
%defattr(0644,jboss,jboss,0755)
%attr(0755,root,root) %{_initrddir}/%{name}
# avoid these symlinks for now
#%attr(-,jboss,jboss) %{tmpdir}/%{name}
# they were replaced by straight dirs
%attr(-,jboss,jboss) %{logdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%dir %{jbhomedir}
%{jbhomedir}/bin
%{jbhomedir}/client
%{jbhomedir}/docs
%{jbhomedir}/lib
%{jbhomedir}/server
%dir %{jbossdir}
%doc %{jbossdir}/JBossORG-EULA.txt
%doc %{jbossdir}/copyright.txt
%{jbossdir}/jar-versions.xml
%doc %{jbossdir}/*.html
%dir %{jbossdir}/bin
%{jbossdir}/bin/*.jar
%attr(0755,root,root) %{_bindir}/*
%attr(0755,jboss,jboss) %{jbossdir}/bin/*.sh
%{jbossdir}/bin/run.conf
%{jbossdir}/client
%{jbossdir}/docs
%{jbossdir}/lib
# javadir
%{_javadir}/jbossas
%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat

%changelog
* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt22_24jpp6
- fixed build

* Tue Jan 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt21_24jpp6
- built with new antlr 

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt20_24jpp6
- built with new jboss-remoting

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt19_24jpp6
- fixed build with new ant

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt18_24jpp6
- build with joramtests 1.5

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt17_24jpp6
- build with compat jbossweb20

* Tue Feb 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt16_24jpp6
- build with compat hibernate 3.2

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt15_24jpp6
- build with jgroups24

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt14_24jpp6
- fixed build

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt13_24jpp6
- fixed build

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt12_24jpp6
- fixed build

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt11_24jpp6
- fixed build with new commons beanutils, httpclient and fileupload

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt10_24jpp6
- rebuild with gnu-getopt 1.0.13

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt9_24jpp6
- rebuild with new commons-codec repolib

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt8_24jpp6
- fixed build

* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt7_24jpp6
- rebuild with new commons-lang repolib

* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt6_24jpp6
- build with wstx 3.2.8

* Sat Oct 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt5_24jpp6
- build with cglib 2.2
- added ghosted .cat

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt4_24jpp6
- built with cglib21 and new commmons-digester

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt3_24jpp6
- tmp hack: added ExclusiveArch: x86_64 to keep incoming alive

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt2_24jpp6
- ant 18 fixes; fixed build in jpp 6 environment

* Wed Oct 13 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt1_24jpp5.M51.1
- init script fixes

* Tue Mar 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt1_24jpp5
- full build

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt0.1jpp
- bootstrap for jbossas

