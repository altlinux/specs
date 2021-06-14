Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: mvn(commons-logging:commons-logging-api) unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: pentaho-reporting-flow-engine
Version: 0.9.4
Release: alt2_19jpp8
Summary: Pentaho Flow Reporting Engine
License: LGPLv2+
Epoch: 1
Source: http://downloads.sourceforge.net/jfreereport/flow-engine-%{version}.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant jpackage-utils libbase libserializer
BuildRequires: libloader libfonts pentaho-libxml xml-commons-apis
BuildRequires: librepository sac flute liblayout libformula
Requires: jpackage-utils libbase >= 1.1.3 libfonts >= 1.1.3
Requires: pentaho-libxml libformula >= 1.1.3 librepository >= 1.1.3
Requires: sac flute liblayout >= 0.2.10 libserializer
BuildArch: noarch
Source44: import.info

%description
Pentaho Reporting Flow Engine is a free Java report library, formerly
known as 'JFreeReport'

%package javadoc
Group: Development/Documentation
Summary: Javadoc for %{name}
Requires: %{name} = 1:%{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
mkdir -p lib
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib commons-logging-api libbase libloader \
    libfonts libxml jaxp libformula librepository sac flute liblayout \
    libserializer

%build
ant jar javadoc

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/flow-engine.jar $RPM_BUILD_ROOT%{_javadir}/flow-engine.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp build/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jun 14 2021 Igor Vlasenko <viy@altlinux.org> 1:0.9.4-alt2_19jpp8
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_19jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_17jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_14jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.9.4-alt1_6jpp7
- new version

