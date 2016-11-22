Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: perl(JSON.pm) perl(Net/LDAP/LDIF.pm) perl(POSIX.pm) perl(Sort/Versions.pm)
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apacheds-ldap-api
%define version 1.0.0
%global namedreltag -M33
%global namedversion %{version}%{?namedreltag}
Name:          apacheds-ldap-api
Version:       1.0.0
Release:       alt1_0.2.M33jpp8
Summary:       Apache Directory LDAP API
License:       ASL 2.0
Url:           http://directory.apache.org/api/
Source0:       http://www.apache.org/dist/directory/api/dist/%{namedversion}/apache-ldap-api-%{namedversion}-src.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(com.google.code.findbugs:annotations)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-pool:commons-pool)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.mina:mina-core)
BuildRequires: mvn(org.codehaus.mojo:antlr-maven-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(xpp3:xpp3)

%if 0
# Test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.directory.junit:junit-addons)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
%endif

BuildArch:     noarch
Source44: import.info

%description
The Apache Directory LDAP API is an ongoing effort to
provide an enhanced LDAP API, as a replacement for JNDI and
the existing LDAP API (jLdap and Mozilla LDAP API).

This is a schema aware API, with some convenient ways to
access a LDAP server. This API is not only targeting the
Apache Directory Server, but should work pristine with
any LDAP server.

It's also an extensible API: new Controls, schema elements and
network layer could be added or used in the near future. It
is also OSGi capable.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n apache-ldap-api-%{namedversion}-src
find . -name "*.class" -delete
find . -name "*.jar" -print -delete

# org.apache.directory.project:project:pom:34
%pom_remove_parent
%pom_remove_dep -r org.ops4j.pax.exam:
%pom_remove_dep -r org.ops4j.pax.url:

%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin -r de.thetaphi:forbiddenapis

%pom_disable_module integ
%pom_disable_module integ-osgi
%pom_disable_module distribution

%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin

# org.osgi:org.osgi.core:6.0.0
%pom_change_dep -r org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi::provided
%pom_change_dep -r findbugs:annotations com.google.code.findbugs:annotations
# TODO add OSGi manifest to these artifacts
%pom_change_dep -r org.apache.servicemix.bundles:org.apache.servicemix.bundles.dom4j dom4j:dom4j
%pom_change_dep -r org.apache.servicemix.bundles:org.apache.servicemix.bundles.xpp3 xpp3:xpp3
%pom_remove_dep -r org.apache.servicemix.bundles:org.apache.servicemix.bundles.antlr
%pom_xpath_remove "pom:dependency[pom:artifactId = 'antlr']/pom:scope" ldap/model
%pom_xpath_remove "pom:dependency[pom:artifactId = 'antlr']/pom:scope" ldap/extras/aci

chmod 644 README.txt

%build
# No test dep org.apache.directory.junit:junit-addons:0.1
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.2.M33jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.1.M33jpp8
- new version

