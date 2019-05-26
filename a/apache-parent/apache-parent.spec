Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apache-parent
Version:        19
Release:        alt1_4jpp8
Summary:        Parent POM file for Apache projects
License:        ASL 2.0
URL:            http://apache.org/
Source0:        http://repo1.maven.org/maven2/org/apache/apache/%{version}/apache-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)

# Not generated automatically
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
Requires:       mvn(org.apache:apache-jar-resource-bundle)
Source44: import.info
Patch33: apache-parent-no-enforcer-loop.patch

%description
This package contains the parent pom file for apache projects.

%prep
%setup -n apache-%{version}

%pom_remove_plugin :maven-site-plugin
%patch33 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 19-alt1_4jpp8
- new version

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 19-alt1_2jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 18-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 18-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 18-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_10jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_7jpp7
- rebuild with new apache-resource-bundles

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 10-alt1_7jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 10-alt1_5jpp7
- new release

