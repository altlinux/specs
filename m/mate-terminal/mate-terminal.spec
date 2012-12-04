# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtk-builder-convert /usr/bin/mateconftool-2 libICE-devel pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(vte-2.90) pkgconfig(x11)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires(pre): rpm-macros-mate-conf
Summary: Terminal emulator for MATE
Name: mate-terminal
Version: 1.4.0
Release: alt3_4
License: GPLv3+
Group: Graphical desktop/Other
URL: http://mate-desktop.org
Source0: http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz


# mateconftool-2
Requires(pre):   mate-conf
Requires(post):  mate-conf
Requires(preun): mate-conf

BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: mate-conf-devel
BuildRequires: libglade2-devel
BuildRequires: libmateui-devel
BuildRequires: libvte-devel
BuildRequires: desktop-file-utils
BuildRequires: rarian-compat
BuildRequires: mate-doc-utils
BuildRequires: mate-common
BuildRequires: libSM-devel

Requires: libmate
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
%configure --with-gtk=2.0 \
           --disable-scrollkeeper \
           --disable-schemas-install

make %{?_smp_mflags}


%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

sed -i -e "s/Icon=mate-terminal.png/Icon=mate-terminal/" \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-terminal.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
  --remove-category=MATE                           \
  --add-category=X-Mate                            \
  --add-category=System                            \
  $RPM_BUILD_ROOT%{_datadir}/applications/mate-terminal.desktop

%find_lang mate-terminal
# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt    %_bindir/%name  48
EOF

%post
%mateconf_schema_upgrade mate-terminal

%pre
%mateconf_schema_prepare mate-terminal

%preun
%mateconf_schema_remove mate-terminal


%files -f mate-terminal.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/mate-terminal
%{_datadir}/mate-terminal/
%{_datadir}/mate/help/mate-terminal/
%{_datadir}/omf/mate-terminal/
%{_datadir}/applications/mate-terminal.desktop
%{_sysconfdir}/mateconf/schemas/mate-terminal.schemas
%_altdir/%name

%changelog
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

