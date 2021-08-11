Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: jcommon-serializer
Version: 0.3.0
Release: alt1_27jpp11
Summary: JFree Java General Serialization Framework
License: LGPLv2+
Source0: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.tar.gz
URL: http://www.jfree.org/jfreereport/jcommon-serializer
BuildRequires: ant jpackage-utils libbase >= 1.0.0
Requires: jpackage-utils libbase >= 1.0.0
BuildArch: noarch
Patch1: jcommon-serializer-0.3.0-depends.patch
Patch2: jcommon-serializer-0.3.0-java11.patch
Patch3: jcommon-serializer-0.3.0-remove-commons-logging.patch
Source44: import.info

%description
Jcommon-serializer is a general serialization framework used by JFreeChart,
JFreeReport and other projects.

%package javadoc
Group: Development/Documentation
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch1 -p1 -b .depends
%patch2 -p1 -b .java11
%patch3 -p1 -b .remove-commons-logging
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib libbase

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  compile javadoc

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
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0.3.0-alt1_27jpp11
- update

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 0.3.0-alt1_25jpp11
- fixed build with new libbase

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0.3.0-alt1_24jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_21jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_19jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_18jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_16jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_15jpp8
- new jpp release

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

