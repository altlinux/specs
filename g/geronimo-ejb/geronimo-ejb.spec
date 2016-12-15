# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global spec_ver 3.1
%global spec_name geronimo-ejb_%{spec_ver}_spec

Name:             geronimo-ejb
Version:          1.0
Release:          alt4_16jpp8
Summary:          Java EE: EJB API v3.1
Group:            Development/Other
License:          ASL 2.0
URL:              http://geronimo.apache.org

Source0:          http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{spec_name}/%{version}/%{spec_name}-%{version}-source-release.tar.gz

BuildArch:        noarch

BuildRequires:    java-devel
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    geronimo-parent-poms
BuildRequires:    jta
BuildRequires:    interceptor_api
BuildRequires:    annotation_api
BuildRequires:    jaxrpc_api
BuildRequires:    geronimo-osgi-locator

Provides:         ejb_api = %{spec_ver}
Source44: import.info

%description
Contains the Enterprise JavaBeans classes and interfaces that define the
contracts between the enterprise bean and its clients and between the
enterprise bean and the EJB container.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{spec_name}-%{version}
sed -i 's/\r//' LICENSE
# Use parent pom files instead of unavailable 'genesis-java5-flava'
%pom_set_parent org.apache.geronimo.specs:specs:1.4

%mvn_alias : org.apache.geronimo.specs:geronimo-ejb_2.1_spec
%mvn_alias : org.apache.geronimo.specs:geronimo-ejb_3.0_spec
%mvn_alias : javax.ejb:ejb
%mvn_alias : javax.ejb:ejb-api

%mvn_file : %{name} ejb

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_16jpp8
- added osgi provides

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_16jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_15jpp8
- added osgi provides

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_15jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_7jpp7
- new version

