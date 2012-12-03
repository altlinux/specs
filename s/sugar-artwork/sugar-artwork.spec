# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/icon-slicer pkgconfig(cairo) pkgconfig(gobject-2.0) pkgconfig(gtk+-2.0) python-devel
# END SourceDeps(oneline)
Summary: Artwork for Sugar look-and-feel
Name: sugar-artwork
Version: 0.96.4
Release: alt1_1
URL: http://sugarlabs.org
Group: Graphical desktop/Sugar
License: LGPLv2+
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: gtk2-devel
BuildRequires: libgtk+3-devel
BuildRequires: /usr/bin/luit /usr/bin/oclock /usr/bin/x11perf /usr/bin/x11perfcomp /usr/bin/xclipboard /usr/bin/xclock /usr/bin/xconsole /usr/bin/xcursorgen /usr/bin/xcutsel /usr/bin/xdpr /usr/bin/xeyes /usr/bin/xfd /usr/bin/xfontsel /usr/bin/xload /usr/bin/xlogo /usr/bin/xmag /usr/bin/xmessage /usr/bin/xpr /usr/bin/xvidtune /usr/bin/xwd /usr/bin/xwud
BuildRequires: perl-XML-Parser
BuildRequires: python-module-em
BuildRequires: icon-naming-utils
BuildRequires: icon-slicer

Requires: gtk2 libgtk+3
Source44: import.info
Patch33: sugar-artwork-0.88.0-sugar-1899.patch

%description
sugar-artwork contains the themes and icons that make up the OLPC default 
look and feel.

%prep
%setup -q
%patch33 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post
touch --no-create %{_datadir}/icons/sugar || :

%postun
touch --no-create %{_datadir}/icons/sugar || :

%files
%doc README COPYING

%{_datadir}/icons/sugar
%{_datadir}/themes/sugar-100/gtk-2.0/gtkrc
%{_datadir}/themes/sugar-72/gtk-2.0/gtkrc
%{_libdir}/gtk-2.0/*/engines/*.so

#gtk3
%{_datadir}/themes/sugar-100/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-100/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-100/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-100/gtk-3.0/assets/*
%{_datadir}/themes/sugar-72/gtk-3.0/gtk.css
%{_datadir}/themes/sugar-72/gtk-3.0/gtk-widgets.css
%{_datadir}/themes/sugar-72/gtk-3.0/settings.ini
%{_datadir}/themes/sugar-72/gtk-3.0/assets/*

%changelog
* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.4-alt1_1
- new version; import from fc17 updates

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.2-alt1_1
- new version; import from fc17 release

* Tue Apr 06 2010 Aleksey Lim <alsroot@altlinux.org> 0.88.0-alt1
- Sucrose 0.88.0 release

* Tue Mar 17 2009 Aleksey Lim <alsroot@altlinux.org> 0.84.1-alt1
- update Sucrose to 0.84.0 version

* Sun Feb 15 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.4-alt1
- new Sucrose 0.83.5 release

* Tue Jan 20 2009 Aleksey Lim <alsroot@altlinux.org> 0.83.3-alt1
- new Sucrose 0.83.4 release

* Tue Dec 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.2-alt1
- new upstream release

* Fri Dec 12 2008 Aleksey Lim <alsroot@altlinux.org> 0.83.1-alt1
- Sugar 0.84 release cycle

* Sun Nov 23 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.1-alt2
- change group tag to "Graphical desktop/Sugar"

* Sat Nov 08 2008 Aleksey Lim <alsroot@altlinux.org> 0.82.1-alt1
- first build for ALT Linux Sisyphus
