Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:              httpcomponents-client
Summary:           HTTP agent implementation based on httpcomponents HttpCore
Version:           4.5.13
Release:           alt1_2jpp11
License:           ASL 2.0
URL:               http://hc.apache.org/
Source0:           https://www.apache.org/dist/httpcomponents/httpclient/source/%{name}-%{version}-src.tar.gz
BuildArch:         noarch

Patch0:            0001-Use-system-copy-of-effective_tld_names.dat.patch
Patch1:            0002-Port-to-mockito-2.patch

BuildRequires:     maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:     mvn(commons-codec:commons-codec)
BuildRequires:     mvn(commons-logging:commons-logging)
BuildRequires:     mvn(junit:junit)
BuildRequires:     mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:     mvn(org.apache.httpcomponents:httpcomponents-parent:pom:)
BuildRequires:     mvn(org.apache.httpcomponents:httpcore)
BuildRequires:     mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:     mvn(org.mockito:mockito-core)
%endif

%if %{without bootstrap}
BuildRequires:     publicsuffix-list
%endif
Requires:          publicsuffix-list
Source44: import.info

Obsoletes: hc-httpclient < 4.1.1
Provides: hc-httpclient = %version

%description
HttpClient is a HTTP/1.1 compliant HTTP agent implementation based on
httpcomponents HttpCore. It also provides reusable components for
client-side authentication, HTTP state management, and HTTP connection
management. HttpComponents Client is a successor of and replacement
for Commons HttpClient 3.x. Users of Commons HttpClient are strongly
encouraged to upgrade.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%mvn_package :::tests: __noinstall

# Change scope of commons-logging to provided
%pom_change_dep :commons-logging :::provided httpclient

# Remove optional build deps not available in Fedora
%pom_disable_module httpclient-osgi
%pom_disable_module httpclient-win
%pom_disable_module fluent-hc
%pom_disable_module httpmime
%pom_disable_module httpclient-cache
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

# Fails due to strict crypto policy - uses DSA in test data
rm httpclient/src/test/java/org/apache/http/conn/ssl/TestSSLSocketFactory.java

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

# requires network
rm httpclient/src/test/java/org/apache/http/client/config/TestRequestConfig.java

%build
%mvn_file ":{*}" httpcomponents/@1

%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -n %{?module_prefix}%{name} -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc README.txt RELEASE_NOTES.txt

%changelog
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

