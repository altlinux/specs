Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          replacer
Version:       1.6
Release:       alt1_13jpp11
Summary:       Replacer Maven Mojo
License:       MIT
URL:           https://github.com/beiliubei/maven-replacer-plugin
# http://code.google.com/p/maven-replacer-plugin/
Source0:       https://github.com/beiliubei/maven-replacer-plugin/archive/%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(xerces:xercesImpl)

BuildArch:     noarch
Source44: import.info

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n maven-replacer-plugin-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :maven-assembly-plugin

%mvn_file :%{name} %{name}
%mvn_alias :%{name} com.google.code.maven-replacer-plugin:maven-replacer-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.6-alt1_13jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_11jpp8
- update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_9jpp8
- build with new mockito

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_2jpp8
- new version

