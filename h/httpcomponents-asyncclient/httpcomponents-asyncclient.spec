Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          httpcomponents-asyncclient
Version:       4.1.2
Release:       alt2_3jpp8
Summary:       Apache components to build asynchronous client side HTTP services
License:       ASL 2.0
URL:           http://hc.apache.org/
Source0:       http://www.apache.org/dist/httpcomponents/httpasyncclient/source/%{name}-%{version}-src.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.httpcomponents:httpclient-cache)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.httpcomponents:httpcore)
BuildRequires: mvn(org.apache.httpcomponents:httpcore-nio)
BuildRequires: mvn(org.apache.httpcomponents:project:pom:)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.mockito:mockito-core)

BuildArch:     noarch
Source44: import.info

%description
Asynch HttpClient is a HTTP/1.1 compliant HTTP agent implementation based on
HttpCore NIO and HttpClient components. It is a complementary module to
Apache HttpClient intended for special cases where ability to handle
a great number of concurrent connections is more important than performance
in terms of a raw data throughput.

%package cache
Group: Development/Java
Summary:       Apache HttpAsyncClient Cache

%description cache
This package provides client side caching for %{name}.

%package parent
Group: Development/Java
Summary:       Apache HttpAsyncClient Parent POM

%description parent
Apache HttpAsyncClient Parent POM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
# Cleanup
find . -name "*.class" -delete
find . -name "*.jar" -type f -delete

# Use unavalable org.apache.httpcomponents:hc-stylecheck:jar:1
%pom_remove_plugin :maven-checkstyle-plugin
# Unwanted
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
# Unavalable
%pom_remove_plugin :clirr-maven-plugin

%pom_disable_module httpasyncclient-osgi

# Prevent build failure
%pom_remove_plugin -r :apache-rat-plugin

# Unavalable test deps: org.easymock:easymockclassextension org.apache.httpcomponents:httpclient-cache:test-jar
%pom_xpath_remove "pom:dependency[pom:type = 'test-jar']" httpasyncclient-cache
%pom_xpath_remove "pom:dependency[pom:scope = 'test']" httpasyncclient-cache
rm -r httpasyncclient-cache/src/test/java

# Add OSGi support
for p in httpasyncclient httpasyncclient-cache; do
 %pom_xpath_set "pom:project/pom:packaging" bundle ${p}
 %pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 ${p} "
 <extensions>true</extensions>
 <configuration>
  <instructions>
    <Export-Package>*</Export-Package>
  </instructions>
  <excludeDependencies>true</excludeDependencies>
 </configuration>"
done

%mvn_file org.apache.httpcomponents:httpasyncclient httpasyncclient
%mvn_file org.apache.httpcomponents:httpasyncclient-cache httpasyncclient-cache

%build

%mvn_build -s -- -Dmaven.test.skip.exec=true  -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-httpasyncclient
%doc README.txt RELEASE_NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files cache -f .mfiles-httpasyncclient-cache
%doc LICENSE.txt NOTICE.txt

%files parent -f .mfiles-%{name}
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2_3jpp8
- fixed build

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_4jpp8
- new fc release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_2jpp8
- new version

