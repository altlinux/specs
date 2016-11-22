# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global bundle org.osgi.foundation

Name:    felix-osgi-foundation
Version: 1.2.0
Release: alt5_20jpp8
Summary: Felix OSGi Foundation EE Bundle
Group:   Development/Other
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: maven-local
BuildRequires: mockito
BuildRequires: felix-parent

Source44: import.info

%description
OSGi Foundation Execution Environment (EE) Classes.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file :%{bundle} "felix/%{bundle}"
%mvn_alias "org.apache.felix:%{bundle}" "org.osgi:%{bundle}"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt5_20jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt5_19jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_10jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_10jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4jpp6
- new version

