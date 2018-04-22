Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.4
%global namedreltag -rc3
%global namedversion %{version}%{?namedreltag}
Name:          jwnl
Version:       1.4
Release:       alt1_0.5.rc3jpp8
Summary:       Java API for accessing the WordNet relational dictionary
License:       BSD
URL:           https://sourceforge.net/projects/jwordnet/
# Source0:       http://downloads.sourceforge.net/jwordnet/jwnl14-rc2.zip
# svn checkout svn://svn.code.sf.net/p/jwordnet/code/trunk/jwnl/  jwnl-1.4-rc3
# tar cJf jwnl-1.4-rc3.tar.xz jwnl-1.4-rc3
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)

BuildArch:     noarch
Source44: import.info

%description
JWNL is a Java API for accessing the WordNet relational dictionary.
WordNet is widely used for developing NLP applications, and a Java
API such as JWNL will allow developers to more easily use Java for
building NLP applications.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

sed -i 's/\r//' changes.txt doc/*

%mvn_file :%{name} %{name}
%mvn_alias %{name}: net.sf.jwordnet:

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc changes.txt doc/*
%doc --no-dereference license.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_0.5.rc3jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_0.4.rc3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_0.3.rc3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_0.2.rc3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_0.1.rc3jpp8
- new version

