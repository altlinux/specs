Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Note to packagers: When rebasing this to a later version, do not
# forget to ensure that sources 1 and 2 are up to date as well as
# the Requires list.

Name:           groovy
Version:        2.4.5
Release:        alt1_7jpp8
Summary:        Dynamic language for the Java Platform

# Some of the files are licensed under BSD and CPL terms, but the CPL has been superceded
# by the EPL. We include copies of both for completeness.
# groovyConsole uses CC-BY licensed icons
# (see: subprojects/groovy-console/target/tmp/groovydoc/groovy/ui/icons/credits.txt)
License:        ASL 2.0 and BSD and EPL and Public Domain and CC-BY
URL:            http://groovy-lang.org

Source0:        https://dl.bintray.com/groovy/maven/apache-groovy-src-%{version}-incubating.zip
Source1:        groovy-script.sh
Source3:        groovy.desktop
Source4:        cpl-v10.txt
Source5:        epl-v10.txt
Source6:        http://central.maven.org/maven2/org/codehaus/groovy/groovy-all/%{version}/groovy-all-%{version}.pom

Patch0:         0001-Port-to-Servlet-API-3.1.patch
Patch1:         0002-Gradle-local-mode.patch
Patch2:         0003-Bintray.patch
Patch3:         0004-Remove-android-support.patch
Patch4:         0005-Port-to-QDox-2.0.patch


BuildRequires:  gradle-local >= 2.1
BuildRequires:  javapackages-local
BuildRequires:  java-devel >= 1.8
BuildRequires:  ant
BuildRequires:  antlr-tool
BuildRequires:  ant-antlr
BuildRequires:  aqute-bnd
BuildRequires:  gpars
BuildRequires:  multiverse
BuildRequires:  apache-parent
BuildRequires:  testng
BuildRequires:  jline
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  checkstyle
BuildRequires:  jarjar
BuildRequires:  glassfish-jsp-api
BuildRequires:  glassfish-servlet-api
BuildRequires:  objectweb-asm3
BuildRequires:  bsf
BuildRequires:  apache-ivy
BuildRequires:  jansi
BuildRequires:  junit
BuildRequires:  xstream
BuildRequires:  desktop-file-utils
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(javax.servlet:jsp-api)

Requires:       %{name}-lib = %{version}
Requires:       glassfish-jsp-api
Requires:       glassfish-servlet-api
# FIXME: this dependency is missing in generated POM files from some reason...
Requires:       apache-commons-cli

# optional in pom.xml, but present in upstream binary tarball
Requires:       xstream
Requires:       xpp3-minimal
Requires:       gpars
Requires:       apache-ivy

# Joint compilation requires tools.jar from java-devel

BuildArch:      noarch
Source44: import.info

%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby and
Smalltalk.  It seamlessly integrates with all existing Java objects and
libraries and compiles straight to Java bytecode so you can use it anywhere
you can use Java.


%package lib
Group: Development/Java
Summary:        Groovy JAR artifact
Obsoletes:      %{name}-javadoc < 2

%description lib
This package contains Groovy JAR artifact.


%prep
%setup -q
cp %{SOURCE4} %{SOURCE5} .
# Remove bundled JARs and classes
find \( -name *.jar -o -name *.class \) -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%gradle_build -f -G distBin -- -x groovydoc -x javadoc

%install
%mvn_artifact %{SOURCE6} target/libs/groovy-all-%{version}-indy.jar
%mvn_install

unzip target/distributions/apache-groovy-binary-%{version}.zip
rm -rf groovy-%{version}/{*LICENSE.txt,NOTICE.txt,bin/*.bat,META-INF}
install -d -m 755 %{buildroot}%{_datadir}/
cp -a groovy-%{version} %{buildroot}%{_datadir}/%{name}

for mod in groovy groovy-ant groovy-bsf groovy-console groovy-docgenerator \
           groovy-groovydoc groovy-groovysh groovy-jmx groovy-json \
           groovy-jsr223 groovy-nio groovy-servlet groovy-sql groovy-swing \
           groovy-templates groovy-test groovy-testng groovy-xml; do
    ln -sf ../../java/%{name}/$mod.jar %{buildroot}%{_datadir}/%{name}/lib/$mod-%{version}.jar
    ln -sf ../../java/%{name}/$mod.jar %{buildroot}%{_datadir}/%{name}/indy/$mod-%{version}-indy.jar
done

ln -sf ../../java/%{name}/groovy-all.jar %{buildroot}%{_datadir}/%{name}/embeddable/groovy-all-%{version}.jar
ln -sf ../../java/%{name}/groovy-all.jar %{buildroot}%{_datadir}/%{name}/embeddable/groovy-all-%{version}-indy.jar

find %{buildroot}%{_datadir}/%{name}/lib/ ! -name "groovy*" -type f -print -delete
xmvn-subst %{buildroot}%{_datadir}/%{name}/

# $GROOVY_HOME/lib probably contains much more JARs (optional deps?) than is actually needed.
# These extra JARs can cause problems, e.g. rhbz#1184269.
# From that reason, let's symlink needed JARs manually for now.
ln -sf `build-classpath ant/ant` %{buildroot}%{_datadir}/%{name}/lib/ant.jar
ln -sf `build-classpath ant/ant-antlr` %{buildroot}%{_datadir}/%{name}/lib/ant-antlr.jar
ln -sf `build-classpath ant/ant-junit` %{buildroot}%{_datadir}/%{name}/lib/ant-junit.jar
ln -sf `build-classpath ant/ant-launcher` %{buildroot}%{_datadir}/%{name}/lib/ant-launcher.jar
ln -sf `build-classpath bsf` %{buildroot}%{_datadir}/%{name}/lib/bsf.jar
ln -sf `build-classpath commons-cli` %{buildroot}%{_datadir}/%{name}/lib/commons-cli.jar
ln -sf `build-classpath commons-logging` %{buildroot}%{_datadir}/%{name}/lib/commons-logging.jar
ln -sf `build-classpath gpars/gpars` %{buildroot}%{_datadir}/%{name}/lib/gpars.jar
ln -sf `build-classpath hamcrest/core` %{buildroot}%{_datadir}/%{name}/lib/hamcrest-core.jar
ln -sf `build-classpath apache-ivy/ivy` %{buildroot}%{_datadir}/%{name}/lib/ivy.jar
ln -sf `build-classpath jansi/jansi` %{buildroot}%{_datadir}/%{name}/lib/jansi.jar
ln -sf `build-classpath beust-jcommander` %{buildroot}%{_datadir}/%{name}/lib/jcommander.jar
ln -sf `build-classpath jline/jline` %{buildroot}%{_datadir}/%{name}/lib/jline.jar
ln -sf `build-classpath glassfish-jsp-api` %{buildroot}%{_datadir}/%{name}/lib/jsp-api.jar
# part of JDK7+ (?)
#ln -sf `build-classpath jsr166y` %{buildroot}%{_datadir}/%{name}/lib/jsr166y.jar
ln -sf `build-classpath junit` %{buildroot}%{_datadir}/%{name}/lib/junit.jar
ln -sf `build-classpath multiverse/multiverse-core` %{buildroot}%{_datadir}/%{name}/lib/multiverse-core.jar
# Android support, removed by patch
#ln -sf `build-classpath openbeans` %{buildroot}%{_datadir}/%{name}/lib/openbeans.jar
ln -sf `build-classpath qdox` %{buildroot}%{_datadir}/%{name}/lib/qdox.jar
ln -sf `build-classpath glassfish-servlet-api` %{buildroot}%{_datadir}/%{name}/lib/servlet-api.jar
ln -sf `build-classpath testng` %{buildroot}%{_datadir}/%{name}/lib/testng.jar
ln -sf `build-classpath xpp3-minimal` %{buildroot}%{_datadir}/%{name}/lib/xpp3-minimal.jar
ln -sf `build-classpath xstream/xstream` %{buildroot}%{_datadir}/%{name}/lib/xstream.jar
# upstream bundles extra166y in gpars
ln -sf `build-classpath extra166y` %{buildroot}%{_datadir}/%{name}/lib/extra166y.jar

# Startup scripts
install -d -m 755 %{buildroot}%{_bindir}/
for cmd in grape groovy groovyc groovyConsole groovydoc groovysh java2groovy; do
    class=$(awk '/^startGroovy/{print$2}' %{buildroot}%{_datadir}/%{name}/bin/$cmd)
    install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/$cmd
    sed -i "s/@CLASS@/$class/" %{buildroot}%{_bindir}/$cmd
    ln -sf %{_bindir}/$cmd %{buildroot}%{_datadir}/%{name}/bin/$cmd
done

# Configuration
install -d -m 755 %{buildroot}%{_sysconfdir}/
mv %{buildroot}%{_datadir}/%{name}/conf/groovy-starter.conf %{buildroot}%{_sysconfdir}/
ln -s %{_sysconfdir}/groovy-starter.conf %{buildroot}%{_datadir}/%{name}/conf/

# Desktop icon
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/applications
install -p -m644 subprojects/groovy-console/src/main/resources/groovy/ui/ConsoleIcon.png \
        %{buildroot}%{_datadir}/pixmaps/groovy.png
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE3}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
SentUpstream: No public bugtracker
-->
<application>
  <id type="desktop">groovy.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Interactive console for the Groovy programming language</summary>
  <description>
    <p>
      Groovy is a dynamic programming language that is commonly used as a
      scripting language for the Java platform. This application provides an
      interactive console for evaluating scripts in the Groovy language.
    </p>
  </description>
  <url type="homepage">http://groovy-lang.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/groovy/a.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
  -->
</application>
EOF

mkdir -p $RPM_BUILD_ROOT`dirname /etc/groovy-starter.conf`
touch $RPM_BUILD_ROOT/etc/groovy-starter.conf

%files
%{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%config(noreplace) %{_sysconfdir}/*
%config(noreplace,missingok) /etc/groovy-starter.conf

%files lib -f .mfiles
%doc LICENSE NOTICE README.adoc

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.5-alt1_7jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.4-alt1_1jpp8
- unbootstrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.9-alt1_5jpp7
- new release

* Sun Jul 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.9-alt1_2jpp7
- update

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.7-alt1_1jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt2_2jpp7
- applied repocop patches

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt1_2jpp7
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_2jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp5
- use maven1

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- selected java5 compiler explicitly

* Sun May 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- disabled rebuild-java-repository

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Nov 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

