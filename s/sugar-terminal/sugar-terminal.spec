# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
Name: sugar-terminal
Version: 39
Release: alt1_1
Summary: Terminal for Sugar
Group: Graphical desktop/Sugar
License: GPLv2+
URL: http://wiki.laptop.org/go/Terminal
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Terminal/Terminal-%{version}.tar.bz2

BuildRequires: sugar-toolkit
BuildRequires: gettext

Requires: sugar
Requires: vte

BuildArch: noarch
Source44: import.info
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
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 39-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 36-alt1_1
- new version; import from fc17 release

