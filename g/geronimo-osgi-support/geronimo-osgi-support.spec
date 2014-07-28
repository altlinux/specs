# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global registry geronimo-osgi-registry
%global locator geronimo-osgi-locator

Name:             geronimo-osgi-support
Version:          1.0
Release:          alt2_12jpp7
Summary:          OSGI spec bundle support
Group:            Development/Java
License:          ASL 2.0 and W3C
URL:              http://geronimo.apache.org/

Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{name}/%{version}/%{name}-%{version}-source-release.tar.gz
# Use parent pom files instead of unavailable 'genesis-java5-flava'
Patch1:           use_parent_pom.patch
# Remove itests due to unavailable dependencies
Patch2:           remove-itests.patch
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    felix-osgi-core
BuildRequires:    felix-osgi-compendium
BuildRequires:    geronimo-parent-poms
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-provider-junit4

Requires:         jpackage-utils
Requires:         felix-osgi-core
Requires:         felix-osgi-compendium

Provides:         geronimo-osgi-locator = %{version}-%{release}
Provides:         geronimo-osgi-registry = %{version}-%{release}
Source44: import.info

%description
This project is a set of bundles and integration tests for implementing
OSGi-specific lookup in the Geronimo spec projects.


%package javadoc
Group:            Development/Java
Summary:          Javadoc for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE
sed -i 's/\r//' LICENSE NOTICE
%patch1 -p0
%patch2 -p0

%pom_xpath_inject "pom:plugin[pom:artifactId[text()='maven-bundle-plugin']]
                       /pom:configuration/pom:instructions" "
    <Export-Package>!*</Export-Package>" geronimo-osgi-locator

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 %{registry}/target/%{registry}-%{version}.jar %{buildroot}%{_javadir}/%{registry}.jar
install -m 644 %{locator}/target/%{locator}-%{version}.jar %{buildroot}%{_javadir}/%{locator}.jar

# poms
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 %{registry}/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{registry}.pom
install -pm 644 %{locator}/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{locator}.pom

%add_maven_depmap JPP-%{name}.pom
%add_maven_depmap JPP-%{registry}.pom %{registry}.jar
%add_maven_depmap JPP-%{locator}.pom %{locator}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9jpp7
- new version

