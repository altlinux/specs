Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: perl(IO/Socket.pm)
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name grizzly
%define version 2.3.6
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
Name:          grizzly
Version:       2.3.6
Release:       alt1_1jpp7
Summary:       Java NIO Server Framework
# see Grizzly_THIRDPARTYLICENSEREADME.txt
License:       (CDDL or GPLv2 with exceptions) and BSD and ASL 2.0 and Public Domain
URL:           http://grizzly.java.net/
# git clone git://java.net/grizzly~git
# (cd grizzly~git/ && git archive --format=tar --prefix=grizzly-2.3.6/ 2_3_6 | xz > ../grizzly-2.3.6.tar.xz)
Source0:       %{name}-%{namedversion}.tar.xz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# grizzly package don't include the license file
Source1:       glassfish-LICENSE.txt
# build support for glassfish-jaxws >= 2.2.7
Patch0:        %{name}-2.3.3-jaws227.patch

BuildRequires: mvn(net.java:jvnet-parent)
# Multiple packages with the same gId:aId.
BuildRequires: glassfish-servlet-api
BuildRequires: mvn(com.sun.xml.ws:jaxws-rt)
BuildRequires: mvn(org.glassfish.gmbal:gmbal)
BuildRequires: mvn(org.glassfish.gmbal:gmbal-api-only)
BuildRequires: mvn(org.osgi:org.osgi.compendium)
BuildRequires: mvn(org.osgi:org.osgi.core)

# test deps
%if 0
# Circular deps
BuildRequires: mvn(com.sun.jersey:jersey-client)
BuildRequires: mvn(com.sun.jersey:jersey-server)
BuildRequires: mvn(com.sun.jersey:jersey-servlet)
%endif
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-istack-commons-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-war-plugin
# Require servlet-api 3.1
Requires:      glassfish-servlet-api
BuildArch:     noarch
Source44: import.info

# config

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
%setup -q -n %{name}-%{namedversion}
find . -name '*.jar' -delete
find . -name '*.class' -delete

%patch0 -p0

# unavailable deps
# org.jvnet.maven-antrun-extended-plugin maven-antrun-extended-plugin
%pom_disable_module bundles extras
%pom_disable_module bundles modules

# org.ops4j maven-pax-plugin  1.5
%pom_disable_module grizzly-httpservice extras

# XMvn don't support file with war extension
%pom_disable_module comet samples

# remove internal libraries
%pom_disable_module websockets/chat samples

# org.glassfish.hk2 config-generator 2.1.57
#%%pom_disable_module config modules
#%%pom_remove_dep :cobertura-maven-plugin
%pom_remove_dep :maven-bundle-plugin
%pom_remove_dep :maven-plugin-tools-api
%pom_remove_dep org.glassfish.hk2:config-types
%pom_remove_dep org.glassfish.hk2:core
%pom_remove_dep org.glassfish.hk2:hk2-config
%pom_remove_dep org.glassfish.hk2:hk2-locator
%pom_remove_dep org.glassfish.hk2:osgi-adapter

%pom_xpath_remove "pom:build/pom:extensions/pom:extension[pom:artifactId = 'wagon-webdav']"

# org.glassfish.grizzly:grizzly-npn-api:1.0
%pom_disable_module spdy modules
%pom_disable_module spdy-samples samples

#%%pom_remove_dep org.glassfish.grizzly:documentation bom
%pom_remove_dep org.glassfish.grizzly:grizzly-comet-server bom
%pom_remove_dep org.glassfish.grizzly:grizzly-compression bom
%pom_remove_dep org.glassfish.grizzly:grizzly-core bom
%pom_remove_dep org.glassfish.grizzly:grizzly-http-all bom
%pom_remove_dep org.glassfish.grizzly:grizzly-http-server-core bom
%pom_remove_dep org.glassfish.grizzly:grizzly-http-server-jaxws bom
%pom_remove_dep org.glassfish.grizzly:grizzly-http-servlet-server bom
%pom_remove_dep org.glassfish.grizzly:grizzly-spdy bom
%pom_remove_dep org.glassfish.grizzly:grizzly-websockets-server bom
%pom_remove_dep org.glassfish.grizzly.osgi:grizzly-httpservice bom
%pom_remove_dep org.glassfish.grizzly.osgi:grizzly-httpservice-bundle bom
%pom_remove_plugin :maven-antrun-extended-plugin bom
%pom_remove_plugin :glassfish-copyright-maven-plugin bom

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :nexus-maven-plugin

# circular deps
%if 0
%pom_add_dep com.sun.jersey:jersey-servlet:'${jersey-version}':test modules/http-servlet
%else
%pom_remove_dep com.sun.jersey: modules/http-servlet
rm -rf modules/http-servlet/src/test/java/filter/*
%endif

cp -p %{SOURCE1} LICENSE.txt
cp -p modules/grizzly/src/main/resources/Grizzly_THIRDPARTYLICENSEREADME.txt .
sed -i 's/\r//' LICENSE.txt Grizzly_THIRDPARTYLICENSEREADME.txt

sed -i 's|${artifactId}|${project.artifactId}|' $(find . -name "pom.xml")
sed -i 's|${version}|${project.version}|' $(find . -name "pom.xml")
sed -i 's|${pom.url}|${project.url}|' $(find . -name "pom.xml")
sed -i 's|${pom.version}|${project.version}|' $(find . -name "pom.xml")

# fix aId for new istack-commons maven plugin
while read f; do

%pom_xpath_set "pom:project/pom:build/pom:plugins/pom:plugin[pom:groupId='com.sun.istack']/pom:artifactId" \
 istack-commons-maven-plugin ${f}

done <<'.'
modules/%{name}
modules/monitoring/%{name}
modules/monitoring/http
modules/monitoring/http-server
.

# Force servlet 3.1 apis
%pom_remove_dep javax.servlet:servlet-api modules/comet
%pom_add_dep javax.servlet:javax.servlet-api:3.1.0:provided modules/comet

%build

%mvn_package org.glassfish.grizzly.samples: samples
# forcing the use of required glassfish-servlet-api 3.1 apis
# test skipped on arm builder
# https://bugzilla.redhat.com/show_bug.cgi?id=991712
%mvn_build \
%ifarch %{arm}
 -f -- \
%else
 -f -- -Dmaven.test.failure.ignore=true \
%endif
 -Dmaven.local.depmap.file="%{_mavendepmapfragdir}/glassfish-servlet-api.xml"

%install
%mvn_install

(
  cd %{buildroot}%{_javadir}/%{name}
  ln -sf %{name}-framework.jar %{name}.jar
)

%files -f .mfiles
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}.jar
%doc LICENSE.txt Grizzly_THIRDPARTYLICENSEREADME.txt

# config

%files samples -f .mfiles-samples
%doc LICENSE.txt Grizzly_THIRDPARTYLICENSEREADME.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt Grizzly_THIRDPARTYLICENSEREADME.txt

%changelog
* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.6-alt1_1jpp7
- new version

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7.3.3-alt2_1jpp5
- fixes for java6 support

* Fri Mar 06 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7.3.3-alt1_1jpp5
- new version

