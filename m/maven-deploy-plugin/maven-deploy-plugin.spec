Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-deploy-plugin
Version:        2.7
Release:        alt2_10jpp7
Summary:        Maven Deploy Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-deploy-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

# Basic stuff

# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-archiver
BuildRequires: mvn(org.apache.maven:maven-artifact:2.0.6)
BuildRequires: mvn(org.apache.maven:maven-model:2.0.6)
# The following maven packages haven't updated yet
BuildRequires: maven-changes-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin

Requires:      mvn(org.apache.maven:maven-artifact:2.0.6)
Requires:      mvn(org.apache.maven:maven-model:2.0.6)

Provides:      maven2-plugin-deploy = 0:%{version}-%{release}
Obsoletes:     maven2-plugin-deploy <= 0:2.0.8
Source44: import.info

%description
Uploads the project artifacts to the internal remote repository.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_xpath_inject pom:project "<build><plugins/></build>"
%pom_add_plugin :maven-plugin-plugin . "
        <configuration>
          <helpPackageName>org.apache.maven.plugin.deploy</helpPackageName>
        </configuration>"

%build

%mvn_file :%{name} %{name}
# A test class doesn't compile
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE 

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_7jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt2_3jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_3jpp7
- new fc release

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

