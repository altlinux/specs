# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           javatar
Version:        2.5
Release:        alt1_9jpp7
Summary:        Java tar archive io package

Group:          Development/Java
License:        Public Domain
URL:            http://www.trustice.com/java/tar/
Source0:        http://www.gjt.org/download/time/java/tar/javatar-%{version}.tar.gz
# Fix srcdir and point to system activation.jar
Patch0:         %{name}-2.5-build.patch
BuildArch:      noarch
#Missing java >= 1:1.6.0
ExcludeArch:    ppc64

BuildRequires:  jpackage-utils
BuildRequires:  ant

Requires:       jpackage-utils
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
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/tar.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/tar-%{version}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rp doc $RPM_BUILD_ROOT/%{_javadocdir}/%{name}


%files
%doc doc/LICENSE
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/tar-%{version}.jar
%{_javadir}/tar.jar

%files javadoc
%doc doc/LICENSE
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_9jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_8jpp7
- new version

