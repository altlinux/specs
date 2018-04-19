Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           kohsuke-pom
Version:        14
Release:        alt1_5jpp8
Summary:        Kohsuke parent POM

# License is specified in pom file
License:        MIT
URL:            https://github.com/kohsuke/pom
Source0:        https://github.com/kohsuke/pom/archive/pom-%{version}.tar.gz
Source1:        https://raw.github.com/kohsuke/youdebug/youdebug-1.5/LICENSE.txt

BuildArch:      noarch

BuildRequires:  maven-local
Source44: import.info

%description
This package contains Kohsuke parent POM file.

%prep
%setup -q -n pom-pom-%{version}

cp %{SOURCE1} LICENSE

# we don't have these plugins and extensions
%pom_xpath_remove pom:extensions
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :gmaven-plugin

# missing dep org.kohsuke:doxia-module-markdown
%pom_remove_plugin :maven-site-plugin

%pom_remove_plugin :maven-release-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 14-alt1_5jpp8
- java update

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 14-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 14-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 14-alt1_2jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 14-alt1_1jpp8
- new version

