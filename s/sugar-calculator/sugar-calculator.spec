# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name: sugar-calculator
Version: 41
Release: alt1_1
Summary: Calculator for Sugar
Group: Graphical desktop/Sugar
License: GPLv2+
URL: http://wiki.laptop.org/go/Calculate
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Calculate/Calculate-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  sugar-toolkit
Requires: sugar
BuildArch: noarch
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity
Obsoletes: sugar-calculate-activity < %version
Conflicts: sugar-calculate-activity < %version

%description
The calculate activity provides a calculator for the Sugar interface.

%prep
%setup -q -n Calculate-%{version}

%build
python ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.Calculate

%files -f org.laptop.Calculate.lang
%doc NEWS
%{sugaractivitydir}/Calculate.activity/

%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 41-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 40-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 39-alt1_1
- new version; import from fc17 release

