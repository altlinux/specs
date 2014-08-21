# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name httpcomponents

Name:              httpcomponents-core
Summary:           Set of low level Java HTTP transport components for HTTP services
Version:           4.2.2
Release:           alt2_1jpp7
Group:             Development/Java
License:           ASL 2.0
URL:               http://hc.apache.org/
Source0:           http://www.apache.org/dist/httpcomponents/httpcore/source/httpcomponents-core-%{version}-src.tar.gz
BuildArch:         noarch

BuildRequires:     httpcomponents-project
BuildRequires:     jpackage-utils
BuildRequires:     maven-surefire-provider-junit4
BuildRequires:     apache-commons-logging
BuildRequires:     junit
%if 0%{?rhel} <= 0
BuildRequires:     mockito
%endif

Requires:          jpackage-utils
Requires:          apache-commons-logging
Requires:          junit
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
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q

%pom_remove_plugin :maven-clover2-plugin httpcore-nio
%pom_remove_plugin :maven-clover2-plugin httpcore
%pom_remove_plugin :maven-notice-plugin
%pom_remove_plugin :docbkx-maven-plugin

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
            </instructions>
          </configuration>
        </plugin>" $module
done

%build
mvn-rpmbuild \
%if 0%{?rhel}
    -Dmaven.test.skip=true \
%endif
    install javadoc:aggregate

%install
install -dm 755 %{buildroot}/%{_mavenpomdir}
install -dm 755 %{buildroot}/%{_javadir}/%{base_name}

for m in httpcore httpcore-nio; do
    # poms
    install -pm 644 $m/pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-$m.pom

    # jars - osgi doesn't have one
    if [ -f $m/target/$m-%{version}.jar ];then
        install -m 644 $m/target/$m-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/$m.jar
    fi

    %add_maven_depmap JPP.%{base_name}-$m.pom %{base_name}/$m.jar
done

# parent
install -pm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-%{name}.pom
%add_maven_depmap JPP.%{base_name}-%{name}.pom

# javadocs
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt NOTICE.txt
%doc README.txt RELEASE_NOTES.txt
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{base_name}*.pom
%{_javadir}/%{base_name}

%files javadoc
%doc LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

%changelog
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

