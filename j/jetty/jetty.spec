BuildRequires: cpptasks
BuildRequires: eclipse-equinox-osgi felix-osgi-foundation xpp3-minimal
BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jetty
%define version 8.1.0
# Copyright (c) 2000-2007, JPackage Project
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

%global jettyname   jetty
%global jtuid       110
%global username    %{name}
%global confdir     %{_sysconfdir}/%{name}
%global logdir      %{_var}/log/%{name}
%global apphomedir     %{_datadir}/%{name}
%global jettycachedir %{_var}/cache/%{name}
%global tempdir     %{jettycachedir}/temp
%global rundir      %{_var}/run/%{name}
%global jettylibdir %{_var}/lib/%{name}
%global appdir      %{jettylibdir}/webapps

%global addver v20120127

Name:           jetty
Version:        8.1.0
Release:        alt3_4jpp7
Summary:        Java Webserver and Servlet Container

Group:          Development/Java
License:        ASL 2.0
URL:            http://jetty.mortbay.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.project.git/snapshot/jetty-%{version}.%{addver}.tar.bz2
Source1:        djetty.script
Source2:        jetty.init
Source3:        jetty.logrotate
Source4:        %{name}-depmap.xml
Source5:        %{name}.service
Patch0:         0001-Remove-javadoc-execution.patch
Patch1:         0002-Cleaup-distribution-generation.patch
Patch2:         0003-Disable-test-artifacts.patch
Patch3:         0004-Change-servelt-groupId-to-javax.servlet.patch
Patch4:         0005-Modify-dependencies.patch
Patch5:         0006-Remove-pmd-plugin.patch

BuildRequires:  tomcat-lib
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  tomcat-jsp-2.2-api
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  tomcat-el-2.2-api
BuildRequires:  maven
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-war-plugin
BuildRequires:  geronimo-jaspic-spec
BuildRequires:  geronimo-jta-1.1-api
BuildRequires:  geronimo-annotation-1.0-api
BuildRequires:  eclipse-rcp
BuildRequires:  eclipse-platform
BuildRequires:  jakarta-taglibs-standard
BuildRequires:  mongo-java-driver >= 2.6.5-4
BuildRequires:  objectweb-asm


# we want javamail not classpathx-javamail
BuildRequires:  %{_javadir}/javamail/mail.jar
BuildRequires:  jetty-parent
BuildRequires:  jetty-distribution-remote-resources
BuildRequires:  jetty-build-support
BuildRequires:  jetty-version-maven-plugin
BuildRequires:  jetty-toolchain
BuildRequires:  jetty-assembly-descriptors
BuildRequires:  jetty-test-policy
BuildRequires:  jetty-artifact-remote-resources


BuildArch:      noarch

Requires:       chkconfig
Requires:       jpackage-utils >= 0:1.6
Requires:       tomcat-servlet-3.0-api
Requires:       jsp22
Requires:       slf4j
Requires:       javamail
Requires:       xerces-j2 >= 0:2.7
Requires:       xml-commons-apis
Requires:       tomcat-lib
Requires:       tomcat-servlet-3.0-api
Requires:       tomcat-jsp-2.2-api
Requires:       tomcat-servlet-3.0-api
Requires:       tomcat-el-2.2-api
Requires:       geronimo-jta-1.1-api
Requires:       geronimo-annotation-1.0-api
Requires:       jakarta-taglibs-standard
Requires:       objectweb-asm
%{?FE_USERADD_REQ}


Provides:       group(%username) = %jtuid
Provides:       user(%username) = %jtuid

Obsoletes: %{name}-manual < %{version}-%{release}
Source44: import.info

%description
Jetty is a 100%% Java HTTP Server and Servlet Container.
This means that you do not need to configure and run a
separate web server (like Apache) in order to use java,
servlets and JSPs to generate dynamic content. Jetty is
a fully featured web server for static and dynamic content.
Unlike separate server/container solutions, this means
that your web server and web application run in the same
process, without interconnection overheads and complications.
Furthermore, as a pure java component, Jetty can be simply
included in your application for demonstration, distribution
or deployment. Jetty is available on all Java supported
platforms.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{jettyname}-%{version}.%{addver}
for f in $(find . -name "*.?ar"); do rm $f; done
find . -name "*.class" -exec rm {} \;

%patch0 -p1 -b .sav
%patch1 -p1 -b .sav
%patch2 -p1 -b .sav
%patch3 -p1 -b .sav
%patch4 -p1 -b .sav
%patch5 -p1 -b .sav

cp %{SOURCE1} djetty

# this needs jetty6 things, so just remove it
# shouldn't cause any trouble since it handled only in loadClass elsewhere
rm jetty-continuation/src/main/java/org/eclipse/jetty/continuation/Jetty6Continuation.java

iconv -f iso-8859-1 -t utf-8 LICENSE-CONTRIBUTOR/CDDLv1.0.txt > \
      LICENSE-CONTRIBUTOR/CDDLv1.0.txt.con
mv LICENSE-CONTRIBUTOR/CDDLv1.0.txt{.con,}

%build
#rm -rf ./*
#ln -sf ~/temp/jetty/jetty-8.1.0.%{addver}.copy/* .
#exit 0
# remove previous lines!
sed -i -e "s|/usr/share|%{_datadir}|g" djetty

mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5   -X \
    -Dmaven.local.depmap.file=%{SOURCE4} \
    -Dmaven.test.skip=true \
    install javadoc:aggregate

%install
# dirs
install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_initrddir}
install -dm 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -dm 755 %{buildroot}%{_javadir}/%{name}


install -dm 755 %{buildroot}%{_javadocdir}/%{name}
install -dm 755 %{buildroot}%{confdir}
install -dm 755 %{buildroot}%{apphomedir}
install -dm 755 %{buildroot}%{logdir}
install -dm 755 %{buildroot}%{rundir}
install -dm 755 %{buildroot}%{tempdir}
install -dm 755 %{buildroot}%{appdir}
install -dm 755 %{buildroot}%{_unitdir}

# systemd unit file
cp %{SOURCE5} %{buildroot}%{_unitdir}/

# main pkg
tar xvf jetty-distribution/target/%{name}-distribution-%{version}.%{addver}.tar.gz -C %{buildroot}%{apphomedir}
mv %{buildroot}%{apphomedir}/%{name}-distribution-%{version}.%{addver}/* %{buildroot}%{apphomedir}/
rmdir %{buildroot}%{apphomedir}/%{name}-distribution-%{version}.%{addver}

chmod +x %{buildroot}%{apphomedir}/bin/jetty-xinetd.sh
chmod +x djetty
mv djetty %{buildroot}%{_bindir}/djetty
ln -s %{apphomedir}/bin/jetty.sh %{buildroot}%{_bindir}/%{name}
install -pm 755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}
install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
echo '# Placeholder configuration file.  No default is provided.' > \
     %{buildroot}%{confdir}/jetty.conf


install -dm 755 %{buildroot}%{_mavenpomdir}
for module in jetty-ajp jetty-annotations jetty-client jetty-continuation \
           jetty-deploy jetty-http jetty-io jetty-jmx jetty-jndi \
           jetty-overlay-deployer jetty-plus jetty-policy \
           jetty-rewrite jetty-security jetty-server jetty-servlet \
           jetty-servlets jetty-util jetty-webapp jetty-websocket \
           jetty-xml; do
    mv %{buildroot}%{apphomedir}/lib/$module-%{version}.%{addver}.jar \
           %{buildroot}%{_javadir}/%{name}/$module.jar
    ln -s  %{_javadir}/%{name}/$module.jar \
           %{buildroot}%{apphomedir}/lib/$module-%{version}.%{addver}.jar
    install -pm 644 $module/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom
    %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar
done

# modules used during build and other jars not included in the
# distribution tarball
for module in jetty-http-spi jetty-jaspi jetty-nested jetty-nosql;do
    install $module/target/$module-%{version}.%{addver}.jar \
           %{buildroot}%{_javadir}/%{name}/$module.jar
    install -pm 644 $module/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom
    %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar
done

pushd jetty-osgi
    install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jetty-osgi.pom
    %add_maven_depmap JPP.%{name}-jetty-osgi.pom
    for submod in boot boot-jsp boot-warurl;do
        module=jetty-osgi-$submod
        install $module/target/$module-%{version}.%{addver}.jar \
           %{buildroot}%{_javadir}/%{name}/$module.jar
        install -pm 644 $module/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom
        %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar
    done

    #httpservice is a bit special (for no good reason)
    module=jetty-httpservice
    install jetty-osgi-httpservice/target/$module-%{version}.%{addver}.jar \
        %{buildroot}%{_javadir}/%{name}/$module.jar
    install -pm 644 jetty-osgi-httpservice/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-$module.pom
    %add_maven_depmap JPP.%{name}-$module.pom %{name}/$module.jar

popd

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-project.pom
%add_maven_depmap JPP.%{name}-project.pom

# recreat tarball structure in lib
ln -sf $(build-classpath tomcat-servlet-3.0-api) \
       %{buildroot}%{apphomedir}/lib/servlet-api-3.0.jar

build-jar-repository %{buildroot}%{apphomedir}/lib/annotations \
                     objectweb-asm/asm-all geronimo-annotation-1.0-api

build-jar-repository %{buildroot}%{apphomedir}/lib/jndi javamail/mail

build-jar-repository %{buildroot}%{apphomedir}/lib/jsp tomcat-el-2.2-api \
           taglibs-core taglibs-standard tomcat/jasper-el eclipse-ecj \
           tomcat/jasper tomcat/tomcat-api tomcat/tomcat-jsp-2.2-api \
           tomcat/tomcat-juli


ln -sf $(build-classpath geronimo-jta-1.1-api) \
       %{buildroot}%{apphomedir}/lib/jta/

mv %{buildroot}%{apphomedir}/lib/monitor/jetty-monitor-%{version}.%{addver}.jar \
   %{buildroot}%{_javadir}/%{name}/jetty-monitor.jar
ln -s %{_javadir}/%{name}/jetty-monitor.jar \
      %{buildroot}%{apphomedir}/lib/monitor/jetty-monitor-%{version}.%{addver}.jar
install -pm 644 jetty-monitor/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jetty-monitor.pom
%add_maven_depmap JPP.%{name}-jetty-monitor.pom %{name}/jetty-monitor.jar

mv %{buildroot}%{apphomedir}/start.jar \
   %{buildroot}%{_javadir}/%{name}/jetty-start.jar
ln -s %{_javadir}/%{name}/jetty-start.jar \
      %{buildroot}%{apphomedir}/start.jar
install -pm 644 jetty-start/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-jetty-start.pom
%add_maven_depmap JPP.%{name}-jetty-start.pom %{name}/jetty-start.jar


( cat << EO_RC
JAVA_HOME=/usr/lib/jvm/java
JAVA_OPTIONS=
JETTY_HOME=%{apphomedir}
JETTY_CONSOLE=%{logdir}/jetty-console.log
JETTY_PORT=8080
JETTY_RUN=%{_var}/run/%{name}
JETTY_PID=\$JETTY_RUN/jetty.pid
EO_RC
) > %{buildroot}%{apphomedir}/.jettyrc

mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d
( cat << EOF
D /var/run/%{name} 0755 %username %{username} -
EOF
) > %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf

rm -fr %{buildroot}%{apphomedir}/logs
ln -s %{logdir} %{buildroot}%{apphomedir}/logs

mv %{buildroot}%{apphomedir}/etc/* %{buildroot}/%{confdir}
rm -fr %{buildroot}%{apphomedir}/etc
ln -s %{confdir} %{buildroot}%{apphomedir}/etc

mv %{buildroot}%{apphomedir}/webapps/* %{buildroot}/%{appdir}
rm -fr %{buildroot}%{apphomedir}/webapps
ln -s %{appdir} %{buildroot}%{apphomedir}/webapps

rm %{buildroot}%{apphomedir}/*.txt  %{buildroot}%{apphomedir}/*.html

# following seem like config directories
for cdir in overlays;do
   mv %{buildroot}%{apphomedir}/$cdir %{buildroot}/%{confdir}/$cdir
   ln -s %{confdir}/$cdir %{buildroot}%{apphomedir}/$cdir
done

# this should be symlinked the other way around but rpm doesn't let us
# do that! BAD BAD rpm
# https://bugzilla.redhat.com/show_bug.cgi?id=447156
for cdir in contexts contexts-available resources;do
    ln -sf %{apphomedir}/$cdir %{buildroot}/%{confdir}/$cdir
done

# javadocs
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

mkdir -p %buildroot%{_sysconfdir}/default/
touch %buildroot%{_sysconfdir}/default/jetty8

%pre
groupadd -r %username || :
# Use /bin/sh so init script will start properly.
useradd  -r -s /bin/sh -d %apphomedir -M          \
                    -g %username %username || :

%post
[ -x /sbin/chkconfig ] && /sbin/chkconfig --add %{name}

%postun
#userdel  %username &>/dev/null || :
#groupdel %username &>/dev/null || :


%preun
if [ $1 = 0 ]; then
    [ -f /var/lock/subsys/%{name} ] && %{_initrddir}/%{name} stop
    [ -f %{_initrddir}/%{name} -a -x /sbin/chkconfig ] && /sbin/chkconfig --del %{name}

    %{_sbindir}/userdel %{name} >> /dev/null 2>&1 || :
fi

%files
%doc NOTICE.txt README.txt VERSION.txt LICENSE*
%config(noreplace) %{_sysconfdir}/tmpfiles.d/%{name}.conf
%config(noreplace) %attr(644, root, root) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace,missingok) %{_sysconfdir}/default/jetty8
%{_bindir}/*
%dir %{_javadir}/%{name}
%{_javadir}/%{name}
%{_mavenpomdir}/JPP*pom
%{_mavendepmapfragdir}/%{name}
%config(noreplace) %{confdir}
%dir %{jettylibdir}
%dir %{jettycachedir}
%{apphomedir}
%attr(755, jetty, jetty) %{logdir}
%attr(755, jetty, jetty) %{tempdir}
#%ghost %dir %attr(755, jetty, jetty) %{rundir}
%{appdir}
%{_initrddir}/%{name}
%{_unitdir}/%{name}.service

%files javadoc
%doc LICENSE*
%doc %{_javadocdir}/%{name}

%changelog
* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt3_4jpp7
- rebuild

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt2_4jpp7
- fixed %pre

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt1_4jpp7
- full version

