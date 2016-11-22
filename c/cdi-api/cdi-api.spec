Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cdi-api
%define version 1.1
%global namedreltag .NOTHING
%global namedversion %{version}%{?namedreltag}

Name:             cdi-api
Version:          1.1
Release:          alt2_13jpp8
Summary:          CDI API
License:          ASL 2.0
URL:              http://seamframework.org/Weld
Source0:          https://github.com/cdi-spec/cdi/archive/%{version}.tar.gz

BuildArch:        noarch
BuildRequires:    maven-local
# geronimo-annotation
BuildRequires:    mvn(javax.annotation:jsr250-api)
BuildRequires:    mvn(javax.el:javax.el-api)
BuildRequires:    mvn(javax.inject:javax.inject)
BuildRequires:    mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires:    mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:    mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires:    mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires:    mvn(org.jboss.weld:weld-parent:pom:)
BuildRequires:    mvn(org.testng:testng::jdk15:)

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

# Generate OSGI info
%pom_xpath_set pom:project/pom:packaging bundle api
%pom_xpath_inject "pom:project" "
    <build>
      <plugins>
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <_nouses>true</_nouses>
              <Export-Package>javax.decorator.*;javax.enterprise.context.*;javax.enterprise.event.*;javax.enterprise.inject.*;javax.enterprise.util.*</Export-Package>
            </instructions>
          </configuration>
        </plugin>
      </plugins>
    </build>" api

%pom_xpath_set "pom:dependency[pom:groupId = 'javax.el']/pom:artifactId" javax.el-api api

cd api
# J2EE API directory
%mvn_file :{cdi-api} %{name}/@1 javax.enterprise.inject/@1

# Use newer version of interceptors API
%pom_remove_dep "org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.1_spec"
%pom_add_dep "org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec"

%build
cd api
%mvn_build -- -Denforcer.skip

%install
cd api
%mvn_install

build-jar-repository %{buildroot}%{_javadir}/javax.enterprise.inject/ \
                     jboss-interceptors-1.2-api geronimo-annotation javax.inject

%files -f api/.mfiles
%dir %{_javadir}/%{name}
%{_javadir}/javax.enterprise.inject/

%files javadoc -f api/.mfiles-javadoc

%changelog
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

