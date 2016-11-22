Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          jackcess
Version:       2.1.2
Release:       alt1_2jpp8
Summary:       Java library for reading from and writing to MS Access databases
License:       ASL 2.0
URL:           http://jackcess.sourceforge.net/
# svn checkout http://svn.code.sf.net/p/jackcess/code/jackcess/tags/jackcess-2.1.2
# tar cJf jackcess-2.1.2.tar.xz jackcess-2.1.2
Source0:       %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:12)
BuildRequires: mvn(org.apache.poi:poi)

BuildArch:     noarch
Source44: import.info

%description
Jackcess is a pure Java library for reading from and
writing to MS Access databases (currently supporting
versions 2000-2013).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

# com.healthmarketscience:openhms-parent:1.1.1
%pom_remove_parent
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_xpath_set "pom:dependency[pom:groupId='log4j']/pom:version" 12

%mvn_file :%{name} %{name}
%mvn_file :%{name}-tests::tests: %{name}-tests
%mvn_package :::tests:

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc TODO.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_1jpp8
- new version

