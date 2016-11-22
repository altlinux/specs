Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-deploy-plugin
Version:        2.8.2
Release:        alt1_5jpp8
Summary:        Maven Deploy Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-deploy-plugin/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Maven and its dependencies
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact:2.0.6)
BuildRequires:  mvn(org.apache.maven:maven-model:2.0.6)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.mockito:mockito-core)
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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.8.2-alt1_5jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.8.2-alt1_4jpp8
- new version

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

