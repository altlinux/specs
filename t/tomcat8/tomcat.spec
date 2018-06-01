%define oldname tomcat
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java zip
# END SourceDeps(oneline)
# fc script use systemctl calls -- gives dependency on systemctl :(
%add_findreq_skiplist %{_sbindir}/tomcat
%define _libexecdir %_prefix/libexec
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name tomcat
%define version 8.5.29
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

%global jspspec 2.3
%global major_version 8
%global minor_version 5
%global micro_version 29
%global packdname apache-tomcat-%{version}-src
%global servletspec 3.1
%global elspec 3.0
%global tcuid 91
# Recommended version is specified in java/org/apache/catalina/core/AprLifecycleListener.java
%global native_version 1.2.8


# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %{_var}/lib/%{oldname}
%global appdir %{basedir}/webapps
%global apphomedir %{_datadir}/%{oldname}
%global bindir %{apphomedir}/bin
%global confdir %{_sysconfdir}/%{oldname}
%global libdir %{_javadir}/%{oldname}
%global logdir %{_var}/log/%{oldname}
%global cachedir %{_var}/cache/%{oldname}
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work
%global _initrddir %{_sysconfdir}/init.d
%global _systemddir /lib/systemd/system

# Fedora doesn't seem to have this macro, so we define it if it doesn't exist
%{!?_mavendepmapfragdir: %global _mavendepmapfragdir /usr/share/maven-metadata}
# Fedora 24 erroneously uses %%{_datadir}/maven-fragments instead of /maven-metadata for some reason...
# Override the mavendepmapfragdir var on fc24
%{?fc24: %global _mavendepmapfragdir /usr/share/maven-metadata}

Name:          tomcat8
Epoch:         1
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       alt3_1jpp8
Summary:       Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

Group:         System/Servers
License:       ASL 2.0
URL:           http://tomcat.apache.org/
Source0:       http://www.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:       %{oldname}-%{major_version}.%{minor_version}.conf
Source3:       %{oldname}-%{major_version}.%{minor_version}.sysconfig
Source4:       %{oldname}-%{major_version}.%{minor_version}.wrapper
Source5:       %{oldname}-%{major_version}.%{minor_version}.logrotate
Source6:       %{oldname}-%{major_version}.%{minor_version}-digest.script
Source7:       %{oldname}-%{major_version}.%{minor_version}-tool-wrapper.script
Source8:       servlet-api-OSGi-MANIFEST.MF
Source9:       jsp-api-OSGi-MANIFEST.MF
Source11:      %{oldname}-%{major_version}.%{minor_version}.service
Source12:      el-api-OSGi-MANIFEST.MF
Source13:      jasper-el-OSGi-MANIFEST.MF
Source14:      jasper-OSGi-MANIFEST.MF
Source15:      tomcat-api-OSGi-MANIFEST.MF
Source16:      tomcat-juli-OSGi-MANIFEST.MF
Source20:      %{oldname}-%{major_version}.%{minor_version}-jsvc.service
Source21:      tomcat-functions
Source30:      tomcat-preamble
Source31:      tomcat-server
Source32:      tomcat-named.service

Patch0:        %{oldname}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        %{oldname}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
Patch2:        %{oldname}-8.0.36-CompilerOptionsV9.patch
Patch3:        disableJavadocFailOnWarning.patch

BuildArch:     noarch

BuildRequires: ant
BuildRequires: ecj >= 1:4.4.0
BuildRequires: findutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-daemon
BuildRequires: apache-commons-dbcp
BuildRequires: apache-commons-pool
BuildRequires: tomcat-taglibs-standard
BuildRequires: java-devel >= 1.6.0
BuildRequires: jpackage-utils >= 0:1.7.0
%if 0%{?fedora} >= 27 || 0%{?rhel} > 7
# add_maven_depmap is deprecated, using javapackages-local for now
# See https://fedora-java.github.io/howto/latest/#_add_maven_depmap_macro
BuildRequires: javapackages-local
%endif
BuildRequires: junit
BuildRequires: geronimo-jaxrpc
BuildRequires: wsdl4j

Requires:      apache-commons-daemon
Requires:      apache-commons-collections
Requires:      apache-commons-dbcp
Requires:      apache-commons-pool
Requires:      jpackage-utils
Requires:      procps
Requires:      tomcat8-el-3.0-api tomcat8-jsp-2.3-api tomcat8-lib tomcat8-servlet-3.1-api
Requires:    tomcat-native >= %{native_version}
Requires(pre):    shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils

# added after log4j sub-package was removed
Provides:         %{oldname}-log4j = %{epoch}:%{version}-%{release}
Source44: import.info
Patch33: tomcat-8.0.46-alt-tomcat-jasper.pom.patch
Source45: tomcat.init
Source46: tomcat-sysv.wrapper

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Group: System/Base
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: Text tools
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package javadoc
Group: Development/Java
Summary: Javadoc generated documentation for Apache Tomcat
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc generated documentation for Apache Tomcat.

%package jsvc
Group: System/Servers
Summary: Apache jsvc wrapper for Apache Tomcat as separate service
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: apache-commons-daemon-jsvc

%description jsvc
Systemd service to start tomcat with jsvc,
which allows tomcat to perform some privileged operations
(e.g. bind to a port < 1024) and then switch identity to a non-privileged user.

%package jsp-%{jspspec}-api
Group: Development/Other
Summary: Apache Tomcat JavaServer Pages v%{jspspec} API Implementation Classes
Provides: jsp = %{jspspec}
Obsoletes: %{oldname}-jsp-2.2-api
Provides: %{oldname}-jsp-3.1-api
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}

%description jsp-%{jspspec}-api
Apache Tomcat JSP API Implementation Classes.

%package lib
Group: Development/Other
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: ecj >= 1:4.2.1
Requires: apache-commons-collections
Requires: apache-commons-dbcp
Requires: apache-commons-pool
Requires(preun): coreutils

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Group: Development/Other
Summary: Apache Tomcat Java Servlet v%{servletspec} API Implementation Classes
Provides: servlet = %{servletspec}
#Provides: servlet6
#Provides: servlet3
Obsoletes: %{oldname}-servlet-3.0-api
Provides: %{oldname}-servlet-%{servletspec}-api = %EVR

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API Implementation Classes.

%package el-%{elspec}-api
Group: Development/Other
Summary: Apache Tomcat Expression Language v%{elspec} API Implementation Classes
Provides: el_api = %{elspec}
Obsoletes: %{oldname}-el-2.2-api

%description el-%{elspec}-api
Apache Tomcat EL API Implementation Classes.

%package webapps
Group: Networking/WWW
Summary: The ROOT and examples web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: tomcat-taglibs-standard >= 0:1.1

%description webapps
The ROOT and examples web applications for Apache Tomcat.

%prep
%setup -q -n %{packdname}
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0

ln -s $(build-classpath tomcat-taglibs-standard/taglibs-standard-impl) webapps/examples/WEB-INF/lib/jstl.jar
ln -s $(build-classpath tomcat-taglibs-standard/taglibs-standard-compat) webapps/examples/WEB-INF/lib/standard.jar
%patch33 -p0

%build
export OPT_JAR_LIST="xalan-j2-serializer"
   # we don't care about the tarballs and we're going to replace
   # tomcat-dbcp.jar with apache-commons-{collections,dbcp,pool}-tomcat5.jar
   # so just create a dummy file for later removal
   touch HACK

   # who needs a build.properties file anyway
   %{ant} -Dbase.path="." \
      -Dbuild.compiler="modern" \
      -Dcommons-collections.jar="$(build-classpath apache-commons-collections)" \
      -Dcommons-daemon.jar="$(build-classpath apache-commons-daemon)" \
      -Dcommons-daemon.native.src.tgz="HACK" \
      -Djdt.jar="$(build-classpath ecj)" \
      -Dtomcat-native.tar.gz="HACK" \
      -Dtomcat-native.home="." \
      -Dcommons-daemon.native.win.mgr.exe="HACK" \
      -Dnsis.exe="HACK" \
      -Djaxrpc-lib.jar="$(build-classpath jaxrpc)" \
      -Dwsdl4j-lib.jar="$(build-classpath wsdl4j)" \
      -Dno.build.dbcp=true \
      -Dversion="%{version}" \
      -Dversion.build="%{micro_version}" \
      -Djava.7.home=%{java_home} \
      -Dexecute.validate=false \
      deploy dist-prepare dist-source javadoc

    # remove some jars that we'll replace with symlinks later
    rm output/build/bin/commons-daemon.jar output/build/lib/ecj.jar
pushd output/dist/src/webapps/docs/appdev/sample/src
mkdir -p ../web/WEB-INF/classes
%{javac} -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
%{jar} cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip output/build/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip output/build/lib/jsp-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE12} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip output/build/lib/el-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE13} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip output/build/lib/jasper-el.jar META-INF/MANIFEST.MF
cp -p %{SOURCE14} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip output/build/lib/jasper.jar META-INF/MANIFEST.MF
cp -p %{SOURCE15} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip output/build/lib/tomcat-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE16} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip output/build/bin/tomcat-juli.jar META-INF/MANIFEST.MF

%install
# build initial path structure
install -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}
install -d -m 0755 ${RPM_BUILD_ROOT}%{_sbindir}
install -d -m 0755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{oldname}
install -d -m 0755 ${RPM_BUILD_ROOT}%{_initrddir}
install -d -m 0755 ${RPM_BUILD_ROOT}%{_systemddir}
install -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -d -m 0755 ${RPM_BUILD_ROOT}%{appdir}
install -d -m 0755 ${RPM_BUILD_ROOT}%{bindir}
install -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}
install -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
install -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/conf.d
/bin/echo "Place your custom *.conf files here. Shell expansion is supported." > ${RPM_BUILD_ROOT}%{confdir}/conf.d/README
install -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}
install -d -m 0775 ${RPM_BUILD_ROOT}%{logdir}
/bin/touch ${RPM_BUILD_ROOT}%{logdir}/catalina.out
install -d -m 0775 ${RPM_BUILD_ROOT}%{_localstatedir}/lib/tomcats
install -d -m 0775 ${RPM_BUILD_ROOT}%{apphomedir}
install -d -m 0775 ${RPM_BUILD_ROOT}%{tempdir}
install -d -m 0775 ${RPM_BUILD_ROOT}%{workdir}
install -d -m 0755 ${RPM_BUILD_ROOT}%{_unitdir}
install -d -m 0755 ${RPM_BUILD_ROOT}%{_libexecdir}/%{oldname}

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    cp -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    cp -a conf/*.{policy,properties,xml,xsd} ${RPM_BUILD_ROOT}%{confdir}
    cp -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    cp -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd
# javadoc
cp -a output/dist/webapps/docs/api/* ${RPM_BUILD_ROOT}%{_javadocdir}/%{oldname}

sed -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > ${RPM_BUILD_ROOT}%{confdir}/%{oldname}.conf
sed -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{oldname}
install -m 0644 %{SOURCE4} \
    ${RPM_BUILD_ROOT}%{_sbindir}/%{oldname}
install -m 0644 %{SOURCE11} \
    ${RPM_BUILD_ROOT}%{_unitdir}/%{oldname}.service
install -m 0644 %{SOURCE20} \
    ${RPM_BUILD_ROOT}%{_unitdir}/%{oldname}-jsvc.service
sed -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{oldname}
sed -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{oldname}-digest
sed -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{oldname}-tool-wrapper

install -m 0644 %{SOURCE21} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/%{oldname}/functions
install -m 0755 %{SOURCE30} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/%{oldname}/preamble
install -m 0755 %{SOURCE31} \
    ${RPM_BUILD_ROOT}%{_libexecdir}/%{oldname}/server
install -m 0644 %{SOURCE32} \
    ${RPM_BUILD_ROOT}%{_unitdir}/%{oldname}@.service

# Substitute libnames in catalina-tasks.xml
sed -i \
   "s,el-api.jar,%{name}-el-%{elspec}-api.jar,;
    s,servlet-api.jar,%{name}-servlet-%{servletspec}-api.jar,;
    s,jsp-api.jar,%{name}-jsp-%{jspspec}-api.jar,;" \
    ${RPM_BUILD_ROOT}%{bindir}/catalina-tasks.xml

# create jsp and servlet API symlinks
pushd ${RPM_BUILD_ROOT}%{_javadir}
   mv %{oldname}/jsp-api.jar %{name}-jsp-%{jspspec}-api.jar
   ln -s %{name}-jsp-%{jspspec}-api.jar %{name}-jsp-api.jar
   mv %{oldname}/servlet-api.jar %{name}-servlet-%{servletspec}-api.jar
   ln -s %{name}-servlet-%{servletspec}-api.jar %{name}-servlet-api.jar
   mv %{oldname}/el-api.jar %{name}-el-%{elspec}-api.jar
   ln -s %{name}-el-%{elspec}-api.jar %{name}-el-api.jar
popd

pushd output/build
    %{_bindir}/build-jar-repository lib apache-commons-collections \
                                        apache-commons-dbcp apache-commons-pool ecj 2>&1
    # need to use -p here with b-j-r otherwise the examples webapp fails to
    # load with a java.io.IOException
    %{_bindir}/build-jar-repository -p webapps/examples/WEB-INF/lib \
    tomcat-taglibs-standard/taglibs-standard-impl.jar tomcat-taglibs-standard/taglibs-standard-compat.jar 2>&1
popd

pushd ${RPM_BUILD_ROOT}%{libdir}
    # symlink JSP and servlet API jars
    ln -s ../../java/%{name}-jsp-%{jspspec}-api.jar .
    ln -s ../../java/%{name}-servlet-%{servletspec}-api.jar .
    ln -s ../../java/%{name}-el-%{elspec}-api.jar .
    ln -s $(build-classpath apache-commons-collections) commons-collections.jar
    ln -s $(build-classpath apache-commons-dbcp) commons-dbcp.jar
    ln -s $(build-classpath apache-commons-pool) commons-pool.jar
    ln -s $(build-classpath ecj) jasper-jdt.jar

    # Temporary copy the juli jar here from /usr/share/java/tomcat (for maven depmap)
    cp -a ${RPM_BUILD_ROOT}%{bindir}/tomcat-juli.jar ./
popd

# symlink to the FHS locations where we've installed things
pushd ${RPM_BUILD_ROOT}%{apphomedir}
    ln -s %{appdir} webapps
    ln -s %{confdir} conf
    ln -s %{libdir} lib
    ln -s %{logdir} logs
    ln -s %{tempdir} temp
    ln -s %{workdir} work
popd

# install sample webapp
mkdir -p ${RPM_BUILD_ROOT}%{appdir}/sample
pushd ${RPM_BUILD_ROOT}%{appdir}/sample
%{jar} xf ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war
popd
rm ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war

# Allow linking for example webapp
mkdir -p ${RPM_BUILD_ROOT}%{appdir}/examples/META-INF
pushd ${RPM_BUILD_ROOT}%{appdir}/examples/META-INF
echo '<?xml version="1.0" encoding="UTF-8"?>' > context.xml
echo '<Context>' >> context.xml
echo '  <Resources allowLinking="true" />' >> context.xml
echo '</Context>' >> context.xml
popd

pushd ${RPM_BUILD_ROOT}%{appdir}/examples/WEB-INF/lib
ln -s -f $(build-classpath tomcat-taglibs-standard/taglibs-standard-impl) jstl.jar
ln -s -f $(build-classpath tomcat-taglibs-standard/taglibs-standard-compat) standard.jar
popd


# Install the maven metadata
install -d -m 0755 ${RPM_BUILD_ROOT}%{_mavenpomdir}
pushd output/dist/src/res/maven
for pom in *.pom; do
    # fix-up version in all pom files
    sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $pom
done

# we won't install dbcp, juli-adapters and juli-extras pom files
for libname in annotations-api catalina jasper-el jasper catalina-ha; do
    cp -a %{oldname}-$libname.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-$libname.pom
    %add_maven_depmap JPP.%{oldname}-$libname.pom %{oldname}/$libname.jar -f "tomcat-lib"
done

# tomcat-util-scan
cp -a %{oldname}-util-scan.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-util-scan.pom
%add_maven_depmap JPP.%{oldname}-util-scan.pom %{oldname}/%{oldname}-util-scan.jar -f "tomcat-lib"

# tomcat-jni
cp -a %{oldname}-jni.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-jni.pom
%add_maven_depmap JPP.%{oldname}-jni.pom %{oldname}/%{oldname}-jni.jar -f "tomcat-lib" -v %version

# servlet-api jsp-api and el-api are not in tomcat subdir, since they are widely re-used elsewhere
cp -a tomcat-jsp-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-tomcat8-jsp-api.pom
%add_maven_depmap JPP-tomcat8-jsp-api.pom tomcat8-jsp-api.jar -f "tomcat8-jsp-api" -a "org.eclipse.jetty.orbit:javax.servlet.jsp" -v %version


cp -a tomcat-el-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-tomcat8-el-api.pom
%add_maven_depmap JPP-tomcat8-el-api.pom tomcat8-el-api.jar -f "tomcat8-el-api" -a "org.eclipse.jetty.orbit:javax.el"

cp -a tomcat-servlet-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-tomcat8-servlet-api.pom
# Generate a depmap fragment javax.servlet:servlet-api pointing to
# tomcat-servlet-3.0-api for backwards compatibility
# also provide jetty depmap (originally in jetty package, but it's cleaner to have it here
#add_maven_depmap JPP-tomcat8-servlet-api.pom tomcat8-servlet-api.jar -f "javax-servlet-api" -a 'javax.servlet:javax.servlet-api' -v 3.1.0
%add_maven_depmap JPP-tomcat8-servlet-api.pom tomcat8-servlet-api.jar -f "tomcat8-servlet-api" -v %version

# replace temporary copy with link
ln -s -f $(abs2rel %{bindir}/tomcat-juli.jar %{libdir}) ${RPM_BUILD_ROOT}%{libdir}/

# two special pom where jar files have different names
cp -a tomcat-tribes.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-catalina-tribes.pom
%add_maven_depmap JPP.%{oldname}-catalina-tribes.pom %{oldname}/catalina-tribes.jar

cp -a tomcat-coyote.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-tomcat-coyote.pom
%add_maven_depmap JPP.%{oldname}-tomcat-coyote.pom %{oldname}/tomcat-coyote.jar

cp -a tomcat-juli.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-tomcat-juli.pom
%add_maven_depmap JPP.%{oldname}-tomcat-juli.pom %{oldname}/tomcat-juli.jar

cp -a tomcat-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-tomcat-api.pom
%add_maven_depmap JPP.%{oldname}-tomcat-api.pom %{oldname}/tomcat-api.jar

cp -a tomcat-util.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-tomcat-util.pom
%add_maven_depmap JPP.%{oldname}-tomcat-util.pom %{oldname}/tomcat-util.jar

cp -a tomcat-jdbc.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-tomcat-jdbc.pom
%add_maven_depmap JPP.%{oldname}-tomcat-jdbc.pom %{oldname}/tomcat-jdbc.jar

# tomcat-websocket-api
cp -a tomcat-websocket-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-websocket-api.pom
%add_maven_depmap JPP.%{oldname}-websocket-api.pom %{oldname}/websocket-api.jar

# tomcat-tomcat-websocket
cp -a tomcat-websocket.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-tomcat-websocket.pom
%add_maven_depmap JPP.%{oldname}-tomcat-websocket.pom %{oldname}/tomcat-websocket.jar

# tomcat-jaspic-api
cp -a tomcat-jaspic-api.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{oldname}-jaspic-api.pom
%add_maven_depmap JPP.%{oldname}-jaspic-api.pom %{oldname}/jaspic-api.jar
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_tomcat8-jsp-2.3-api<<EOF
%{_javadir}/jsp.jar	%{_javadir}/%{name}-jsp-%{jspspec}-api.jar	20200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_tomcat8-servlet-3.1-api<<EOF
%{_javadir}/servlet.jar	%{_javadir}/%{name}-servlet-%{servletspec}-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/elspec_tomcat8-el-3.0-api<<EOF
%{_javadir}/elspec.jar	%{_javadir}/%{name}-el-%{elspec}-api.jar	20300
EOF
install -D -m 755 %{S:45} %buildroot%_initdir/%oldname
install -D -m 755 %{S:46} %buildroot%_sbindir/%{oldname}-sysv


%pre
%{_sbindir}/groupadd -g %{tcuid} -r tomcat 2>/dev/null || :
%{_sbindir}/useradd -c "Apache Tomcat" -u %{tcuid} -g tomcat \
    -s /sbin/nologin -r -d %{apphomedir} tomcat 2>/dev/null || :

%post
%post_service %{oldname}

%preun
%{__rm} -rf %{workdir}/* %{tempdir}/*
%preun_service %{oldname}

%if 0
%files 
%defattr(0644,root,tomcat,0755)
%attr(0755,root,root) %doc LICENSE
%attr(0755,root,root) %doc NOTICE
%attr(0755,root,root) %doc RELEASE*
%attr(0755,root,root) %{_bindir}/%{oldname}-digest
%attr(0755,root,root) %{_bindir}/%{oldname}-tool-wrapper
%attr(0755,root,root) %{_sbindir}/%{oldname}
%attr(0644,root,root) %{_unitdir}/%{oldname}.service
%attr(0644,root,root) %{_unitdir}/%{oldname}@.service
%attr(0755,root,root) %dir %{_libexecdir}/%{oldname}
%attr(0755,root,root) %dir %{_localstatedir}/lib/tomcats
%attr(0644,root,root) %{_libexecdir}/%{oldname}/functions
%attr(0755,root,root) %{_libexecdir}/%{oldname}/preamble
%attr(0755,root,root) %{_libexecdir}/%{oldname}/server
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{oldname}
%attr(0755,root,tomcat) %dir %{basedir}
%attr(0755,root,tomcat) %dir %{confdir}

%defattr(0664,tomcat,root,0770)
%attr(0770,tomcat,root) %dir %{logdir}

%defattr(0644,root,tomcat,0770)
%attr(0770,root,tomcat) %dir %{cachedir}
%attr(0770,root,tomcat) %dir %{tempdir}
%attr(0770,root,tomcat) %dir %{workdir}

%defattr(0644,root,tomcat,0775)
%attr(0775,root,tomcat) %dir %{appdir}
%attr(0775,root,tomcat) %dir %{confdir}/Catalina
%attr(0775,root,tomcat) %dir %{confdir}/Catalina/localhost
%attr(0755,root,tomcat) %dir %{confdir}/conf.d
%{confdir}/conf.d/README
%config(noreplace) %{confdir}/%{oldname}.conf
%config(noreplace) %{confdir}/*.policy
%config(noreplace) %{confdir}/*.properties
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/server.xml
%attr(0640,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%attr(0644,root,tomcat) %{confdir}/tomcat-users.xsd
%attr(0644,root,tomcat) %config(noreplace) %{confdir}/jaspic-providers.xml
%attr(0644,root,tomcat) %{confdir}/jaspic-providers.xsd
%config(noreplace) %{confdir}/web.xml
%attr(0755,root,root) %dir %{apphomedir}
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{apphomedir}/lib
%{apphomedir}/temp
%{apphomedir}/webapps
%{apphomedir}/work
%{apphomedir}/logs
%{apphomedir}/conf
%attr(0755,root,root) %_initdir/%oldname
%attr(0755,root,root) %_sbindir/%{oldname}-sysv
%attr(0755,root,root) %dir %{bindir}

%files admin-webapps
%defattr(0664,root,tomcat,0755)
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%{appdir}/docs

%files javadoc
%{_javadocdir}/%{oldname}
%endif

%if 0
%files jsp-%{jspspec}-api -f output/dist/src/res/maven/.mfiles-tomcat8-jsp-api
%_altdir/jsp_tomcat-jsp-2.3-api
%{_javadir}/%{oldname}-jsp-%{jspspec}*.jar
%endif

%if 0
%files lib -f output/dist/src/res/maven/.mfiles-tomcat-lib
%dir %{libdir}
%{libdir}/*.jar
%{_javadir}/*.jar
%{bindir}/tomcat-juli.jar
%{_mavenpomdir}/JPP.%{oldname}-annotations-api.pom
%{_mavenpomdir}/JPP.%{oldname}-catalina-ha.pom
%{_mavenpomdir}/JPP.%{oldname}-catalina-tribes.pom
%{_mavenpomdir}/JPP.%{oldname}-catalina.pom
%{_mavenpomdir}/JPP.%{oldname}-jasper-el.pom
%{_mavenpomdir}/JPP.%{oldname}-jasper.pom
%{_mavenpomdir}/JPP.%{oldname}-tomcat-api.pom
%{_mavenpomdir}/JPP.%{oldname}-tomcat-juli.pom
%{_mavenpomdir}/JPP.%{oldname}-tomcat-coyote.pom
%{_mavenpomdir}/JPP.%{oldname}-tomcat-util.pom
%{_mavenpomdir}/JPP.%{oldname}-tomcat-jdbc.pom
%{_mavenpomdir}/JPP.%{oldname}-websocket-api.pom
%{_mavenpomdir}/JPP.%{oldname}-tomcat-websocket.pom
%{_mavenpomdir}/JPP.%{oldname}-jaspic-api.pom
%{_datadir}/maven-metadata/tomcat*.xml
%exclude %{libdir}/%{oldname}-el-%{elspec}-api.jar
%exclude %{_javadir}/%{oldname}-servlet-%{servletspec}*.jar
%exclude %{_javadir}/%{oldname}-el-%{elspec}-api.jar
%exclude %{_javadir}/%{oldname}-jsp-%{jspspec}*.jar
%endif

%files servlet-%{servletspec}-api -f output/dist/src/res/maven/.mfiles-tomcat8-servlet-api
%_altdir/servlet_tomcat8-servlet-3.1-api
%doc LICENSE
%{_javadir}/%{name}-servlet-%{servletspec}*.jar

%if 0
%files el-%{elspec}-api -f output/dist/src/res/maven/.mfiles-tomcat8-el-api
%_altdir/elspec_tomcat8-el-3.0-api
%doc LICENSE
%{_javadir}/%{name}-el-%{elspec}-api.jar
#%{libdir}/%{name}-el-%{elspec}-api.jar
%endif

%if 0
%files webapps
%defattr(0644,tomcat,tomcat,0755)
%{appdir}/ROOT
%{appdir}/examples
%{appdir}/sample

%files jsvc
%defattr(755,root,root,0755)
%attr(0644,root,root) %{_unitdir}/%{oldname}-jsvc.service
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{oldname}
%attr(0660,tomcat,tomcat) %verify(not size md5 mtime) %{logdir}/catalina.out
%endif

%changelog
* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:8.5.29-alt3_1jpp8
- added compat provides

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:8.5.29-alt2_1jpp8
- compat package

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:8.5.29-alt1_1jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:8.0.47-alt1_2jpp8
- new version

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:8.0.46-alt1_1jpp8
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1:8.0.43-alt1_1jpp8
- new jpp release

* Thu Apr 28 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.32-alt4_4jpp8
- tomcat-native is Recommended, not Required

* Sun Mar 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.32-alt3_4jpp8
- logrotate bugfix thanks to Chess@

* Sun Mar 13 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.32-alt2_4jpp8
- sysVinit bugfixes thanks to Chess@

* Sat Mar 05 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.32-alt1_4jpp8
- new version

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.26-alt2_1jpp8
- fixed relative links in CATALINA_HOME

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.26-alt1_1jpp8
- java 8 mass update

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:7.0.28-alt1_0jpp7
- bootstrap build (w/o jsvc)

