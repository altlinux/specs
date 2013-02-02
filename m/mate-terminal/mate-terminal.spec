Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtk-builder-convert libICE-devel libgio-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(vte-2.90) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary:        Terminal emulator for MATE
Name:           mate-terminal
Version:        1.5.0
Release:        alt1_1
License:        GPLv3+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires: libdconf-devel
BuildRequires: desktop-file-utils
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: libSM-devel
BuildRequires: mate-doc-utils
BuildRequires: mate-common
BuildRequires: rarian-compat
BuildRequires: librarian-devel
BuildRequires: libvte-devel
BuildRequires: gsettings-desktop-schemas-devel
Source44: import.info
Provides: xvt

%description
Mate-terminal is a terminal emulator for MATE. It supports translucent
backgrounds, opening multiple terminals in a single window (tabs) and
clickable URLs.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static                \
           --with-gtk=2.0                  \
           --disable-scrollkeeper          \
           --disable-schemas-compile       \
           --with-gnu-ld                   

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install
%find_lang %{name}

desktop-file-install							\
	--remove-category="MATE"					\
	--add-category="X-Mate"						\
	--delete-original						\
	--dir=%{buildroot}%{_datadir}/applications			\
%{buildroot}%{_datadir}/applications/mate-terminal.desktop
# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt    %_bindir/%name  48
EOF

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mate-terminal
%{_datadir}/mate-terminal
%{_datadir}/mate/help/mate-terminal
%{_datadir}/omf/mate-terminal
%{_datadir}/applications/mate-terminal.desktop
%{_datadir}/glib-2.0/schemas/org.mate.terminal.gschema.xml
%_altdir/%name

%changelog
* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- new fc release

* Tue Dec 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt3_4
- added xvt provides (closes: 28160)

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_4
- added xvt alternative

* Fri Nov 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_4
- rebase to fc

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Thu Jul 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- 20120622 mate snapshot

