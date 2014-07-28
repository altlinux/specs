# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: jcommon-serializer
Version: 0.3.0
Release: alt1_9jpp7
Summary: JFree Java General Serialization Framework
License: LGPLv2+
Group: System/Libraries
Source0: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.tar.gz
URL: http://www.jfree.org/jfreereport/jcommon-serializer
BuildRequires: ant jpackage-utils libbase >= 1.0.0
Requires: jpackage-utils libbase >= 1.0.0
BuildArch: noarch
Patch1: jcommon-serializer-0.3.0-depends.patch
Source44: import.info

%description
Jcommon-serializer is a general serialization framework used by JFreeChart,
JFreeReport and other projects.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_8jpp7
- new version

