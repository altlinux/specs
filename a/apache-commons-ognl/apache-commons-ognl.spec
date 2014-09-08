BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name commons-ognl

Name:           apache-%{short_name}
Version:        3.0.2
Release:        alt2_6.20120313svn1102435jpp7
Summary:        Object Graph Navigation Library

Group:          Development/Java
License:        ASL 2.0
URL:            http://commons.apache.org/ognl/
# svn export -r1102435 http://svn.apache.org/repos/asf/commons/proper/ognl/trunk/ apache-commons-ognl-3.0.2
# tar caf apache-commons-ognl-3.0.2.tar.xz apache-commons-ognl-3.0.2
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: javassist
BuildRequires: jna
Source44: import.info

%description
OGNL is an expression language for getting and setting properties of
Java objects, plus other extras such as list projection and selection
and lambda expressions.

%package javadoc
Summary:      API documentation for %{name}
Group:        Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_6.20120313svn1102435jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_4.20120313svn1102435jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_2.20120313svn1102435jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_2.20120313svn1102435jpp7
- new version

