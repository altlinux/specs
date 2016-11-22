Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          ehcache-sizeof-agent
Version:       1.0.1
Release:       alt2_11jpp8
Summary:       Ehcache Size Of Agent
License:       ASL 2.0
URL:           http://www.terracotta.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/sizeof-agent-1.0.1
# tar czf ehcache-sizeof-agent-1.0.1.tar.gz sizeof-agent-1.0.1
Source0:       %{name}-%{version}.tar.gz
# ehcache-sizeof-agent package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt


BuildRequires: maven-local
BuildRequires: maven-shared
BuildRequires: maven-gpg-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-pmd-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-release-plugin
BuildRequires: ehcache-parent
Requires:      ehcache-parent
BuildArch:     noarch
Source44: import.info

%description
Ehcache is a widely used, pure Java, in-process, distributed cache.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep

%setup -q -n sizeof-agent-%{version}

cp %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%mvn_file :sizeof-agent %{name}

%build

%mvn_build 

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2jpp7
- new version

