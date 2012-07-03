Name: pavuk
Version: 0.9.35
Release: alt6.1
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.org>
Summary: Pavuk WWW Graber
Summary(ru_RU.KOI8-R): Вор с WWW - паук
Copyright: GPL
Group: Networking/WWW
URL: https://sourceforge.net/projects/pavuk/
Source: http://dl.sourceforge.net/%name/%name-%version.tar.bz2
Patch: pavuk-0.9.35-altlinux-fix-owerflow.patch
Patch1: pavuk.desktop-1.3-1.5-cvs.patch
Patch2:	pavuk-0.9.35-altlinux-fix-misprint.patch 
Patch3: pavuk-ld-add-needed.patch
Patch4: pavuk-0.9.35-alt-DSO.patch

# Automatically added by buildreq on Thu Oct 27 2005
BuildRequires: fontconfig freetype2 glib2-devel hostinfo libatk-devel libgtk+2-devel libpango-devel libpcre-devel libssl-devel pkgconfig vixie-cron zlib-devel libX11-devel libXext-devel

%description
Pavuk is used to download or mirror web sites or files. It transfers documents
from HTTP, FTP, Gopher and optionally from HTTPS (HTTP over SSL) servers. An
optional GTK GUI allows easy configuration. Many options allow fine-tuning for
the usage scenario. This is an tool for experts and much to complicated for
beginners.

%description -l ru_RU.KOI8-R
Эта программа используется для зеркалирования файлов, расположенных на 
HTTP, FTP, HTTPS и Gopher серверах.

%prep

%setup -q -n %name-%version
%patch -p1
%patch1 -p0
%patch2 -p2
%patch3 -p0 -b .X11
%patch4 -p2

%build

%configure \
        --disable-gnome \
        --enable-utf-8 
#	--disable-socks # --with-regex=pcre
make %{?jobs:-j%jobs}

%make_build

%install

make DESTDIR=$RPM_BUILD_ROOT install

pushd $RPM_BUILD_ROOT/usr/share/icons
mkdir -p $RPM_BUILD_ROOT{%_miconsdir,%_niconsdir,%_liconsdir}
mkdir -p $RPM_BUILD_ROOT%_iconsdir/hicolor/64x64/apps/
mv pavuk_32x32.xpm $RPM_BUILD_ROOT%_niconsdir/%{name}.xpm
mv pavuk_16x16.xpm $RPM_BUILD_ROOT%_miconsdir/%{name}.xpm
mv pavuk_as_icon.xpm $RPM_BUILD_ROOT%_liconsdir/%{name}.xpm
mv pavuk_64x64.xpm $RPM_BUILD_ROOT%_iconsdir/hicolor/64x64/apps/%{name}.xpm
popd

mkdir -p $RPM_BUILD_ROOT%_desktopdir
subst 's,^Encoding,#Encoding,' pavuk.desktop
install -m 644 pavuk.desktop $RPM_BUILD_ROOT%_desktopdir/

%{find_lang} %{name}

%files -f %{name}.lang
#olddoc FAQ 
%doc ABOUT-NLS AUTHORS BUGS ChangeLog COPYING CREDITS INSTALL MAILINGLIST NEWS README TODO 
%doc pavukrc.sample pavuk_authinfo.sample wget-pavuk.HOWTO button_icons/
%_bindir/*
%_niconsdir/*.xpm
%_miconsdir/*.xpm
%_liconsdir/*.xpm
%_iconsdir/hicolor/64x64/apps/%{name}.xpm
%_man1dir/*
%_desktopdir/*.desktop
#_datadir/pixmaps/*.xpm

%changelog 
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.9.35-alt6.1
- Fixed build

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.9.35-alt6
- fixed build

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 1:0.9.35-alt5
- BuildReq: cleanup

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.9.35-alt4.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.9.35-alt4
- removed obsolete update_menu calls

* Tue Jul 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.9.35-alt3
- fixed desktop file (closed repocop warn) 

* Thu Feb 07 2008 Igor Vlasenko <viy@altlinux.ru> 1:0.9.35-alt2
- menu replaced with .desktop

* Wed Feb 28 2007 Igor Vlasenko <viy@altlinux.ru> 1:0.9.35-alt1
- new version
- fixed error (call will always overflow destination buffer) 
  in ip v6 handling (thanks to ldv@ for report).

* Fri Aug 25 2006 Igor Vlasenko <viy@altlinux.ru> 1:0.9.34-alt3
- added %%_niconsdir support

* Mon Feb 06 2006 Igor Vlasenko <viy@altlinux.ru> 1:0.9.34-alt2
- s/xorg-x11-devel-static/xorg-x11-devel/

* Wed Jan 11 2006 Igor Vlasenko <viy@altlinux.ru> 1:0.9.34-alt1
- new version

* Tue Dec 13 2005 Igor Vlasenko <viy@altlinux.ru> 1:0.9.33-alt3
- added epoch:1 to allow upgrade from old-named pavuks

* Thu Oct 27 2005 Igor Vlasenko <viy@altlinux.ru> 0.9.33-alt2
- added support for regexp=pcre
- fixed bug with regexp=pcre

* Tue Oct 11 2005 Igor Vlasenko <viy@altlinux.ru> 0.9.33-alt1
- new version
- added icons in menu

* Thu Apr 21 2005 Igor Vlasenko <viy@altlinux.ru> 0.9.32-alt1
- new version

* Thu Dec 30 2004 Igor Vlasenko <viy@altlinux.ru> 0.9.28-alt3
- fix build for Sisyphus; changed for new version scheme (as current 0.9.31)

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 0.9pl28-alt2
- rebuild

* Fri Jan 04 2002 Rider <rider@altlinux.ru> 0.9pl28-alt1
- 0.9pl28

* Fri Jan 05 2001 AEN <aen@logic.ru>
- adopted for RE

* Fri Dec 15 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.9pl27-1mdk
- updated to 0.9pl27

* Fri Nov 17 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.9pl26-1mdk
- new in contribs
