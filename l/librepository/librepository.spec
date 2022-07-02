Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: librepository
Version: 1.1.3
Release: alt2_34jpp11
Summary: Hierarchical repository abstraction layer
License: LGPLv2
#Original source: http://downloads.sourceforge.net/jfreereport/%%name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{name}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant jpackage-utils libbase >= 1.1.3
Requires: jpackage-utils libbase >= 1.1.3
BuildArch: noarch
Patch0: librepository-1.1.2.build.patch
Patch1: librepository-1.1.2.java11.patch
Patch2: librepository-1.1.3-remove-ant-contrib-support.patch
Patch3: librepository-1.1.3-remove-commons-logging.patch
Source44: import.info

%description
LibRepository provides a simple abstraction layer to access bulk content that
is organized in a hierarchical layer.

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
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.1.3-alt2_34jpp11
- update

* Tue Jun 15 2021 Igor Vlasenko <viy@altlinux.org> 1.1.3-alt2_30jpp11
- fc34 update

* Mon Jun 14 2021 Igor Vlasenko <viy@altlinux.org> 1.1.3-alt2_29jpp11
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.1.3-alt1_29jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.1.3-alt1_27jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_21jpp8
- update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_19jpp8
- fc update & java 8 build

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_17jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_16jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_5jpp7
- new version

