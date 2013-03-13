# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
Name: sugar-terminal
Version: 41
Release: alt1_1
Summary: Terminal for Sugar
Group: Graphical desktop/Sugar
License: GPLv2+
URL: http://wiki.laptop.org/go/Terminal
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Terminal/Terminal-%{version}.tar.bz2

BuildRequires: python-devel
BuildRequires: sugar-base
BuildRequires: sugar-toolkit-gtk3
BuildRequires: gettext

Requires: sugar
Requires: vte3

BuildArch: noarch
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity
Obsoletes: sugar-terminal-activity < %version
Conflicts: sugar-terminal-activity < %version

%description
The terminal activity provides a vte-based terminal for the Sugar interface.

%prep
%setup -q -n Terminal-%{version}

# remove bogus pseudo.po
rm -vf po/pseudo.po

%build
python ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.Terminal

%files -f org.laptop.Terminal.lang
%doc NEWS README
%{sugaractivitydir}/Terminal.activity/

%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 41-alt1_1
- update from fc18 release

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 39-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 36-alt1_1
- new version; import from fc17 release

