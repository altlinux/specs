# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global srcname dirq
Name:		java-dirq
Version:	1.4
Release:	alt1_2jpp7
Summary:	Directory based queue

Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/cern-mig/%{name}
Source0:	https://github.com/cern-mig/%{name}/archive/%{srcname}-%{version}.tar.gz

BuildArch:	noarch
%if 0%{?rhel} > 1
ExcludeArch:	ppc ppc64
%endif

BuildRequires:	jpackage-utils
BuildRequires:	ant
%if 0%{?rhel} != 5
BuildRequires:	ant-junit
BuildRequires:	junit4
%endif
BuildRequires:	jna

Requires:	jpackage-utils
Requires:	jna
Source44: import.info

%description
The goal of this module is to offer a simple queue system using the
underlying file system for storage, security and to prevent race
conditions via atomic operations. It focuses on simplicity, robustness
and scalability.

This module allows multiple concurrent readers and writers to interact
with the same queue.

A port of Perl module Directory::Queue and a Python dirq implementation
of the same algorithm are available so readers and writers can be written
in different programming languages.

%package javadoc
Summary:	Javadocs for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{srcname}-%{version}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build 
mkdir lib
export CLASSPATH=$(build-classpath jna junit4)
build-jar-repository -s -p lib jna
%if 0%{?rhel} != 5
build-jar-repository -s -p lib junit4
%endif
%if 0%{?rhel} == 5
sed -i "s/compile,test/compile/" maven-build.xml
%endif
%if 0%{?rhel} > 1
find src/test -name "*java" -exec rm -f {} \;
%endif
ant -Dmaven.mode.offline=true -Djunit.custom.dependencies=lib -Djunit.skipped=true
ant javadoc

%install
mkdir -p %{buildroot}%{_javadir}
cp -p target/%{srcname}*.jar %{buildroot}%{_javadir}/%{srcname}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{srcname}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{srcname}

%files
%doc license.txt readme.md
%{_javadir}/%{srcname}*.jar

%files javadoc
%{_javadocdir}/%{srcname}/

%changelog
* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3jpp7
- new release

