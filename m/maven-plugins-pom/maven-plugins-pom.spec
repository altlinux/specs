#BuildRequires: mvn(xerces:xercesImpl) mvn(net.sf.cglib:cglib) mvn(net.sf.jtidy:jtidy) mvn(backport-util-concurrent:backport-util-concurrent) mvn(commons-beanutils:commons-beanutils) mvn(commons-digester:commons-digester) mvn(oro:oro) mvn(bsh:bsh)
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name maven-plugins

Name:           %{short_name}-pom
Version:        23
Release:        alt1_0jpp7
Summary:        Maven Plugins POM
BuildArch:      noarch
Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/
Source:         http://repo.maven.apache.org/maven2/org/apache/maven/plugins/%{short_name}/%{version}/%{short_name}-%{version}-source-release.zip

BuildRequires:  maven
Source44: import.info

%description
This package provides Maven Plugins parent POM used by different
Apache Maven plugins.

%prep
%setup -q -n %{short_name}-%{version}
# Enforcer plugin is used to ban plexus-component-api.
%pom_remove_plugin :maven-enforcer-plugin

%build

%install
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 23-alt1_0jpp7
- intermediate build

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 23-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

