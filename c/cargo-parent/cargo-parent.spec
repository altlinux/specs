Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           cargo-parent
Version:        4.13
Release:        alt1_8jpp8
Summary:        Parent pom file for cargo.codehaus.org project
License:        ASL 2.0
URL:            http://cargo.codehaus.org/
#svn export http://svn.codehaus.org/cargo/pom/tags/cargo-parent-4.13/
Source0:        %{name}-%{version}.tar.gz
# cargo-parent package don't include the license file
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-checkstyle-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  codehaus-parent
Source44: import.info

%description
This package contains the cargo parent pom.

%prep
%setup -q

# remove org.apache.maven.wagon wagon-webdav
%pom_xpath_remove "pom:build/pom:extensions"

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.13-alt1_8jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 4.13-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.13-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.12-alt1_3jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.11-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 4.11-alt1_2jpp7
- new release

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.7-alt1_1jpp7
- new version

