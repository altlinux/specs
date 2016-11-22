# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global tag a594629

Name:           sonatype-plugins-parent
Version:        8
Release:        alt2_9jpp8
Summary:        Sonatype Plugins Parent POM
BuildArch:      noarch
Group:          Development/Other
License:        ASL 2.0
URL:            https://github.com/sonatype/oss-parents
Source:         https://github.com/sonatype/oss-parents/tarball/plugins-parent-%{version}#/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  forge-parent
Source44: import.info

%description
This package provides Sonatype plugins parent POM used by other Sonatype
packages.

%prep
%setup -q -n sonatype-oss-parents-%{tag}
cp -p %{SOURCE1} LICENSE

%build
cd ./plugins-parent
%mvn_build

%install
cd ./plugins-parent
%mvn_install

%files -f plugins-parent/.mfiles
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 8-alt2_9jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 8-alt2_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 8-alt2_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 8-alt2_5jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 8-alt2_1jpp7
- rebuild with maven-local

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 8-alt1_1jpp7
- new version

