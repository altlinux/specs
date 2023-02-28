Group: System/Servers
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-alternatives rpm-macros-java
# END SourceDeps(oneline)
# fc script use systemctl calls -- gives dependency on systemctl :(
%add_findreq_skiplist %_sbindir/tomcat
%define _libexecdir %prefix/libexec
%define tomcat_user tomcat
%define tomcat_group tomcat
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
%define fedora 34
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
# %%tomcatname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define tomcatname tomcat
%define name tomcat10
%define version 10.1.5
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

%global jspspec 3.1
%global major_version 10
%global minor_version 1
%global micro_version 5
%global packdname apache-tomcat-%version-src
%global servletspec 6.0
%global elspec 5.0
%global tcuid 53
# Recommended version is specified in java/org/apache/catalina/core/AprLifecycleListener.java
%global native_version 1.2.21

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %_var/lib/%tomcatname
%global appdir %basedir/webapps
%global apphomedir %_datadir/%tomcatname
%global bindir %apphomedir/bin
%global confdir %_sysconfdir/%tomcatname
%global libdir %_javadir/%tomcatname
%global logdir %_var/log/%tomcatname
%global cachedir %_var/cache/%tomcatname
%global tempdir %cachedir/temp
%global workdir %cachedir/work
%global _systemddir /lib/systemd/system

Name: tomcat10
Epoch: 1
Version: %major_version.%minor_version.%micro_version
Release: alt1_jvm11
Summary: Apache Servlet/JSP Engine, RI for Servlet %servletspec/JSP %jspspec API

License: Apache-2.0
Url: http://tomcat.apache.org/
Source0: http://www.apache.org/dist/tomcat/tomcat-%major_version/v%version/src/%packdname.tar.gz
Source1: %tomcatname-%major_version.%minor_version.conf
Source3: %tomcatname-%major_version.%minor_version.sysconfig
Source4: %tomcatname-%major_version.%minor_version.wrapper
Source5: %tomcatname-%major_version.%minor_version.logrotate
Source6: %tomcatname-%major_version.%minor_version-digest.script
Source7: %tomcatname-%major_version.%minor_version-tool-wrapper.script
Source11: %tomcatname-%major_version.%minor_version.service
Source21: tomcat-functions
Source30: tomcat-preamble
Source31: tomcat-server
Source32: tomcat-named.service
Source33: java-9-start-up-parameters.conf
Source40: jakartaee-migration-1.0.6-shaded.jar
Source41: geronimo-spec-jaxrpc-1.1-rc4.jar
Source42: biz.aQute.bnd-6.3.1.jar

Patch0: %tomcatname-%major_version.%minor_version-bootstrap-MANIFEST.MF.patch
Patch1: %tomcatname-%major_version.%minor_version-tomcat-users-webapp.patch
Patch2: %tomcatname-build.patch
Patch3: %tomcatname-%major_version.%minor_version-catalina-policy.patch
Patch4: rhbz-1857043.patch
Patch5: %tomcatname-%major_version.%minor_version-JDTCompiler.patch

BuildArch: noarch

BuildRequires: ant
BuildRequires: ecj >= 1:4.10
BuildRequires: findutils
BuildRequires: javapackages-local
#BuildRequires: aqute-bnd
#BuildRequires: aqute-bndlib
BuildRequires: wsdl4j
BuildRequires: libsystemd-devel libudev-devel systemd systemd-analyze systemd-homed systemd-networkd systemd-portable systemd-sysvinit

Requires: javapackages-tools
Requires: procps
Requires: %name-lib = %epoch:%version-%release
%if 0%{?fedora} || 0%{?rhel} > 7
Requires: tomcat-native >= %native_version
%endif
Requires(pre):    shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils

# added after log4j sub-package was removed
Provides: %name-log4j = %epoch:%version-%release
Conflicts: %tomcatname
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
Requires: %name = %epoch:%version-%release
Conflicts: %tomcatname-admin-webapps

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: Text tools
Summary: The docs web application for Apache Tomcat
Requires: %name = %epoch:%version-%release
Conflicts: %tomcatname-docs-webapp

%description docs-webapp
The docs web application for Apache Tomcat.

%package jsp-%jspspec-api
Group: Development/Other
Summary: Apache Tomcat JavaServer Pages v%jspspec API Implementation Classes
Provides: jsp = %jspspec
Obsoletes: %name-jsp-2.2-api
Requires: %name-servlet-%servletspec-api = %epoch:%version-%release
Requires: %name-el-%elspec-api = %epoch:%version-%release
Conflicts: %tomcatname-jsp-%jspspec-ap

%description jsp-%jspspec-api
Apache Tomcat JSP API Implementation Classes.

%package lib
Group: Development/Other
Summary: Libraries needed to run the Tomcat Web container
Requires: %name-jsp-%jspspec-api = %epoch:%version-%release
Requires: %name-servlet-%servletspec-api = %epoch:%version-%release
Requires: %name-el-%elspec-api = %epoch:%version-%release
Requires: ecj >= 1:4.10
Requires(preun): coreutils
Conflicts: %tomcatname-lib

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%servletspec-api
Group: Development/Other
Summary: Apache Tomcat Java Servlet v%servletspec API Implementation Classes
Provides: servlet = %servletspec
Provides: servlet6
Provides: servlet3
Obsoletes: %name-servlet-3.1-api
Conflicts: %tomcatname-servlet-%servletspec-api

%description servlet-%servletspec-api
Apache Tomcat Servlet API Implementation Classes.

%package el-%elspec-api
Group: Development/Other
Summary: Apache Tomcat Expression Language v%elspec API Implementation Classes
Provides: el_api = %elspec
Obsoletes: %name-el-2.2-api
Conflicts: %tomcatname-el-%elspec-api

%description el-%elspec-api
Apache Tomcat EL API Implementation Classes.

%package webapps
Group: Networking/WWW
Summary: The ROOT web application for Apache Tomcat
Requires: %name = %epoch:%version-%release
Conflicts: %tomcatname-webapps

%description webapps
The ROOT web application for Apache Tomcat.

%prep
%setup -n %packdname
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0

# Remove webservices naming resources as it's generally unused
rm -rf java/org/apache/naming/factory/webservices

# Configure maven files
%mvn_package ":tomcat-el-api" tomcat-el-api
%mvn_alias "org.apache.tomcat:tomcat-el-api" "org.eclipse.jetty.orbit:javax.el"
%mvn_package ":tomcat-jsp-api" tomcat-jsp-api
%mvn_alias "org.apache.tomcat:tomcat-jsp-api" "org.eclipse.jetty.orbit:javax.servlet.jsp"
%mvn_package ":tomcat-servlet-api" tomcat-servlet-api
%patch33 -p0

%build
export OPT_JAR_LIST="xalan-j2-serializer"
# we don't care about the tarballs and we're going to replace
# tomcat-dbcp.jar with apache-commons-{collections,dbcp,pool}-tomcat5.jar
# so just create a dummy file for later removal
touch HACK

# who needs a build.properties file anyway
%ant -Dant.build.javac.source=11 -Dant.build.javac.target=11  -Dbase.path="." \
  -Dbuild.compiler="modern" \
  -Dcommons-daemon.jar="HACK" \
  -Dcommons-daemon.native.src.tgz="HACK" \
  -Djdt.jar="$(build-classpath ecj/ecj)" \
  -Dtomcat-native.tar.gz="HACK" \
  -Dtomcat-native.home="." \
  -Dcommons-daemon.native.win.mgr.exe="HACK" \
  -Dnsis.exe="HACK" \
  -Djaxrpc-lib.jar="HACK" \
  -Dwsdl4j-lib.jar="$(build-classpath wsdl4j)" \
  -Dmigration-lib.jar="%SOURCE40" \
  -Djaxrpc-lib.jar="%SOURCE41" \
  -Dbnd.jar="%SOURCE42" \
  -Dosgi-annotations.jar="$(build-classpath aqute-bnd/biz.aQute.bnd.annotation)" \
  -Dslf4j-api.jar="$(build-classpath slf4j/slf4j-api)" \
  -Dosgi-cmpn.jar="$(build-classpath osgi-compendium/osgi.cmpn)" \
  -Dversion="%version" \
  -Dversion.build="%micro_version" \
  deploy

# remove some jars that we'll replace with symlinks later
rm output/build/bin/commons-daemon.jar output/build/lib/ecj.jar
# Remove the example webapps per Apache Tomcat Security Considerations
# see https://tomcat.apache.org/tomcat-9.0-doc/security-howto.html
rm -rf output/build/webapps/examples

%install
# build initial path structure
install -d -m 0755 $RPM_BUILD_ROOT%_bindir
install -d -m 0755 $RPM_BUILD_ROOT%_sbindir
install -d -m 0755 $RPM_BUILD_ROOT%_systemddir
install -d -m 0755 $RPM_BUILD_ROOT%_sysconfdir/logrotate.d
install -d -m 0755 $RPM_BUILD_ROOT%_sysconfdir/sysconfig
install -d -m 0755 $RPM_BUILD_ROOT%appdir
install -d -m 0755 $RPM_BUILD_ROOT%bindir
install -d -m 0775 $RPM_BUILD_ROOT%confdir
install -d -m 0775 $RPM_BUILD_ROOT%confdir/Catalina/localhost
install -d -m 0775 $RPM_BUILD_ROOT%confdir/conf.d
/bin/echo "Place your custom *.conf files here. Shell expansion is supported." > $RPM_BUILD_ROOT%confdir/conf.d/README
install -d -m 0755 $RPM_BUILD_ROOT%libdir
install -d -m 0775 $RPM_BUILD_ROOT%logdir
install -d -m 0775 $RPM_BUILD_ROOT%_localstatedir/lib/tomcats
install -d -m 0775 $RPM_BUILD_ROOT%apphomedir
install -d -m 0775 $RPM_BUILD_ROOT%tempdir
install -d -m 0775 $RPM_BUILD_ROOT%workdir
install -d -m 0755 $RPM_BUILD_ROOT%_unitdir
install -d -m 0755 $RPM_BUILD_ROOT%_libexecdir/%tomcatname

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    cp -a bin/*.{jar,xml} $RPM_BUILD_ROOT%bindir
    cp -a conf/*.{policy,properties,xml,xsd} $RPM_BUILD_ROOT%confdir
    cp -a lib/*.jar $RPM_BUILD_ROOT%libdir
    cp -a webapps/* $RPM_BUILD_ROOT%appdir
popd

sed -e "s|\@\@\@TCHOME\@\@\@|%apphomedir|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%tempdir|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%_libdir|g" %SOURCE1 \
    > $RPM_BUILD_ROOT%confdir/%tomcatname.conf
sed -e "s|\@\@\@TCHOME\@\@\@|%apphomedir|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%tempdir|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%_libdir|g" %SOURCE3 \
    > $RPM_BUILD_ROOT%_sysconfdir/sysconfig/%tomcatname
install -m 0644 %SOURCE4 \
    $RPM_BUILD_ROOT%_sbindir/%tomcatname
install -m 0644 %SOURCE11 \
    $RPM_BUILD_ROOT%_unitdir/%tomcatname.service
sed -e "s|\@\@\@TCLOG\@\@\@|%logdir|g" %SOURCE5 \
    > $RPM_BUILD_ROOT%_sysconfdir/logrotate.d/%tomcatname.disabled
sed -e "s|\@\@\@TCHOME\@\@\@|%apphomedir|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%tempdir|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%_libdir|g" %SOURCE6 \
    > $RPM_BUILD_ROOT%_bindir/%tomcatname-digest
sed -e "s|\@\@\@TCHOME\@\@\@|%apphomedir|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%tempdir|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%_libdir|g" %SOURCE7 \
    > $RPM_BUILD_ROOT%_bindir/%tomcatname-tool-wrapper

install -m 0644 %SOURCE21 \
    $RPM_BUILD_ROOT%_libexecdir/%tomcatname/functions
install -m 0755 %SOURCE30 \
    $RPM_BUILD_ROOT%_libexecdir/%tomcatname/preamble
install -m 0755 %SOURCE31 \
    $RPM_BUILD_ROOT%_libexecdir/%tomcatname/server
install -m 0644 %SOURCE32 \
    $RPM_BUILD_ROOT%_unitdir/%tomcatname@.service

install -m 0644 %SOURCE33 $RPM_BUILD_ROOT%confdir/conf.d/

# Substitute libnames in catalina-tasks.xml
sed -i \
   "s,el-api.jar,%tomcatname-el-%elspec-api.jar,;
    s,servlet-api.jar,%tomcatname-servlet-%servletspec-api.jar,;
    s,jsp-api.jar,%tomcatname-jsp-%jspspec-api.jar,;" \
    $RPM_BUILD_ROOT%bindir/catalina-tasks.xml

# create jsp and servlet API symlinks
pushd $RPM_BUILD_ROOT%_javadir
   mv %tomcatname/jsp-api.jar %tomcatname-jsp-%jspspec-api.jar
   ln -s %tomcatname-jsp-%jspspec-api.jar %tomcatname-jsp-api.jar
   mv %tomcatname/servlet-api.jar %tomcatname-servlet-%servletspec-api.jar
   ln -s %tomcatname-servlet-%servletspec-api.jar %tomcatname-servlet-api.jar
   mv %tomcatname/el-api.jar %tomcatname-el-%elspec-api.jar
   ln -s %tomcatname-el-%elspec-api.jar %tomcatname-el-api.jar
popd

pushd output/build
    %_bindir/build-jar-repository lib ecj 2>&1
popd

pushd $RPM_BUILD_ROOT%libdir
    # symlink JSP and servlet API jars
    ln -s ../../java/%tomcatname-jsp-%jspspec-api.jar .
    ln -s ../../java/%tomcatname-servlet-%servletspec-api.jar .
    ln -s ../../java/%tomcatname-el-%elspec-api.jar .
    ln -s $(build-classpath ecj/ecj) jasper-jdt.jar
popd

# symlink to the FHS locations where we've installed things
pushd $RPM_BUILD_ROOT%apphomedir
    ln -s %appdir webapps
    ln -s %confdir conf
    ln -s %libdir lib
    ln -s %logdir logs
    ln -s %tempdir temp
    ln -s %workdir work
popd

# Install the maven metadata for the spec impl artifacts as other projects use them
#install -d -m 0755 $RPM_BUILD_ROOT%_mavenpomdir
pushd res/maven
    for pom in tomcat-el-api.pom tomcat-jsp-api.pom tomcat-servlet-api.pom; do
        # fix-up version in all pom files
        sed -i 's/@MAVEN.DEPLOY.VERSION@/%version/g' $pom
    done
popd

# Configure and install maven artifacts
%mvn_artifact res/maven/tomcat-el-api.pom output/build/lib/el-api.jar
%mvn_artifact res/maven/tomcat-jsp-api.pom output/build/lib/jsp-api.jar
%mvn_artifact res/maven/tomcat-servlet-api.pom output/build/lib/servlet-api.jar
%mvn_install
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_tomcat-jsp-3.1-api<<EOF
%_javadir/jsp.jar	%_javadir/%name-jsp-%jspspec-api.jar	20200
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_tomcat-servlet-6.0-api<<EOF
%_javadir/servlet.jar	%_javadir/%name-servlet-%servletspec-api.jar	30000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/elspec_tomcat-el-5.0-api<<EOF
%_javadir/elspec.jar	%_javadir/%name-el-%elspec-api.jar	20300
EOF
install -D -m 755 %{S:45} %buildroot%_initdir/%tomcatname
install -D -m 755 %{S:46} %buildroot%_sbindir/%tomcatname-sysv

%pre
getent group %tomcat_group >/dev/null || %_sbindir/groupadd -f -r %tomcat_group
if ! getent passwd %tomcat_user >/dev/null ; then
    %_sbindir/useradd -r -g %tomcat_group -d %apphomedir -s /sbin/nologin -c "Apache Tomcat" %tomcat_user
fi
exit 0

%post
%post_service %tomcatname

%preun
%__rm -rf %workdir/* %tempdir/*
%preun_service %tomcatname
%files
%defattr(0644,root,tomcat,0755)
%attr(0755,root,root) %doc LICENSE
%attr(0755,root,root) %doc NOTICE
%attr(0755,root,root) %doc RELEASE*
%attr(0755,root,root) %_bindir/%tomcatname-digest
%attr(0755,root,root) %_bindir/%tomcatname-tool-wrapper
%attr(0755,root,root) %_sbindir/%tomcatname
%attr(0644,root,root) %_unitdir/%tomcatname.service
%attr(0644,root,root) %_unitdir/%tomcatname@.service
%attr(0755,root,root) %dir %_libexecdir/%tomcatname
%attr(0755,root,root) %dir %_localstatedir/lib/tomcats
%attr(0644,root,root) %_libexecdir/%tomcatname/functions
%attr(0755,root,root) %_libexecdir/%tomcatname/preamble
%attr(0755,root,root) %_libexecdir/%tomcatname/server
%attr(0644,root,root) %config(noreplace) %_sysconfdir/sysconfig/%tomcatname
%attr(0644,root,root) %config(noreplace) %_sysconfdir/logrotate.d/%tomcatname.disabled
%attr(0755,root,tomcat) %dir %basedir
%attr(0755,root,tomcat) %dir %confdir

%defattr(0664,tomcat,root,0770)
%attr(0770,tomcat,root) %dir %logdir

%defattr(0644,root,tomcat,0770)
%attr(0770,root,tomcat) %dir %cachedir
%attr(0770,root,tomcat) %dir %tempdir
%attr(0770,root,tomcat) %dir %workdir

%defattr(0644,root,tomcat,0775)
%attr(0775,root,tomcat) %dir %appdir
%attr(0775,root,tomcat) %dir %confdir/Catalina
%attr(0775,root,tomcat) %dir %confdir/Catalina/localhost
%attr(0755,root,tomcat) %dir %confdir/conf.d
%confdir/conf.d/README
%confdir/conf.d/java-9-start-up-parameters.conf
%config(noreplace) %confdir/%tomcatname.conf
%config(noreplace) %confdir/*.policy
%config(noreplace) %confdir/*.properties
%config(noreplace) %confdir/context.xml
%config(noreplace) %confdir/server.xml
%attr(0640,root,tomcat) %config(noreplace) %confdir/tomcat-users.xml
%attr(0644,root,tomcat) %confdir/tomcat-users.xsd
%attr(0644,root,tomcat) %config(noreplace) %confdir/jaspic-providers.xml
%attr(0644,root,tomcat) %confdir/jaspic-providers.xsd
%config(noreplace) %confdir/web.xml
%attr(0755,root,root) %dir %apphomedir
%bindir/bootstrap.jar
%bindir/catalina-tasks.xml
%apphomedir/lib
%apphomedir/temp
%apphomedir/webapps
%apphomedir/work
%apphomedir/logs
%apphomedir/conf
%attr(0755,root,root) %_initdir/%tomcatname
%attr(0755,root,root) %_sbindir/%tomcatname-sysv
%attr(0755,root,root) %dir %bindir

%files admin-webapps
%defattr(0664,root,tomcat,0755)
%appdir/host-manager
%appdir/manager

%files docs-webapp
%appdir/docs

%files lib
%dir %libdir
%libdir/*.jar
%_javadir/*.jar
%bindir/tomcat-juli.jar
%exclude %libdir/%tomcatname-el-%elspec-api.jar
%exclude %_javadir/%tomcatname-servlet-%{servletspec}*.jar
%exclude %_javadir/%tomcatname-el-%elspec-api.jar
%exclude %_javadir/%tomcatname-jsp-%{jspspec}*.jar

%files jsp-%jspspec-api -f .mfiles-tomcat-jsp-api
%_altdir/jsp_tomcat-jsp-3.1-api
%_javadir/%tomcatname-jsp-%{jspspec}*.jar

%files servlet-%servletspec-api -f .mfiles-tomcat-servlet-api
%_altdir/servlet_tomcat-servlet-6.0-api
%doc LICENSE
%_javadir/%tomcatname-servlet-%{servletspec}*.jar

%files el-%elspec-api -f .mfiles-tomcat-el-api
%_altdir/elspec_tomcat-el-5.0-api
%doc LICENSE
%_javadir/%tomcatname-el-%elspec-api.jar
%libdir/%tomcatname-el-%elspec-api.jar

%files webapps
%defattr(0644,tomcat,tomcat,0755)
%appdir/ROOT

%changelog
* Tue Feb 28 2023 Ilfat Aminov <aminov@altlinux.org> 1:10.1.5-alt1_jvm11
- tomcat 10.1.5

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:9.0.59-alt1_3jpp11
- new version

* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 1:9.0.52-alt1_1jpp11
- new version

* Fri Aug 27 2021 Stanislav Levin <slev@altlinux.org> 1:9.0.50-alt2_2jpp11
- Packaged missing jars (closes: #40819).

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 1:9.0.50-alt1_2jpp11
- new version

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 1:9.0.45-alt1_1jpp11
- new verison (closes: #40087)

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:9.0.44-alt1_1jpp11
- new version

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 1:9.0.38-alt1_1jpp11
- new version
- merged slev@:
  46306c0 spec: Don't package files twice
  48af392 spec: Fix the License tag
  dbe4df1 ALT: Don't allocate static uid/gid

* Tue Sep 15 2020 Stanislav Levin <slev@altlinux.org> 1:9.0.37-alt1
- 9.0.13 -> 9.0.37.

* Mon Mar 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:9.0.13-alt1_2jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:9.0.7-alt1_1jpp8
- new version

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

