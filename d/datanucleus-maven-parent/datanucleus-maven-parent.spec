Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 8e55762cef51784b0308ed4cdcfeceaadb03e1d6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           datanucleus-maven-parent
Version:        3.3
Release:        alt1_8jpp8
Summary:        DataNucleus Maven parent project 

License:        ASL 2.0
URL:            https://github.com/datanucleus/datanucleus-maven-parent
Source:         https://github.com/datanucleus/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

# jira opened for missing ASL file
# http://www.datanucleus.org/servlet/jira/browse/NUCACCESS-130
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  maven-clean-plugin
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
Datanucleus Maven parent pom used by other datanucleus packages.

%prep
%setup -q -n %{name}-%{commit}
cp -p %{SOURCE1} LICENSE
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin

%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-ssh-external']]"

%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_8jpp8
- java update

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1_7jpp8
- new version

