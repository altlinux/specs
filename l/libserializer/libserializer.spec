Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: libserializer
Version: 1.1.2
Release: alt2_33jpp11
Summary: JFreeReport General Serialization Framework
License: LGPLv2+
#Original source: http://downloads.sourceforge.net/jfreereport/libserializer-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: libserializer-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org
BuildRequires: ant jpackage-utils libbase >= 1.1.2
Requires: jpackage-utils libbase >= 1.1.2
BuildArch: noarch
Patch0: libserializer-1.1.2.build.patch
Patch1: libserializer-1.1.2.java11.patch
Patch2:	libserializer-1.1.2-remove-antcontrib-support.patch
Patch3:	libserializer-1.1.2-remove-commons-logging.patch
Source44: import.info

%description
Libserializer contains a general serialization framework that simplifies the
task of writing custom java serialization handlers.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
%patch1 -p1 -b .java11
%patch2 -p1 -b .no_antcontrib
%patch3 -p1 -b .no_commons_logging

find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  jar javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/libserializer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt2_33jpp11
- update

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt2_29jpp11
- fc34 update

* Mon Jun 14 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt2_28jpp11
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt1_28jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt1_26jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_22jpp8
- update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_20jpp8
- fc update & java 8 build

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_18jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_17jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_16jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_14jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_8jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_6jpp7
- new version

