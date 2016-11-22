Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          aries-util
Version:       0.4
Release:       alt2_9jpp8
Summary:       Apache Aries Util
License:       ASL 2.0
URL:           http://aries.apache.org/
# svn export http://svn.apache.org/repos/asf/aries/tags/org.apache.aries.util-0.4/ aries-util-0.4
# tar cafJ aries-util-0.4.tar.xz aries-util-0.4
Source0:       %{name}-%{version}.tar.xz
Patch0:        %{name}-%{version}-java.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: maven-release-plugin
BuildRequires: mvn(org.apache.felix:org.osgi.compendium)
BuildRequires: mvn(org.apache.felix:org.osgi.core)
Source44: import.info

%description
This package contains the OSGi common util for Apache Aries.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>org.apache.aries</groupId>"
#%%pom_xpath_remove "pom:project/pom:packaging"
%pom_xpath_set "pom:project/pom:packaging" jar
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId = 'org.osgi.compendium' ]/pom:groupId" org.apache.felix
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId = 'org.osgi.core' ]/pom:groupId" org.apache.felix
%pom_remove_dep org.eclipse:osgi

%build

%mvn_file :org.apache.aries.util %{name}
# test disabled because of missing dependency:
# org.apache.aries.testsupport:org.apache.aries.testsupport.unit:jar
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_8jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new version

