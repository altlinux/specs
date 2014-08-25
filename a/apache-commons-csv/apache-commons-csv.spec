BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       csv
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.0
Release:          alt3_0.6.svn1071189jpp7
Summary:          Utilities to assist with handling of CSV files
License:          ASL 2.0
Group:            Development/Java
URL:              http://commons.apache.org/sandbox/%{base_name}
# svn export -r 1071189 http://svn.apache.org/repos/asf/commons/sandbox/csv/trunk/ apache-commons-csv-1.0
# tar caf apache-commons-csv-1.0.tar.xz apache-commons-csv-1.0
Source0:          %{name}-%{version}.tar.xz
BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    jpackage-utils
BuildRequires:    junit4
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    apache-commons-parent
Source44: import.info


%description
Commons CSV was started to unify a common and simple interface for
reading and writing CSV files under an ASL license.

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
sed -i 's/\r//' *.txt
sed -i 's:commons-sandbox-parent:commons-parent:' pom.xml

%build
%mvn_file  : %{short_name} %{name}
%mvn_alias : %{short_name}:%{short_name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.6.svn1071189jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.3.svn1071189jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.3.svn1071189jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.svn1071189jpp7
- new version

