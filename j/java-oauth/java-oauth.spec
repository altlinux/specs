Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname oauth
Name:          java-oauth
Version:       20100601
Release:       alt2_12jpp8
Summary:       An open protocol to allow API authentication
License:       ASL 2.0
Url:           http://code.google.com/p/oauth/
# svn export http://oauth.googlecode.com/svn/code/java oauth-20100601
# find oauth-20100601 -name "*.bat" -delete
# find oauth-20100601 -name "*.class" -delete
# find oauth-20100601 -name "*.jar" -delete
# tar czf oauth-20100601-clean-src-svn.tar.gz oauth-20100601
Source0:       oauth-20100601-clean-src-svn.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-httpclient:commons-httpclient)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)

BuildArch:     noarch
Source44: import.info

%description
An open protocol to allow API authentication
in a simple and standard method from desktop and
web applications.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

%pom_remove_plugin :maven-source-plugin

%pom_disable_module core-old
%pom_disable_module example
%pom_disable_module test core
# jetty-embedded:6.1.11
%pom_remove_dep org.mortbay.jetty: core/httpclient4
%pom_remove_dep org.mortbay.jetty: core/test

%pom_xpath_set "pom:dependency[pom:groupId = 'javax.servlet']/pom:version" 3.1.0 core/provider
%pom_xpath_set "pom:dependency[pom:groupId = 'javax.servlet']/pom:artifactId" javax.servlet-api core/provider

%mvn_file :%{oname} %{oname}/%{oname}
%mvn_file :%{oname}-consumer %{oname}/%{oname}-consumer
%mvn_file :%{oname}-httpclient3 %{oname}/%{oname}-httpclient3
%mvn_file :%{oname}-httpclient4 %{oname}/%{oname}-httpclient4
%mvn_file :%{oname}-provider %{oname}/%{oname}-provider

%build

# unavailable test deps
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 20100601-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 20100601-alt1_3jpp7
- new version

