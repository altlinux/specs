# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global site_name org.apache.felix.utils
%global grp_name  felix

Name:             felix-utils
Version:          1.2.0
Release:          alt1_1jpp7
Summary:          Utility classes for OSGi
License:          ASL 2.0
Group:            Development/Java
URL:              http://felix.apache.org

Source0:          http://archive.apache.org/dist/%{grp_name}/%{site_name}-%{version}-source-release.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    jpackage-utils
BuildRequires:    felix-osgi-compendium
BuildRequires:    felix-osgi-core
BuildRequires:    maven-clean-plugin
BuildRequires:    maven-surefire-provider-junit4

Requires:         jpackage-utils
Requires:         felix-osgi-compendium
Requires:         felix-osgi-core
Source44: import.info

%description
Utility classes for OSGi

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}

# Remove compiler plugin so default target of 1.5 is used
%pom_remove_plugin :maven-compiler-plugin
# Remove rat plugin that is not in Fedora
%pom_remove_plugin org.codehaus.mojo:rat-maven-plugin

%build
# one of the tests fails in mock (local build is ok)
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.failure.ignore=true

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
%doc LICENSE NOTICE DEPENDENCIES
%{_javadir}/%{grp_name}/%{name}.jar
%{_mavenpomdir}/JPP.%{grp_name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_5jpp7
- new release

