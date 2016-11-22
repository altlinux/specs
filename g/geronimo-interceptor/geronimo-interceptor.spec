Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global spec_ver 3.0
%global spec_name geronimo-interceptor_%{spec_ver}_spec

Name:             geronimo-interceptor
Version:          1.0.1
Release:          alt2_15jpp8
Summary:          Java EE: Interceptor API v3.0
License:          ASL 2.0
URL:              http://geronimo.apache.org/

# svn export http://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-interceptor_3.0_spec-1.0.1/
# tar czf geronimo-interceptor_3.0_spec-1.0.1.tar.gz geronimo-interceptor_3.0_spec-1.0.1/
Source0:          %{spec_name}-%{version}.tar.gz
BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    maven-local
BuildRequires:    geronimo-parent-poms

Provides:         interceptor_api = %{spec_ver}
Source44: import.info

%description
Contains annotations and interfaces for defining interceptor methods,
interceptor classes and for binding interceptor classes to target classes.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{spec_name}-%{version}

%mvn_alias : org.apache.geronimo.specs:geronimo-interceptor_1.1_spec

%mvn_file : %{name} interceptor

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7jpp7
- new version

