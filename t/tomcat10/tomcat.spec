%define _unpackaged_files_terminate_build 1

%define tomcat_user tomcat
%define tomcat_group tomcat

%global jspspec 3.1
%global servletspec 6.0
%global elspec 5.0

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%define _libexecdir %prefix/libexec
%global basedir %_sharedstatedir/tomcat
%global appdir %basedir/webapps
%global apphomedir %_datadir/tomcat
%global bindir %apphomedir/bin
%global confdir %_sysconfdir/tomcat
%global libdir %_javadir/%name
%global logdir %_logdir/tomcat
%global cachedir %_cachedir/tomcat
%global tempdir %cachedir/temp
%global workdir %cachedir/work

Name: tomcat10
Version: 10.1.56
Release: alt1
Epoch: 1
Summary: Apache Servlet/JSP Engine, RI for Servlet %servletspec/JSP %jspspec API
License: Apache-2.0
Group: System/Servers
Url: http://tomcat.apache.org/
Vcs: https://github.com/apache/tomcat
BuildArch: noarch
Source0: %name-%version.tar
Source1: tomcat-10.1.conf
Source2: tomcat-10.1.sysconfig
Source3: tomcat-10.1.wrapper
Source4: tomcat-10.1.logrotate
Source5: tomcat-10.1-digest.script
Source6: tomcat-10.1-tool-wrapper.script
Source7: tomcat-10.1.service
Source8: tomcat-functions
Source9: tomcat-preamble
Source10: tomcat-server
Source11: tomcat-named.service
Source12: module-start-up-parameters.conf
Patch0: tomcat-10.1-bootstrap-MANIFEST.MF.patch
Patch1: tomcat-10.1-tomcat-users-webapp.patch
Patch2: tomcat-build.patch
Patch3: tomcat-10.1-catalina-policy.patch
Patch4: rhbz-1857043.patch
Patch5: tomcat-10.1-JDTCompiler.patch
Patch6: tomcat-10.1-alt-build-without-docs-and-examples.patch
AutoReq: yes,noosgi
# fc script use systemctl calls -- gives dependency on systemctl :(
%add_findreq_skiplist %_sbindir/tomcat
Requires: javapackages-tools
Requires: %name-lib
Conflicts: tomcat
BuildRequires(pre): rpm-macros-java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-17-compat
BuildRequires: ant
BuildRequires: ecj >= 1:4.10
BuildRequires: findutils
BuildRequires: javapackages-local
BuildRequires: mvn(biz.aQute:bnd)
BuildRequires: mvn(biz.aQute:bndlib)
BuildRequires: mvn(org.apache.tomcat:jakartaee-migration)
BuildRequires: mvn(commons-daemon:commons-daemon)

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
Requires: %name
Conflicts: tomcat-admin-webapps

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package jsp-%jspspec-api
Group: Development/Other
Summary: Apache Tomcat JavaServer Pages v%jspspec API Implementation Classes
Requires: %name-servlet-%servletspec-api
Requires: %name-el-%elspec-api
Conflicts: tomcat-jsp-2.3-api

%description jsp-%jspspec-api
Apache Tomcat JSP API Implementation Classes.

%package lib
Group: Development/Other
Summary: Libraries needed to run the Tomcat Web container
Requires: %name-jsp-%jspspec-api
Requires: %name-servlet-%servletspec-api
Requires: %name-el-%elspec-api
Requires: ecj >= 1:4.10
Requires(preun): coreutils
Conflicts: tomcat-lib

%description lib
Libraries needed to run the Tomcat Web container.

%package servlet-%servletspec-api
Group: Development/Other
Summary: Apache Tomcat Java Servlet v%servletspec API Implementation Classes
Conflicts: tomcat-servlet-4.0-api

%description servlet-%servletspec-api
Apache Tomcat Servlet API Implementation Classes.

%package el-%elspec-api
Group: Development/Other
Summary: Apache Tomcat Expression Language v%elspec API Implementation Classes
Conflicts: tomcat-el-3.0-api

%description el-%elspec-api
Apache Tomcat EL API Implementation Classes.

%package webapps
Group: Networking/WWW
Summary: The ROOT web application for Apache Tomcat
Requires: %name
Conflicts: tomcat-webapps

%description webapps
The ROOT web application for Apache Tomcat.

%prep
%setup
%autopatch -p0
# remove pre-built binaries and windows files
find . -type f \( \
    -name "*.bat" \
    -o -name "*.class" \
    -o -name Thumbs.db \
    -o -name "*.gz" \
    -o -name "*.jar" \
    -o -name "*.war" \
    -o -name "*.zip" \
\) -delete

# Remove webservices naming resources as it's generally unused
rm -r java/org/apache/naming/factory/webservices

# Configure maven files
%mvn_package ":tomcat-el-api" tomcat-el-api
%mvn_alias "org.apache.tomcat:tomcat-el-api" "jakarta.servlet:jakarta.servlet-api"
%mvn_package ":tomcat-jsp-api" tomcat-jsp-api
%mvn_alias "org.apache.tomcat:tomcat-jsp-api" "jakarta.servlet:jakarta.servlet.jsp"
%mvn_package ":tomcat-servlet-api" tomcat-servlet-api

%build
# who needs a build.properties file anyway
%ant \
  -Dexecute.download=false \
  -Dant.build.javac.source=17 \
  -Dant.build.javac.target=17 \
  -Dbase.path="." \
  -Dbuild.compiler="modern" \
  -Dcommons-daemon.jar="$(build-classpath commons-daemon)" \
  -Djdt.jar="$(build-classpath ecj/ecj)" \
  -Dtomcat-native.home="." \
  -Dmigration-lib.jar="$(build-classpath org.apache.tomcat:jakartaee-migration)" \
  -Dbnd.jar="$(build-classpath biz.aQute:bnd)" \
  -Dexamples.sources.skip=true \
  echoproperties \
  deploy

# remove some jars that we'll replace with symlinks later
rm output/build/bin/commons-daemon.jar output/build/lib/ecj.jar
# Remove the example webapps per Apache Tomcat Security Considerations
# see https://tomcat.apache.org/tomcat-9.0-doc/security-howto.html
rm -r output/build/webapps/examples

%install
# build initial path structure
install -d -m 0755 %buildroot%_bindir
install -d -m 0755 %buildroot%_sbindir
install -d -m 0755 %buildroot%_unitdir
install -d -m 0755 %buildroot%_sysconfdir/logrotate.d
install -d -m 0755 %buildroot%_sysconfdir/sysconfig
install -d -m 0755 %buildroot%appdir
install -d -m 0755 %buildroot%bindir
install -d -m 0775 %buildroot%confdir
install -d -m 0775 %buildroot%confdir/Catalina/localhost
install -d -m 0775 %buildroot%confdir/conf.d
/bin/echo "Place your custom *.conf files here. Shell expansion is supported." > %buildroot%confdir/conf.d/README
install -d -m 0755 %buildroot%libdir
install -d -m 0775 %buildroot%logdir
install -d -m 0775 %buildroot%_localstatedir/lib/tomcats
install -d -m 0775 %buildroot%apphomedir
install -d -m 0775 %buildroot%tempdir
install -d -m 0775 %buildroot%workdir
install -d -m 0755 %buildroot%_libexecdir/tomcat

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    cp -a bin/*.{jar,xml} %buildroot%bindir
    cp -a conf/*.{policy,properties,xml,xsd} %buildroot%confdir
    cp -a lib/*.jar %buildroot%libdir
    cp -a webapps/* %buildroot%appdir
popd

sed -e "s|\@\@\@TCHOME\@\@\@|%apphomedir|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%tempdir|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%_libdir|g" %SOURCE1 \
    > %buildroot%confdir/tomcat.conf
sed -e "s|\@\@\@TCHOME\@\@\@|%apphomedir|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%tempdir|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%_libdir|g" %SOURCE2 \
    > %buildroot%_sysconfdir/sysconfig/tomcat
sed -e "s|\@\@\@TCLOG\@\@\@|%logdir|g" %SOURCE4 \
    > %buildroot%_sysconfdir/logrotate.d/tomcat.disabled
sed -e "s|\@\@\@TCHOME\@\@\@|%apphomedir|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%tempdir|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%_libdir|g" %SOURCE5 \
    > %buildroot%_bindir/tomcat-digest
sed -e "s|\@\@\@TCHOME\@\@\@|%apphomedir|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%tempdir|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%_libdir|g" %SOURCE6 \
    > %buildroot%_bindir/tomcat-tool-wrapper

install -m 0644 %SOURCE3 %buildroot%_sbindir/tomcat
install -m 0644 %SOURCE7 %buildroot%_unitdir/tomcat.service
install -m 0644 %SOURCE8 %buildroot%_libexecdir/tomcat/functions
install -m 0755 %SOURCE9 %buildroot%_libexecdir/tomcat/preamble
install -m 0755 %SOURCE10 %buildroot%_libexecdir/tomcat/server
install -m 0644 %SOURCE11 %buildroot%_unitdir/tomcat@.service
install -m 0644 %SOURCE12 %buildroot%confdir/conf.d/

# Substitute libnames in catalina-tasks.xml
sed -i \
   "s,el-api.jar,tomcat-el-%elspec-api.jar,;
    s,servlet-api.jar,tomcat-servlet-%servletspec-api.jar,;
    s,jsp-api.jar,tomcat-jsp-%jspspec-api.jar,;" \
    %buildroot%bindir/catalina-tasks.xml

# create jsp and servlet API symlinks
pushd %buildroot%_javadir
   mv %name/jsp-api.jar tomcat-jsp-%jspspec-api.jar
   ln -s tomcat-jsp-%jspspec-api.jar tomcat-jsp-api.jar
   mv %name/servlet-api.jar tomcat-servlet-%servletspec-api.jar
   ln -s tomcat-servlet-%servletspec-api.jar tomcat-servlet-api.jar
   mv %name/el-api.jar tomcat-el-%elspec-api.jar
   ln -s tomcat-el-%elspec-api.jar tomcat-el-api.jar
popd

pushd output/build
    %_bindir/build-jar-repository lib ecj 2>&1
popd

pushd %buildroot%libdir
    # symlink JSP and servlet API jars
    ln -s ../../java/tomcat-jsp-%jspspec-api.jar .
    ln -s ../../java/tomcat-servlet-%servletspec-api.jar .
    ln -s ../../java/tomcat-el-%elspec-api.jar .
    ln -s $(build-classpath ecj/ecj) jasper-jdt.jar

    cp ../../tomcat/bin/tomcat-juli.jar .
popd

# symlink to the FHS locations where we've installed things
pushd %buildroot%apphomedir
    ln -s %appdir webapps
    ln -s %confdir conf
    ln -s %libdir lib
    ln -s %logdir logs
    ln -s %tempdir temp
    ln -s %workdir work
popd

# Install the maven metadata for the spec impl artifacts as other projects use them
pushd res/maven
    for pom in *.pom ; do
        # fix-up version in all pom files
        sed -i 's/@MAVEN.DEPLOY.VERSION@/%version/g' $pom
    done
popd

# Configure and install maven artifacts
%mvn_artifact res/maven/tomcat-el-api.pom output/build/lib/el-api.jar
%mvn_artifact res/maven/tomcat-jsp-api.pom output/build/lib/jsp-api.jar
%mvn_artifact res/maven/tomcat-servlet-api.pom output/build/lib/servlet-api.jar

%mvn_file org.apache.tomcat:tomcat-annotations-api %name/annotations-api
%mvn_artifact res/maven/tomcat-annotations-api.pom %buildroot%libdir/annotations-api.jar
%mvn_artifact res/maven/tomcat-api.pom %buildroot%libdir/tomcat-api.jar
%mvn_file org.apache.tomcat:tomcat-catalina-ant %name/catalina-ant
%mvn_artifact res/maven/tomcat-catalina-ant.pom %buildroot%libdir/catalina-ant.jar
%mvn_file org.apache.tomcat:tomcat-catalina-ha %name/catalina-ha
%mvn_artifact res/maven/tomcat-catalina-ha.pom %buildroot%libdir/catalina-ha.jar
%mvn_file org.apache.tomcat:tomcat-catalina %name/catalina
%mvn_artifact res/maven/tomcat-catalina.pom %buildroot%libdir/catalina.jar
%mvn_artifact res/maven/tomcat-coyote.pom %buildroot%libdir/tomcat-coyote.jar
%mvn_artifact res/maven/tomcat-dbcp.pom %buildroot%libdir/tomcat-dbcp.jar
%mvn_artifact res/maven/tomcat-i18n-cs.pom %buildroot%libdir/tomcat-i18n-cs.jar
%mvn_artifact res/maven/tomcat-i18n-de.pom %buildroot%libdir/tomcat-i18n-de.jar
%mvn_artifact res/maven/tomcat-i18n-es.pom %buildroot%libdir/tomcat-i18n-es.jar
%mvn_artifact res/maven/tomcat-i18n-fr.pom %buildroot%libdir/tomcat-i18n-fr.jar
%mvn_artifact res/maven/tomcat-i18n-ja.pom %buildroot%libdir/tomcat-i18n-ja.jar
%mvn_artifact res/maven/tomcat-i18n-ko.pom %buildroot%libdir/tomcat-i18n-ko.jar
%mvn_artifact res/maven/tomcat-i18n-pt-BR.pom %buildroot%libdir/tomcat-i18n-pt-BR.jar
%mvn_artifact res/maven/tomcat-i18n-ru.pom %buildroot%libdir/tomcat-i18n-ru.jar
%mvn_artifact res/maven/tomcat-i18n-zh-CN.pom %buildroot%libdir/tomcat-i18n-zh-CN.jar
%mvn_file org.apache.tomcat:tomcat-jasper-el %name/jasper-el
%mvn_artifact res/maven/tomcat-jasper-el.pom %buildroot%libdir/jasper-el.jar
%mvn_file org.apache.tomcat:tomcat-jasper %name/jasper
%mvn_artifact res/maven/tomcat-jasper.pom %buildroot%libdir/jasper.jar
%mvn_file org.apache.tomcat:tomcat-jaspic-api %name/jaspic-api
%mvn_artifact res/maven/tomcat-jaspic-api.pom %buildroot%libdir/jaspic-api.jar
%mvn_artifact res/maven/tomcat-jdbc.pom %buildroot%libdir/tomcat-jdbc.jar
%mvn_artifact res/maven/tomcat-jni.pom %buildroot%libdir/tomcat-jni.jar
%mvn_artifact res/maven/tomcat-juli.pom %buildroot%libdir/tomcat-juli.jar
%mvn_file org.apache.tomcat:tomcat-ssi %name/catalina-ssi
%mvn_artifact res/maven/tomcat-ssi.pom %buildroot%libdir/catalina-ssi.jar
%mvn_file org.apache.tomcat:tomcat-storeconfig %name/catalina-storeconfig
%mvn_artifact res/maven/tomcat-storeconfig.pom %buildroot%libdir/catalina-storeconfig.jar
%mvn_file org.apache.tomcat:tomcat-tribes %name/catalina-tribes
%mvn_artifact res/maven/tomcat-tribes.pom %buildroot%libdir/catalina-tribes.jar
%mvn_artifact res/maven/tomcat-util-scan.pom %buildroot%libdir/tomcat-util-scan.jar
%mvn_artifact res/maven/tomcat-util.pom %buildroot%libdir/tomcat-util.jar
%mvn_file org.apache.tomcat:tomcat-websocket-api %name/websocket-api
%mvn_artifact res/maven/tomcat-websocket-api.pom %buildroot%libdir/websocket-api.jar
%mvn_artifact res/maven/tomcat-websocket.pom %buildroot%libdir/tomcat-websocket.jar
%mvn_artifact res/maven/tomcat-websocket-client-api.pom %buildroot%libdir/websocket-client-api.jar
%mvn_artifact res/maven/tomcat.pom

%mvn_install

%pre
getent group %tomcat_group >/dev/null || %_sbindir/groupadd -f -r %tomcat_group
if ! getent passwd %tomcat_user >/dev/null ; then
    %_sbindir/useradd -r -g %tomcat_group -d %apphomedir -s /sbin/nologin -c "Apache Tomcat" %tomcat_user
fi
exit 0

%post
%post_service tomcat

%preun
%__rm -rf %workdir/* %tempdir/*
%preun_service tomcat

%files
%doc README.*
%defattr(0644,root,%tomcat_group,0755)
%attr(0755,root,root) %_bindir/tomcat-digest
%attr(0755,root,root) %_bindir/tomcat-tool-wrapper
%attr(0755,root,root) %_sbindir/tomcat
%attr(0644,root,root) %_unitdir/tomcat.service
%attr(0644,root,root) %_unitdir/tomcat@.service
%attr(0755,root,root) %dir %_libexecdir/tomcat
%attr(0755,root,root) %dir %_localstatedir/lib/tomcats
%attr(0644,root,root) %_libexecdir/tomcat/functions
%attr(0755,root,root) %_libexecdir/tomcat/preamble
%attr(0755,root,root) %_libexecdir/tomcat/server
%attr(0644,root,root) %config(noreplace) %_sysconfdir/sysconfig/tomcat
%attr(0644,root,root) %config(noreplace) %_sysconfdir/logrotate.d/tomcat.disabled
%attr(0755,root,%tomcat_group) %dir %basedir
%attr(0755,root,%tomcat_group) %dir %confdir

%defattr(0664,%tomcat_user,root,0770)
%attr(0770,%tomcat_user,root) %dir %logdir

%defattr(0644,root,%tomcat_group,0770)
%attr(0770,root,%tomcat_group) %dir %cachedir
%attr(0770,root,%tomcat_group) %dir %tempdir
%attr(0770,root,%tomcat_group) %dir %workdir

%defattr(0644,root,%tomcat_group,0775)
%attr(0775,root,%tomcat_group) %dir %appdir
%attr(0775,root,%tomcat_group) %dir %confdir/Catalina
%attr(0775,root,%tomcat_group) %dir %confdir/Catalina/localhost
%attr(0755,root,%tomcat_group) %dir %confdir/conf.d
%confdir/conf.d/README
%confdir/conf.d/module-start-up-parameters.conf
%config(noreplace) %confdir/tomcat.conf
%config(noreplace) %confdir/*.policy
%config(noreplace) %confdir/*.properties
%config(noreplace) %confdir/context.xml
%config(noreplace) %confdir/server.xml
%attr(0640,root,%tomcat_group) %config(noreplace) %confdir/tomcat-users.xml
%attr(0644,root,%tomcat_group) %confdir/tomcat-users.xsd
%attr(0644,root,%tomcat_group) %config(noreplace) %confdir/jaspic-providers.xml
%attr(0644,root,%tomcat_group) %confdir/jaspic-providers.xsd
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
%attr(0755,root,root) %dir %bindir

%files admin-webapps
%defattr(0664,root,%tomcat_group,0755)
%appdir/host-manager
%appdir/manager

%files lib -f .mfiles
%dir %libdir
%libdir/*.jar
%_javadir/*.jar
%bindir/tomcat-juli.jar
%exclude %libdir/tomcat-el-%elspec-api.jar
%exclude %libdir/tomcat-jsp-api.jar
%exclude %libdir/tomcat-servlet-api.jar
%exclude %libdir/tomcat-el-api.jar
%exclude %_javadir/tomcat-servlet-%{servletspec}*.jar
%exclude %_javadir/tomcat-el-%elspec-api.jar
%exclude %_javadir/tomcat-jsp-%{jspspec}*.jar

%files jsp-%jspspec-api -f .mfiles-tomcat-jsp-api
%_javadir/tomcat-jsp-%{jspspec}*.jar

%files servlet-%servletspec-api -f .mfiles-tomcat-servlet-api
%_javadir/tomcat-servlet-%{servletspec}*.jar

%files el-%elspec-api -f .mfiles-tomcat-el-api
%_javadir/tomcat-el-%elspec-api.jar
%libdir/tomcat-el-%elspec-api.jar

%files webapps
%defattr(0644,%tomcat_user,%tomcat_group,0755)
%appdir/ROOT

%changelog
* Tue Jun 23 2026 Stanislav Levin <slev@altlinux.org> 1:10.1.56-alt1
- 10.1.55 -> 10.1.56.

* Tue May 12 2026 Stanislav Levin <slev@altlinux.org> 1:10.1.55-alt1_jvm17
- 10.1.54 -> 10.1.55 (fixes: CVE-2026-41284, CVE-2026-41293, CVE-2026-42498,
  CVE-2026-43512, CVE-2026-43513, CVE-2026-43514, CVE-2026-43515).

* Fri Apr 03 2026 Stanislav Levin <slev@altlinux.org> 1:10.1.54-alt1_jvm17
- 10.1.53 -> 10.1.54.

* Thu Mar 26 2026 Stanislav Levin <slev@altlinux.org> 1:10.1.53-alt2_jvm17
- Replaced or removed links to local docs (closes: #58401).

* Wed Mar 25 2026 Stanislav Levin <slev@altlinux.org> 1:10.1.53-alt1_jvm17
- 10.1.52 -> 10.1.53.

* Thu Feb 12 2026 Stanislav Levin <slev@altlinux.org> 1:10.1.52-alt1_jvm17
- 10.1.47 -> 10.1.52.
- Made it compatible with dogtag-pki.

* Mon Jan 19 2026 Ilfat Aminov <aminov@altlinux.org> 1:10.1.47-alt1_jvm17
- 10.1.47

* Thu Dec 11 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1:10.1.20-alt4_jvm17
- pre-compiled JAR files were excluded from the source tree:
  + aqute-bnd v6.3.1
  + jakartaee-migration v1.0.9
  + geronimo-spec-jaxrpc v1.1-rc4

* Wed Mar 12 2025 Stanislav Levin <slev@altlinux.org> 1:10.1.20-alt3_jvm17
- actualized conflicts with tomcat 9 (closes: #53331, #53333).

* Fri Mar 29 2024 Ilfat Aminov <aminov@altlinux.org> 1:10.1.20-alt2_jvm17
- fix tomcat-10.1-JDTCompiler.patch for java 17 build

* Thu Mar 28 2024 Ilfat Aminov <aminov@altlinux.org> 1:10.1.20-alt1_jvm17
- 10.1.20

* Fri Sep 01 2023 Ilfat Aminov <aminov@altlinux.org> 1:10.1.5-alt2_jvm11
- change Provides to differ from tomcat 9

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

