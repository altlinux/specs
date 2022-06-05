Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             cookxml
Version:          3.0.2
Release:          alt5_17jpp8
Summary:          Dynamic XML data binding tool
License:          BSD
URL:              http://cookxml.yuanheng.org/

Source0:          http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_src-%{version}.zip
Source1:          %{name}-build.xml
Source2:          %{name}-pom.xml

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    javapackages-local

Requires:         jpackage-utils
Source44: import.info

%description
CookXml is a powerful general purpose dynamic XML data binding tool.
It is designed to be easy to use and easily extensible. 

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -qc

find . -name '*.jar' -exec rm -rf {} \;

sed -i 's/\r//' LICENSE
# install in _javadir
%mvn_file org.yuanheng.%{name}:%{name} %{name}

%build
cp %{SOURCE1} .
ant -f %{name}-build.xml cookxml_jar apidoc

%mvn_artifact %{SOURCE2} dist/%{name}-%{version}.jar

%install
%mvn_install -J apidoc

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sun Jun 05 2022 Igor Vlasenko <viy@altlinux.org> 3.0.2-alt5_17jpp8
- migrated to %%mvn_artifact

* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt4_17jpp8
- fixed build with new java

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt3_17jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt3_16jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt3_15jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt3_12jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_4jpp7
- update to new release by jppimport

* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_3jpp7
- new version

