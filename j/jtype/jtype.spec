Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jtype
Version:        0.1.2
Release:        alt2_12jpp8
Summary:        A small library for working with the Java 5 type system
License:        ASL 2.0
URL:            https://github.com/markhobson/jtype
Source0:        https://github.com/markhobson/jtype/archive/%{version}.tar.gz
# Add missing method getAnnotatedBounds()
Patch0:         jtype-0.1.2-java8.patch

BuildArch:      noarch
BuildRequires:  maven-local
# test deps
BuildRequires:  mvn(junit:junit)
Source44: import.info
#BuildRequires:  mvn(org.jmock:jmock-junit4)
#BuildRequires:  mvn(org.jmock:jmock-legacy)

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
%patch0 -p0

%mvn_file : %{name}

%build

# Disable test suite jmock require cglib < 3.x
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2_7jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2_5jpp7
- added BR: for xmvn

* Sun Jul 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_5jpp7
- new release

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt1_3jpp7
- new version

