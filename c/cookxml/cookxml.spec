BuildRequires: javapackages-local
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             cookxml
Version:          3.0.2
Release:          alt3_12jpp8
Summary:          Dynamic XML data binding tool
Group:            Development/Other
License:          BSD
URL:              http://cookxml.yuanheng.org/

Source0:          http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_src-%{version}.zip
Source1:          %{name}-build.xml
Source2:          %{name}-pom.xml

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    java-devel
BuildRequires:    ant

Requires:         jpackage-utils
Source44: import.info

%description
CookXml is a powerful general purpose dynamic XML data binding tool.
It is designed to be easy to use and easily extensible. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -qc

find . -name '*.jar' -exec rm -rf {} \;

sed -i 's/\r//' LICENSE

%build
cp %{SOURCE1} .
ant -f %{name}-build.xml cookxml_jar apidoc

%install
# JAR
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# JAVADOC
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp apidoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# DEPMAP
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc LICENSE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
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

