BuildRequires(pre): rpm-macros-alternatives
%define dist %nil
BuildRequires: ant-trax
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 5.5.31
%define name tomcat5
# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# If you want only apis to be built,
# give rpmbuild option '--with apisonly'
%define with_apisonly %{?_with_apisonly:1}%{!?_with_apisonly:0}
%define without_apisonly %{!?_with_apisonly:1}%{?_with_apisonly:0}

# If you don't want direct ecj support to be built in,
# while ecj isn't available, give rpmbuild option '--without ecj'
%define without_ecj %{?_without_ecj:1}%{!?_without_ecj:0}
%define with_ecj %{!?_without_ecj:1}%{?_without_ecj:0}

%define full_jname jasper5
%define jname jasper
%define majversion 5.5
%define minversion 31
%define servletspec 2.4
%define jspspec 2.0

%define tcuid 91

%define packdname apache-tomcat-%{version}-src

# FHS 2.2 compliant tree structure
# see http://www.pathname.com/fhs/2.2/
%define confdir %{_sysconfdir}/%{name}
# normally this would be _localstatedir instead of _var, see changelog
%define logdir %{_var}/log/%{name}
%define apphomedir %{_datadir}/%{name}
%define bindir %{_datadir}/%{name}/bin
%define tempdir %{_var}/cache/%{name}/temp
%define workdir %{_var}/cache/%{name}/work
%define appdir %{_var}/lib/%{name}/webapps
%define serverdir %{_var}/lib/%{name}/server
%define commondir %{_var}/lib/%{name}/common
%define shareddir %{_var}/lib/%{name}/shared
%define _initrddir %_initdir

Name: tomcat5
Epoch: 0
Version: %{majversion}.%{minversion}
Release: alt6_3jpp6
Summary: Apache Servlet/JSP Engine, RI for Servlet 2.4/JSP 2.0 API

Group: Development/Java
License: ASL 2.0
URL: http://tomcat.apache.org
Source0: http://www.apache.org/dist/tomcat/tomcat-5/v%{version}/src/%{packdname}.tar.gz
Source1: %{name}-%{majversion}.init
Source2: %{name}-%{majversion}.conf
Source3: %{name}-%{majversion}.wrapper
Source4: %{name}-%{majversion}.logrotate
Source5: %{name}-%{majversion}.relink
Source6: %{name}-poms-%{version}.tar.bz2
#Source6: %{name}-poms-%{version}.tar.bz2
Source7: jasper-OSGi-MANIFEST.MF
Source8: servlet-api-OSGi-MANIFEST.MF
Source9: jsp-api-OSGi-MANIFEST.MF
Patch0: %{name}-%{majversion}.link_admin_jar.patch
Patch1: %{name}-%{majversion}-skip-build-on-install.patch
Patch2: %{name}-%{majversion}-jt5-build.patch
Patch3: %{name}-%{majversion}-jtc-build.patch
Patch4: %{name}-%{majversion}-jtj-build.patch
Patch5: %{name}-%{majversion}-javaxssl.patch
Patch7: %{name}-%{majversion}-catalina.sh.patch
Patch8: %{name}-%{majversion}-jasper.sh.patch
Patch9: %{name}-%{majversion}-jspc.sh.patch
Patch10: %{name}-%{majversion}-setclasspath.sh.patch
Patch12: %{name}-%{majversion}-util-build.patch
Patch13: %{name}-%{majversion}-http11-build.patch
Patch14: %{name}-%{majversion}-jk-build.patch
Patch15: %{name}-%{majversion}-unversioned-commons-logging-jar.patch
Patch16: %{name}-%{majversion}-jspc-classpath.patch
#FIXME Disable JSP pre-compilation on ppc64, x390x and alpha
Patch18: %{name}-%{majversion}-skip-jsp-precompile.patch
# XXX:
# Seems to be only needed when building with ECJ for java 1.5 since
# the default source type for ecj is still 1.4
Patch19: %{name}-%{majversion}-connectors-util-build.patch
Patch20: %{name}-%{majversion}-nonative.patch

BuildArch: noarch

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
%if %{without_apisonly}
%if %{with_ecj}
BuildRequires: ecj >= 0:3.3.1.1
%endif
BuildRequires: ant-nodeps
BuildRequires: xalan-j2
BuildRequires: jakarta-commons-beanutils >= 0:1.7
BuildRequires: jakarta-commons-collections >= 0:3.1
BuildRequires: jakarta-commons-daemon >= 0:1.0.1
BuildRequires: jakarta-commons-dbcp >= 0:1.2.1
BuildRequires: jakarta-commons-digester >= 0:1.7
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jakarta-commons-fileupload >= 0:1.0
BuildRequires: jakarta-commons-io >= 0:1.3
BuildRequires: jakarta-commons-modeler >= 0:2.0
BuildRequires: jakarta-commons-pool >= 0:1.2
BuildRequires: jakarta-commons-launcher >= 0:0.9
BuildRequires: jakarta-commons-el10 >= 0:1.0
BuildRequires: junit >= 0:3.8.1
BuildRequires: regexp >= 0:1.3
BuildRequires: struts >= 0:1.2.9
BuildRequires: struts-taglib >= 0:1.3.8
BuildRequires: xerces-j2 >= 0:2.7.1
BuildRequires: zip
# xml-commons-apis is needed by Xerces-J2
BuildRequires: xml-commons-jaxp-1.3-apis
# FIXME taglibs-standard is not listed in the Tomcat build.properties.default
BuildRequires: jakarta-taglibs-standard >= 0:1.1.0
# formerly non-free stuff
# jta can be provided by geronimo-jta-version-api
BuildRequires: jta
# javamail can be provided by classpathx-mail
BuildRequires: javamail
BuildRequires: mx4j
Requires(post): xml-commons-jaxp-1.3-apis
# libgcj aot-compiled native libraries
Requires(post): jpackage-utils >= 0:1.7.4
Requires(post): coreutils
Requires(preun): coreutils
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(post): findutils
Requires(preun): findutils
Requires(pre): shadow-utils
Requires(post): jakarta-commons-dbcp >= 0:1.2.1
Requires(post): jakarta-commons-collections >= 0:3.1
Requires(post): jakarta-commons-pool >= 0:1.2
Requires: jakarta-commons-logging >= 0:1.0.4
Requires(post): jakarta-commons-logging >= 0:1.0.4
Requires: javamail
Requires(post): javamail
%if %{with_ecj}
Requires: ecj >= 0:3.3.1.1
Requires(post): ecj >= 0:3.3.1.1
%endif
%endif
Requires: jpackage-utils >= 0:1.7.4
# xml parsing packages
Requires: xerces-j2 >= 0:2.7.1
Requires: xml-commons-jaxp-1.3-apis
# jakarta-commons packages
Requires: jakarta-commons-daemon >= 0:1.0.1
Requires(post): jakarta-commons-daemon >= 0:1.0.1
Requires: jakarta-commons-launcher >= 0:0.9
# alternatives
# And it needs its own API subpackages for running
Requires: %{name}-common-lib = %{epoch}:%{version}-%{release}
Requires: %{name}-server-lib = %{epoch}:%{version}-%{release}
# And it needs its own API subpackages before being installed
Requires(post): %{name}-common-lib = %{epoch}:%{version}-%{release}
Requires(post): %{name}-server-lib = %{epoch}:%{version}-%{release}
Source44: Op1OSP7SFm
Requires: %name-parent = %{epoch}:%{version}-%{release}
BuildRequires: zip
Provides: %{name}-server = %{version}-%{release}
Obsoletes: %{name}-server <= 5.5.16-alt1.1

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License. Tomcat is intended to be
a collaboration of the best-of-breed developers from around the world.



%if %{without_apisonly}
%package webapps
Group: Development/Java
# Replace PreReq
Requires(pre): %{name} = %{epoch}:%{version}-%{release}
Requires(postun): %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-taglibs-standard >= 0:1.1.0
Summary: Web applications for Apache Tomcat
Requires(post): jpackage-utils >= 0:1.7.4
Requires(preun): findutils
Requires(preun): coreutils

%description webapps
Web applications for Apache Tomcat

%package webapps-admin
Group: Development/Java
Summary: Administrative web applications for Apache Tomcat
Requires(pre): %{name} = %{epoch}:%{version}-%{release}
Requires(postun): %{name} = %{epoch}:%{version}-%{release}
Requires: struts >= 0:1.2.9
Requires: struts-taglib >= 0:1.3.8
Requires(post): jpackage-utils >= 0:1.7.4
Requires(post): findutils
Requires(post): jakarta-commons-beanutils
Requires(post): jakarta-commons-collections
Requires(post): jakarta-commons-digester
Requires(post): jakarta-commons-io
Requires(post): struts
Requires(post): struts-taglib
Requires(preun): findutils
Requires(preun): coreutils
Requires(post): commons-fileupload
Requires: %name-parent = %{epoch}:%{version}-%{release}
Provides: %{name}-admin-webapps = %{version}-%{release}

%description webapps-admin
The administrative web applications (admin and manager) for Apache Tomcat.
%endif

%package servlet-%{servletspec}-api
Group: Development/Java
Requires: alternatives >= 0:0.4
Summary: Apache Tomcat Servlet implementation classes
Obsoletes: servletapi5
Provides: servlet
Provides: servlet5
Provides: servlet24
Provides: servletapi5
Provides: servlet_2_4_api
Requires: %name-parent = %{epoch}:%{version}-%{release}

%description servlet-%{servletspec}-api
Contains the implementation classes
of the Apache Tomcat Servlet API (packages javax.servlet).

%package servlet-%{servletspec}-api-javadoc
Group: Development/Documentation
Summary: Javadoc generated documentation for %{name}-servlet-%{servletspec}-api
Obsoletes: servletapi5-javadoc
Provides: servletapi5-javadoc
Requires(post): coreutils

%description servlet-%{servletspec}-api-javadoc
Contains the javadoc generated documentation for the implementation classes
of the Apache Tomcat Servlet and JSP APIs (packages javax.servlet).

%package jsp-%{jspspec}-api
Group: Development/Java
Requires: alternatives >= 0:0.4
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
# We need this to indirectly get rid of legacy jsp included in old
# servlet packages (one day we will be able to remove this)
# Replace PreReq
Requires(pre): %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(postun): %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Summary: Apache Tomcat Servlet and JSP implementation classes
Provides: jsp
Provides: jsp_2_0_api
Requires: %name-parent = %{epoch}:%{version}-%{release}

%description jsp-%{jspspec}-api
Contains the implementation classes
of the Apache Tomcat JSP API (packages javax.servlet.jsp).

%package jsp-%{jspspec}-api-javadoc
Group: Development/Documentation
Summary: Javadoc generated documentation for %{name}-jsp-%{jspspec}-api
Requires(post): coreutils

%description jsp-%{jspspec}-api-javadoc
Contains the javadoc generated documentation for the implementation classes
of the Apache Tomcat JSP API (packages javax.servlet.jsp).

%if %{without_apisonly}
%package common-lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container (part)
Requires(post): jpackage-utils >= 0:1.7.4
Requires: jakarta-commons-collections >= 0:3.1
Requires(post): jakarta-commons-collections >= 0:3.1
Requires: jakarta-commons-dbcp >= 0:1.2.1
Requires(post): jakarta-commons-dbcp >= 0:1.2.1
Requires: jakarta-commons-el10 >= 0:1.0
Requires(post): jakarta-commons-el10 >= 0:1.0
# FIXME commons-pool is not listed in the Tomcat build.properties.default
Requires: jakarta-commons-pool >= 0:1.2
Requires(post): jakarta-commons-pool >= 0:1.2
%if %{with_ecj}
Requires: ecj >= 0:3.3.1.1
Requires(post): ecj >= 0:3.3.1.1
%endif
# Other subpackages must go in first
Requires(post): %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires(post): %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires(post): findutils
Requires(preun): findutils
Requires(post): coreutils
Requires(preun): coreutils
Requires: %name-parent = %{epoch}:%{version}-%{release}

%description common-lib
Libraries needed to run the Tomcat Web container (part)

%package server-lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container (part)
Requires(post): jpackage-utils >= 0:1.7.4
Requires: jakarta-commons-modeler >= 0:2.0
Requires(post): jakarta-commons-modeler >= 0:2.0
# Other subpackages must go in first
Requires: %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires(post): %{name}-%{jname} = %{epoch}:%{version}-%{release}
Requires(post): findutils
Requires(preun): findutils
Requires(post): coreutils
Requires(preun): coreutils
Requires: %name-parent = %{epoch}:%{version}-%{release}
Requires: jaf javamail

%description server-lib
Libraries needed to run the Tomcat Web container (part)

%package %{jname}
Group: Development/Java
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Summary: Compiler JARs and associated scripts for %{name}
Obsoletes: jasper5
Provides: jasper5
Requires: %name-parent = %{epoch}:%{version}-%{release}

%description %{jname}
Compiler JARs and associated scripts for %{name}

%package %{jname}-javadoc
Group: Development/Documentation
Summary: Javadoc generated documentation for %{name}-%{jname}
Obsoletes: jasper5-javadoc
Provides: jasper5-javadoc

%description %{jname}-javadoc
Javadoc for generated documentation %{name}-%{jname}
%endif

%if %{without_apisonly}
%if %{with_ecj}
%package jasper-eclipse
Group: Editors
Summary: Jasper OSGi Eclipse plugin

%description jasper-eclipse
Jasper OSGi Eclipse plugin that contains class files from jasper-compiler,
jasper-runtime and ECJ.
%endif
%endif


%package parent
Group: Development/Java
Summary: Apache Tomcat parent pom for maven2
Obsoletes: tomcat5-poms < %{epoch}:%{version}

%description parent
Apache Tomcat parent pom for maven2


%prep
%{__rm} -rf ${RPM_BUILD_DIR}/%{name}-%{version}

%setup -q -c -T -a 0
%setup -q -D -T -a 6
cd %{packdname}
%patch0 -p0
%patch1 -p0
#%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch7 -p0
%patch8 -p0
#%patch9 -p0
%patch10 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%{__sed} -i -e 's|\@JAVA_HOME\@|%{java_home}|' build/build.xml
%ifarch ppc64 s390x alpha
%patch18 -p0
%endif
%if %{with_ecj}
%patch19 -p0 
%endif
%patch20 -b .sav

%if %{without_ecj}
    %{__rm} %{jname}/src/share/org/apache/jasper/compiler/JDTCompiler.java
%endif

#find -type f -name '*.jsp' | xargs -t perl -pi -e 's/<html:html locale="true">/<html:html>/g'
mkdir commons-launcher
pushd commons-launcher
jar xf /usr/share/java/commons-launcher.jar
cp LauncherBootstrap.class ../..
popd

for i in container/webapps/admin/*.jsp container/webapps/admin/*/*.jsp; do
    subst 's,locale="true",lang="true",' $i
done

%build
# remove pre-built binaries
for dir in ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname} ; do
    find $dir \( -name "*.jar" -o -name "*.class" \) | xargs -t %{__rm} -f
done
# build jspapi and servletapi as ant dist will require them later
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi
    pushd jsr154
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dservletapi.build="build" \
            -Dservletapi.dist="dist" \
            -Dbuild.compiler="modern" dist
    popd
    pushd jsr152
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dservletapi.build="build" \
            -Dservletapi.dist="dist" \
            -Dbuild.compiler="modern" dist
    popd
popd
%if %{without_apisonly}
# build jasper subpackage
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}
    %{__cat} > build.properties << EOBP
ant.jar=$(build-classpath ant)
servlet-api.jar=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar
jsp-api.jar=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar
tools.jar=%{java_home}/lib/tools.jar
xerces.jar=$(build-classpath xerces-j2)
xercesImpl.jar=$(build-classpath jaxp_parser_impl)
xmlParserAPIs.jar=$(build-classpath xml-commons-jaxp-1.3-apis)
commons-el.jar=$(build-classpath commons-el10)
commons-collections.jar=$(build-classpath commons-collections)
commons-logging.jar=$(build-classpath commons-logging)
commons-daemon.jar=$(build-classpath commons-daemon)
junit.jar=$(build-classpath junit)
%if %{without_apisonly}
jasper-compiler-jdt.jar=$(build-classpath ecj)
%endif
EOBP
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Djava.home="%{java_home}" -Dbuild.compiler="modern" javadoc
popd

# build tomcat 5
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/build
    %{__cat} >> build.properties << EOBP
version=%{version}
version.build=%{minversion}
ant.jar=%{_javadir}/ant.jar
ant-launcher.jar=%{_javadir}/ant-launcher.jar
jtc.home=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/connectors/
%{jname}.home=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}
commons-beanutils.jar=$(build-classpath commons-beanutils)
commons-collections.jar=$(build-classpath commons-collections)
commons-daemon.jar=$(build-classpath commons-daemon)
commons-dbcp.jar=$(build-classpath commons-dbcp)
commons-digester.jar=$(build-classpath commons-digester)
commons-el.jar=$(build-classpath commons-el10)
commons-fileupload.jar=$(build-classpath commons-fileupload)
commons-io.jar=$(build-classpath commons-io)
commons-launcher.jar=$(build-classpath commons-launcher)
commons-launcher.bootstrap.class=${RPM_BUILD_DIR}/%{name}-%{version}/LauncherBootstrap.class
commons-logging.jar=$(build-classpath commons-logging)
commons-logging-api.jar=$(build-classpath commons-logging-api)
commons-modeler.jar=$(build-classpath commons-modeler)
commons-pool.jar=$(build-classpath commons-pool)
jmx.jar=$(build-classpath mx4j/mx4j-jmx.jar)
jmx-remote.jar=$(build-classpath mx4j/mx4j-remote.jar)
jmx-tools.jar=$(build-classpath mx4j/mx4j-tools.jar)
jmxri.jar=$(build-classpath mx4j/mx4j-jmx.jar)
junit.jar=$(build-classpath junit)
regexp.jar=$(build-classpath regexp)
servlet-api.jar=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar
%if %{without_apisonly}
jsp-api.jar=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar
%endif
servlet.doc=${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/docs/api
xercesImpl.jar=$(build-classpath jaxp_parser_impl)
xml-apis.jar=$(build-classpath xml-commons-jaxp-1.3-apis)
struts.jar=$(build-classpath struts)
struts.lib=%{_datadir}/struts
mail.jar=$(build-classpath javamail/mail)
jta.jar=$(build-classpath jta)
jaas.jar=$(build-classpath jaas)
jndi.jar=$(build-classpath jndi)
jdbc20ext.jar=$(build-classpath jdbc-stdext)
jcert.jar=$(build-classpath jsse/jcert)
jnet.jar=$(build-classpath jsse/jnet)
jsse.jar=$(build-classpath jsse/jsse)
servletapi.build.notrequired=true
jspapi.build.notrequired=true
EOBP
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.compiler="modern" -Djava.home="%{java_home}" init
cp ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar \
        ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/build/build/common/lib/servlet-api.jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.compiler="modern" -Djava.home="%{java_home}" -Djdk1.4.present=true -Dtomcat-dbcp.jar=$(build-classpath commons-dbcp) build 
popd
# build the connectors
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/connectors
# use the JARs created above to build
    export CLASSPATH="${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar:${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/build/build/server/lib/tomcat-util.jar"
    %{__cat} > build.properties << EOBP
ant.jar=%{_javadir}/ant.jar
junit.jar=$(build-classpath junit)
commons-beanutils.jar=$(build-classpath commons-beanutils)
commons-collections.jar=$(build-classpath commons-collections)
commons-daemon.jar=$(build-classpath commons-daemon)
commons-digester.jar=$(build-classpath commons-digester)
commons-fileupload.jar=$(build-classpath commons-fileupload)
commons-io.jar=$(build-classpath commons-io)
commons-launcher.jar=$(build-classpath commons-launcher)
commons-logging.jar=$(build-classpath commons-logging)
commons-logging-api.jar=$(build-classpath commons-logging-api)
commons-modeler.jar=$(build-classpath commons-modeler)
commons-pool.jar=$(build-classpath commons-pool)
regexp.jar=$(build-classpath regexp)
jmx.jar=$(build-classpath mx4j/mx4j-jmx)
mail.jar=$(build-classpath javamail/mail)
jta.jar=$(build-classpath jta)
jaas.jar=$(build-classpath jaas)
jndi.jar=$(build-classpath jndi)
jdbc20ext.jar=$(build-classpath jdbc-stdext)
jcert.jar=$(build-classpath jsse/jcert)
jnet.jar=$(build-classpath jsse/jnet)
jsse.jar=$(build-classpath jsse/jsse)
tomcat5.home=../../build/build
EOBP
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.compiler="modern" -Djava.home="%{java_home}" build
popd
%endif

%if %{without_apisonly}
# create jasper-eclipse jar
%if %{with_ecj}
mkdir -p org.apache.jasper
pushd org.apache.jasper
unzip -qq ../apache-tomcat-%{version}-src/build/build/common/lib/jasper-compiler.jar
unzip -qq ../apache-tomcat-%{version}-src/build/build/common/lib/jasper-runtime.jar \
  -x META-INF/MANIFEST.MF org/apache/jasper/compiler/Localizer.class
unzip -qq %{_javadir}/ecj.jar -x META-INF/MANIFEST.MF
cp -p %{SOURCE7} META-INF/MANIFEST.MF
rm -f plugin.properties plugin.xml about.html jdtCompilerAdapter.jar META-INF/eclipse.inf
zip -qq -r ../org.apache.jasper_5.5.17.v200706111724.jar .
popd
%endif
%endif

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
%if %{without_apisonly}
zip -u %{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar META-INF/MANIFEST.MF
%endif

%install
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadir}
%if %{without_apisonly}
export CLASSPATH="$(build-classpath xalan-j2 xml-commons-jaxp-1.3-apis jakarta-taglibs-core jakarta-taglibs-standard):${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr152/dist/lib/jsp-api.jar:${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi/jsr154/dist/lib/servlet-api.jar"
# build initial path structure
%{__install} -d -m 755 \
    ${RPM_BUILD_ROOT}{%{confdir},%{logdir},%{apphomedir},%{bindir}}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}{%{serverdir},%{tempdir},%{workdir}}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}{%{appdir},%{commondir},%{shareddir}}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_initrddir}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadir}/%{name}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/maven2/poms
%{__install} -m 755 %{SOURCE5} ${RPM_BUILD_ROOT}%{bindir}/relink
# SysV init and configuration
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
# Service-specific configuration file
cat > %{name} << EOT
# Service-specific configuration file for %{name} services
# This will be sourced by the SysV service script after the global
# configuration file /etc/%{name}/%{name}.conf, thus allowing values
# to be overridden on a per-service way
#
# NEVER change the init script itself:
# To change values for all services make your changes in
# /etc/%{name}/%{name}.conf
# To change values for a specific service, change it here
# To create a new service, create a link from /etc/init.d/<you new service> to
# /etc/init.d/%{name} (do not copy the init script) and make a copy of the
# /etc/sysconfig/%{name} file to /etc/sysconfig/<you new service> and change
# the property values so the two services won't conflict
# Register the new service in the system as usual (see chkconfig and similars)
#
EOT
%{__install} -m 0644 %{name} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
%{__rm} %{name}
%{__install} %{SOURCE1} \
    ${RPM_BUILD_ROOT}%{_initrddir}/%{name}
# Global configuration file
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{confdir}
%{__cat} > %{name}.conf << EOT
# System-wide configuration file for %{name} services
# This will be sourced by %{name} and any secondary service
# Values will be overridden by service-specific configuration
# files in /etc/sysconfig
# Use this one to change default values for all services
# Change the service specific ones to affect only one service
# (see, for instance, /etc/sysconfig/%{name})
#
EOT
%{__cat} %{SOURCE2} >> %{name}.conf
%{__install} -m 0644 %{name}.conf ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf
%{__rm} -f %{name}.conf
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/build
    export usejikes="false"
    export OPT_JAR_LIST="ant/ant-nodeps ant/ant-trax xalan-j2-serializer struts-taglib"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.compiler="modern" -Djava.home=%{java_home} -Djasper-compiler-jdt.jar=%{_javadir}/ecj.jar -Dtomcat-dbcp.jar=$(build-classpath commons-dbcp) dist
    pushd dist
        %{__mv} bin/* ${RPM_BUILD_ROOT}%{bindir}
        %{__mv} common/* ${RPM_BUILD_ROOT}%{commondir}
        %{__mv} conf/* ${RPM_BUILD_ROOT}%{confdir}
        %{__mv} server/* ${RPM_BUILD_ROOT}%{serverdir}
        %{__mv} shared/* ${RPM_BUILD_ROOT}%{shareddir}
        %{__mv} webapps/* ${RPM_BUILD_ROOT}%{appdir}
    popd
popd
# rename catalina.sh into dtomcat5 to let wrapper take precedence
%{__install} ${RPM_BUILD_ROOT}%{bindir}/catalina.sh \
    ${RPM_BUILD_ROOT}%{_bindir}/d%{name}
%{__rm} -f ${RPM_BUILD_ROOT}%{bindir}/catalina.sh.* \
    ${RPM_BUILD_ROOT}%{bindir}/setclasspath.*
# Remove leftover files
%{__rm} -f ${RPM_BUILD_ROOT}%{bindir}/*.orig
# install wrapper as tomcat5
%{__install} %{SOURCE3} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
# install logrotate support
%{__install} %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
# remove / reorder non-usefull stuff
%{__rm} -rf ${RPM_BUILD_ROOT}%{apphomedir}/src/
%{__rm} -f  ${RPM_BUILD_ROOT}%{bindir}/*.sh ${RPM_BUILD_ROOT}%{bindir}/*.bat
# FHS compliance patches, not easy to track them all boys :)
for i in ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf \
    ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name} \
    ${RPM_BUILD_ROOT}%{_bindir}/d%{name} \
    ${RPM_BUILD_ROOT}%{_bindir}/%{name} \
    ${RPM_BUILD_ROOT}%{_initrddir}/%{name} \
    ${RPM_BUILD_ROOT}%{bindir}/relink \
    ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}; do
    %{__sed} -i \
        -e 's|\@\@\@LIBDIR\@\@\@|%{_libdir}|g' \
        -e 's|\@\@\@TCCONF\@\@\@|%{confdir}|g' \
        -e "s|\@\@\@TCCONF\@\@\@|%{confdir}|g" \
        -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
        -e "s|\@\@\@TCBIN\@\@\@|%{bindir}|g" \
        -e "s|\@\@\@TCCOMMON\@\@\@|%{commondir}|g" \
        -e "s|\@\@\@TCSERVER\@\@\@|%{serverdir}|g" \
        -e "s|\@\@\@TCSHARED\@\@\@|%{shareddir}|g" \
        -e "s|\@\@\@TCAPP\@\@\@|%{appdir}|g" \
        -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" $i
done
%add_to_maven_depmap tomcat tomcat-parent %{version} JPP/%{name} parent
    %{__install} -m 644 \
        ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/tomcat-parent-%{version}.pom \
        $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-parent.pom
# Process bin
# Remove local JARs (to be replaced with jpp links in post)
pushd ${RPM_BUILD_ROOT}%{bindir}
    # tomcat-juli will be installed in a public repository
    %{__mv} tomcat-juli.jar \
        ${RPM_BUILD_ROOT}%{_javadir}/%{name}/tomcat-juli-%{version}.jar
    pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
        %{__ln_s} -f tomcat-juli-%{version}.jar tomcat-juli.jar
    popd
    %add_to_maven_depmap tomcat tomcat-juli %{version} JPP/%{name} tomcat-juli
    %{__install} -m 644 \
        ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/tomcat-juli-%{version}.pom \
        $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-tomcat-juli.pom

    find . -name "*.jar" -not -name "*bootstrap*" \
           -exec %{__rm} -f {} \;
popd
# Process server/lib
# Remove local JARs (to be replaced with jpp links in post)
pushd ${RPM_BUILD_ROOT}%{serverdir}/lib
    find . -name "*.jar" -not -name "catalina*" \
        -not -name "servlets-*" \
        -not -name "tomcat-*" | xargs -t %{__rm} -f
    # catalina-ant will be installed in a public repository
    %{__mv} catalina-ant.jar \
        ${RPM_BUILD_ROOT}%{_javadir}/catalina-ant-%{version}.jar
    pushd ${RPM_BUILD_ROOT}%{_javadir}
        %{__ln_s} -f catalina-ant-%{version}.jar catalina-ant5.jar
    popd
    %add_to_maven_depmap tomcat catalina-ant %{version} JPP catalina-ant5
    %{__install} -m 644 \
        ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/catalina-ant-%{version}.pom \
        $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-catalina-ant5.pom

    # catalina* jars will be installed in a public repository
    for i in catalina*.jar; do
        j="`echo $i | %{__sed} -e 's|\.jar$||'`"
        %{__mv} ${j}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
        %add_to_maven_depmap tomcat ${j} %{version} JPP/tomcat5 ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${j}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${j}.pom
    done
    # servlets* jars will be installed in a public repository
    for i in servlets-*.jar; do
        j="`echo $i | %{__sed} -e 's|\.jar$||'`"
        %{__mv} ${j}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
        %add_to_maven_depmap tomcat ${j} %{version} JPP/tomcat5 ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${j}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${j}.pom
    done
    # tomcat* jars will be installed in a public repository
    for i in tomcat-*.jar; do
        j="`echo $i | %{__sed} -e 's|\.jar$||'`"
        %{__mv} ${j}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
        %add_to_maven_depmap tomcat ${j} %{version} JPP/tomcat5 ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${j}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${j}.pom
    done
popd
# Process admin webapp server/webapps/admin
pushd ${RPM_BUILD_ROOT}%{serverdir}/webapps/admin/WEB-INF/lib
    find . -name "*.jar" -not -name 'catalina-admin*' | xargs -t %{__rm} -f
    for i in catalina-admin; do
        %{__mv} ${i}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${i}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${i}-%{version}.jar ${i}.jar
        popd
        %add_to_maven_depmap tomcat ${i} %{version} JPP/tomcat5 ${i}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${i}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${i}.pom
    done
popd
# Process manager webapp server/webapps/manager
pushd ${RPM_BUILD_ROOT}%{serverdir}/webapps/manager/WEB-INF/lib
    find . -name "*.jar" -not -name 'catalina-manager*' | xargs -t %{__rm} -f
    for i in catalina-manager; do
        %{__mv} ${i}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${i}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${i}-%{version}.jar ${i}.jar
        popd
        %add_to_maven_depmap tomcat ${i} %{version} JPP/tomcat5 ${i}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${i}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${i}.pom
    done
popd
# Process host-manager webapp server/webapps/host-manager
pushd ${RPM_BUILD_ROOT}%{serverdir}/webapps/host-manager/WEB-INF/lib
    find . -name "*.jar" -not -name 'catalina-host-manager*' \
        | xargs -t %{__rm} -f
    for i in catalina-host-manager; do
        %{__mv} ${i}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${i}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${i}-%{version}.jar ${i}.jar
        popd
        %add_to_maven_depmap tomcat ${i} %{version} JPP/tomcat5 ${i}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${i}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${i}.pom
    done
popd
# Process common/lib
pushd ${RPM_BUILD_ROOT}%{commondir}/lib
    find . -name "*.jar" -not -name "%{jname}*" \
        -not -name "naming*" | xargs -t %{__rm} -f
    # jasper's jars will be installed in a public repository
    for i in %{jname}-compiler %{jname}-runtime; do
        j="`echo $i | %{__sed} -e 's|%{jname}-|%{jname}5-|'`"
        %{__mv} ${i}.jar ${RPM_BUILD_ROOT}%{_javadir}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
        %add_to_maven_depmap tomcat ${i} %{version} JPP ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${i}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-${j}.pom
    done
    # naming* jars will be installed in a public repository
    for i in naming-*.jar; do
        j="`echo $i | %{__sed} -e 's|\.jar$||'`"
        %{__mv} ${j}.jar \
            ${RPM_BUILD_ROOT}%{_javadir}/%{name}/${j}-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f ${j}-%{version}.jar ${j}.jar
        popd
        %add_to_maven_depmap tomcat ${j} %{version} JPP/tomcat5 ${j}
        %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/${j}-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.tomcat5-${j}.pom
    done
popd
# Process common/endorsed
pushd ${RPM_BUILD_ROOT}%{commondir}/endorsed
    find . -name "*.jar" | xargs -t %{__rm} -f
popd
# avoid duplicate servlet.jar
%{__rm} -f ${RPM_BUILD_ROOT}%{commondir}/lib/servlet.jar
# Add catalina-deployer
%{__install} -m 644 %{packdname}/build/deployer/lib/catalina-deployer.jar \
    ${RPM_BUILD_ROOT}%{_javadir}/%{name}/catalina-deployer-%{version}.jar
        pushd ${RPM_BUILD_ROOT}%{_javadir}/%{name}
            %{__ln_s} -f catalina-deployer-%{version}.jar catalina-deployer.jar
        popd

# Perform FHS translation
# (final links)
pushd ${RPM_BUILD_ROOT}%{apphomedir}
    [ -d bin ] || %{__ln_s} -f %{bindir} bin
    [ -d common ] || %{__ln_s} -f %{commondir} common
    [ -d conf ] || %{__ln_s} -f %{confdir} conf
    [ -d logs ] || %{__ln_s} -f %{logdir} logs
    [ -d server ] || %{__ln_s} -f %{serverdir} server
    [ -d shared ] || %{__ln_s} -f %{shareddir} shared
    [ -d webapps ] || %{__ln_s} -f %{appdir} webapps
    [ -d work ] || %{__ln_s} -f %{workdir} work
    [ -d temp ] || %{__ln_s} -f %{tempdir} temp
popd
%endif
# begin servlet api subpackage install
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi
    %{__install} -m 644 jsr154/dist/lib/servlet-api.jar \
        ${RPM_BUILD_ROOT}%{_javadir}/%{name}-servlet-%{servletspec}-api-%{version}.jar
    pushd ${RPM_BUILD_ROOT}%{_javadir}
        %{__ln_s} -f %{name}-servlet-%{servletspec}-api-%{version}.jar \
            %{name}-servlet-%{servletspec}-api.jar
        # For backward compatibility with old JPP packages
        %{__ln_s} -f %{name}-servlet-%{servletspec}-api-%{version}.jar \
            servletapi5.jar
    popd
    # depmap frag for standard alternative
    %if %{without_apisonly}
       %add_to_maven_depmap javax.servlet servlet-api %{servletspec} JPP servlet_2_4_api
       %add_to_maven_depmap tomcat servlet-api %{version} JPP %{name}-servlet-%{servletspec}-api
    %endif
    %{__mkdir} -p $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/ ||:
    %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/servlet-api-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}-servlet-%{servletspec}-api.pom
    # javadoc servlet
    %{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-servlet-%{servletspec}-api-%{version}
    %{__cp} -pr jsr154/build/docs/api/* \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-servlet-%{servletspec}-api-%{version}
    %{__ln_s} -f %{name}-servlet-%{servletspec}-api-%{version} \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-servlet-%{servletspec}-api
popd
# begin jsp api subpackage install
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/servletapi
    %{__install} -m 644 jsr152/dist/lib/jsp-api.jar \
        ${RPM_BUILD_ROOT}%{_javadir}/%{name}-jsp-%{jspspec}-api-%{version}.jar
    pushd ${RPM_BUILD_ROOT}%{_javadir}
        %{__ln_s} -f %{name}-jsp-%{jspspec}-api-%{version}.jar \
            %{name}-jsp-%{jspspec}-api.jar
        # For backward compatibility with old JPP packages
        %{__ln_s} -f %{name}-jsp-%{jspspec}-api-%{version}.jar \
            jspapi.jar
    popd
    %if %{without_apisonly}
       %add_to_maven_depmap javax.servlet jsp-api %{jspspec} JPP jsp_2_0_api
       %add_to_maven_depmap tomcat jsp-api %{version} JPP %{name}-jsp-%{jspspec}-api
    %endif
    %{__install} -m 644 \
            ${RPM_BUILD_DIR}/%{name}-%{version}/tomcat5-poms/jsp-api-%{version}.pom \
            $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}-jsp-%{jspspec}-api.pom
    # javadoc jsp
    %{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
    %{__cp} -pr jsr152/build/docs/api/* \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
    %{__ln_s} %{name}-jsp-%{jspspec}-api-%{version} \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}-jsp-%{jspspec}-api
popd
%if %{without_apisonly}
# begin jasper subpackage install
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}
    %{__install} -m 755 src/bin/jspc.sh \
        ${RPM_BUILD_ROOT}%{_bindir}/jspc5.sh
    %{__install} -m 755 src/bin/%{jname}.sh \
        ${RPM_BUILD_ROOT}%{_bindir}/%{full_jname}.sh
popd
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/container
    %{__install} -m 755 catalina/src/bin/setclasspath.sh \
        ${RPM_BUILD_ROOT}%{_bindir}/%{full_jname}-setclasspath.sh
popd
# javadoc
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{jname}-%{version}
pushd ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}
    %{__cp} -pr build/javadoc/* \
        ${RPM_BUILD_ROOT}%{_javadocdir}/%{jname}-%{version}
    %{__ln_s} %{jname}-%{version} ${RPM_BUILD_ROOT}%{_javadocdir}/%{jname}
popd
%endif

%if %{without_apisonly}
%if %{with_ecj}
%{__install} -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/eclipse/plugins
%{__cp} -p org.apache.jasper_5.5.17.v200706111724.jar ${RPM_BUILD_ROOT}%{_datadir}/eclipse/plugins
%endif
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_tomcat5-servlet-2.4-api<<EOF
%{_javadir}/servlet.jar	%{_javadir}/%{name}-servlet-%{servletspec}-api.jar	20400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_2_4_api_tomcat5-servlet-2.4-api<<EOF
%{_javadir}/servlet_2_4_api.jar	%{_javadir}/%{name}-servlet-%{servletspec}-api.jar	20400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_tomcat5-jsp-2.0-api<<EOF
%{_javadir}/jsp.jar	%{_javadir}/%{name}-jsp-%{jspspec}-api.jar	20000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_2_0_api_tomcat5-jsp-2.0-api<<EOF
%{_javadir}/jsp_2_0_api.jar	%{_javadir}/%{name}-jsp-%{jspspec}-api.jar	20000
EOF

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete
mkdir -p $RPM_BUILD_ROOT/%_altdir/
cat >>$RPM_BUILD_ROOT/%_altdir/servletapi_%{name}<<EOF
%{_javadir}/servletapi.jar	%{_javadir}/%{name}-servlet-2.4-api-%{version}.jar	20400
EOF

%triggerpostun -- tomcat5-server <= 5.5.16-alt1.1
for i in common/classes common/endorsed common/lib shared/classes shared/lib webapps; do
if [ -d /usr/lib/tomcat5/$i ]; then
    echo "upgrade: moving old /usr/lib/tomcat5/$i to /var/lib/tomcat5/$i"
    mv -f /usr/lib/tomcat5/$i/* /var/lib/tomcat5/$i/
fi
done || :
%if %{without_apisonly}

%post
%force_update_alternatives
# install tomcat5 (but don't activate)
/sbin/chkconfig --add %{name}
# Remove old automated symlinks
for repository in %{bindir} ; do
    find $repository -name '*.jar' -type l | xargs %{__rm} -f
done
for repository in %{commondir}/endorsed ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
done
for repository in %{commondir}/lib ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
done
for repository in %{serverdir}/lib ; do
    find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
done
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
%{__rm} -f %{bindir}/commons-daemon.jar
%{__ln_s} $(build-classpath commons-daemon) %{bindir}  2>&1
%{__rm} -f %{bindir}/commons-logging-api.jar
%{__ln_s} $(build-classpath commons-logging-api) %{bindir}  2>&1
%{__rm} -f %{bindir}/tomcat-juli.jar
%{__ln_s} $(build-classpath tomcat5/tomcat-juli) %{bindir}  2>&1
build-jar-repository %{commondir}/endorsed jaxp_parser_impl \
    xml-commons-jaxp-1.3-apis 2>&1
build-jar-repository %{commondir}/lib commons-collections \
    commons-dbcp commons-el10 commons-pool javamail/mail jsp \
    %{name}/naming-factory %{name}/naming-resources servlet \
    %{jname}5-compiler %{jname}5-runtime 2>&1
%if %{with_ecj}
    build-jar-repository %{commondir}/lib ecj 2>&1
%endif
build-jar-repository %{serverdir}/lib catalina-ant5 commons-modeler \
    %{name}/catalina-ant-jmx %{name}/catalina-cluster %{name}/catalina \
    %{name}/catalina-optional %{name}/catalina-storeconfig \
    %{name}/servlets-default %{name}/servlets-invoker %{name}/servlets-webdav \
    %{name}/tomcat-ajp %{name}/tomcat-apr %{name}/tomcat-coyote \
    %{name}/tomcat-http %{name}/tomcat-jkstatus-ant %{name}/tomcat-util 2>&1
/sbin/service %name condrestart

%post webapps 
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
build-jar-repository %{appdir}/jsp-examples/WEB-INF/lib \
    jakarta-taglibs-core jakarta-taglibs-standard 2>&1
/sbin/service %name condrestart

%post webapps-admin
# Remove old automated symlinks
find %{serverdir}/webapps/admin/WEB-INF/lib -name '\[*\]*.jar' -type d \
    | xargs %{__rm} -f
# Create automated links - since all needed extensions may not have been
# installed for this jvm output is muted
build-jar-repository %{serverdir}/webapps/admin/WEB-INF/lib \
    commons-beanutils commons-collections commons-digester struts struts-taglib \
    %{name}/catalina-admin 2>&1
build-jar-repository %{serverdir}/webapps/host-manager/WEB-INF/lib \
    %{name}/catalina-host-manager 2>&1
build-jar-repository %{serverdir}/webapps/manager/WEB-INF/lib \
    commons-io commons-fileupload %{name}/catalina-manager 2>&1

%endif
/sbin/service %name condrestart

%post servlet-%{servletspec}-api-javadoc
%{__rm} -f %{_javadocdir}/servletapi # legacy symlink

%post jsp-%{jspspec}-api-javadoc
%{__rm} -f %{_javadocdir}/jsp-api # legacy symlink
%if %{without_apisonly}

%preun
# Always clean up workdir and tempdir on upgrade/removal
%{__rm} -fr %{workdir}/* %{tempdir}/*
if [ $1 = 0 ]; then
    [ -f /var/lock/subsys/%{name} ] && %{_initrddir}/%{name} stop
    [ -f %{_initrddir}/%{name} ] && /sbin/chkconfig --del %{name}
    # Remove automated symlinks
    for repository in %{commondir}/endorsed; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
    done
    for repository in %{commondir}/lib ; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
    done
    for repository in %{serverdir}/lib ; do
        find $repository -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
    done
fi

%preun webapps-admin
if [ $1 = 0 ]; then
    find %{serverdir}/webapps/*/WEB-INF/lib  \
        -name '\[*\]*.jar' -not -type d | xargs %{__rm} -f
fi
[ $1 != 0 ] || /sbin/service %name condrestart

%preun webapps
if [ $1 = 0 ]; then
    find %{appdir}/jsp-examples/WEB-INF/lib  \
        -name '\[*\]*.jar' \
        -not -type d | xargs %{__rm} -f
fi
[ $1 != 0 ] || /sbin/service %name condrestart

%pre
# Add the "tomcat" user and group
# we need a shell to be able to use su - later
%{_sbindir}/groupadd  -r tomcat 2> /dev/null || :
%{_sbindir}/useradd -c "Apache Tomcat"  -g tomcat \
    -s /bin/sh -r -d %{apphomedir} tomcat 2> /dev/null || :
%endif

%if %{without_apisonly}
%files
%doc %{packdname}/LICENSE
%doc %{packdname}/build/{RELE*,RUNNING.txt,BENCHMARKS.txt}
# symlinks
%{_datadir}/%{name}/common
%{_datadir}/%{name}/temp
%{_datadir}/%{name}/logs
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/server
%{_datadir}/%{name}/shared
%{_datadir}/%{name}/work
%{_datadir}/%{name}/webapps
# Normal directories
%dir %{apphomedir}
%dir %{bindir}
%dir %{_var}/lib/%{name}
%dir %{_var}/cache/%{name}
%dir %{commondir}
%dir %{commondir}/classes
%dir %{commondir}/lib
%dir %{commondir}/endorsed
%dir %{commondir}/i18n
%dir %{serverdir}
%dir %{serverdir}/classes
%dir %{serverdir}/lib
%{serverdir}/lib/*.renametojar
%dir %{shareddir}
%dir %{shareddir}/classes
%dir %{shareddir}/lib
# Directories with special permissions
%attr(0775,root,tomcat) %dir %{appdir}
%attr(0775,root,tomcat) %dir %{confdir}
%attr(0770,root,tomcat) %dir %{tempdir}
%attr(0770,root,tomcat) %dir %{workdir}
%attr(0755,tomcat,tomcat) %dir %{logdir}
%attr(0775,root,tomcat) %dir %{confdir}/Catalina
%attr(0775,root,tomcat) %dir %{confdir}/Catalina/localhost
%attr(0755,root,root) %{_bindir}/*
%attr(0755,root,root) %{bindir}/relink
%attr(0644,root,root) %{bindir}/*.jar
%attr(0644,root,root) %{bindir}/*.xml
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0644,root,tomcat) %config(noreplace) %{confdir}/catalina.policy
%attr(0644,root,tomcat) %config(noreplace) %{confdir}/catalina.properties
%attr(0660,root,tomcat) %config(noreplace) %{confdir}/logging.properties
%attr(0660,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/server-minimal.xml
%config(noreplace) %{confdir}/server.xml
%config(noreplace) %{confdir}/web.xml
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{commondir}/i18n/*
%exclude %_bindir/jasper5-setclasspath.sh
%exclude %_bindir/jasper5.sh
%exclude %_bindir/jspc5.sh

%files common-lib
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/naming*.jar
%{_datadir}/maven2/poms/JPP.tomcat5-naming-factory.pom
%{_datadir}/maven2/poms/JPP.tomcat5-naming-resources.pom

%files server-lib
%{_javadir}/catalina*.jar
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/catalina-ant-jmx*.jar
%{_javadir}/%{name}/catalina-cluster*.jar
%{_javadir}/%{name}/catalina-deployer*.jar
%{_javadir}/%{name}/catalina.jar
%{_javadir}/%{name}/catalina-%{version}.jar
%{_javadir}/%{name}/catalina-optional*.jar
%{_javadir}/%{name}/catalina-storeconfig*.jar
%{_javadir}/%{name}/servlets*.jar
%{_javadir}/%{name}/tomcat*.jar
%{_datadir}/maven2/poms/JPP-catalina-ant5.pom
%{_datadir}/maven2/poms/JPP.tomcat5-catalina-ant-jmx.pom
%{_datadir}/maven2/poms/JPP.tomcat5-catalina-cluster.pom
%{_datadir}/maven2/poms/JPP.tomcat5-catalina.pom
%{_datadir}/maven2/poms/JPP.tomcat5-catalina-optional.pom
%{_datadir}/maven2/poms/JPP.tomcat5-catalina-storeconfig.pom
%{_datadir}/maven2/poms/JPP.tomcat5-servlets-default.pom
%{_datadir}/maven2/poms/JPP.tomcat5-servlets-invoker.pom
%{_datadir}/maven2/poms/JPP.tomcat5-servlets-webdav.pom
%{_datadir}/maven2/poms/JPP.tomcat5-tomcat-ajp.pom
%{_datadir}/maven2/poms/JPP.tomcat5-tomcat-apr.pom
%{_datadir}/maven2/poms/JPP.tomcat5-tomcat-coyote.pom
%{_datadir}/maven2/poms/JPP.tomcat5-tomcat-http.pom
%{_datadir}/maven2/poms/JPP.tomcat5-tomcat-juli.pom
%{_datadir}/maven2/poms/JPP.tomcat5-tomcat-util.pom

%files webapps
%defattr(0644,root,tomcat,0775)
%dir %{appdir}/servlets-examples
%{appdir}/servlets-examples/*
%dir %{appdir}/jsp-examples
%{appdir}/jsp-examples/*
%dir %{appdir}/ROOT
%{appdir}/ROOT/*
%dir %{appdir}/tomcat-docs
%{appdir}/tomcat-docs/*
%dir %{appdir}/webdav
%{appdir}/webdav/*

%files webapps-admin
%defattr(0640,root,tomcat,0750)
%attr(0660,root,tomcat) %{confdir}/Catalina/localhost/manager.xml
%attr(0660,root,tomcat) %{confdir}/Catalina/localhost/host-manager.xml
%{confdir}/Catalina/localhost/admin.xml
%dir %{appdir}/balancer
%{appdir}/balancer/*
%dir %{serverdir}/webapps
%{serverdir}/webapps/*
%attr(0644,root,root) %{_javadir}/%{name}/catalina-admin*.jar
%attr(0644,root,root) %{_javadir}/%{name}/catalina-manager*.jar
%attr(0644,root,root) %{_javadir}/%{name}/catalina-host-manager*.jar
%{_datadir}/maven2/poms/JPP.tomcat5-catalina-admin.pom
%{_datadir}/maven2/poms/JPP.tomcat5-catalina-host-manager.pom
%{_datadir}/maven2/poms/JPP.tomcat5-catalina-manager.pom

%files %{jname}
%doc ${RPM_BUILD_DIR}/%{name}-%{version}/%{packdname}/%{jname}/doc/jspc.html
%{_javadir}/%{jname}5-*.jar
%attr(0755,root,root) %{_bindir}/%{jname}*.sh
%attr(0755,root,root) %{_bindir}/jspc*.sh
%{_datadir}/maven2/poms/JPP-jasper5-compiler.pom
%{_datadir}/maven2/poms/JPP-jasper5-runtime.pom

%files %{jname}-javadoc
%{_javadocdir}/%{jname}-%{version}
%{_javadocdir}/%{jname}
%endif

%files servlet-%{servletspec}-api
%_altdir/servlet_2_4_api_tomcat5-servlet-2.4-api
%_altdir/servlet_tomcat5-servlet-2.4-api
%doc %{packdname}/LICENSE
%{_javadir}/%{name}-servlet-%{servletspec}-api*.jar
%{_javadir}/servletapi5.jar
%{_datadir}/maven2/poms/JPP-tomcat5-servlet-2.4-api.pom
%_altdir/servletapi_*

%files servlet-%{servletspec}-api-javadoc
%{_javadocdir}/%{name}-servlet-%{servletspec}-api-%{version}
%{_javadocdir}/%{name}-servlet-%{servletspec}-api

%files jsp-%{jspspec}-api
%_altdir/jsp_2_0_api_tomcat5-jsp-2.0-api
%_altdir/jsp_tomcat5-jsp-2.0-api
%doc %{packdname}/LICENSE
%{_javadir}/%{name}-jsp-%{jspspec}-api*.jar
%{_javadir}/jspapi.jar
%{_datadir}/maven2/poms/JPP-tomcat5-jsp-2.0-api.pom

%files jsp-%{jspspec}-api-javadoc
%{_javadocdir}/%{name}-jsp-%{jspspec}-api-%{version}
%{_javadocdir}/%{name}-jsp-%{jspspec}-api

%if %{without_apisonly}
%if %{with_ecj}
%files jasper-eclipse
%dir %{_datadir}/eclipse
%dir %{_datadir}/eclipse/plugins
%{_datadir}/eclipse/plugins/org.apache.jasper_*
%endif
%endif

%files parent
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/JPP.tomcat5-parent.pom


%changelog
* Sun May 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.5.31-alt6_3jpp6
- set target 5

* Thu Apr 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.5.31-alt5_3jpp6
- added osgi provides

* Sun Jan 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.5.31-alt5_2jpp6
- target 5 for catalina-manager.jar

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.5.31-alt4_2jpp6
- moved depmap to parent pom subpackage

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.5.31-alt3_2jpp6
- added parent pom subpackage

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.5.31-alt2_2jpp6
- fixed pom conflicts

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:5.5.31-alt1_2jpp6
- new version

* Fri Mar 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.5.27-alt4_7.4jpp5
- updated to fc 7.4
- CVE-2009-0033, CVE-2009-0580 (closes: 20311, 20314)
- su -s /bin/sh -c instead of su - (closes: #23073)

* Wed May 20 2009 Igor Vlasenko <viy@altlinux.ru> 0:5.5.27-alt4_6.2jpp5
- fixed build

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0:5.5.27-alt4_6.1jpp5
- moved poms to subpackage (poms break old depmaps)

* Wed Jan 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:5.5.27-alt3_6.1jpp5
- build with target 1.5 everywhere

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:5.5.27-alt2_6.1jpp5
- repocop fixes applied

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:5.5.27-alt1_6.1jpp6
- fixed xml-commons-apis link

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.5.27-alt1_4.9jpp5
- new version

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.5.26-alt3.2_1jpp5.1
- NMU (by repocop): the following fixes applied:
 * windows-thumbnail-database-in-package for tomcat5-webapps-admin

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.5.26-alt3.2_1jpp5
- rebuild with osgi provides

* Sat Mar 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.5.26-alt2.2_1jpp5.0
- fixed servletapi alternative

* Sat Mar 08 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.5.26-alt1.2_1jpp5.0
- new version; merged from fc9-devel

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.5.25-alt1_1.1jpp5.0
- Updated to 5.5.25, to fix the following issues:
  * CVE-2007-1355
  * CVE-2007-3386
  * CVE-2007-3385
  * CVE-2007-3382
  * CVE-2007-2450
  * CVE-2007-2449
- Applied patch(20) for CVE-2007-5461
- Applied patch(21) for CVE-2007-1358
- Add jasper-eclipse subpackage which is needed for eclipse 3.3.
- Inject OSGi manifest into servlet api jar and jsp api jar.

* Fri Aug 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.5.24-alt3_3jpp1.7
- added requires to javamail and jaf (do required)

* Fri Aug 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.5.24-alt2_3jpp1.7
- fixed bug in upgrade trigger

* Mon Jul 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.5.24-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 5.5.16-alt1.1
- rebuild with java-1.4
- provides tomcat-admin-webapps

* Sat Mar 25 2006 Vladimir Lettiev <crux@altlinux.ru> 5.5.16-alt1
- 5.5.16

* Tue Apr 05 2005 Vladimir Lettiev <crux@altlinux.ru> 5.0.30-alt1
- Initial build for ALT Linux Sisyphus

