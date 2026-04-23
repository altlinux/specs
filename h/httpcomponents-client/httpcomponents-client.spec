Name:            httpcomponents-client
Version:         4.5.14
Release:         alt2

Summary:         HTTP agent implementation based on httpcomponents HttpCore
License:         Apache-2.0
Group:           Development/Java
URL:             http://hc.apache.org/
VCS:             https://github.com/apache/httpcomponents-client

Source0:         %name-%version-src.tar.gz

Patch0:          0001-Use-system-copy-of-effective_tld_names.dat.patch
Patch1:          0002-Port-to-mockito-2.patch
Patch2:          0003-Port-to-Mockito-5.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.httpcomponents:httpcomponents-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(commons-logging:commons-logging)

BuildArch:      noarch

Requires:       publicsuffix-list

%description
HttpClient is a HTTP/1.1 compliant HTTP agent implementation based on
httpcomponents HttpCore. It also provides reusable components for
client-side authentication, HTTP state management, and HTTP connection
management. HttpComponents Client is a successor of and replacement
for Commons HttpClient 3.x. Users of Commons HttpClient are strongly
encouraged to upgrade.

%javadoc_package

%package -n     fluent-hc
Summary:        Apache HttpClient Fluent API
Group:          Development/Java

%description -n fluent-hc
Apache HttpComponents Client fluent API.

%package -n     httpmime
Summary:        Apache HttpClient Mime
Group:          Development/Java

%description -n httpmime
Apache HttpComponents HttpClient - MIME coded entities.

%prep
%setup -n %name-%version
%autopatch -p1

%mvn_package :::tests: __noinstall

# Change scope of commons-logging to provided
%pom_change_dep :commons-logging :::provided httpclient

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :download-maven-plugin httpclient

%pom_xpath_inject "pom:archive" "
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>"

%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <executions>
        <execution>
          <id>bundle-manifest</id>
          <phase>process-classes</phase>
          <goals>
            <goal>manifest</goal>
          </goals>
        </execution>
      </executions>
    </plugin>"

%pom_xpath_inject pom:build "
<pluginManagement>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions>
          <Export-Package>org.apache.http.*,!org.apache.http.param</Export-Package>
          <Private-Package></Private-Package>
          <_nouses>true</_nouses>
          <Import-Package>!org.apache.avalon.framework.logger,!org.apache.log,!org.apache.log4j,*</Import-Package>
        </instructions>
        <excludeDependencies>true</excludeDependencies>
      </configuration>
    </plugin>
  </plugins>
</pluginManagement>
" httpclient

# Fails due to strict crypto policy - uses DSA in test data
rm httpclient/src/test/java/org/apache/http/conn/ssl/TestSSLSocketFactory.java
# requires network
rm httpclient/src/test/java/org/apache/http/client/config/TestRequestConfig.java

# requires ehcache
%pom_disable_module httpclient-cache
# no need
%pom_disable_module httpclient-win
%pom_disable_module httpclient-osgi

%mvn_package :fluent-hc fluent-hc
%mvn_package :httpmime httpmime

%mvn_file ":{*}" httpcomponents/@1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt
%doc README.txt RELEASE_NOTES.txt

%files -n fluent-hc -f .mfiles-fluent-hc
%files -n httpmime -f .mfiles-httpmime

%changelog
* Tue Apr 21 2026 Evgeniy Serov <scala@altlinux.org> 4.5.14-alt2
- Re-enabled modules (fluent-hc, httpmime).

* Wed Mar 04 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 4.5.14-alt1
- fixed FTBFS: new version
- added patch to fix tests with Mockito (thx CentOS Stream)

* Wed Aug 18 2021 Igor Vlasenko <viy@altlinux.org> 4.5.13-alt1_2jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 4.5.10-alt2_6jpp11
- fc34 update

* Tue May 25 2021 Igor Vlasenko <viy@altlinux.org> 4.5.10-alt2_2jpp11
- set compiler.release to 8 thanks to slev@

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 4.5.10-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 4.5.7-alt1_3jpp8
- update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.7-alt1_1jpp8
- new version

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.6-alt1_3jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 4.5.5-alt1_5jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 4.5.5-alt1_4jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 4.5.3-alt1_4jpp8
- new version

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.2-alt1_4jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.2-alt1_2jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.5-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.5-alt1_3jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.5-alt1_1jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt3_3jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_3jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_1jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

