# prevent perl.req to fail
%set_perl_req_method relaxed
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%_datadir/shutter/resources/modules'
# run "buildreq-src --update --spec shutter.spec ." to update BuildRequires below
# note: remove perl(Furl/HTTP.pm) as it is optional dependency from autoimports
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp/Always.pm) perl(Encode.pm) perl(Encode/Locale.pm) perl(File/Copy/Recursive.pm) perl(File/Which.pm) perl(Glib.pm) perl(Glib/Object/Introspection.pm) perl(Glib/Object/Subclass.pm) perl(GooCanvas2.pm) perl(GooCanvas2/CairoTypes.pm) perl(Gtk3.pm) perl(Gtk3/ImageView.pm) perl(HTTP/Request.pm) perl(HTTP/Request/Common.pm) perl(HTTP/Status.pm) perl(IO/Socket/SSL.pm) perl(Image/Magick.pm) perl(JSON/MaybeXS.pm) perl(LWP/UserAgent.pm) perl(Locale/gettext.pm) perl(Net/DBus.pm) perl(Net/DBus/Reactor.pm) perl(Net/FTP.pm) perl(Net/OAuth.pm) perl(Number/Bytes/Human.pm) perl(Pango.pm) perl(Path/Class.pm) perl(Pod/Usage.pm) perl(Proc/Killfam.pm) perl(Proc/Simple.pm) perl(Sort/Naturally.pm) perl(URI.pm) perl(URI/Escape.pm) perl(URI/Split.pm) perl(WWW/Mechanize.pm) perl(WebService/Gyazo/B.pm)
BuildRequires: perl(X11/Protocol.pm) perl(XML/Simple.pm) perl(diagnostics.pm)
# END SourceDeps(oneline)
Name: shutter
Version: 0.99.2
Release: alt1

Summary: Shutter is a feature-rich screenshot program
License: GPLv3+
Group: Graphics

Url: http://shutter-project.org/

# https://github.com/shutter-project/shutter.git
Source: shutter-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: libwnck3-gir

Requires: libwnck3-gir
Requires: perl-GooCanvas2-CairoTypes
Requires: perl-Number-Bytes-Human
Requires: perl-File-Which
Requires: perl-File-Copy-Recursive
Requires: perl-Proc-Simple
Requires: perl-Sort-Naturally
Requires: perl-Regexp-Parser
Requires: perl-devel
Requires: perl-Perl-Tidy
Requires: perl-Carp-Always
Requires: perl-GooCanvas2
Requires: libgoocanvas2
Requires: libgoocanvas2-gir

%description
Shutter is a feature-rich screenshot program. You can take a screenshot of a
specific area, window, your whole screen, or even a Web site, apply different
effects to it, draw on it to highlight points, and then upload to an image
hosting site, all within one window.

%prep
%setup

subst 's/Application;/Graphics;2DGraphics;RasterGraphics;/' share/applications/shutter.desktop

# in external library
rm share/shutter/resources/modules/X11/Protocol/Ext/XFIXES.pm
%build
./po2mo.sh

%install
install -pDm 755 bin/shutter %buildroot%_bindir/shutter
cp -a share %buildroot/usr

%find_lang shutter
%find_lang --append --output=shutter.lang shutter-plugins shutter-upload-plugins

%files -f shutter.lang
%doc COPYING README
%_bindir/*
%_datadir/shutter
%_datadir/appdata/shutter.appdata.xml
%_man1dir/*
%_desktopdir/*
%_pixmapsdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/128x128/*
%_iconsdir/hicolor/192x192/*
%_iconsdir/hicolor/22x22/*
%_iconsdir/hicolor/24x24/*
%_iconsdir/hicolor/256x256/*
%_iconsdir/hicolor/36x36/*
%_iconsdir/hicolor/64x64/*
%_iconsdir/hicolor/72x72/*
%_iconsdir/hicolor/96x96/*
%_iconsdir/hicolor/scalable/*/*
%dir %_iconsdir/HighContrast
%dir %_iconsdir/HighContrast/scalable
%dir %_iconsdir/HighContrast/scalable/apps
%_iconsdir/HighContrast/scalable/apps/shutter*

%changelog
* Mon Dec 26 2022 Anton Vyatkin <toni@altlinux.org> 0.99.2-alt1
- new version 0.99.2

* Tue Feb 09 2021 Igor Vlasenko <viy@altlinux.ru> 0.95-alt2
- added perl magic

* Mon Feb 08 2021 Grigory Ustinov <grenka@altlinux.org> 0.95-alt1
- Build new version (Closes: #39323).

* Tue Oct 06 2020 Grigory Ustinov <grenka@altlinux.org> 0.94.3-alt1
- Build new version (Closes: #39038).

* Thu Dec 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.94.2-alt3
- Translation fixed

* Tue Oct 02 2018 Grigory Ustinov <grenka@altlinux.org> 0.94.2-alt2
- Remove dependency on ImageMagick.

* Thu Sep 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.94.2-alt1
- Build new version.

* Fri Aug 03 2018 Grigory Ustinov <grenka@altlinux.org> 0.94-alt2
- Fix desktop names (Closes: #35149).

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 0.94-alt1
- Build new version.

* Sat Jul 09 2016 Andrey Cherepanov <cas@altlinux.org> 0.93.1-alt1
- 0.93.1 (ALT #32228)
- Add requires of perl-podlators (ALT #31413)

* Tue Feb 28 2012 Radik Usupov <radik@altlinux.org> 0.88.2-alt1
- 0.88.2
- Added requires (Closes: 26996)

* Fri Feb 10 2012 Radik Usupov <radik@altlinux.org> 0.88.1-alt1
- 0.88.1

* Thu Sep 01 2011 Radik Usupov <radik@altlinux.org> 0.87.3-alt1
- 0.87.3
- New packager

* Mon Sep 13 2010 Victor Forsiuk <force@altlinux.org> 0.86.4-alt1
- 0.86.4

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 0.86.3-alt1
- 0.86.3

* Wed Jun 09 2010 Victor Forsiuk <force@altlinux.org> 0.86.2-alt1
- 0.86.2
- Set relaxed perl.req mode instead of skipping files it fails to process.

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.86.1-alt1
- 0.86.1

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 0.86-alt1
- 0.86

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 0.85.1-alt1
- 0.85.1

* Mon Nov 23 2009 Victor Forsyuk <force@altlinux.org> 0.85-alt1
- 0.85

* Thu Aug 13 2009 Victor Forsyuk <force@altlinux.org> 0.80.1-alt1
- Initial build.
