BuildRequires: mvn(com.google.guava:guava)
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 28
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora}
%bcond_with dnplugin
%endif

Name:          google-oauth-java-client
Version:       1.22.0
Release:       alt1_3jpp8
Summary:       Google OAuth Client Library for Java
License:       ASL 2.0
URL:           https://github.com/google/google-oauth-java-client
Source0:       https://github.com/google/google-oauth-java-client/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.http-client:google-http-client)
BuildRequires: mvn(com.google.http-client:google-http-client-jackson)
BuildRequires: mvn(com.google.http-client:google-http-client-jdo)
BuildRequires: mvn(javax.jdo:jdo2-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(mysql:mysql-connector-java)
BuildRequires: mvn(org.datanucleus:datanucleus-core)
BuildRequires: mvn(org.datanucleus:datanucleus-api-jdo)
BuildRequires: mvn(org.datanucleus:datanucleus-rdbms)
%if %{with dnplugin}
BuildRequires: mvn(org.datanucleus:datanucleus-maven-plugin)
%endif
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Google OAuth Client Library for Java. Functionality that
works on all supported Java platforms, including Java 5
(or higher) desktop (SE) and web (EE), Android, and
Google App Engine.

%package java6
Group: Development/Java
Summary:       Google OAuth Client Java 6 extensions

%description java6
Java 6 (and higher) extensions to the
Google OAuth Client Library for Java.

%package parent
Group: Development/Java
Summary:       Google OAuth Client Parent POM

%description parent
Parent POM for the Google OAuth Client Library for Java.

%package servlet
Group: Development/Java
Summary:       Google OAuth Client Servlet and JDO extensions

%description servlet
Servlet and JDO extensions to the
Google OAuth Client Library for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :clirr-maven-plugin
%pom_remove_plugin -r :findbugs-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-source-plugin
# duplicate declaration
%pom_remove_plugin -r :maven-release-plugin

%pom_disable_module google-oauth-client-assembly
# com.google.appengine:appengine-{api-1.0-sdk,testing,api-stubs}:1.7.7
%pom_disable_module google-oauth-client-appengine

# org.mortbay.jetty:jetty
%pom_disable_module google-oauth-client-jetty

%pom_disable_module samples/dailymotion-cmdline-sample

%pom_change_dep -r :guava-jdk5 :guava
%pom_change_dep -r :servlet-api :javax.servlet-api:3.1.0

%if %{without dnplugin}
%pom_remove_plugin org.datanucleus:maven-datanucleus-plugin google-oauth-client-servlet
%else
# Generate:
# ENHANCED (PersistenceCapable) : com.google.api.client.extensions.auth.helpers.oauth.OAuthHmacThreeLeggedFlow
# ENHANCED (PersistenceCapable) : com.google.api.client.extensions.auth.helpers.oauth.OAuthHmacCredential
# Upgrade datanucleus-maven-plugin refs
%pom_xpath_set "pom:plugin[pom:groupId='org.datanucleus']/pom:artifactId" datanucleus-maven-plugin google-oauth-client-servlet
# Fix datanucleus-maven-plugin runtime deps
# Error: Could not find or load main class org.datanucleus.enhancer.DataNucleusEnhancer
%pom_xpath_inject "pom:plugin[pom:groupId='org.datanucleus']" "
<dependencies>
    <dependency>
      <groupId>org.datanucleus</groupId>
      <artifactId>datanucleus-core</artifactId>
      <version>3.2.9</version>
    </dependency>
    <dependency>
      <groupId>org.datanucleus</groupId>
      <artifactId>datanucleus-api-jdo</artifactId>
      <version>3.2.6</version>
    </dependency>
</dependencies>" google-oauth-client-servlet
# Class "com.google.api.client.extensions.auth.helpers.oauth.OAuthHmacThreeLeggedFlow"
# field "authorizationUrl" : marked as persistent yet is final so cannot be persisted
#sed -i "s|private final String authorizationUrl;|private String authorizationUrl;|" \
# google-oauth-client-servlet/src/main/java/com/google/api/client/extensions/auth/helpers/oauth/OAuthHmacThreeLeggedFlow.java
%endif

%pom_xpath_remove -r "pom:plugin[pom:artifactId ='maven-jar-plugin']/pom:executions"

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-google-oauth-client
%doc README.md
%doc --no-dereference LICENSE

%files java6 -f .mfiles-google-oauth-client-java6

%files parent -f .mfiles-google-oauth-client-parent
%doc --no-dereference LICENSE

%files servlet -f .mfiles-google-oauth-client-servlet

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.22.0-alt1_3jpp8
- new version

