Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          jboss-annotations-1.2-api
Version:       1.0.0
Release:       alt1_4jpp8
Summary:       Common Annotations 1.2 API
License:       CDDL or GPLv2 with exceptions
URL:           https://github.com/jboss/jboss-annotations-api_spec
Source0:       https://github.com/jboss/jboss-annotations-api_spec/archive/jboss-annotations-api_1.2_spec-%{namedversion}.tar.gz
Source1:       cddl.txt

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
This package contains Common Annotations 1.2 API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-annotations-api_spec-jboss-annotations-api_1.2_spec-%{namedversion}

cp %{SOURCE1} .

%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%doc --no-dereference cddl.txt LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference cddl.txt LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.6.Alpha1jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Alpha1jpp8
- java 8 mass update

