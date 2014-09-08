Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:           async-http-client
Version:        1.7.19
Release:        alt1_1jpp7
Summary:        Asynchronous Http Client for Java

License:        ASL 2.0
URL:            https://github.com/AsyncHttpClient/%{name}
Source0:        https://github.com/AsyncHttpClient/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(io.netty:netty)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
# Test dependencies
BuildRequires:  mvn(commons-fileupload:commons-fileupload)
Source44: import.info


%description
Async Http Client library purpose is to allow Java applications to
easily execute HTTP requests and asynchronously process the HTTP
responses. The Async HTTP Client library is simple to use.


%package javadoc
Group: Development/Java
Summary:   API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Remove test deps
%pom_remove_dep ch.qos.logback:logback-classic
%pom_remove_dep org.eclipse.jetty:jetty-websocket
%pom_remove_dep org.eclipse.jetty:jetty-servlets
%pom_remove_dep org.eclipse.jetty:jetty-server
%pom_remove_dep org.eclipse.jetty:jetty-servlet
%pom_remove_dep org.eclipse.jetty:jetty-security
%pom_remove_dep org.apache.tomcat:coyote
%pom_remove_dep org.apache.tomcat:catalina

# Remove tests that we can't build because of missing dependencies
# Some tests require jetty 8 or tomcat 6
rm -Rf src/test/java/com/ning/http/client/async
rm -Rf src/test/java/com/ning/http/client/websocket

# Remove things for which we are missing dependencies
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-gitsite']]"
%pom_xpath_remove "pom:profiles/pom:profile[pom:id[text()='grizzly']]"

# Animal sniffer is causing more trouble than good
%pom_remove_plugin :animal-sniffer-maven-plugin

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc README.md LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt


%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.19-alt1_1jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.14-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt3_4jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

