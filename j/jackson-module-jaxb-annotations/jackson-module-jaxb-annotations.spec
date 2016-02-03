Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 23
Name:          jackson-module-jaxb-annotations
Version:       2.5.0
Release:       alt1_2jpp8
Summary:       JAXB annotations support for Jackson (2.x)
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonJAXBAnnotations
Source0:       https://github.com/FasterXML/jackson-module-jaxb-annotations/archive/%{name}-%{version}.tar.gz

%if %{?fedora} > 20
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent:pom:)
%else
BuildRequires: mvn(com.fasterxml.jackson:jackson-parent)
%endif
# Require glassfish-jaxb-api
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)

# test deps
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: replacer
# bundle-plugin Requires
#BuildRequires: mvn(org.sonatype.aether:aether)

Provides:      jackson2-module-jaxb-annotations = %{version}-%{release}
Obsoletes:     jackson2-module-jaxb-annotations < %{version}-%{release}

BuildArch:     noarch
Source44: import.info

%description
Support for using JAXB annotations as an alternative to
"native" Jackson annotations, for configuring data binding.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

