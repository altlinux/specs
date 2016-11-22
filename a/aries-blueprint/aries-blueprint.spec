# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          aries-blueprint
Version:       0.3.1
Release:       alt2_12jpp8
Summary:       Apache Aries Blueprint
License:       ASL 2.0
Group:         Development/Other
URL:           http://aries.apache.org/

# svn export http://svn.apache.org/repos/asf/aries/tags/blueprint-0.3.1/ aries-blueprint-0.3.1
# tar cafJ aries-blueprint-0.3.1.tar.xz aries-blueprint-0.3.1

Source0:       %{name}-%{version}.tar.xz
Patch0:        %{name}-%{version}-xml.patch
Patch1:        %{name}-%{version}-java.patch

BuildArch:     noarch

Epoch:         1

BuildRequires: javapackages-tools rpm-build-java
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: aries-util
BuildRequires: aries-proxy
BuildRequires: aries-quiesce
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: xbean
BuildRequires: objectweb-asm3
Source44: import.info

%description
Implementation of the Blueprint Container Specification.

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1



%build
# tests disabled because of
# missing dependency on org.apache.aries.unittest
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README LICENSE NOTICE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.3.1-alt2_12jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.3.1-alt2_11jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.3.1-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_3jpp7
- new version

