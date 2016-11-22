Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          json-path
Version:       0.9.1
Release:       alt1_8jpp8
Summary:       Java JsonPath implementation
# Some files in src/main/java/com/jayway/jsonassert/impl/matcher/ are licensed under BSD
License:       ASL 2.0 and BSD
URL:           https://github.com/jayway/JsonPath
Source0:       https://github.com/jayway/JsonPath/archive/%{name}-%{version}.tar.gz
# Disable test which fails on java8
Patch0:        %{name}-0.9.1-disable-tests.patch

BuildRequires: maven-local
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.minidev:json-smart)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Java DSL for reading and testing JSON documents.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n JsonPath-%{name}-%{version}
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin
# use web connection
rm -r json-path/src/test/java/com/jayway/jsonpath/JsonModelTest.java
%patch0 -p1

%mvn_file :%{name} %{name}
%mvn_file :%{name}-assert %{name}-assert

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_8jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_6jpp8
- unbootsrap build

