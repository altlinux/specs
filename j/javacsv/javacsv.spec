# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global srcname JavaCsv

Name:		javacsv
Version:	2.0
Release:	alt1_6jpp7
Summary:	Stream-based Java library for reading and writing CSV and other delimited data

Group:		Development/Java
License:	LGPLv2+
URL:		http://www.csvreader.com/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{srcname}/%{srcname}%%20{version}/%{name}%{version}.zip
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	ant

Requires:	jpackage-utils
Source44: import.info



%description
Java CSV is a small fast open source Java 
library for reading and writing CSV and plain
delimited text files. All kinds of CSV files
can be handled, text qualified, Excel formatted, etc.

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

rm src/AllTests.java


%build
ant
ant -buildfile javadoc.xml

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm doc/javadocs.zip
cp -rp doc/*  \
$RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}*
%doc

%files javadoc
%{_javadocdir}/%{name}*

%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_6jpp7
- new version

