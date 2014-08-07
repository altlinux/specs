BuildRequires: maven-plugin-plugin
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name maven-plugins

Name:           %{short_name}-pom
Version:        23
Release:        alt3_2jpp7
Summary:        Maven Plugins POM
BuildArch:      noarch
Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/
Source:         http://repo.maven.apache.org/maven2/org/apache/maven/plugins/%{short_name}/%{version}/%{short_name}-%{version}-source-release.zip

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-enforcer-plugin

Requires:       jpackage-utils
Source44: import.info

%description
This package provides Maven Plugins parent POM used by different
Apache Maven plugins.

%prep
%setup -q -n %{short_name}-%{version}

%check
mvn-rpmbuild verify

%install
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%files
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 23-alt3_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 23-alt2_2jpp7
- fixed build

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 23-alt1_2jpp7
- new version

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 23-alt1_0jpp7
- intermediate build

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 23-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

