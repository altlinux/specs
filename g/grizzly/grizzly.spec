Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: perl(IO/Socket.pm)
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name grizzly
%define version 2.3.24
%global namedreltag %{nil}
%global _version %(echo %version | tr . _)
%global namedversion %{_version}%{?namedreltag}

# Conditionals to help breaking grizzly <-> jersey dependency cycle
%if 0%{?fedora}
#def_with jersey
%bcond_with jersey
%endif

Name:          grizzly
Version:       2.3.24
Release:       alt1_1jpp8
Summary:       Java NIO Server Framework
# see Grizzly_THIRDPARTYLICENSEREADME.txt
License:       (CDDL or GPLv2 with exceptions) and BSD and ASL 2.0 and Public Domain
URL:           http://grizzly.java.net/
# git clone git://java.net/grizzly~git
# (cd grizzly~git/ && git archive --format=tar --prefix=grizzly-2.3.6/ 2_3_6 | xz > ../grizzly-2.3.6.tar.xz)
Source0:       https://github.com/GrizzlyNIO/grizzly-mirror/archive/%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.sun.istack:istack-commons-maven-plugin)
%if %{with jersey}
BuildRequires: mvn(com.sun.jersey:jersey-client)
BuildRequires: mvn(com.sun.jersey:jersey-server)
BuildRequires: mvn(com.sun.jersey:jersey-servlet)
%endif
BuildRequires: mvn(com.sun.xml.ws:rt)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.glassfish.gmbal:gmbal)
BuildRequires: mvn(org.glassfish.gmbal:gmbal-api-only)
BuildRequires: mvn(org.glassfish.grizzly:grizzly-npn-api)
BuildRequires: mvn(org.glassfish.grizzly:grizzly-npn-bootstrap)
BuildRequires: mvn(org.glassfish.hk2:hk2-inhabitant-generator)
BuildRequires: mvn(org.glassfish.hk2:osgiversion-maven-plugin)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)

BuildArch:     noarch
Source44: import.info

%description
Writing scalable server applications in the Java programming
language has always been difficult. Before the advent of the
Java New I/O API (NIO), thread management issues made it
impossible for a server to scale to thousands of users. The
Grizzly framework has been designed to help developers to take
advantage of the Java NIO API. Originally developed under the
GlassFish umbrella, the framework is now available as a
standalone project. Grizzly goals is to help developers to
build scalable and robust servers using NIO.

%package samples
Group: Development/Java
Summary:       Grizzly samples

%description samples
This package contains samples for %{name}.

%package javadoc
Group: Development/Documentation
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-mirror-%{namedversion}
find . -name '*.class' -delete
find . -name '*.jar' -print -delete
find . -name '*.js' -print -delete

# unavailable deps
# org.jvnet.maven-antrun-extended-plugin maven-antrun-extended-plugin
%pom_disable_module bundles extras
%pom_disable_module bundles modules

# org.ops4j maven-pax-plugin  1.5
%pom_disable_module grizzly-httpservice extras
# Unsupport war extension
%pom_disable_module comet samples
%pom_disable_module websockets/chat samples
%pom_disable_module websockets/chat-ssl samples

%pom_remove_dep :maven-bundle-plugin
%pom_remove_dep :maven-plugin-tools-api
%pom_remove_dep org.glassfish.hk2:config-types
%pom_remove_dep org.glassfish.hk2:core
%pom_remove_dep org.glassfish.hk2:hk2-config
%pom_remove_dep org.glassfish.hk2:hk2-locator
%pom_remove_dep org.glassfish.hk2:osgi-adapter

# wagon-webdav & wagon-ssh-external
%pom_xpath_remove "pom:build/pom:extensions"

# org.glassfish.grizzly:grizzly-npn-bootstrap:1.0
%pom_xpath_inject "pom:dependency[pom:artifactId = 'grizzly-spdy']" '<version>${project.version}</version>' samples/spdy-samples

#%% pom_remove_dep org.glassfish.grizzly:documentation bom
%pom_remove_dep org.glassfish.grizzly:grizzly-comet-server bom
%pom_remove_dep org.glassfish.grizzly:grizzly-compression bom
%pom_remove_dep org.glassfish.grizzly:grizzly-core bom
%pom_remove_dep org.glassfish.grizzly:grizzly-http-all bom
%pom_remove_dep org.glassfish.grizzly:grizzly-http-server-core bom
%pom_remove_dep org.glassfish.grizzly:grizzly-http-server-jaxws bom
%pom_remove_dep org.glassfish.grizzly:grizzly-http-servlet-server bom
%pom_remove_dep org.glassfish.grizzly:grizzly-websockets-server bom
%pom_remove_dep org.glassfish.grizzly.osgi:grizzly-httpservice bom
%pom_remove_dep org.glassfish.grizzly.osgi:grizzly-httpservice-bundle bom
%pom_remove_plugin :maven-antrun-extended-plugin bom
%pom_remove_plugin :glassfish-copyright-maven-plugin bom

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :nexus-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

%if %{without jersey}
%pom_remove_dep com.sun.jersey: modules/http-servlet
rm -rf modules/http-servlet/src/test/java/filter/*
%else
%pom_add_dep com.sun.jersey:jersey-servlet:'${jersey-version}':test modules/http-servlet
%endif

cp -p modules/grizzly/src/main/resources/Grizzly_THIRDPARTYLICENSEREADME.txt .
sed -i 's/\r//' LICENSE.txt Grizzly_THIRDPARTYLICENSEREADME.txt

%pom_xpath_set -r "pom:plugin[pom:groupId='com.sun.istack']/pom:artifactId" istack-commons-maven-plugin

# Force servlet 3.1 apis
%pom_change_dep -r javax.servlet:servlet-api javax.servlet:javax.servlet-api:'${servlet-version}'

%pom_xpath_set "pom:dependency[pom:groupId ='com.sun.xml.ws']/pom:artifactId" rt extras/http-server-jaxws
%pom_xpath_set "pom:dependency[pom:groupId ='com.sun.xml.ws']/pom:artifactId" rt samples/http-jaxws-samples

%mvn_package org.glassfish.grizzly.samples: samples

%build
# forcing the use of required glassfish-servlet-api 3.1 apis
# test skipped on arm builder
# https://bugzilla.redhat.com/show_bug.cgi?id=991712
%mvn_build \
%ifarch %{arm}
 -f -- \
%else
 -- -Dmaven.test.failure.ignore=true \
%endif
 -Dmaven.test.skip.exec=true \
 -Dmaven.local.depmap.file="%{_mavendepmapfragdir}/glassfish-servlet-api.xml"

%install
%mvn_install

(
  cd %{buildroot}%{_javadir}/%{name}
  ln -sf %{name}-framework.jar %{name}.jar
)

%files -f .mfiles
%{_javadir}/%{name}/%{name}.jar
%doc LICENSE.txt Grizzly_THIRDPARTYLICENSEREADME.txt

%files samples -f .mfiles-samples
%doc LICENSE.txt Grizzly_THIRDPARTYLICENSEREADME.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt Grizzly_THIRDPARTYLICENSEREADME.txt

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.24-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.19-alt1_2jpp8
- java 8 mass update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.6-alt1_1jpp7
- new version

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7.3.3-alt2_1jpp5
- fixes for java6 support

* Fri Mar 06 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.3.3-alt1_1jpp5
- new version

