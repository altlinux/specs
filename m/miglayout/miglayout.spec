# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           miglayout
Version:        4.0
Release:        alt1_4jpp7
Summary:        Versatile and flexible Swing and SWT layout manager
URL:            http://www.miglayout.com/
License:        BSD
Group:          System/Libraries

Source0:        http://www.migcalendar.com/miglayout/versions/%{version}/miglayout-%{version}-sources.jar

BuildArch:      noarch
BuildRequires:  eclipse-swt dos2unix jpackage-utils

Requires:       jpackage-utils
Source44: import.info

%description
MiGLayout is a versatile SWT/Swing layout manager.  It uses String or
API type-checked constraints to format the layout. MiGLayout can
produce flowing, grid based, absolute (with links), grouped and
docking layouts. MiGLayout is created to be to manually coded layouts
what Matisse/GroupLayout is to IDE supported visual layouts.

%package javadoc
Summary:        Javadocs for MiGLayout
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package contains the API documentation for MiGLayout.

%package examples
Summary:        Examples and demo code for MiGLayout
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description examples
This package contains examples and demos code for MiGLayout.

%prep
%setup -q -c %{name}
# Fix line endings in some demo and example source files.
dos2unix net/miginfocom/demo/{CallbackDemo,SwingDemo,SwtDemo}.java
dos2unix net/miginfocom/examples/{Example01,Example,ExampleGood}.java
# Convert Windows codepage 1251 quotes in SwtDemo.java to UTF-8.
iconv --from=windows-1251 --to=UTF-8 net/miginfocom/demo/SwtDemo.java >net/miginfocom/demo/SwtDemo.java.new
touch -r net/miginfocom/demo/SwtDemo.java{,.new}
mv net/miginfocom/demo/SwtDemo.java{.new,}

%build
export CLASSPATH=%{_libdir}/java/swt.jar:.
javac -encoding utf8 net/miginfocom/{layout,swing,swt}/*.java

# We'll build the demos and examples just to ensure that they compile,
# but we're not going to package the binaries.
# We can't build demo/HiDPISimulator.java due to a missing prerequisite
# (org.jvnet.substance).
javac -encoding utf8 net/miginfocom/demo/[CS]*.java
javac -encoding utf8 net/miginfocom/examples/*.java

jar cmf META-INF/MANIFEST.MF \
        %{name}-%{version}.jar  \
        net/miginfocom/{layout,swing,swt}/*.class
javadoc -d doc net.miginfocom.{layout,swing,swt}

%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_javadocdir}
cp -a %{name}-%{version}.jar %{buildroot}%{_javadir}/
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
cp -a doc %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%files examples
%doc net/miginfocom/demo/*.java
%doc net/miginfocom/examples/*.java

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_4jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2jpp7
- new version

