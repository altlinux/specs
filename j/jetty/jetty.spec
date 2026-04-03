%define _unpackaged_files_terminate_build 1

Name: jetty
Version: 12.1.8
Release: alt1

Summary: Java Webserver and Servlet Container
License: Apache-2.0 or EPL-2.0
Group: Networking/WWW
Url: https://jetty.org
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-shade-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: jackson-bom
BuildRequires: jackson-parent
BuildRequires: slf4j
BuildRequires: junit5
BuildRequires: maven-resolver
BuildRequires: maven-common-artifact-filters
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-file-management
BuildRequires: maven-shared-io
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-dependency-tree

%description
Jetty is a Java HTTP Server and Servlet Container.

%package util
Summary: Utilities module for Jetty
Group: Networking/WWW

%description util
Jetty utility classes.

%package util-ajax
Summary: AJAX utility module for Jetty
Group: Networking/WWW

%description util-ajax
Jetty utility classes for AJAX processing.

%package jmx
Summary: JMX module for Jetty
Group: Networking/WWW

%description jmx
Jetty JMX integration.

%package io
Summary: I/O module for Jetty
Group: Networking/WWW

%description io
Jetty I/O module.

%package http
Summary: HTTP module for Jetty
Group: Networking/WWW

%description http
Jetty HTTP module.

%package server
Summary: Server module for Jetty
Group: Networking/WWW

%description server
Jetty server module.

%package security
Summary: Security module for Jetty
Group: Networking/WWW

%description security
Jetty security module.

%package session
Summary: Session module for Jetty
Group: Networking/WWW

%description session
Jetty session management module.

%package alpn-client
Summary: ALPN client API for Jetty
Group: Networking/WWW

%description alpn-client
Jetty ALPN client API module.

%package alpn-server
Summary: ALPN server API for Jetty
Group: Networking/WWW

%description alpn-server
Jetty ALPN server API module.

%package alpn-java-client
Summary: ALPN Java client implementation for Jetty
Group: Networking/WWW

%description alpn-java-client
Jetty ALPN Java client implementation.

%package alpn-java-server
Summary: ALPN Java server implementation for Jetty
Group: Networking/WWW

%description alpn-java-server
Jetty ALPN Java server implementation.

%package client
Summary: HTTP client module for Jetty
Group: Networking/WWW

%description client
Jetty HTTP client module.

%package compression-common
Summary: Compression common module for Jetty
Group: Networking/WWW

%description compression-common
Jetty compression common module.

%package compression-gzip
Summary: Compression gzip module for Jetty
Group: Networking/WWW

%description compression-gzip
Jetty gzip compression module.

%package http2-hpack
Summary: HTTP/2 HPACK module for Jetty
Group: Networking/WWW

%description http2-hpack
Jetty HTTP/2 HPACK module.

%package http2-common
Summary: HTTP/2 common module for Jetty
Group: Networking/WWW

%description http2-common
Jetty HTTP/2 common module.

%package http2-client
Summary: HTTP/2 client module for Jetty
Group: Networking/WWW

%description http2-client
Jetty HTTP/2 client module.

%package http2-client-transport
Summary: HTTP/2 client transport module for Jetty
Group: Networking/WWW

%description http2-client-transport
Jetty HTTP/2 client transport module.

%package http2-server
Summary: HTTP/2 server module for Jetty
Group: Networking/WWW

%description http2-server
Jetty HTTP/2 server module.

%package ee-webapp
Summary: EE webapp core module for Jetty
Group: Networking/WWW

%description ee-webapp
Jetty core EE webapp module.

%package ee9-nested
Summary: EE9 nested server adapter module for Jetty
Group: Networking/WWW

%description ee9-nested
Jetty EE9 nested server adapter module.

%package ee9-security
Summary: EE9 security module for Jetty
Group: Networking/WWW

%description ee9-security
Jetty EE9 security module.

%package servlet
Summary: Legacy jetty-servlet compatibility coordinates
Group: Networking/WWW
Provides: mvn(org.eclipse.jetty:jetty-servlet)
Provides: mvn(org.eclipse.jetty:jetty-servlet:pom:)

%description servlet
Compatibility package that provides legacy org.eclipse.jetty:jetty-servlet
Maven coordinates via Jetty EE9 servlet module.

%prep
%setup

rm -f .mvn/extensions.xml .mvn/maven.config

# Keep build focused on packaging; disable non-essential QA/release tooling.
%pom_remove_plugin -r -f :maven-checkstyle-plugin
%pom_remove_plugin -r -f :maven-enforcer-plugin
%pom_remove_plugin -r -f :license-maven-plugin
%pom_remove_plugin -r -f :maven-source-plugin
%pom_remove_plugin -r -f :maven-resources-plugin
%pom_remove_plugin -r -f :maven-deploy-plugin
%pom_remove_plugin -r -f :jacoco-maven-plugin
%pom_remove_plugin -r -f :maven-release-plugin
%pom_remove_plugin -r -f :buildnumber-maven-plugin
%pom_remove_plugin -r -f :h2spec-maven-plugin
%pom_remove_plugin -r -f :maven-remote-resources-plugin
%pom_remove_plugin -r -f :spotbugs-maven-plugin
%pom_remove_plugin -r -f org.codehaus.mojo:flatten-maven-plugin
%pom_remove_plugin -r -f com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin -r -f org.eclipse.jetty.toolchain:jetty-version-maven-plugin
%pom_remove_plugin -r -f org.eclipse.jetty.toolchain:jetty-modify-sources-maven-plugin
%pom_remove_plugin -r -f :cyclonedx-maven-plugin

# Drop Maven build extensions/BOM imports unavailable in offline ALT buildroot.
%pom_xpath_remove -r -f "//pom:extension[pom:groupId='eu.maveniverse.maven.njord' and pom:artifactId='extension3']"
%pom_xpath_remove -r -f "//pom:extension[pom:groupId='eu.maveniverse.maven.mimir' and pom:artifactId='extension3']"
%pom_xpath_remove -r -f "//pom:extension[pom:groupId='org.apache.maven.extensions' and pom:artifactId='maven-build-cache-extension']"
%pom_xpath_remove -r -f "//pom:profile[pom:id='config']"
%pom_remove_dep -r -f io.netty:netty-bom
%pom_remove_dep -r -f org.hibernate.search:hibernate-search-bom
%pom_remove_dep -r -f org.infinispan:infinispan-bom
%pom_remove_dep -r -f org.testcontainers:testcontainers-bom
%pom_remove_dep -r -f jakarta.platform:jakarta.jakartaee-bom
%pom_remove_dep -r -f org.eclipse.jetty.toolchain:jetty-modify-sources-maven-plugin
%pom_xpath_remove "//pom:plugin[pom:artifactId='maven-dependency-plugin']/pom:executions/pom:execution[pom:id='unpack']" jetty-core/jetty-client/pom.xml

# Not available in repository right now.
%pom_disable_module jetty-alpn-conscrypt-client jetty-core/jetty-alpn
%pom_disable_module jetty-alpn-conscrypt-server jetty-core/jetty-alpn
%pom_disable_module jetty-alpn-bouncycastle-client jetty-core/jetty-alpn
%pom_disable_module jetty-alpn-bouncycastle-server jetty-core/jetty-alpn

# Native/extra compression modules are not required for Jersey buildability.
%pom_disable_module jetty-compression-brotli jetty-core/jetty-compression
%pom_disable_module jetty-compression-zstandard jetty-core/jetty-compression
%pom_disable_module jetty-compression-tests jetty-core/jetty-compression

# Skip test/reactor-only modules.
%pom_disable_module build
%pom_disable_module jetty-bom jetty-core
%pom_disable_module jetty-slf4j-impl jetty-core
%pom_disable_module jetty-http2-tests jetty-core/jetty-http2
%pom_disable_module jetty-tests jetty-core
%pom_disable_module jetty-http3 jetty-core
%pom_disable_module jetty-quic jetty-core
%pom_disable_module jetty-osgi jetty-core
%pom_disable_module jetty-coreapp jetty-core
%pom_disable_module jetty-staticapp jetty-core
%pom_disable_module jetty-deploy jetty-core
%pom_disable_module jetty-fcgi jetty-core
%pom_disable_module jetty-http-spi jetty-core
%pom_disable_module jetty-http-tools jetty-core
%pom_disable_module jetty-maven jetty-core
%pom_disable_module jetty-plus jetty-core
%pom_disable_module jetty-proxy jetty-core
%pom_disable_module jetty-rewrite jetty-core
%pom_disable_module jetty-start jetty-core
%pom_disable_module jetty-unixdomain-server jetty-core
%pom_disable_module jetty-websocket jetty-core
%pom_disable_module jetty-annotations jetty-core
%pom_disable_module jetty-jndi jetty-core
%pom_disable_module jetty-keystore jetty-core
%pom_disable_module jetty-xml jetty-core
%pom_disable_module jetty-compression-server jetty-core/jetty-compression
%pom_disable_module jetty-compression-client jetty-core/jetty-compression
%pom_disable_module jetty-ee-test-resources jetty-core/jetty-ee

%pom_disable_module jetty-ee11
%pom_disable_module jetty-ee10
%pom_disable_module jetty-ee8
%pom_disable_module jetty-demos
%pom_disable_module jetty-home
%pom_disable_module jetty-integrations
%pom_disable_module tests
%pom_disable_module documentation
%pom_disable_module jetty-p2

# Keep only the minimal EE9 chain needed for jetty-servlet compatibility.
%pom_disable_module jetty-ee9-annotations jetty-ee9
%pom_disable_module jetty-ee9-apache-jsp jetty-ee9
%pom_disable_module jetty-ee9-bom jetty-ee9
%pom_disable_module jetty-ee9-cdi jetty-ee9
%pom_disable_module jetty-ee9-demos jetty-ee9
%pom_disable_module jetty-ee9-fcgi-proxy jetty-ee9
%pom_disable_module jetty-ee9-glassfish-jstl jetty-ee9
%pom_disable_module jetty-ee9-home jetty-ee9
%pom_disable_module jetty-ee9-jaspi jetty-ee9
%pom_disable_module jetty-ee9-jndi jetty-ee9
%pom_disable_module jetty-ee9-jspc-maven-plugin jetty-ee9
%pom_disable_module jetty-ee9-maven-plugin jetty-ee9
%pom_disable_module jetty-ee9-openid jetty-ee9
%pom_disable_module jetty-ee9-osgi jetty-ee9
%pom_disable_module jetty-ee9-plus jetty-ee9
%pom_disable_module jetty-ee9-proxy jetty-ee9
%pom_disable_module jetty-ee9-quickstart jetty-ee9
%pom_disable_module jetty-ee9-servlets jetty-ee9
%pom_disable_module jetty-ee9-tests jetty-ee9
%pom_disable_module jetty-ee9-webapp jetty-ee9
%pom_disable_module jetty-ee9-websocket jetty-ee9

# Build against jakarta-servlet API available in the distro.
%pom_remove_dep -f org.eclipse.jetty.toolchain:jetty-jakarta-servlet-api jetty-ee9/jetty-ee9-nested/pom.xml
%pom_add_dep javax.servlet:javax.servlet-api:5.0.0 jetty-ee9/jetty-ee9-nested/pom.xml
sed -i 's/requires transitive jetty.servlet.api;/requires transitive jakarta.servlet;/' \
  jetty-ee9/jetty-ee9-nested/src/main/java/module-info.java

# Do not install aggregate parent POMs.
%mvn_package :jetty-project __noinstall
%mvn_package :jetty-core __noinstall
%mvn_package :jetty-alpn __noinstall
%mvn_package :jetty-http2 __noinstall
%mvn_package :jetty-compression __noinstall
%mvn_package :jetty-ee __noinstall
%mvn_package :jetty-ee9 __noinstall

%mvn_package :jetty-ee9-servlet servlet

%mvn_alias org.eclipse.jetty.ee9:jetty-ee9-servlet org.eclipse.jetty:jetty-servlet

%build
%mvn_build -s -j -f

%install
%mvn_install

%files
%doc --no-dereference README.md VERSION.txt LICENSE NOTICE.txt

%files util -f .mfiles-jetty-util
%files util-ajax -f .mfiles-jetty-util-ajax
%files jmx -f .mfiles-jetty-jmx
%files io -f .mfiles-jetty-io
%files http -f .mfiles-jetty-http
%files server -f .mfiles-jetty-server
%files security -f .mfiles-jetty-security
%files session -f .mfiles-jetty-session
%files alpn-client -f .mfiles-jetty-alpn-client
%files alpn-server -f .mfiles-jetty-alpn-server
%files alpn-java-client -f .mfiles-jetty-alpn-java-client
%files alpn-java-server -f .mfiles-jetty-alpn-java-server
%files client -f .mfiles-jetty-client
%files compression-common -f .mfiles-jetty-compression-common
%files compression-gzip -f .mfiles-jetty-compression-gzip
%files http2-hpack -f .mfiles-jetty-http2-hpack
%files http2-common -f .mfiles-jetty-http2-common
%files http2-client -f .mfiles-jetty-http2-client
%files http2-client-transport -f .mfiles-jetty-http2-client-transport
%files http2-server -f .mfiles-jetty-http2-server
%files ee-webapp -f .mfiles-jetty-ee-webapp
%files ee9-nested -f .mfiles-jetty-ee9-nested
%files ee9-security -f .mfiles-jetty-ee9-security
%files servlet -f .mfiles-servlet

%changelog
* Wed Apr 01 2026 Ivan Khanas <xeno@altlinux.org> 12.1.8-alt1
- New version.

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
