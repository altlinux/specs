Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           httpcomponents-core
Summary:        Set of low level Java HTTP transport components for HTTP services
Version:        4.4.13
Release:        alt1_4jpp11
License:        ASL 2.0
URL:            http://hc.apache.org/
Source0:        https://www.apache.org/dist/httpcomponents/httpcore/source/httpcomponents-core-%{version}-src.tar.gz
Patch0:         0001-Port-to-mockito-2.patch

BuildArch:      noarch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.httpcomponents:httpcomponents-parent:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
Source44: import.info

Obsoletes: hc-httpcore < 4.1.1
Provides: hc-httpcore = %version

%description
HttpCore is a set of low level HTTP transport components that can be
used to build custom client and server side HTTP services with a
minimal footprint. HttpCore supports two I/O models: blocking I/O
model based on the classic Java I/O and non-blocking, event driven I/O
model based on Java NIO.

The blocking I/O model may be more appropriate for data intensive, low
latency scenarios, whereas the non-blocking model may be more
appropriate for high latency scenarios where raw data throughput is
less important than the ability to handle thousands of simultaneous
HTTP connections in a resource efficient manner.

%{?javadoc_package}

%prep
%setup -q
%patch0 -p1

# Random test failures on ARM -- 100 ms sleep is not eneough on this
# very performant arch, lets make it 2 s
sed -i '/Thread.sleep/s/100/2000/' httpcore-nio/src/test/java/org/apache/http/nio/integration/TestHttpAsyncHandlers.java

%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

# We don't have conscrypt for testing
%pom_remove_dep :conscrypt-openjdk-uber httpcore-nio
rm httpcore-nio/src/test/java/org/apache/http/nio/integration/TestJSSEProviderIntegration.java

# we don't need these artifacts right now
%pom_disable_module httpcore-osgi
%pom_disable_module httpcore-ab

# OSGify modules
for module in httpcore httpcore-nio; do
    %pom_xpath_remove "pom:project/pom:packaging" $module
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" $module
    %pom_remove_plugin :maven-jar-plugin $module
    %pom_xpath_inject "pom:build/pom:plugins" "
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <Export-Package>*</Export-Package>
              <Private-Package></Private-Package>
              <Automatic-Module-Name>org.apache.httpcomponents.$module</Automatic-Module-Name>
              <_nouses>true</_nouses>
            </instructions>
          </configuration>
        </plugin>" $module
done

# install JARs to httpcomponents/ for compatibility reasons
# several other packages expect to find the JARs there
%mvn_file ":{*}" httpcomponents/@1

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc README.txt RELEASE_NOTES.txt

%changelog
* Wed Aug 18 2021 Igor Vlasenko <viy@altlinux.org> 4.4.13-alt1_4jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 4.4.12-alt2_4jpp11
- fixed build

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 4.4.12-alt1_2jpp11
- new version

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 4.4.10-alt1_5jpp8
- build with new mockito

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.4.10-alt1_3jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 4.4.9-alt1_4jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.4.8-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 4.4.6-alt1_4jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.4.6-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.4.5-alt1_2jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 4.4.4-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 4.4.1-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.4-alt1_5jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.4-alt1_3jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt2_1jpp7
- added maven-local BR:

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1_1jpp7
- new release

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_3jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_2jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

