# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global osginame org.apache.felix.resolver

Name:             felix-osgi-obr-resolver
Version:          1.2.0
Release:          alt1_1jpp8
Summary:          Apache Felix Resolver
Group:            Development/Java
License:          ASL 2.0
URL:              http://felix.apache.org/documentation/subprojects/apache-felix-osgi-bundle-repository.html

Source0:          http://apache.cbox.biz//felix/org.apache.felix.resolver-1.2.0-source-release.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    felix-parent
BuildRequires:    felix-framework
BuildRequires:    apache-rat-plugin
BuildRequires:    mockito
Source44: import.info

%description
This package contains the Apache Felix Resolver

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{osginame}-%{version}

%pom_change_dep org.osgi:org.osgi.core org.apache.felix:org.apache.felix.framework

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE
%doc NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_0.9.Beta1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_0.7.Beta1jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2_0.5.Beta1jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_0.5.Beta1jpp7
- new version

