# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           javatar
Version:        2.5
Release:        alt1_19jpp8
Summary:        Java tar archive io package

Group:          Development/Other
License:        Public Domain
URL:            http://www.trustice.com/java/tar/
Source0:        http://www.gjt.org/download/time/java/tar/javatar-%{version}.tar.gz
# Fix srcdir and point to system activation.jar
Patch0:         %{name}-2.5-build.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  ant

Requires:       jpackage-utils
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%else
Requires:       java >= 1.6.0
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
Requires:       jpackage-utils
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
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_19jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_18jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_17jpp8
- new jpp release

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

