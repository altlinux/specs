Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 22
Name:          jackson-annotations
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       Core annotations for Jackson data processor 
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonHome
Source0:       https://github.com/FasterXML/jackson-annotations/archive/%{name}-%{version}.tar.gz
%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin

Provides:      jackson2-annotations = %{version}-%{release}
Obsoletes:     jackson2-annotations < %{version}-%{release}

BuildArch:     noarch
Source44: import.info

%description
Core annotations used for value types,
used by Jackson data-binding package.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p src/main/resources/META-INF/LICENSE .
sed -i 's/\r//' LICENSE

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

