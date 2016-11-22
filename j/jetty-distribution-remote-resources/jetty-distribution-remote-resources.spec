Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jetty-distribution-remote-resources
Version:        1.1
Release:        alt3_11jpp8
Summary:        Jetty toolchain artifact for distribution remote resources

License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  jetty-toolchain

Requires: javapackages-tools rpm-build-java
Requires:       maven
Requires:       maven-remote-resources-plugin
Requires:       jetty-toolchain
Source44: import.info

%description
Jetty toolchain artifact for distribution remote distribution resources

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/LICENSE*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_4jpp7
- fixed build

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new version

