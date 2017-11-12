Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           sonar-plugins-parent
Version:        16
Release:        alt1_6jpp8
Summary:        Sonar Plugins Parent POM

License:        LGPLv3+
URL:            http://www.sonarqube.org
# svn export https://svn.codehaus.org/sonar-plugins/tags/parent-16/ sonar-plugins-parent-16
# tar cjf sonar-plugins-parent-16.tar.bz2 sonar-plugins-parent-16/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.codehaus.sonar:sonar-packaging-maven-plugin)

BuildArch:      noarch
Source44: import.info

%description
Sonar Plugins Parent POM.

%prep
%setup -q

%pom_xpath_remove pom:build/pom:extensions
%pom_remove_plugin :maven-license-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%mvn_file ':{*}' @1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 16-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 16-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 16-alt1_4jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 16-alt1_2jpp8
- new version

