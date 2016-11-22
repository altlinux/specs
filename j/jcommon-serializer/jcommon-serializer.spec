# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name: jcommon-serializer
Version: 0.3.0
Release: alt1_14jpp8
Summary: JFree Java General Serialization Framework
License: LGPLv2+
Group: System/Libraries
Source0: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.tar.gz
URL: http://www.jfree.org/jfreereport/jcommon-serializer
BuildRequires: ant javapackages-tools rpm-build-java libbase >= 1.0.0
Requires: javapackages-tools rpm-build-java libbase >= 1.0.0
BuildArch: noarch
Patch1: jcommon-serializer-0.3.0-depends.patch
Source44: import.info

%description
Jcommon-serializer is a general serialization framework used by JFreeChart,
JFreeReport and other projects.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
Requires: %{name} = %{version}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch1 -p1 -b .depends
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib libbase commons-logging-api

%build
ant compile javadoc

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_8jpp7
- new version

