Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.2
%global namedreltag .NOTHING
%global namedversion %{version}%{?namedreltag}

Name:             cdi-api
Version:          1.2
Release:          alt1_4jpp8
Summary:          CDI API
License:          ASL 2.0
URL:              http://seamframework.org/Weld
Source0:          https://github.com/cdi-spec/cdi/archive/%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    asciidoc asciidoc-a2x
BuildRequires:    maven-local
BuildRequires:    mvn(javax.el:javax.el-api)
BuildRequires:    mvn(javax.inject:javax.inject)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires:    mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:    mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires:    mvn(org.jboss.weld:weld-parent:pom:)
BuildRequires:    mvn(org.testng:testng::jdk15:)
BuildRequires:    /usr/bin/pygmentize

Provides:         javax.enterprise.inject
Source44: import.info

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n cdi-%{version}

cd api
# J2EE API directory
%mvn_file :{cdi-api} %{name}/@1 javax.enterprise.inject/@1

# Use newer version of interceptors API
%pom_change_dep "javax.interceptor:javax.interceptor-api" "org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec"

%build

(
 cd api
 %mvn_build -- -Denforcer.skip
)

cd spec/src/main/doc
asciidoc -n -b html5 -a toc2 -a toclevels=3 -a pygments -f html5.conf -o ../../../../cdi-spec.html cdi-spec.asciidoc
asciidoc -n -b html5 -a toc2 -a toclevels=3 -a pygments -f html5.conf -o ../../../../license-asl2.html license-asl2.asciidoc
asciidoc -n -b html5 -a toc2 -a toclevels=3 -a pygments -f html5.conf -o ../../../../license-jcp.html license-jcp.asciidoc

%install
cd api
%mvn_install

build-jar-repository %{buildroot}%{_javadir}/javax.enterprise.inject/ \
                     jboss-interceptors-1.2-api glassfish-el-api javax.inject

%files -f api/.mfiles
%{_javadir}/javax.enterprise.inject/
%doc cdi-spec.html
%doc license-asl2.html license-jcp.html

%files javadoc -f api/.mfiles-javadoc
%doc license-asl2.html license-jcp.html

%changelog
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

