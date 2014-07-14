BuildRequires: /proc
BuildRequires: jpackage-compat
%global spec_ver 1.3
%global spec_name geronimo-saaj_%{spec_ver}_spec

Name:             geronimo-saaj
Version:          1.1
Release:          alt2_8jpp7
Summary:          Java EE: SOAP with Attachments API Package v1.3
Group:            Development/Java
License:          ASL 2.0 and W3C

URL:              http://geronimo.apache.org/
Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz
Source1:          %{name}.depmap
# Use parent pom files instead of unavailable 'genesis-java5-flava'
Patch1:           use_parent_pom.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    geronimo-parent-poms
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    geronimo-osgi-locator

Requires:         jpackage-utils
Requires:         geronimo-osgi-locator

Provides:         saaj_api = %{spec_ver}
Source44: import.info


%description
Provides the API for creating and building SOAP messages. 

%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{spec_name}-%{version}
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE
sed -i 's/\r//' LICENSE NOTICE
%patch1 -p0

%build
mvn-rpmbuild \
        -Dmaven.local.depmap.file="%{SOURCE1}" \
        install javadoc:javadoc

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

install -p -m 644 target/%{spec_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a org.apache.geronimo.specs:geronimo-saaj_1.1_spec,javax.xml.soap:saaj-api

cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%doc LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8jpp7
- new version

