BuildRequires: /proc
BuildRequires: jpackage-compat

Name:           async-http-client
Version:        1.7.14
Release:        alt1_1jpp7
Summary:        Asynchronous Http Client for Java

Group:          Development/Java
License:        ASL 2.0
URL:            https://github.com/AsyncHttpClient/%{name}
Source0:        https://github.com/AsyncHttpClient/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-release-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  sonatype-oss-parent
BuildRequires:  netty
Source44: import.info


%description
Async Http Client library purpose is to allow Java applications to
easily execute HTTP requests and asynchronously process the HTTP
responses. The Async HTTP Client library is simple to use.


%package javadoc
Summary:   API documentation for %{name}
Group:     Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Remove things for which we are missing dependencies
%pom_remove_plugin :clirr-maven-plugin
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-gitsite']]"
%pom_xpath_remove "pom:profiles/pom:profile[pom:id[text()='grizzly']]"

# Animal sniffer is causing more trouble than good
%pom_remove_plugin :animal-sniffer-maven-plugin


%build
# we don't have all test dependencies available so disable tests
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%doc README.md LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt


%changelog
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

