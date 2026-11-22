%global srcname jetty
%global addver  .v20250814
%global compatver 9.4

Name:           jetty9
Version:        9.4.58
Release:        alt3

Summary:        Java Webserver and Servlet Container (compat 9.x libraries)
License:        Apache-2.0 or EPL-1.0
Group:          Networking/WWW
URL:            https://jetty.org/
VCS:            https://github.com/jetty/jetty.project

Source0:        %srcname-%version%addver.tar.gz
Source1:        LICENSE-MIT

Patch1:         0001-Port-to-servlet-api-4-5.patch
Patch2:         0002-Disable-Jetty-util-tests-that-require-removed-binari.patch
Patch3:         0003-Use-an-attribute-only-ServletContext-in-the-SameSite.patch
Patch4:         0004-Disable-XML-parser-test-that-requires-external-DTD-r.patch
Patch5:         0005-Exclude-unavailable-ZIP-filesystem-range-inputs-in-o.patch
Patch6:         0006-Disable-servlet-suites-blocked-by-unavailable-test-f.patch
Patch7:         0007-Exclude-webapp-tests-with-unavailable-package-fixtur.patch
Patch8:         0008-Disable-timing-sensitive-TLS-variant-of-the-HTTP-met.patch
Patch9:         0009-Exclude-the-gzip-test-input-stripped-by-RPM-preparat.patch
Patch10:        0010-Skip-the-two-gigabyte-response-stress-test-on-32-bit.patch
Patch11:        0011-Remove-the-script-tag-from-the-Resource-Javadoc-exam.patch
Patch12:        0012-Scale-the-HTTP-2-stream-stress-test-on-32-bit-JVMs.patch

BuildRequires(pre):  rpm-macros-java
BuildRequires:  java-21-openjdk-devel
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)

BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-test-helper)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-perf-helper)
BuildRequires:  mvn(org.junit:junit-bom:pom:)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.junit.vintage:junit-vintage-engine)
BuildRequires:  mvn(org.awaitility:awaitility)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.slf4j:slf4j-jdk14)
BuildRequires:  mvn(net.minidev:json-smart)

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

%package        alpn-client
Group:          Networking/WWW
Summary:        Jetty 9.x ALPN client module (compat)
%description    alpn-client
Jetty 9.x compatibility library: ALPN client module.

%package        alpn-server
Group:          Networking/WWW
Summary:        Jetty 9.x ALPN server module (compat)
%description    alpn-server
Jetty 9.x compatibility library: ALPN server module.

%package        alpn-java-client
Group:          Networking/WWW
Summary:        Jetty 9.x Java ALPN client module (compat)
%description    alpn-java-client
Jetty 9.x compatibility library: Java ALPN client module.

%package        alpn-java-server
Group:          Networking/WWW
Summary:        Jetty 9.x Java ALPN server module (compat)
%description    alpn-java-server
Jetty 9.x compatibility library: Java ALPN server module.

%package        alpn-openjdk8-client
Group:          Networking/WWW
Summary:        Jetty 9.x OpenJDK 8 ALPN client module (compat)
%description    alpn-openjdk8-client
Jetty 9.x compatibility library: OpenJDK 8 ALPN client module.

%package        alpn-openjdk8-server
Group:          Networking/WWW
Summary:        Jetty 9.x OpenJDK 8 ALPN server module (compat)
%description    alpn-openjdk8-server
Jetty 9.x compatibility library: OpenJDK 8 ALPN server module.

%package        http2-client
Group:          Networking/WWW
Summary:        Jetty 9.x HTTP/2 client module (compat)
%description    http2-client
Jetty 9.x compatibility library: HTTP/2 client module.

%package        http2-common
Group:          Networking/WWW
Summary:        Jetty 9.x HTTP/2 common module (compat)
%description    http2-common
Jetty 9.x compatibility library: HTTP/2 common module.

%package        http2-hpack
Group:          Networking/WWW
Summary:        Jetty 9.x HTTP/2 HPACK module (compat)
%description    http2-hpack
Jetty 9.x compatibility library: HTTP/2 HPACK module.

%package        http2-http-client-transport
Group:          Networking/WWW
Summary:        Jetty 9.x HTTP/2 HTTP client transport module (compat)
%description    http2-http-client-transport
Jetty 9.x compatibility library: HTTP/2 HTTP client transport module.

%package        http2-server
Group:          Networking/WWW
Summary:        Jetty 9.x HTTP/2 server module (compat)
%description    http2-server
Jetty 9.x compatibility library: HTTP/2 server module.

%package        servlets
Group:          Networking/WWW
Summary:        Jetty 9.x Servlet utilities module (compat)
%description    servlets
Jetty 9.x compatibility library: Servlet utilities module.

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

# JaCoCo is disabled, so Surefire must not expand its late @{argLine}.
surefire="pom:plugin[pom:artifactId='maven-surefire-plugin']"
managed="pom:build/pom:pluginManagement/pom:plugins/$surefire"
webapp="pom:profiles/pom:profile[pom:id='jdk9']"
webapp="$webapp/pom:build/pom:plugins/$surefire"
test_heap='-Xmx6g -Xms2g'
java=%_jvmdir/java-21-openjdk/bin/java
if "$java" -XshowSettings:properties -version 2>&1 | \
    grep -Fq 'sun.arch.data.model = 32'; then
    test_heap='-Xmx1g -Xms128m'
fi
test_args='-Dfile.encoding=UTF-8 -Duser.language=en -Duser.region=US'
test_args="$test_args -showversion"
%pom_xpath_replace "$managed/pom:configuration/pom:argLine" \
    "<argLine>$test_args $test_heap -XX:+PrintGCDetails</argLine>"
%pom_xpath_replace "$webapp/pom:configuration/pom:argLine" \
    '<argLine>--module-path src/test/resources/mods</argLine>' jetty-webapp

# Skip only compile-time fixtures whose test dependencies are unavailable.
compiler=':maven-compiler-plugin:${maven.compiler.plugin.version}'
exclude='<configuration><testExcludes><testExclude>'
end='</testExclude></testExcludes></configuration>'
%pom_add_plugin "$compiler" jetty-client \
    "$exclude**/SPNEGOAuthenticationTest.java$end"
%pom_add_plugin "$compiler" jetty-http2/http2-client \
    "$exclude**/ProxyTest.java$end"
%pom_add_plugin "$compiler" jetty-jaas \
    "$exclude**/JAASLdapLoginServiceTest.java$end"
%pom_add_plugin "$compiler" jetty-jmx "$exclude**/PojoTest.java$end"

%pom_remove_dep org.apache.kerby:kerb-simplekdc jetty-client
%pom_remove_dep org.eclipse.jetty:jetty-proxy jetty-http2/http2-client
%pom_remove_dep com.openpojo:openpojo jetty-jmx
%pom_remove_dep org.apache.directory.server:apacheds-test-framework jetty-jaas
%pom_remove_dep org.apache.directory.server:apacheds-server-integ jetty-jaas
%pom_remove_dep org.apache.directory.server:apacheds-core-integ jetty-jaas

%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin

%pom_remove_plugin -r :h2spec-maven-plugin
%pom_xpath_remove pom:build/pom:extensions

# Unnecessary pom flattening can be skipped
%pom_remove_plugin -r :flatten-maven-plugin jetty-bom

%pom_disable_module aggregates/jetty-all

# Jetty accesses these JDK packages reflectively, so their imports are optional.
jdk_imports='sun.misc;resolution:=optional'
jdk_imports="$jdk_imports,com.sun.nio.file;resolution:=optional"
%pom_xpath_inject pom:configuration/pom:instructions \
    "<Import-Package>$jdk_imports,*</Import-Package>"

%pom_change_dep -r org.mortbay.jasper:apache-jsp org.apache.tomcat:tomcat-jasper

# provided by glassfish-jsp-api that has newer version
%pom_change_dep -r javax.servlet.jsp:jsp-api \
    javax.servlet.jsp:javax.servlet.jsp-api

# txt artifact - not installable
%pom_remove_plugin ":jetty-version-maven-plugin"

# These bundles have a dep on Eclipse that is not available on every arch
%pom_disable_module jetty-osgi

# We don't have asciidoctor-maven-plugin
%pom_disable_module jetty-documentation
%pom_remove_dep -r :jetty-documentation

# We don't have gcloud-java-datastore
%pom_disable_module jetty-gcloud

# we don't have com.googlecode.xmemcached:xmemcached yet
%pom_disable_module jetty-memcached

# Hazelcast is too old to build against
%pom_disable_module jetty-hazelcast

# Infinispan is too old to build against
%pom_disable_module jetty-infinispan

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

cp %SOURCE1 .

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
%pom_disable_module jetty-fcgi
%pom_disable_module jetty-websocket
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
%pom_disable_module jetty-home
%pom_disable_module jetty-openid

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

%mvn_compat_version : %compatver %version%addver

%build
export JAVA_HOME=%_jvmdir/java-21-openjdk
export PATH="$JAVA_HOME/bin:$PATH"
%mvn_build -s

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

%files alpn-client -f .mfiles-jetty-alpn-client
%files alpn-server -f .mfiles-jetty-alpn-server
%files alpn-java-client -f .mfiles-jetty-alpn-java-client
%files alpn-java-server -f .mfiles-jetty-alpn-java-server
%files alpn-openjdk8-client -f .mfiles-jetty-alpn-openjdk8-client
%files alpn-openjdk8-server -f .mfiles-jetty-alpn-openjdk8-server
%files http2-client -f .mfiles-http2-client
%files http2-common -f .mfiles-http2-common
%files http2-hpack -f .mfiles-http2-hpack
%files http2-http-client-transport -f .mfiles-http2-http-client-transport
%files http2-server -f .mfiles-http2-server
%files servlets -f .mfiles-jetty-servlets

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 9.4.58-alt3
- Package the Jetty 9 HTTP/2, Servlets and ALPN modules.
- Enable tests and adjust them for the 32-bit JVM.

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

