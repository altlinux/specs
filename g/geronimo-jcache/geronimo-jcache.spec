Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name geronimo-jcache
%define version 1.0
%global spec_ver 1.0
%global spec_name geronimo-jcache_%{spec_ver}_spec

%global namedreltag -alpha-1
%global namedversion %{version}%{?namedreltag}

Name:          geronimo-jcache
Version:       1.0
Release:       alt1_0.2.alpha.1jpp8
Summary:       Apache Geronimo JCache Spec 1.0
License:       ASL 2.0
URL:           http://geronimo.apache.org/
Source0:       http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{namedversion}/%{spec_name}-%{namedversion}-source-release.zip

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:specs:pom:)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jcdi_1.0_spec)

BuildArch:     noarch
Source44: import.info

%description
Apache Geronimo implementation of JSR-107.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{spec_name}-%{namedversion}

# org.apache.geronimo.genesis:genesis-java5-flava:2.2
%pom_remove_parent
%pom_add_parent org.apache.geronimo.specs:specs:1.4

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.2.alpha.1jpp8
- new version

