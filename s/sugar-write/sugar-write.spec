# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/icon-slicer /usr/bin/pygtk-codegen-2.0 libICE-devel libSM-devel libalsa-devel libgtk+3-gir-devel pkgconfig(cairo) pkgconfig(gdk-pixbuf-2.0) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) pkgconfig(ice) python-devel
# END SourceDeps(oneline)
Name: sugar-write
Version: 79
Release: alt1_1
Summary: Word processor for Sugar
Group: Graphical desktop/Sugar
License: GPLv2+
URL: http://wiki.sugarlabs.org/go/Activities/Write
Source0: http://download.sugarlabs.org/sources/sucrose/fructose/Write/Write-%{version}.tar.bz2

BuildRequires:  sugar-toolkit
BuildRequires:  sugar-toolkit
BuildRequires:  gettext

Requires: sugar python-module-telepathy
Requires: python-module-abiword

BuildArch: noarch
Source44: import.info
Provides: sugar-write-activity = %version
Obsoletes: sugar-write-activity < %version
Conflicts: sugar-write-activity < %version

%description
The Write activity provides a word processor for the Sugar interface.

%prep
%setup -q -n Write-%{version}

%build
python ./setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{sugaractivitydir}
python ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}

%find_lang org.laptop.AbiWordActivity


%files -f  org.laptop.AbiWordActivity.lang
%doc NEWS
%{sugaractivitydir}/Write.activity/


%changelog
* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 79-alt1_1
- new version; import from fc17 release

