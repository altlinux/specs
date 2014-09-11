Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           jtype
Version:        0.1.2
Release:        alt2_7jpp7
Summary:        A small library for working with the Java 5 type system
License:        ASL 2.0 
# svn export http://jtype.googlecode.com/svn/tags/0.1.2 jtype-0.1.2
# tar caf jtype-0.1.2.tar.xz jtype-0.1.2
URL:            http://code.google.com/p/jtype/
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  maven-local
# test deps
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.jmock:jmock-junit4)
BuildRequires:  mvn(org.jmock:jmock-legacy)
Source44: import.info

%description
Java 5 introduced a richer type system for generics with Type and its various
sub-types, but lacks any easy way to perform common operations on these types.
JType aims to fill this gap. 

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
# disable org.jvnet.wagon-svn:wagon-svn
%pom_xpath_remove "pom:project/pom:build/pom:extensions"

%build

%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2_7jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2_5jpp7
- added BR: for xmvn

* Sun Jul 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_5jpp7
- new release

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_3jpp7
- new version

