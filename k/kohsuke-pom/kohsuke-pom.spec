Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           kohsuke-pom
Version:        14
Release:        alt1_2jpp8
Summary:        Kohsuke parent POM

# License is specified in pom file
License:        MIT
URL:            https://github.com/kohsuke/pom
Source0:        https://github.com/kohsuke/pom/archive/pom-%{version}.tar.gz
Source1:        https://raw.github.com/kohsuke/youdebug/youdebug-1.5/LICENSE.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-manager-plexus)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-gitexe)
Source44: import.info

%description
This package contains Kohsuke parent POM file.

%prep
%setup -q -n pom-pom-%{version}

cp %{SOURCE1} LICENSE

# we don't have these plugins and extensions
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-gitsite']]"
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :gmaven-plugin

# missing dep org.kohsuke:doxia-module-markdown
%pom_remove_plugin :maven-site-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 14-alt1_2jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 14-alt1_1jpp8
- new version

