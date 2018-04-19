Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          rome
Version:       1.7.0
Release:       alt1_4jpp8
Summary:       RSS and Atom Utilities
License:       ASL 2.0
URL:           http://rometools.github.io/rome/
# Original source archive 73,8 MB
# sh rome-create-tarball.sh < VERSION >
# Repackaged source archive 575 KB
Source0:       %{name}-%{version}.tar.xz
Source1:       %{name}-create-tarball.sh

BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(commons-httpclient:commons-httpclient)
BuildRequires: mvn(javax.persistence:persistence-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.oauth.core:oauth)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.xmlrpc:xmlrpc-client)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.jdom:jdom2)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(xmlunit:xmlunit)

BuildArch:     noarch
Source44: import.info

%description
ROME is an set of open source Java tools for parsing, generating and
publishing RSS and Atom feeds.

%package certiorem
Group: Development/Java
Summary:       A PubSubHubub implementation for Java based on ROME

%description certiorem
PubSubHubub protocol implementation based on ROME.

%package fetcher
Group: Development/Java
Summary:       Retrieves RSS feeds via HTTP conditional gets using ROME

%description fetcher
ROME Fetcher is a caching feed fetcher that supports retrieval of
feeds via HTTP conditional GET. Supports ETags, GZip compression,
and RFC3229 Delta encoding.

%package modules
Group: Development/Java
Summary:       Plugin collection for the ROME RSS and Atom Utilities
# LGPL:
# rome-modules/src/main/java/com/rometools/modules/base/Course.java
# rome-modules/src/main/java/com/rometools/modules/base/CustomTagImpl.java
# rome-modules/src/main/java/com/rometools/modules/content/ContentItem.java
# rome-modules/src/main/java/com/rometools/modules/itunes/types/Duration.java
# rome-modules/src/main/java/com/rometools/modules/photocast/PhotocastModule.java
# rome-modules/src/main/java/com/rometools/modules/slash/Slash.java
# rome-modules/src/main/java/com/rometools/modules/yahooweather/YWeatherEntryModule.java
License:       ASL 2.0 and LGPLv2

%description modules
This module contains extensions that enable ROME to
handle several feed extensions like MediaRSS,
GeoRSS and others.

%package opml
Group: Development/Java
Summary:       Support for OPML 1 and OPML 2 in ROME

%description opml
This module contains Outline Processor Markup Language parser and tools.

#%%package parent
#Summary:       Parent for all ROME projects

#%%description parent
#Parent POM for all ROME projects.

%package propono
Group: Development/Java
Summary:       ROME Propono

%description propono
The ROME Propono sub-project is a Java class library that
supports publishing protocols, specifically the Atom Publishing Protocol
and the legacy MetaWeblog API. Propono includes an Atom client library,
Atom server framework and a Blog client that supports both Atom protocol
and the MetaWeblog API. 

%package utils
Group: Development/Java
Summary:       Utility classes for ROME projects

%description utils
This modules provides utility classes for all ROME projects.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

# Unneeded tasks
%pom_remove_plugin -r :maven-scm-publish-plugin

%pom_xpath_remove -r "pom:Embed-Dependency" %{name} %{name}-modules
%pom_xpath_remove "pom:Embed-Transitive" %{name}-modules

%pom_change_dep -r com.rometools: ::'${project.version}'

# Force servlet 3.1
%pom_change_dep -r :servlet-api javax.servlet:javax.servlet-api:3.1.0
sed -i "s|String, Object|String, String[]|" \
 %{name}-propono/src/main/java/com/rometools/propono/atom/server/AtomRequestImpl.java \
 %{name}-propono/src/main/java/com/rometools/propono/atom/server/AtomRequest.java

# com.google.inject.extensions:guice-servlet
%pom_disable_module rome-certiorem-webapp
# No test deps (contains only tests)
# org.ops4j.pax.exam:pax-exam-container-native:4.8.0
# org.ops4j.pax.exam:pax-exam-junit4:4.8.0
# org.ops4j.pax.exam:pax-exam-link-mvn:4.8.0
# org.ops4j.pax.url:pax-url-wrap:2.4.5
%pom_disable_module rome-osgi-test

# No test dep
# jetty:jetty:4.2.12
%pom_remove_dep -r jetty:jetty
rm %{name}-fetcher/src/test/java/com/rometools/fetcher/AbstractJettyTest.java \
 %{name}-fetcher/src/test/java/com/rometools/fetcher/impl/HttpClientFeedFetcherTest.java \
 %{name}-fetcher/src/test/java/com/rometools/fetcher/impl/HttpURLFeedFetcherTest.java \
 %{name}-propono/src/test/java/com/rometools/propono/atom/server/AtomClientServerTest.java \
 %{name}-propono/src/test/java/com/rometools/propono/atom/server/TestAtomHandlerImpl.java \
 %{name}-propono/src/test/java/com/rometools/propono/atom/server/TestAtomHandlerFactory.java

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' README.md
touch -r README.md.orig README.md
rm README.md.orig

# @ random fails: AssertionError
rm %{name}-modules/src/test/java/com/rometools/modules/cc/types/LicenseTest.java

%mvn_alias com.rometools:%{name} %{name}:%{name} net.java.dev.%{name}:%{name}
# Avoid problems with old rome-parent-1.5.0 package
%mvn_package :%{name}-parent %{name}

%build

%mvn_build -s 

%install
%mvn_install

%files -f .mfiles-%{name}
%files certiorem -f .mfiles-%{name}-certiorem
%files fetcher -f .mfiles-%{name}-fetcher
%files modules -f .mfiles-%{name}-modules
%files opml -f .mfiles-%{name}-opml

#%%files parent -f .mfiles-%%{name}-parent
#%%license LICENSE

%files propono -f .mfiles-%{name}-propono
%doc --no-dereference %{name}-propono/NOTICE

%files utils -f .mfiles-%{name}-utils
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_20jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_19jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_13jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3_12jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_12jpp7
- fc version

* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_7jpp6
- update to new release by jppimport

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_1jpp5
- fixed build

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1jpp5
- new version

