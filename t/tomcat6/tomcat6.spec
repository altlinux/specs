BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 6.0.32
%define name tomcat6
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

%global jspspec 2.1
%global major_version 6
%global minor_version 0
%global micro_version 32
%global packdname apache-tomcat-%{version}-src
%global servletspec 2.5
%global elspec 2.1
%global tcuid 91

# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir %{_var}/lib/%{name}
%global appdir %{basedir}/webapps
%global bindir %{_datadir}/%{name}/bin
%global confdir %{_sysconfdir}/%{name}
%global apphomedir %{_datadir}/%{name}
%global libdir %{_javadir}/%{name}
%global logdir %{_var}/log/%{name}
%global cachedir %{_var}/cache/%{name}
%global tempdir %{cachedir}/temp
%global workdir %{cachedir}/work
%global _initrddir %_initdir

Name:          tomcat6
Epoch:         0
Version:       %{major_version}.%{minor_version}.%{micro_version}
Release:       alt1_15jpp6
Summary:       Apache Servlet/JSP Engine, RI for Servlet %{servletspec}/JSP %{jspspec} API

Group:         Development/Java
License:       ASL 2.0
URL:           http://tomcat.apache.org/
Source0:       http://www.apache.org/dist/tomcat/tomcat-6/v%{version}/src/%{packdname}.tar.gz
Source1:       %{name}-%{major_version}.%{minor_version}.conf
Source2:       %{name}-%{major_version}.%{minor_version}.init
Source3:       %{name}-%{major_version}.%{minor_version}.sysconfig
Source4:       %{name}-%{major_version}.%{minor_version}.wrapper
Source5:       %{name}-%{major_version}.%{minor_version}.logrotate
Source6:       %{name}-%{major_version}.%{minor_version}-digest.script
Source7:       %{name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source8:       servlet-api-OSGi-MANIFEST.MF
Source9:       jsp-api-OSGi-MANIFEST.MF
Source10:      %{name}-%{major_version}.%{minor_version}-log4j.properties
Patch0:        %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
Patch1:        %{name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
# In 6.0.32 source
#Patch2:        %{name}-%{major_version}.%{minor_version}-rhbz-674601.patch
Patch3:        %{name}-6.0.32-CVE-2011-2204-rhbz-717016.patch
Patch4: tomcat6-6.0.32-CVE-2011-2526-rhbz-721087.patch

	
BuildArch:     noarch

BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: ecj
BuildRequires: findutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-daemon
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-pool
BuildRequires: jakarta-taglibs-standard
BuildRequires: jpackage-utils >= 0:1.7.0
BuildRequires: junit
BuildRequires: log4j
Requires:      jakarta-commons-daemon
Requires:      jakarta-commons-logging
Requires:      jakarta-commons-collections
Requires:      jakarta-commons-dbcp
Requires:      jakarta-commons-pool
Requires:      procps
Requires:      %{name}-lib = %{epoch}:%{version}-%{release}
Requires(pre):    shadow-utils
Requires(pre):    shadow-utils
Requires(post):   chkconfig
Requires(preun):  chkconfig

# added after log4j sub-package was removed
Provides:         %{name}-log4j = %{epoch}:%{version}-%{release}
Source44: import.info
BuildRequires: ant-trax

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License version 2.0. Tomcat is intended
to be a collaboration of the best-of-breed developers from around the world.

%package admin-webapps
Group: Development/Java
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: Development/Java
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package javadoc
Group: Development/Java
Summary: Javadoc generated documentation for Apache Tomcat
BuildArch: noarch

%description javadoc
Javadoc generated documentation for Apache Tomcat.

%package jsp-%{jspspec}-api
Group: Development/Java
Summary: Apache Tomcat JSP API implementation classes
Provides: jsp = %{jspspec}
Provides: jsp21
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires(post): chkconfig
Requires(postun): chkconfig

%description jsp-%{jspspec}-api
Apache Tomcat JSP API implementation classes.


%package lib
Group: Development/Java
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name}-jsp-%{jspspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-servlet-%{servletspec}-api = %{epoch}:%{version}-%{release}
Requires: %{name}-el-%{elspec}-api = %{epoch}:%{version}-%{release}
Requires: ecj
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-pool
Requires(preun): coreutils

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%{servletspec}-api
Group: Development/Java
Summary: Apache Tomcat Servlet API implementation classes
Provides: servlet = %{servletspec}
Provides: servlet6
Provides: servlet25
Requires(post): chkconfig
Requires(postun): chkconfig

%description servlet-%{servletspec}-api
Apache Tomcat Servlet API implementation classes.

%package el-%{elspec}-api
Group: Development/Java
Summary: Expression Language v1.0 API
Provides: el_1_0_api = %{epoch}:%{version}-%{release}
Provides: el_api = %{elspec}
Requires(post): chkconfig
Requires(postun): chkconfig
Obsoletes: tomcat6-el-1.0-api < %{epoch}:%{version}-%{release}
Conflicts: tomcat6-el-1.0-api < %{epoch}:%{version}-%{release}

%description el-%{elspec}-api
Expression Language 1.0.

%package webapps
Group: Development/Java
Summary: The ROOT and examples web applications for Apache Tomcat
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-taglibs-standard >= 0:1.1

%description webapps
The ROOT and examples web applications for Apache Tomcat.

%prep
%setup -q -n %{packdname}
# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
   -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -delete

%patch0 -p0
%patch1 -p0
# %patch2 -p0
%patch3 -p0
%patch4 -p0

%{__ln_s} $(build-classpath jakarta-taglibs-core) webapps/examples/WEB-INF/lib/jstl.jar
%{__ln_s} $(build-classpath jakarta-taglibs-standard) webapps/examples/WEB-INF/lib/standard.jar

%build
export OPT_JAR_LIST="xalan-j2-serializer ant/ant-trax"
   # we don't care about the tarballs and we're going to replace
   # tomcat-dbcp.jar with apache-commons-{collections,dbcp,pool}-tomcat5.jar
   # so just create a dummy file for later removal
   touch HACK
   # who needs a build.properties file anyway
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbase.path="." \
      -Dbuild.compiler="modern" \
      -Dcommons-collections.jar="$(build-classpath apache-commons-collections)" \
      -Dcommons-daemon.jar="$(build-classpath apache-commons-daemon)" \
      -Dcommons-daemon.native.src.tgz="HACK" \
      -Djasper-jdt.jar="$(build-classpath ecj)" \
      -Djdt.jar="$(build-classpath ecj)" \
      -Dtomcat-dbcp.jar="$(build-classpath apache-commons-dbcp)" \
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
   %{__rm} output/build/bin/tomcat-native.tar.gz
pushd output/dist/src/webapps/docs/appdev/sample/src
%{__mkdir_p} ../web/WEB-INF/classes
%{javac}  -target 1.5 -source 1.5 -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
%{jar} cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE8} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/servlet-api.jar META-INF/MANIFEST.MF
cp -p %{SOURCE9} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u output/build/lib/jsp-api.jar META-INF/MANIFEST.MF

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
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{confdir}/Catalina/localhost
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{libdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{logdir}
/bin/touch ${RPM_BUILD_ROOT}%{logdir}/catalina.out
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{apphomedir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{tempdir}
%{__install} -d -m 0775 ${RPM_BUILD_ROOT}%{workdir}

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    %{__cp} -a bin/*.{jar,xml} ${RPM_BUILD_ROOT}%{bindir}
    %{__cp} %{SOURCE10} conf/log4j.properties
    %{__cp} -a conf/*.{policy,properties,xml} ${RPM_BUILD_ROOT}%{confdir}
    %{__cp} -a lib/*.jar ${RPM_BUILD_ROOT}%{libdir}
    %{__cp} -a webapps/* ${RPM_BUILD_ROOT}%{appdir}
popd
# javadoc
%{__cp} -a output/dist/webapps/docs/api/* ${RPM_BUILD_ROOT}%{_javadocdir}/%{name}

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
   %{__mv} %{name}/jsp-api.jar %{name}-jsp-%{jspspec}-api.jar
   %{__ln_s} %{name}-jsp-%{jspspec}-api.jar %{name}-jsp-api.jar
   %{__mv} %{name}/servlet-api.jar %{name}-servlet-%{servletspec}-api.jar
   %{__ln_s} %{name}-servlet-%{servletspec}-api.jar %{name}-servlet-api.jar
   %{__mv} %{name}/el-api.jar %{name}-el-%{elspec}-api.jar
   %{__ln_s} %{name}-el-%{elspec}-api.jar %{name}-el-api.jar
popd

# apache-commons-dbcp
pushd output/build
    %{_bindir}/build-jar-repository lib apache-commons-collections \
                   apache-commons-dbcp apache-commons-pool ecj 2>&1

    # need to use -p here with b-j-r otherwise the examples webapp fails to
    # load with a java.io.IOException
    %{_bindir}/build-jar-repository -p webapps/examples/WEB-INF/lib \
    taglibs-core.jar taglibs-standard.jar 2>&1
popd

pushd ${RPM_BUILD_ROOT}%{libdir}
    # symlink JSP and servlet API jars
    %{__ln_s} ../%{name}-jsp-%{jspspec}-api.jar .
    %{__ln_s} ../%{name}-servlet-%{servletspec}-api.jar .
    %{__ln_s} ../%{name}-el-%{elspec}-api.jar .
    %{__ln_s} $(build-classpath apache-commons-collections) commons-collections.jar
    %{__ln_s} $(build-classpath apache-commons-dbcp) commons-dbcp.jar
	 %{__ln_s} $(build-classpath apache-commons-pool) commons-pool.jar
    %{__ln_s} $(build-classpath log4j) log4j.jar
    %{__ln_s} $(build-classpath ecj) jasper-jdt.jar

    # Link the juli jar into /usr/share/java/tomcat6
    %{__ln_s} %{bindir}/tomcat-juli.jar .
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


# Generate a depmap fragment javax.servlet:servlet-api pointing to
# tomcat6-servlet-2.5-api for backwards compatibility
%add_to_maven_depmap javax.servlet servlet-api %{servletspec} JPP %{name}-servlet-%{servletspec}-api
# also provide jetty depmap (originally in jetty package, but it's cleaner to have it here)
%add_to_maven_depmap org.mortbay.jetty servlet-api %{servletspec} JPP %{name}-servlet-%{servletspec}-api
mv %{buildroot}%{_mavendepmapfragdir}/%{name} %{buildroot}%{_mavendepmapfragdir}/%{name}-servlet-api

# Install the maven metadata
%{__install} -d -m 0755 ${RPM_BUILD_ROOT}%{_mavenpomdir}
pushd output/dist/src/res/maven
for pom in *.pom; do
    # fix-up version in all pom files
    sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $pom
done

# we won't install dbcp, juli-adapters and juli-extras pom files
for pom in annotations-api.pom catalina.pom jasper-el.pom jasper.pom \
           catalina-ha.pom el-api.pom; do
    %{__cp} -a $pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{name}-$pom
    base=`basename $pom .pom`
    %add_to_maven_depmap org.apache.tomcat $base %{version} JPP/%{name} $base
done

# servlet-api jsp-api and el-api are not in tomcat6 subdir, since they are widely re-used elsewhere
for pom in jsp-api.pom servlet-api.pom el-api.pom;do
    %{__cp} -a $pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP-%{name}-$pom
    base=`basename $pom .pom`
    %add_to_maven_depmap org.apache.tomcat $base %{version} JPP %{name}-$base
done

# two special pom where jar files have different names
%{__cp} -a tribes.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{name}-catalina-tribes.pom
%add_to_maven_depmap org.apache.tomcat tribes %{version} JPP/%{name} catalina-tribes

%{__cp} -a juli.pom ${RPM_BUILD_ROOT}%{_mavenpomdir}/JPP.%{name}-tomcat-juli.pom
%add_to_maven_depmap org.apache.tomcat juli %{version} JPP/%{name} tomcat-juli
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsp_tomcat6-jsp-2.1-api<<EOF
%{_javadir}/jsp.jar	%{_javadir}/%{name}-jsp-%{jspspec}-api.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/servlet_tomcat6-servlet-2.5-api<<EOF
%{_javadir}/servlet.jar	%{_javadir}/%{name}-servlet-%{servletspec}-api.jar	20500
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/elspec_tomcat6-el-2.1-api<<EOF
%{_javadir}/elspec.jar	%{_javadir}/%{name}-el-%{elspec}-api.jar	20250
EOF

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/el_api_%{name}-el-1.0-api<<EOF
%{_javadir}/el_api.jar	%{_javadir}/%{name}-el-%{elspec}-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/el_1_0_api_%{name}-el-1.0-api<<EOF
%{_javadir}/el_1_0_api.jar	%{_javadir}/%{name}-el-%{elspec}-api.jar	10000
EOF


%pre
# add the tomcat user and group
%{_sbindir}/groupadd  -r tomcat 2>/dev/null || :
%{_sbindir}/useradd -c "Apache Tomcat"  -g tomcat \
    -s /bin/nologin -r -d %{apphomedir} tomcat 2>/dev/null || :
# Save the conf, app, and lib dirs
%post
# install but don't activate
/sbin/chkconfig --add %{name}
/sbin/service %name condrestart

# 1# %%posttrans
# # if [ -d %{_tmppath}/%{name}-webapps.bak ]; then
# #   %{__cp} -rp %{_tmppath}/%{name}-webapps.bak/* %{appdir}
# #   %{__rm} -rf %{_tmppath}/%{name}-webapps.bak
# # fi
# # if [ -d %{_tmppath}/%{name}-libdir.bak ]; then
# #   %{__cp} -rp %{_tmppath}/%{name}-libdir.bak/* %{libdir}
# #   %{__rm} -rf %{_tmppath}/%{name}-libdir.bak
# # fi
# # if [ -d %{_tmppath}/%{name}-confdir.bak ]; then
# #   %{__cp} -rp %{_tmppath}/%{name}-confdir.bak/* %{confdir}
# #   %{__rm} -rf %{_tmppath}/%{name}-confdir.bak
# # fi
# # 
# # # execute only when update is run
# # if [ "$1" -eq "0" ]; then
# #    mkdir -p %{workdir}
# #    mkdir -p %{tempdir}
# #    chown tomcat:tomcat %{workdir}
# #    chown tomcat:tomcat %{tempdir}
# #    chmod 775 %{workdir}
# #    chmod 775 %{tempdir}
# # fi
# # 
%preun
# don't remove under any condition
##%{__rm} -rf %{workdir} %{tempdir}
if [ "$1" = "0" ]; then
    %{_initrddir}/%{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi


%files
%defattr(0644,root,tomcat,0755)
%doc {LICENSE,NOTICE,RELEASE*}
%attr(0755,root,root) %{_bindir}/%{name}-digest
%attr(0755,root,root) %{_bindir}/%{name}-tool-wrapper
%attr(0755,root,root) %{_sbindir}/d%{name}
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0755,root,root) %{_initrddir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0775,root,tomcat) %dir %{basedir}
%attr(0775,root,tomcat) %dir %{appdir}
%attr(0775,root,tomcat) %dir %{confdir}
%attr(0775,root,tomcat) %dir %{confdir}/Catalina
%attr(0775,root,tomcat) %dir %{confdir}/Catalina/localhost
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/%{name}.conf
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/*.policy
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/*.properties
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/context.xml
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/server.xml
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/log4j.properties
%attr(0664,tomcat,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%attr(0666,tomcat,tomcat) %config(noreplace) %{confdir}/web.xml
%attr(0775,root,tomcat) %dir %{cachedir}
%attr(0775,root,tomcat) %dir %{tempdir}
%attr(0775,root,tomcat) %dir %{workdir}
%attr(0775,root,tomcat) %dir %{logdir}
%attr(0664,tomcat,tomcat) %{logdir}/catalina.out
%dir %{apphomedir}
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{bindir}/tomcat-juli.jar
%{apphomedir}/lib
%{apphomedir}/temp
%{apphomedir}/webapps
%{apphomedir}/work
%{apphomedir}/logs
%{apphomedir}/conf
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*.pom
# Exclude the POMs that are in sub-packages
%exclude %{_mavenpomdir}/*api*
%dir %{bindir}
%exclude /etc/tomcat6/log4j.properties

%files admin-webapps
%defattr(0664,root,tomcat,0775)
%{appdir}/host-manager
%{appdir}/manager

%files docs-webapp
%{appdir}/docs

%files javadoc
%{_javadocdir}/%{name}

%files jsp-%{jspspec}-api
%_altdir/jsp_tomcat6-jsp-2.1-api
%{_javadir}/%{name}-jsp-%{jspspec}*.jar
%{_javadir}/%{name}-jsp-api.jar
%{_mavenpomdir}/JPP-%{name}-jsp-api.pom

%files lib
%{libdir}
%exclude %{libdir}/log4j*jar
%exclude %{libdir}/tomcat6-el-2.1-api*jar

%files servlet-%{servletspec}-api
%_altdir/servlet_tomcat6-servlet-2.5-api
%{_javadir}/%{name}-servlet-%{servletspec}*.jar
%{_javadir}/%{name}-servlet-api.jar
%{_mavendepmapfragdir}/%{name}-servlet-api
%{_mavenpomdir}/JPP-%{name}-servlet-api.pom

%files el-%{elspec}-api
%_altdir/elspec_tomcat6-el-2.1-api
%{_javadir}/%{name}-el-%{elspec}-api.jar
%{_javadir}/%{name}-el-api.jar
%{_javadir}/%{name}/%{name}-el-%{elspec}-api.jar
%{_mavenpomdir}/JPP-%{name}-el-api.pom
%_altdir/el_1_0_api_%{name}-el-1.0-api
%_altdir/el_api_%{name}-el-1.0-api

%files webapps
%defattr(0664,root,tomcat,0775)
%{appdir}/ROOT
%{appdir}/examples
%{appdir}/sample

%changelog
* Thu Sep 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.0.32-alt1_15jpp6
- update to new release by jppimport

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.0.30-alt1_2jpp6
- new version

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt4_16jpp6
- added obsoletes to tomcat6-el-1.0-api

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt3_16jpp6
- fixes

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt3_13jpp6
- fixed permissions (closes: 24633)

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt2_13jpp6
- fixed symlinks

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt2_12jpp6
- added el_1_0_api alternative

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt2_11jpp6
- CVE-2010-2227 fix (closes: 23779)

* Wed Oct 13 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt2_8jpp6
- permission fixes in tomcat6-log4j

* Mon Oct 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt1_8jpp6
- added OSGi manifest for eclipse

* Fri Mar 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.26-alt1_1jpp5
- new version, thanks to php_coder
- synced with jpackage
- use plain su (closes: 23073)

* Thu Jan 14 2010 Slava Semushin <php-coder@altlinux.ru> 0:6.0.18-alt6_8jpp5
- NMU
- Applied upstream patches to fix following vulnerabilities:
  + CVE-2009-0033: DoS when using Java AJP connector
    (Closes: #20313)
  + CVE-2009-0580: User enumeration vulnerability with FORM authentication
    (Closes: #20315)
  + CVE-2009-0781: XSS in calendar example

* Wed Feb 25 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.0.18-alt5_8jpp5
- fixed init script (#18986) thanks to php_coder@

* Mon Jan 26 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.0.18-alt4_8jpp5
- really fixed #18640

* Mon Jan 26 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.0.18-alt3_8jpp5
- really fixed #18640

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.0.18-alt2_8jpp5
- fixed build with new ecj

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:6.0.18-alt1_8jpp5
- fixed build with new ecj

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0.16-alt1_1jpp5.1
- NMU (by repocop): the following fixes applied:
 * windows-thumbnail-database-in-package for tomcat6-docs-webapp
 * windows-thumbnail-database-in-package for tomcat6-admin-webapps

* Tue Mar 11 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0.16-alt1_1jpp5.0
- new version

