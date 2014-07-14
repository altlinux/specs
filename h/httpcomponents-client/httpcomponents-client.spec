BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name httpcomponents

Name:              httpcomponents-client
Summary:           HTTP agent implementation based on httpcomponents HttpCore
Version:           4.2.1
Release:           alt2_3jpp7
Group:             Development/Java
License:           ASL 2.0
URL:               http://hc.apache.org/
Source0:           http://www.apache.org/dist/httpcomponents/httpclient/source/httpcomponents-client-%{version}-src.tar.gz

BuildArch:         noarch

BuildRequires:     httpcomponents-project
BuildRequires:     httpcomponents-core
BuildRequires:     apache-mime4j
BuildRequires:     apache-commons-codec

Requires:          jpackage-utils
Requires:          httpcomponents-core
Requires:          apache-mime4j
Requires:          apache-commons-codec
Source44: import.info

Obsoletes: hc-httpclient < 4.1.1
Provides: hc-httpclient = %version

%description
HttpClient is a HTTP/1.1 compliant HTTP agent implementation based on
httpcomponents HttpCore. It also provides reusable components for
client-side authentication, HTTP state management, and HTTP connection
management. HttpComponents Client is a successor of and replacement
for Commons HttpClient 3.x. Users of Commons HttpClient are strongly
encouraged to upgrade.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q

# Remove optional build deps not available in Fedora
%pom_disable_module httpclient-cache
%pom_disable_module httpclient-osgi
%pom_remove_dep :mockito-core httpclient
%pom_remove_plugin :maven-notice-plugin
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :maven-clover2-plugin httpclient

# Add proper Apache felix bundle plugin instructions
# so that we get a reasonable OSGi manifest.
for module in httpclient httpmime; do
    %pom_xpath_remove "pom:project/pom:packaging" $module
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" $module
done

# Make httpmime into bundle
%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
    </plugin>" httpmime

# Make httpclient into bundle
%pom_xpath_inject pom:reporting/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <configuration>
        <instructions>
          <Export-Package>*</Export-Package>
          <Private-Package></Private-Package>
          <Import-Package>!org.apache.avalon.framework.logger,!org.apache.log,!org.apache.log4j,*</Import-Package>
        </instructions>
      </configuration>
    </plugin>" httpclient
%pom_xpath_inject pom:build/pom:plugins "
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Export-Package>org.apache.http.*,!org.apache.http.param</Export-Package>
          <Private-Package></Private-Package>
          <_nouses>true</_nouses>
          <Import-Package>!org.apache.avalon.framework.logger,!org.apache.log,!org.apache.log4j,*</Import-Package>
        </instructions>
        <excludeDependencies>true</excludeDependencies>
      </configuration>
    </plugin>" httpclient


%build
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
# jars
install -dm 755 %{buildroot}%{_javadir}/%{base_name}
install -m 644 httpclient/target/httpclient-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/httpclient.jar
install -m 644 httpmime/target/httpmime-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/httpmime.jar

# main pom
install -dm 755 %{buildroot}/%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-httpcomponents-client.pom
%add_maven_depmap JPP.%{base_name}-httpcomponents-client.pom

# pom
install -pm 644 httpclient/pom.xml \
    %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-httpclient.pom
%add_maven_depmap JPP.%{base_name}-httpclient.pom %{base_name}/httpclient.jar

install -pm 644 httpmime/pom.xml \
    %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-httpmime.pom
%add_maven_depmap JPP.%{base_name}-httpmime.pom %{base_name}/httpmime.jar


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
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_3jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_1jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

