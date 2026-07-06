%global srcname jetty
%global addver  .v20250814
%global compatver 9.4

Name:           jetty9
Version:        9.4.58
Release:        alt2

Summary:        Java Webserver and Servlet Container (compat 9.x libraries)
License:        Apache-2.0 or EPL-1.0
Group:          Networking/WWW
URL:            https://jetty.org/
VCS:            https://github.com/jetty/jetty.project

Source0:        %srcname-%version%addver.tar.gz
Source6:        LICENSE-MIT

Patch1:         0001-Distro-jetty.home.patch
Patch2:         0002-Port-to-servlet-api-4-5.patch

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)

BuildArch:      noarch

%description
Jetty is a 100%% Java HTTP Server and Servlet Container, providing a fully
featured web server for static and dynamic content.

This package contains the Jetty 9.x compatibility libraries, installed as
versioned (compat) Maven artifacts so they can coexist with a newer Jetty.

%package        client
Group:          Networking/WWW
Summary:        Jetty 9.x client module (compat)
%description    client
Jetty 9.x compatibility library: HTTP client module.

%package        continuation
Group:          Networking/WWW
Summary:        Jetty 9.x continuation module (compat)
%description    continuation
Jetty 9.x compatibility library: continuation module.

%package        http
Group:          Networking/WWW
Summary:        Jetty 9.x http module (compat)
%description    http
Jetty 9.x compatibility library: HTTP module.

%package        io
Group:          Networking/WWW
Summary:        Jetty 9.x io module (compat)
%description    io
Jetty 9.x compatibility library: I/O module.

%package        jaas
Group:          Networking/WWW
Summary:        Jetty 9.x jaas module (compat)
%description    jaas
Jetty 9.x compatibility library: JAAS module.

%package        jmx
Group:          Networking/WWW
Summary:        Jetty 9.x jmx module (compat)
%description    jmx
Jetty 9.x compatibility library: JMX module.

%package        security
Group:          Networking/WWW
Summary:        Jetty 9.x security module (compat)
%description    security
Jetty 9.x compatibility library: security module.

%package        server
Group:          Networking/WWW
Summary:        Jetty 9.x server module (compat)
%description    server
Jetty 9.x compatibility library: server module.

%package        servlet
Group:          Networking/WWW
Summary:        Jetty 9.x servlet module (compat)
%description    servlet
Jetty 9.x compatibility library: servlet module.

%package        util
Group:          Networking/WWW
Summary:        Jetty 9.x util module (compat)
# Utf8Appendable.java is additionally under MIT license
License:        (Apache-2.0 or EPL-1.0) and MIT
%description    util
Jetty 9.x compatibility library: utility module.

%package        util-ajax
Group:          Networking/WWW
Summary:        Jetty 9.x util-ajax module (compat)
%description    util-ajax
Jetty 9.x compatibility library: AJAX utility module.

%package        webapp
Group:          Networking/WWW
Summary:        Jetty 9.x webapp module (compat)
%description    webapp
Jetty 9.x compatibility library: webapp module.

%package        xml
Group:          Networking/WWW
Summary:        Jetty 9.x xml module (compat)
%description    xml
Jetty 9.x compatibility library: XML module.

%javadoc_package

%prep
%setup -n jetty.project-jetty-%version%addver
%autopatch -p1

find . -name "*.?ar" -exec rm {} \;
find . -name "*.class" -exec rm {} \;

# Plugins irrelevant or harmful to building the package
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :spotbugs-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :license-maven-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :h2spec-maven-plugin
%pom_xpath_remove pom:build/pom:extensions

# Unnecessary pom flattening can be skipped
%pom_remove_plugin -r :flatten-maven-plugin jetty-bom

%pom_disable_module aggregates/jetty-all

# Reflective use of classes that might not be present in the JDK should be optional OSGi-wise
%pom_xpath_inject "pom:configuration/pom:instructions" \
"<Import-Package>sun.misc;resolution:=optional,com.sun.nio.file;resolution:=optional,*</Import-Package>"

%pom_remove_dep "com.sun.net.httpserver:http" jetty-http-spi

%pom_change_dep -r org.mortbay.jasper:apache-jsp org.apache.tomcat:tomcat-jasper

%pom_add_dep 'org.junit.jupiter:junit-jupiter-engine:${junit.version}' tests/test-sessions/test-sessions-common

# provided by glassfish-jsp-api that has newer version
%pom_change_dep -r javax.servlet.jsp:jsp-api javax.servlet.jsp:javax.servlet.jsp-api

# txt artifact - not installable
%pom_remove_plugin ":jetty-version-maven-plugin"
%pom_xpath_remove "pom:artifactItem[pom:classifier='version']" jetty-home

# Disable building source release
%pom_xpath_remove 'pom:execution[pom:id="sources"]' jetty-home

# Unwanted JS in javadoc
sed -i '/^\s*\*.*<script>/d' jetty-util/src/main/java/org/eclipse/jetty/util/resource/Resource.java

# only used for integration tests
%pom_remove_plugin :maven-invoker-plugin jetty-jspc-maven-plugin

# These bundles have a dep on Eclipse that is not available on every arch
%pom_disable_module jetty-osgi

# We don't have asciidoctor-maven-plugin
%pom_disable_module jetty-documentation
%pom_remove_dep -r :jetty-documentation
%pom_xpath_remove 'pom:execution[pom:id="unpack-documentation"]' jetty-distribution

%pom_xpath_remove 'pom:artifactItem[pom:artifactId="libsetuid-osx"]' jetty-home/pom.xml

# TODO remove when jetty-setuid is packaged
%pom_xpath_remove "pom:execution[pom:id[text()='copy-setuid-deps']]" jetty-home/pom.xml

# We don't have gcloud-java-datastore
%pom_disable_module jetty-gcloud
%pom_disable_module test-gcloud-sessions tests/test-sessions
%pom_remove_dep :jetty-gcloud-session-manager jetty-home

# we don't have com.googlecode.xmemcached:xmemcached yet
%pom_disable_module jetty-memcached
%pom_disable_module test-memcached-sessions tests/test-sessions
%pom_remove_dep :jetty-memcached-sessions jetty-home

# Hazelcast is too old to build against
%pom_disable_module jetty-hazelcast
%pom_disable_module test-hazelcast-sessions tests/test-sessions
%pom_remove_dep :jetty-hazelcast jetty-home

# Infinispan is too old to build against
%pom_disable_module jetty-infinispan
%pom_disable_module test-infinispan-sessions tests/test-sessions
%pom_remove_dep :infinispan-embedded jetty-home
%pom_remove_dep :infinispan-embedded-query jetty-home
%pom_remove_dep :infinispan-remote jetty-home
%pom_remove_dep :infinispan-remote-query jetty-home
%pom_xpath_remove "pom:execution[pom:id='unpack-infinispan-config']" jetty-home

# Springframework not available
%pom_disable_module jetty-spring

# Not currently able to build tests, so can't build benchmarks
%pom_disable_module jetty-jmh

# Distribution tests require internet access, so disable
%pom_disable_module test-distribution tests

# missing conscrypt
%pom_disable_module jetty-alpn-conscrypt-server jetty-alpn
%pom_disable_module jetty-alpn-conscrypt-client jetty-alpn
%pom_remove_dep -r :jetty-alpn-conscrypt-server
%pom_remove_dep -r :jetty-alpn-conscrypt-client
rm -fr examples/embedded/src/main/java/org/eclipse/jetty/embedded/ManyConnectors.java

cp %SOURCE6 .

# the default location is not allowed by SELinux
sed -i '/<SystemProperty name="jetty.state"/d' \
    jetty-home/src/main/resources/etc/jetty-started.xml

# Remove org.apache.directory.api support
%pom_remove_dep :api-ldap-schema-data jetty-jaas
%pom_remove_dep :api-ldap-model jetty-jaas
%pom_remove_dep :api-util jetty-jaas
%pom_remove_dep :api-asn1-api jetty-jaas

# remote-resources only copies about.html
%pom_remove_plugin :maven-remote-resources-plugin
# packages module configs, we don't need those in a libraries-only build
%pom_remove_plugin :maven-assembly-plugin
# only useful when tests are enabled (copies test deps)
%pom_remove_plugin :maven-dependency-plugin jetty-client
%pom_xpath_remove "pom:dependency[pom:artifactId='testcontainers-bom']"
%pom_xpath_remove "pom:dependency[pom:artifactId='infinispan-bom']"

# Drop everything that is not part of the minimal libraries set.
%pom_disable_module jetty-ant
%pom_disable_module jetty-http2
%pom_disable_module jetty-fcgi
%pom_disable_module jetty-websocket
%pom_disable_module jetty-servlets
%pom_disable_module apache-jsp
%pom_disable_module apache-jstl
%pom_disable_module jetty-maven-plugin
%pom_disable_module jetty-jspc-maven-plugin
%pom_disable_module jetty-deploy
%pom_disable_module jetty-start
%pom_disable_module jetty-plus
%pom_disable_module jetty-annotations
%pom_disable_module jetty-jndi
%pom_disable_module jetty-cdi
%pom_disable_module jetty-proxy
%pom_disable_module jetty-jaspi
%pom_disable_module jetty-rewrite
%pom_disable_module jetty-nosql
%pom_disable_module jetty-unixsocket
%pom_disable_module tests
%pom_disable_module examples
%pom_disable_module jetty-quickstart
%pom_disable_module jetty-distribution
%pom_disable_module jetty-runner
%pom_disable_module jetty-http-spi
%pom_disable_module jetty-alpn
%pom_disable_module jetty-home
%pom_disable_module jetty-openid

%mvn_package :jetty-home __noinstall
%mvn_package :jetty-distribution __noinstall
%mvn_package :build-resources __noinstall

# Do not install aggregate POMs separately.
%mvn_package ':*-project' __noinstall
%mvn_package ':*-parent' __noinstall
%mvn_package ':*-bom' __noinstall

%mvn_package ':test-*' __noinstall
%mvn_package ':*-tests' __noinstall
%mvn_package ':*-it' __noinstall
%mvn_package ':example-*' __noinstall
%mvn_package org.eclipse.jetty.tests: __noinstall
%mvn_package ::war: __noinstall
%mvn_package :jetty-runner __noinstall

%mvn_compat_version : %compatver %version%addver

%build
%mvn_build -f -s

%install
%mvn_install

%files client -f .mfiles-jetty-client
%files continuation -f .mfiles-jetty-continuation
%files http -f .mfiles-jetty-http
%files io -f .mfiles-jetty-io
%files jaas -f .mfiles-jetty-jaas
%files jmx -f .mfiles-jetty-jmx
%files security -f .mfiles-jetty-security
%files server -f .mfiles-jetty-server
%files servlet -f .mfiles-jetty-servlet
%files util -f .mfiles-jetty-util
%doc --no-dereference LICENSE NOTICE.txt LICENSE-MIT
%files util-ajax -f .mfiles-jetty-util-ajax
%files webapp -f .mfiles-jetty-webapp
%files xml -f .mfiles-jetty-xml

%changelog
* Thu Jul 02 2026 Evgeniy Serov <scala@altlinux.org> 9.4.58-alt2
- Split jetty9 compat package off jetty 9.4.58.
- Marked all Maven artifacts as compat (9.4) to coexist with jetty 12.

* Mon Feb 09 2026 Andrey Cherepanov <cas@altlinux.org> 9.4.58-alt1
- New version (fixes: CVE-2025-5115).

* Mon Mar 24 2025 Andrey Cherepanov <cas@altlinux.org> 9.4.57-alt1
- New version (fixes CVE-2024-6763)

* Thu Nov 21 2024 Andrey Cherepanov <cas@altlinux.org> 9.4.56-alt1
- New version.
- Change URL to https://jetty.org/
- Security fixes: CVE-2021-34429, CVE-2022-2047, CVE-2023-26048, CVE-2023-26049,
  CVE-2023-40167, CVE-2023-41900, CVE-2024-22201

* Sun Feb 13 2022 Igor Vlasenko <viy@altlinux.org> 9.4.40-alt1_2jpp11
- do not package init script in minimal version (closes: 41882)

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 9.4.40-alt1_1jpp11
- fc update

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 9.4.38-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 9.4.31-alt1_3jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 9.4.24-alt1_3.v20191120jpp8
- fc update

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 9.4.19-alt1_1.v20190610jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 9.4.11-alt1_3.v20180605jpp8
- new version

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 9.4.10-alt1_1.v20180503jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 9.4.7-alt1_1.v20170914jpp8
- new version

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 9.4.6-alt2_2.v20170531jpp8
- fixed build with new tomcat

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 9.4.6-alt1_2.v20170531jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 9.4.3-alt1_3.v20170317jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 9.4.0-alt1_0.2.M0jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 9.3.7-alt1_2.v20160115jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 9.3.0-alt1_6jpp8
- new version

* Wed Apr 24 2013 Repocop Q. A. Robot <repocop@altlinux.org> 8.1.5-alt4_6jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * systemd-files-in-etc for jetty

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt4_6jpp7
- fixed init script

* Sun Mar 24 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt3_6jpp7
- fixed scripts and provides

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt2_6jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_6jpp7
- fc update

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_5jpp7
- new version (closes: #27671)

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.5-alt1_2jpp7
- prebuild using manual depmap 

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt4_4jpp7
- fixed build

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt3_4jpp7
- rebuild

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt2_4jpp7
- fixed %pre

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 8.1.0-alt1_4jpp7
- full version

