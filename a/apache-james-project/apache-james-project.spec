# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global server_ver      2.2.0
%global short_name      apache-james

Name:             %{short_name}-project
Version:          1.8.1
Release:          alt1_3jpp7
Summary:          Main project POM files and resources
License:          ASL 2.0
Group:            Development/Java
URL:              http://james.apache.org/
Source0:          http://repo1.maven.org/maven2/org/apache/james/james-project/%{version}/james-project-%{version}-source-release.zip
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit4
Source44: import.info


%description
Main project POM files and resources for Apache James project

%prep
%setup -q -n james-project-%{version}

# generates erroneous runtime dependency
%pom_remove_plugin :maven-doap-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_3jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_3jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3jpp7
- new release

