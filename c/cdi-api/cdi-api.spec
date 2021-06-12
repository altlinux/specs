Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname cdi

Name:           cdi-api
Version:        2.0
Release:        alt1_2jpp11
Summary:        Contexts and Dependency Injection API
License:        ASL 2.0

URL:            https://github.com/eclipse-ee4j/cdi
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.interceptor:jakarta.interceptor-api)
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jboss.weld:weld-parent:pom:)
BuildRequires:  mvn(org.testng:testng)
Source44: import.info

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{version}


# do not build specification documentation
%pom_disable_module spec

# do not install useless parent POM
%mvn_package javax.enterprise:cdi-spec __noinstall

# use new jakarta interceptors coordinates
%pom_change_dep :javax.interceptor-api jakarta.interceptor:jakarta.interceptor-api api


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference spec/src/main/asciidoc/license-asl2.asciidoc
%doc --no-dereference spec/src/main/asciidoc/license-jcp-final.asciidoc
%doc spec/src/main/asciidoc/cdi-spec.asciidoc

%files javadoc -f .mfiles-javadoc
%doc --no-dereference spec/src/main/asciidoc/license-asl2.asciidoc
%doc --no-dereference spec/src/main/asciidoc/license-jcp-final.asciidoc


%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.0-alt1_2jpp11
- new version

* Mon May 31 2021 Igor Vlasenko <viy@altlinux.org> 1.2-alt2_12jpp8
- build w/o asciidoc (python2)

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_12jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9jpp8
- fc29 update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8jpp8
- java fc28+ update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_6jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp8
- new jpp release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_13jpp8
- added osgi provides

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12jpp8
- fixed osgi provides

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_12jpp8
- added osgi provides

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_11jpp8
- java 8 mass update

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9.SP4jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6.SP4jpp7
- fc update

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4.SP4jpp7
- new version

