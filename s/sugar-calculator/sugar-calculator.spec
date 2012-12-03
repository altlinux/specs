# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
Name: sugar-calculator
Version: 40
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
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 40-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 39-alt1_1
- new version; import from fc17 release

