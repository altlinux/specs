Group: File tools
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/perl pkgconfig(glib-2.0) pkgconfig(gtk+-3.0) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-dialogs
Version:        1.5.0
Release:        alt2_2
Summary:        Displays dialog boxes from shell scripts
License:        LGPLv2+ and GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(gtk+)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  rarian-compat
BuildRequires:	libmatenotify-devel
Source44: import.info

%description
Displays dialog boxes from shell scripts.

%prep
%setup -q


%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static \
           --enable-libmatenotify

make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}

%find_lang %{name} --with-gnome


%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/gdialog
%{_bindir}/matedialog
%{_mandir}/man1/*
%{_datadir}/mate/help/matedialog/
%{_datadir}/omf/matedialog/
%{_datadir}/matedialog/
%exclude %_bindir/gdialog

%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_2
- new fc release

* Sat Nov 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_1
- dropped gdialog compat script (conflicts with real gdialog)

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

