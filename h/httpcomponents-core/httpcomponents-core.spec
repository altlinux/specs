Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
# READ BEFORE UPDATING: After updating this package to new upstream
# version eclipse-ecf should be rebuilt.  For more info, see:
# https://fedoraproject.org/wiki/SIGs/Java#Package_Update.2FRebuild_Notes

%global base_name httpcomponents

Name:              httpcomponents-core
Summary:           Set of low level Java HTTP transport components for HTTP services
Version:           4.4.4
Release:           alt1_2jpp8
# The project is licensed under ASL 2.0, but it contains annotations
# in the package org.apache.http.annotation which are derived
# from JCIP-ANNOTATIONS project (CC-BY licensed)
License:           ASL 2.0 and CC-BY
URL:               http://hc.apache.org/
Source0:           http://www.apache.org/dist/httpcomponents/httpcore/source/httpcomponents-core-%{version}-src.tar.gz
BuildArch:         noarch

BuildRequires:     maven-local
BuildRequires:     httpcomponents-project
BuildRequires:     java >= 1.6.0
BuildRequires:     jpackage-utils
BuildRequires:     apache-commons-logging
BuildRequires:     junit
BuildRequires:     mvn(org.codehaus.mojo:build-helper-maven-plugin)
%if 0%{?fedora}
BuildRequires:     mockito
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

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q

%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin

# we don't need these artifacts right now
%pom_disable_module httpcore-osgi
%pom_disable_module httpcore-ab

# OSGify modules
for module in httpcore httpcore-nio; do
    %pom_xpath_remove "pom:project/pom:packaging" $module
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" $module
    %pom_xpath_inject "pom:build/pom:plugins" "
        <plugin>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <extensions>true</extensions>
          <configuration>
            <instructions>
              <Export-Package>*</Export-Package>
              <Private-Package></Private-Package>
              <_nouses>true</_nouses>
            </instructions>
          </configuration>
        </plugin>" $module
done

# install JARs to httpcomponents/ for compatibility reasons
# several other packages expect to find the JARs there
%mvn_file ":{*}" httpcomponents/@1

%build
%mvn_build %{!?fedora -f}

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/httpcomponents
%doc LICENSE.txt NOTICE.txt README.txt RELEASE_NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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

