Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name   jcommander

Name:             beust-%{short_name}
Version:          1.47
Release:          alt1_3jpp8
Summary:          Java framework for parsing command line parameters
License:          ASL 2.0
URL:              http://jcommander.org/
Source0:          https://github.com/cbeust/%{short_name}/archive/%{short_name}-%{version}.tar.gz
BuildArch:        noarch
BuildRequires:    maven-local
Source44: import.info

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the %{summary}.

%prep
%setup -q -n %{short_name}-%{short_name}-%{version}
chmod -x license.txt

%build
%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc license.txt notice.md README.markdown

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.md

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_4jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt2_2.2jpp7
- new version

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1_2.2jpp7
- new version

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

