Epoch: 0
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jdependency
Version:        0.7
Release:        alt1_9jpp7
Summary:        This project provides an API to analyse class dependencies
License:        ASL 2.0
URL:            http://github.com/tcurdt/%{name}
BuildArch:      noarch

Source0:        http://github.com/tcurdt/%{name}/archive/%{name}-%{version}.tar.gz
# Upstream uses different version of objectweb-asm than Fedora has.
Patch0:         %{name}-asm.patch

BuildRequires:  maven-local
BuildRequires:  objectweb-asm
BuildRequires:  apache-commons-io
Source44: import.info

%description
%{name} is small library that helps you analyze class level
dependencies, clashes and missing classes.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0
%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_6jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_4jpp7
- new fc release

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_1jpp7
- fc version

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_5jpp6
- new version

