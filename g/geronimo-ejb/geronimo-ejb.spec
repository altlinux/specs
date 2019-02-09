Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           geronimo-ejb
Version:        1.0
Release:        alt4_21jpp8
Summary:        Java EE: EJB API v3.1
License:        ASL 2.0
URL:            http://geronimo.apache.org
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{name}_3.1_spec/%{version}/%{name}_3.1_spec-%{version}-source-release.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-annotation_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-interceptor_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jaxrpc_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-osgi-locator)
BuildRequires:  mvn(org.apache.geronimo.specs:specs:pom:)
Source44: import.info

%description
Contains the Enterprise JavaBeans classes and interfaces that define the
contracts between the enterprise bean and its clients and between the
enterprise bean and the EJB container.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}_3.1_spec-%{version}
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
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_21jpp8
- fc29 update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_20jpp8
- java fc28+ update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_19jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_18jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_17jpp8
- new jpp release

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

