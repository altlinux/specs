Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           apache-james-project
Version:        1.8.1
Release:        alt1_13jpp8
Summary:        Main project POM files and resources
License:        ASL 2.0
URL:            http://james.apache.org/
BuildArch:      noarch

# ./create-tarball.sh %%{VERSION}
Source0:        james-project-1.8.1-clean.tar.gz
Source1:        create-tarball.sh

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-site-plugin)
Source44: import.info

%description
Main project POM files and resources for Apache James project.

%prep
%setup -q -n james-project-%{version}

# generates erroneous runtime dependency
%pom_remove_plugin :maven-doap-plugin

%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-ssh-external']]"
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='wagon-ssh']]"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_13jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_3jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_3jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3jpp7
- new release

