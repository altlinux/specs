# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          aries-quiesce
Version:       0.3
Release:       alt2_10jpp8
Summary:       Apache Aries Quiesce
License:       ASL 2.0
Group:         Development/Other
URL:           http://aries.apache.org/

# svn export http://svn.apache.org/repos/asf/aries/tags/quiesce-0.3/ aries-quiesce-0.3
# tar cafJ aries-quiesce-0.3.tar.xz aries-quiesce-0.3

Source0:       %{name}-%{version}.tar.xz
Patch0:        %{name}-%{version}-xml.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: apache-commons-lang
BuildRequires: apache-commons-pool
BuildRequires: apache-commons-collections
BuildRequires: aries-util
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: slf4j
Source44: import.info

%description
Quiesce support for Aries.

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_10jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_9jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_2jpp7
- new version

