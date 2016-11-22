Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           miglayout
Version:        4.2
Release:        alt1_5jpp8
Summary:        Versatile and flexible Swing layout manager
URL:            http://www.miglayout.com/
License:        BSD

# Hidden in maven.org labyrinth, so no download URL's
Source0:        miglayout-core-4.2-sources.jar
Source1:        miglayout-swing-4.2-sources.jar

BuildArch:      noarch

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

