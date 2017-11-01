Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jackson-dataformat-csv
Version:       2.7.6
Release:       alt1_2jpp8
Summary:       Jackson extension for adding support for reading and writing CSV formatted data 
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonExtensionCSV
Source0:       https://github.com/FasterXML/jackson-dataformat-csv/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)

BuildArch:     noarch
Source44: import.info

%description
Jackson data format module for reading and writing CSV encoded data,
either as "raw" data (sequence of String arrays), or via data binding to
from Java Objects (POJOs).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find . -name "*.jar" -delete

%pom_xpath_remove "pom:properties/pom:osgi.private"

sed -i 's/\r//' src/main/resources/META-INF/LICENSE
cp -p src/main/resources/META-INF/LICENSE .

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_2jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

