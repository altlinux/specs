# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:           javatar
Version:        2.5
Release:        alt1_16jpp8
Summary:        Java tar archive io package

Group:          Development/Other
License:        Public Domain
URL:            http://www.trustice.com/java/tar/
Source0:        http://www.gjt.org/download/time/java/tar/javatar-%{version}.tar.gz
# Fix srcdir and point to system activation.jar
Patch0:         %{name}-2.5-build.patch
BuildArch:      noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant

Requires: javapackages-tools rpm-build-java
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%else
%endif
Source44: import.info

%description
The package com.ice.tar implements a tar archive io package. This package
allows you to create, and extract tar archives. Since the package uses
InputStream and OutputStream, it is possible to combine this package with the
java.util.zip package to handle .tar.gz files.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Documentation
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1 -b .build
find \( -name '*.jar' -o -name '*.class' \) -exec rm -f '{}' +
# Fix line endings
find \( -name '*.java' -o -name '*.txt' -o -name '*.xml' -o -name LICENSE \) -exec sed -i 's/\r//' '{}' +
#Remove manifest classpath and name
sed -i -e '/^Class-Path:/d' -e '/^Name:/d' source/com/ice/tar/META-INF/MANIFEST.MF


%build
ant -buildfile source/com/ice/tar/build.xml deploy


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p tar-%{version}/jars/tar.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/tar.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp doc $RPM_BUILD_ROOT/%{_javadocdir}/%{name}


%files
%doc doc/LICENSE
%{_javadir}/%{name}.jar
%{_javadir}/tar.jar

%files javadoc
%doc doc/LICENSE
%{_javadocdir}/%{name}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_16jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_9jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_8jpp7
- new version

