# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global site_name org.apache.felix.bundlerepository
%global grp_name  felix

Name:             felix-bundlerepository
Version:          1.6.6
Release:          alt2_9jpp7
Summary:          Bundle repository service
License:          ASL 2.0 and BSD
Group:            Development/Java
URL:              http://felix.apache.org/site/apache-felix-osgi-bundle-repository.html

Source0:          http://www.fightrice.com/mirrors/apache/felix/org.apache.felix.bundlerepository-%{version}-source-release.tar.gz
Patch1:           0001-Unbundle-libraries.patch
Patch2:           0002-Add-xpp3-dependency.patch
Patch3:           0003-Make-felix-utils-mandatory-dep.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    felix-shell
BuildRequires:    felix-utils
BuildRequires:    kxml
BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    woodstox-core
BuildRequires:    xpp3

Requires:         jpackage-utils
Requires:         felix-shell
Requires:         felix-utils
Requires:         kxml
Requires:         woodstox-core
Requires:         xpp3
Source44: import.info


%description
Bundle repository service

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mvn-rpmbuild package javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{site_name}-%{version}.jar %{buildroot}%{_javadir}/%{grp_name}/%{name}.jar

# pom
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{grp_name}-%{name}.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP.%{grp_name}-%{name}.pom %{grp_name}/%{name}.jar

%files
%doc LICENSE LICENSE.kxml2 NOTICE DEPENDENCIES
%{_javadir}/%{grp_name}/%{name}.jar
%{_mavenpomdir}/JPP.%{grp_name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE LICENSE.kxml2 NOTICE
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1_7jpp7
- new release

