Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global site_name org.apache.felix.configadmin
%global grp_name  felix

Name:             felix-configadmin
Version:          1.4.0
Release:          alt2_15jpp8
Summary:          Felix Configuration Admin Service
License:          ASL 2.0
URL:              http://felix.apache.org/site/apache-felix-config-admin.html

Source0:          http://www.fightrice.com/mirrors/apache/felix/%{site_name}-%{version}-source-release.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    felix-parent
BuildRequires:    felix-osgi-compendium >= 1.4.0
BuildRequires:    felix-osgi-core
BuildRequires:    aqute-bndlib
BuildRequires:    maven-shared
Source44: import.info

%description
Implementation of the OSGi Configuration Admin Service Specification 1.4.

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%build
# Pax test dependency unavailable
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_14jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3jpp7
- new release

