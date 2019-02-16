Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without     memcached
%bcond_without     ehcache

Name:              httpcomponents-client
Summary:           HTTP agent implementation based on httpcomponents HttpCore
Version:           4.5.5
Release:           alt1_5jpp8
License:           ASL 2.0
URL:               http://hc.apache.org/
Source0:           http://www.apache.org/dist/httpcomponents/httpclient/source/%{name}-%{version}-src.tar.gz

Patch0:            0001-Use-system-copy-of-effective_tld_names.dat.patch

BuildArch:         noarch

BuildRequires:     maven-local
BuildRequires:     mvn(commons-codec:commons-codec)
BuildRequires:     mvn(commons-logging:commons-logging)
BuildRequires:     mvn(junit:junit)
%if %{with ehcache}
BuildRequires:     mvn(net.sf.ehcache:ehcache-core)
%endif
%if %{with memcached}
BuildRequires:     mvn(net.spy:spymemcached)
%endif
BuildRequires:     mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:     mvn(org.apache.httpcomponents:httpcore)
BuildRequires:     mvn(org.apache.httpcomponents:project:pom:)
BuildRequires:     mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:     mvn(org.easymock:easymock)
BuildRequires:     mvn(org.mockito:mockito-core)

BuildRequires:     publicsuffix-list
Requires:          publicsuffix-list

Obsoletes:         %{name}-tests < 4.4
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

%package        cache
Group: Development/Java
Summary:        Cache module for %{name}

%description    cache
This package provides client side caching for %{name}.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%mvn_package :httpclient-cache cache

# Remove optional build deps not available in Fedora
%pom_disable_module httpclient-osgi
%pom_disable_module httpclient-win
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

# Fails due to strict crypto policy - uses DSA in test data
rm httpclient/src/test/java/org/apache/http/conn/ssl/TestSSLSocketFactory.java

# Don't compile/run httpclient-cache tests - they are incompatible with EasyMock 3.3
%pom_remove_plugin org.apache.maven.plugins:maven-jar-plugin httpclient-cache
%pom_remove_dep org.easymock:easymockclassextension
for dep in org.easymock:easymockclassextension org.slf4j:slf4j-jcl; do
    %pom_remove_dep $dep httpclient-cache
done
rm -rf httpclient-cache/src/test

%pom_remove_plugin :download-maven-plugin httpclient

# Add proper Apache felix bundle plugin instructions
# so that we get a reasonable OSGi manifest.
for module in httpclient httpmime httpclient-cache fluent-hc; do
    %pom_xpath_remove "pom:project/pom:packaging" $module
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" $module
done

# Make fluent-hc into bundle
%pom_xpath_inject pom:build "
<plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
    </plugin>
</plugins>" fluent-hc

# Make httpmime into bundle
%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
    </plugin>" httpmime

# Make httpclient into bundle
%pom_xpath_inject pom:reporting/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions>
          <Export-Package>*</Export-Package>
          <Private-Package></Private-Package>
          <Import-Package>!org.apache.avalon.framework.logger,!org.apache.log,!org.apache.log4j,*</Import-Package>
        </instructions>
      </configuration>
    </plugin>" httpclient
%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Export-Package>org.apache.http.*,!org.apache.http.param</Export-Package>
          <Private-Package></Private-Package>
          <_nouses>true</_nouses>
          <Import-Package>!org.apache.avalon.framework.logger,!org.apache.log,!org.apache.log4j,*</Import-Package>
        </instructions>
        <excludeDependencies>true</excludeDependencies>
      </configuration>
    </plugin>" httpclient

# Make httpclient-cache into bundle
%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Export-Package>*</Export-Package>
          <Import-Package>net.sf.ehcache;resolution:=optional,net.spy.memcached;resolution:=optional,*</Import-Package>
          <Private-Package></Private-Package>
          <_nouses>true</_nouses>
        </instructions>
        <excludeDependencies>true</excludeDependencies>
      </configuration>
    </plugin>" httpclient-cache

# requires network
rm httpclient/src/test/java/org/apache/http/client/config/TestRequestConfig.java

%if %{without memcached}
rm -r httpclient-cache/src/*/java/org/apache/http/impl/client/cache/memcached
%pom_remove_dep :spymemcached httpclient-cache
%endif
%if %{without ehcache}
rm -r httpclient-cache/src/*/java/org/apache/http/impl/client/cache/ehcache
%pom_remove_dep :ehcache-core httpclient-cache
%endif

%build
%mvn_file ":{*}" httpcomponents/@1

%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt RELEASE_NOTES.txt

%files cache -f .mfiles-cache

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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

