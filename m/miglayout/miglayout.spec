Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           miglayout
Version:        4.2
Release:        alt1_10jpp8
Summary:        Versatile and flexible Swing layout manager
URL:            http://www.miglayout.com/
License:        BSD

# Hidden in maven.org labyrinth, so no download URL's
Source0:        miglayout-core-4.2-sources.jar
Source1:        miglayout-swing-4.2-sources.jar

BuildArch:      noarch
BuildRequires:  java-devel

Requires:       java
# We no longer have an examples sub-package, note no provides as the examples
# are no longer packaged, so we do not provide them
Obsoletes:      %{name}-examples < %{version}-%{release}
Source44: import.info

%description
MiGLayout is a versatile Swing layout manager.  It uses String or
API type-checked constraints to format the layout. MiGLayout can
produce flowing, grid based, absolute (with links), grouped and
docking layouts. MiGLayout is created to be to manually coded layouts
what Matisse/GroupLayout is to IDE supported visual layouts.


%package javadoc
Group: Development/Java
Summary:        Javadocs for MiGLayout
BuildArch: noarch

%description javadoc
This package contains the API documentation for MiGLayout.


%prep
%setup -q -c %{name}
unzip -oq %{SOURCE1}


%build
javac -encoding utf8 net/miginfocom/{layout,swing}/*.java

jar cmf META-INF/MANIFEST.MF %{name}-core.jar net/miginfocom/layout/*.class
jar cmf META-INF/MANIFEST.MF %{name}-swing.jar net/miginfocom/swing/*.class
javadoc -Xdoclint:none -d doc net.miginfocom.{layout,swing}


%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_javadocdir}
cp -a %{name}-*.jar %{buildroot}%{_javadir}
cp -a doc %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_10jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_7jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_4jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2jpp7
- new version

