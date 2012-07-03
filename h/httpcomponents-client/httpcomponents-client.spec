BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name httpcomponents

Name:              httpcomponents-client
Summary:           HTTP agent implementation based on httpcomponents HttpCore
Version:           4.1.3
Release:           alt1_1jpp7
Group:             Development/Java
License:           ASL 2.0
URL:               http://hc.apache.org/
Source0:           http://www.apache.org/dist/httpcomponents/httpclient/source/httpcomponents-client-%{version}-src.tar.gz
# Remove optional build deps not available in Fedora
# and add proper Apache felix bundle plugin instructions
# so that we get a reasonable OSGi manifest.
Patch0:            0001-Remove-few-modules-and-deps.patch
Patch1:            0002-Make-httpmime-into-bundle.patch
Patch2:            0003-Make-httpclient-into-bundle.patch



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
API docs for %{name}.


%prep
%setup -q
%patch0 -p1 -b .sav
%patch1 -p1 -b .sav
%patch2 -p1 -b .sav

%build
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
# jars
install -D -m 0644 httpclient/target/httpclient-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/httpclient.jar
install -D -m 0644 httpmime/target/httpmime-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/httpmime.jar

# main pom
install -D -m 0644 pom.xml \
    %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-httpcomponents-client.pom
%add_to_maven_depmap org.apache.httpcomponents httpcomponents-client %{version} JPP/%{base_name} httpcomponents-client
# pom
install -D -m 0644 httpclient/pom.xml \
    %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-httpclient.pom
%add_maven_depmap JPP.%{base_name}-httpclient.pom %{base_name}/httpclient.jar

install -D -m 0644 httpmime/pom.xml \
    %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-httpmime.pom
%add_maven_depmap JPP.%{base_name}-httpmime.pom %{base_name}/httpmime.jar


# javadocs
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc README.txt LICENSE.txt RELEASE_NOTES.txt
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{base_name}*.pom
%{_javadir}/%{basename}

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_1jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

