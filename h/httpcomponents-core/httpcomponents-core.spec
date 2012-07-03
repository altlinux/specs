BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name httpcomponents

Name:              httpcomponents-core
Summary:           Set of low level Java HTTP transport components for HTTP services
Version:           4.1.3
Release:           alt1_2jpp7
Group:             Development/Java
License:           ASL 2.0
URL:               http://hc.apache.org/
Source0:           http://www.apache.org/dist/httpcomponents/httpcore/source/httpcomponents-core-%{version}-src.tar.gz
Patch0:            0001-Remove-unneeded-pom-dependencies.patch
Patch1:            0002-Osgify-modules.patch
BuildArch:         noarch

BuildRequires:     httpcomponents-project
BuildRequires:     jpackage-utils
BuildRequires:     maven-surefire-provider-junit4

Requires:          jpackage-utils
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
%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d %{buildroot}/%{_mavenpomdir}
install -d %{buildroot}/%{_javadir}/%{base_name}

for m in httpcore httpcore-nio; do
    # poms
    install -m 0644 $m/pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-$m.pom

    # jars - osgi doesn't have one
    if [ -f $m/target/$m-%{version}.jar ];then
        install -m 0644 $m/target/$m-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/$m.jar
    fi

    %add_maven_depmap JPP.%{base_name}-$m.pom %{base_name}/$m.jar
done

# parent
install -D -m 0644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{base_name}-%{name}.pom
%add_maven_depmap JPP.%{base_name}-%{name}.pom

# javadocs
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc README.txt LICENSE.txt RELEASE_NOTES.txt
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{basename}*.pom
%{_javadir}/%{basename}

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_2jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

