BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 2.1.3
%define name jbossweb2
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with bootstrap
%bcond_with bootstrap
#def_with jci
%bcond_with jci


%define jspspec 2.1
%define major_version 2
%define minor_version 1
%define micro_version 3
%define packdname .
%define servletspec 2.5

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%define appdir %{_var}/lib/%{name}/webapps
%define bindir %{_datadir}/%{name}/bin
%define confdir %{_sysconfdir}/%{name}
%define apphomedir %{_datadir}/%{name}
%define libdir %{_javadir}/%{name}
%define logdir %{_var}/log/%{name}
%define tempdir %{_var}/cache/%{name}/temp
%define workdir %{_var}/cache/%{name}/work
%define _initrddir %_initdir

Name:           jbossweb2
Version:        %{major_version}.%{minor_version}.%{micro_version}
Release:	alt1_2jpp6
Epoch:          0
Summary:        JBoss Web Server based on Apache Tomcat
Group:          Development/Java
License:        LGPLv3
URL:            http://labs.jboss.com/jbossweb/
# svn export -q http://anonsvn.jboss.org/repos/jbossweb/tags/JBOSSWEB_2_1_3_GA/ jbossweb2-2.1.3 && tar cjf jbossweb2-2.1.3.tar.bz2 jbossweb2-2.1.3
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-%{major_version}.%{minor_version}.conf
Source2:        %{name}-%{major_version}.%{minor_version}.init
Source3:        %{name}-%{major_version}.%{minor_version}.sysconfig
Source4:        %{name}-%{major_version}.%{minor_version}.wrapper
Source5:        %{name}-%{major_version}.%{minor_version}.logrotate
Source6:        %{name}-%{major_version}.%{minor_version}-digest.script
Source7:        %{name}-%{major_version}.%{minor_version}-tool-wrapper.script
# Remove Class-Path and add a newline to the bootstrap.jar manifest
Patch0:         %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
# Add some (commented) user roles for the webapps
Patch1:         %{name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
Requires: ecj >= 0:3.1.2
Requires: jpackage-utils >= 0:1.6.0
Requires(pre): shadow-utils
Requires: procps
Requires: %{name}-lib = %{epoch}:%{version}-%{release}
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(post): /lib/lsb/init-functions
Requires(preun): /lib/lsb/init-functions
BuildRequires: ant
BuildRequires: ant-trax
BuildRequires: axis
BuildRequires: jakarta-commons-daemon
%if %with jci
BuildRequires: jakarta-commons-jci
%endif
BuildRequires: javamail_1_3_1_api
BuildRequires: ecj >= 0:3.1.2
BuildRequires: jpackage-utils >= 0:1.6.0
BuildRequires: wsdl4j
BuildArch:      noarch
Source44: import.info

%description
JBoss Web Server is an enterprise ready web server designed for medium
and large applications, based on the Apache Tomcat. It is meant to be
used as a replacement for the standard Web servers on all major
platforms. JBoss Web Server provides organizations with a single
deployment platform for Java Server Pages (JSP) and Java Servlet
technologies, Microsoft .NET, PHP, and CGI. It uses a genuine high
performance hybrid technology that incorporates the best of the most
recent OS technologies for processing high volume data, while keeping
all the reference Java specifications. It supports both in and out of
the process execution of CGI and PHP scripts, as well as .NET
applications. The hybrid technology model offers the best from
threading and event processing models, and that makes the JBoss Web
Server one of the fastest and most scalable web servers in the market.

%package admin-webapps
Group: Development/Java
Summary: The host-manager and manager web applications for JBoss Web Server
Requires: %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for JBoss Web Server.

%package docs-webapp
Group: Development/Java
Summary: The docs web application for JBoss Web Server
Requires: %{name} = %{epoch}:%{version}-%{release}

%description docs-webapp
The docs web application for JBoss Web Server.

%package javadoc
Group: Development/Java
Summary: Javadoc generated documentation for JBoss Web Server
BuildArch: noarch

%description javadoc
Javadoc generated documentation for JBoss Web Server.

%package jsp-%{jspspec}-api
Group: Development/Java
Summary: JBoss Web Server JSP API implementation classes
Provides: jsp = %{jspspec}
Provides: jsp21
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): alternatives >= 0:0.4
Requires(preun): alternatives >= 0:0.4

%description jsp-%{jspspec}-api
JBoss Web Server JSP API implementation classes.

%package lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): ecj
Requires(post): %{_javadir}/ecj.jar
Requires(post): jakarta-commons-collections-tomcat5
Requires(post): jakarta-commons-dbcp-tomcat5
Requires(post): jakarta-commons-pool-tomcat5
Requires(post): jpackage-utils
Requires(preun): coreutils

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Group: Development/Java
Summary: JBoss Web Server Servlet API implementation classes
Provides: servlet = %{servletspec}
Provides: servlet6
Provides: servlet25
Requires(post): alternatives >= 0:0.4
Requires(preun): alternatives >= 0:0.4

%description servlet-%{servletspec}-api
JBoss Web Server Servlet API implementation classes.

%package webapps
Group: Development/Java
Summary: The ROOT and examples web applications for JBoss Web Server
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires(post): jakarta-taglibs-standard >= 0:1.1
%if 0
Requires(post): jpackage-utils
%endif

%description webapps
The ROOT and examples web applications for JBoss Web Server.

%prep
%setup -q
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
          -name "*.jar" -o -name "*.war" -o -name "*.zip" \) | xargs -t %{__rm}
pushd %{packdname}
%patch0 -p0
%patch1 -p0
popd

pushd lib
%if %with jci
build-jar-repository -s -p . commons-jci-core
%endif
build-jar-repository -s -p . axis/jaxrpc
build-jar-repository -s -p . ecj
build-jar-repository -s -p . javamail_1_3_1_api
build-jar-repository -s -p . wsdl4j
popd

%if %without jci
rm java/org/apache/jasper/compiler/JCICompiler.java
%endif

%build
export CLASSPATH=
export OPT_JAR_LIST="jaxp_transform_impl ant/ant-trax xalan-j2-serializer"

pushd %{packdname}
    # we don't care about the tarballs and we're going to replace
    # tomcat-dbcp.jar with jakarta-commons-{collections,dbcp,pool}-tomcat5.jar
    # so just create a dummy file for later removal
    touch HACK
    # who needs a build.properties file anyway
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbase.path="." \
        -Dbuild.compiler="modern" \
        -Dcommons-collections.jar="$(build-classpath commons-collections)" \
        -Dcommons-daemon.jar="$(build-classpath commons-daemon)" \
        -Dcommons-daemon.jsvc.tar.gz="HACK" \
        -Djasper-jdt.jar="$(build-classpath ecj)" \
        -Djdt.jar="$(build-classpath ecj)" \
        -Dtomcat-dbcp.jar="HACK" \
        -Dtomcat-native.tar.gz="HACK" \
        -Dversion="%{version}" \
        -Dversion.build="%{micro_version}"
    # javadoc generation
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f dist.xml dist-prepare
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f dist.xml dist-source
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f dist.xml dist-javadoc
    # remove some jars that we'll replace with symlinks later
    %{__rm} output/build/bin/commons-daemon.jar \
            output/build/lib/ecj.jar
    # remove the cruft we created
    %{__rm} output/build/bin/HACK \
%if 0
            output/build/bin/tomcat-native.tar.gz \
%endif
            output/build/lib/HACK
popd
pushd %{packdname}/output/dist/src/webapps/docs/appdev/sample/src
%{__mkdir_p} ../web/WEB-INF/classes
%{javac}  -target 1.5 -source 1.5 -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
%{jar} cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

%install
# build initial path structure
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sbindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_initrddir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{appdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{bindir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{confdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{logdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{apphomedir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{tempdir}
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{workdir}
# move things into place
pushd %{packdname}/output/build
    %{__cp} -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} -a conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd
# javadoc
pushd %{packdname}/output/dist/webapps
    %{__cp} -a docs/api/* ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}
popd
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
         -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
         -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > ${RPM_BUILD_ROOT}%{confdir}/%{name}.conf
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
         -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
         -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/%{name}
%{__install} -m 0644 %{SOURCE2} \
    ${RPM_BUILD_ROOT}%{_initrddir}/%{name}
%{__install} -m 0644 %{SOURCE4} \
    ${RPM_BUILD_ROOT}%{_sbindir}/%{name}
%{__ln_s} %{name} ${RPM_BUILD_ROOT}%{_sbindir}/d%{name}
%{__sed} -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
         -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
         -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{name}-digest
%{__sed} -e "s|\@\@\@TCHOME\@\@\@|%{apphomedir}|g" \
         -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
         -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > ${RPM_BUILD_ROOT}%{_bindir}/%{name}-tool-wrapper
# create jsp and servlet API symlinks
pushd ${RPM_BUILD_ROOT}%{_javadir}
    %{__mv} %{name}/jsp-api.jar %{name}-jsp-%{jspspec}-api-%{version}.jar
    %{__mv} %{name}/servlet-api.jar \
        %{name}-servlet-%{servletspec}-api-%{version}.jar
    %{__ln_s} %{name}-jsp-%{jspspec}-api-%{version}.jar \
        %{name}-jsp-%{jspspec}-api.jar
    %{__ln_s} %{name}-servlet-%{servletspec}-api-%{version}.jar \
        %{name}-servlet-%{servletspec}-api.jar
popd
pushd ${RPM_BUILD_ROOT}%{libdir}
    # fix up jars to include version number
    for i in *.jar; do
        j="$(echo $i | %{__sed} -e 's,\.jar$,,')"
        %{__mv} ${j}.jar ${j}-%{version}.jar
        %{__ln_s} ${j}-%{version}.jar ${j}.jar
    done
    # symlink JSP and servlet API jars
    %{__ln_s} ../%{name}-jsp-%{jspspec}-api-%{version}.jar .
    %{__ln_s} ../%{name}-servlet-%{servletspec}-api-%{version}.jar .
popd
pushd ${RPM_BUILD_ROOT}%{bindir}
    # fix up jars to include version number
    for i in *.jar; do
        j="$(echo $i | %{__sed} -e 's,\.jar$,,')"
        %{__mv} ${j}.jar ${j}-%{version}.jar
        %{__ln_s} ${j}-%{version}.jar ${j}.jar
    done
popd
# symlink to the FHS locations where we've installed things
pushd ${RPM_BUILD_ROOT}%{apphomedir}
    %{__ln_s} %{appdir} webapps
    %{__ln_s} %{confdir} conf
    %{__ln_s} %{libdir} lib
    %{__ln_s} %{logdir} logs
    %{__ln_s} %{tempdir} temp
    %{__ln_s} %{workdir} work
popd

# install sample webapp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{appdir}/sample
pushd ${RPM_BUILD_ROOT}%{appdir}/sample
%{jar} xf ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war
popd
%{__rm} ${RPM_BUILD_ROOT}%{appdir}/docs/appdev/sample/sample.war
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_jbossweb2-jsp-2.1-api<<EOF
%{_javadir}/jsp.jar	%{_javadir}/%{name}-jsp-%{jspspec}-api.jar	20099
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_jbossweb2-servlet-2.5-api<<EOF
%{_javadir}/servlet.jar	%{_javadir}/%{name}-servlet-%{servletspec}-api.jar	20499
EOF

%pre
%{_bindir}/getent group jbossweb >/dev/null || %{_sbindir}/groupadd -r jbossweb
%{_bindir}/getent passwd jbossweb >/dev/null || %{_sbindir}/useradd -r -g jbossweb -d %{apphomedir} -s /bin/sh -c "JBoss Web Server" jbossweb
exit 0

%post
# install but don't activate
/sbin/chkconfig --add %{name}

%post lib
%{_bindir}/build-jar-repository %{libdir} commons-collections-tomcat5 \
    commons-dbcp-tomcat5 commons-pool-tomcat5 ecj 2>&1
%if 0

%post webapps
%{_bindir}/build-jar-repository %{appdir}/examples/WEB-INF/lib \
    taglibs-core.jar taglibs-standard.jar 2>&1
%endif

%preun
# clean tempdir and workdir on removal or upgrade
%{__rm} -rf %{workdir}/* %{tempdir}/*
if [ "$1" = "0" ]; then
    %{_initrddir}/%{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%preun lib
if [ "$1" = "0" ]; then
    %{__rm} -f %{libdir}/\[commons-collections-tomcat5\].jar \
        %{libdir}/\[commons-dbcp-tomcat5\].jar \
        %{libdir}/\[commons-pool-tomcat5\].jar \
        %{libdir}/\[ecj\].jar >/dev/null 2>&1
fi

%files
%doc %{packdname}/{LICENSE,NOTICE,RELEASE*}
%doc %{packdname}/{KEYS,PATCHES.txt,BUILDING.txt,RUNNING.txt}
%attr(0755,root,root) %{_bindir}/%{name}-digest
%attr(0755,root,root) %{_bindir}/%{name}-tool-wrapper
%attr(0755,root,root) %{_sbindir}/d%{name}
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0775,root,jbossweb) %dir %{logdir}
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0775,root,jbossweb) %dir %{appdir}
%dir %{confdir}
%dir %{confdir}/Catalina
%attr(0775,root,jbossweb) %dir %{confdir}/Catalina/localhost
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/*.policy
%config(noreplace) %{confdir}/*.properties
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/server.xml
%attr(0660,root,jbossweb) %config(noreplace) %{confdir}/tomcat-users.xml
%config(noreplace) %{confdir}/web.xml
%attr(0775,root,jbossweb) %dir %{tempdir}
%attr(0775,root,jbossweb) %dir %{workdir}
%{apphomedir}

%files admin-webapps
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%{appdir}/docs

%files javadoc
%{_javadocdir}/%{name}

%files jsp-%{jspspec}-api
%_altdir/jsp_jbossweb2-jsp-2.1-api
%{_javadir}/%{name}-jsp*.jar

%files lib
%{libdir}

%files servlet-%{servletspec}-api
%_altdir/servlet_jbossweb2-servlet-2.5-api
%{_javadir}/%{name}-servlet*.jar

%files webapps
%{appdir}/ROOT
%if 0
%{appdir}/examples
%endif
%{appdir}/sample

%changelog
* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp6
- new jpp release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_7jpp6
- new version

