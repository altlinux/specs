Name: mldonkey
Version: 3.1.6
Release: alt1
Group: Networking/File transfer
Summary: The eDonkey client for Linux/Unix/Windows
URL: https://github.com/ygrek/mldonkey
License: GPL
# git https://github.com/ygrek/mldonkey
Source: %name-%version.tar
Source1: %name.service
Source2: %name.logrotate
Source3: %name.tmpfiles.conf

BuildRequires: bzlib-devel ocaml-camlp4-devel ocaml-lablgtk-devel  fontconfig libfreetype-devel glib2-devel libatk-devel libgd2-devel libjpeg-devel libncurses-devel libpango-devel libpng12-devel librsvg-devel libXpm-devel ocaml-runtime pkgconfig wget zlib-devel
BuildRequires: libgtk+2-devel desktop-file-utils
# for mldonkey-submit
BuildRequires(pre): perl-libwww-perl

Provides: mldonkey-server
Obsoletes: mldonkey-server

%description
MLDonkey - the Open Source eDonkey client
features:
* 100%% OpenSource, GPL license
* runs on Linux, Unix, Solaris, MacOSX, MorphOS and Windows
* Core and Guis are separated or linked.
* written in ObjectiveCaml, with some C and even some Assembler parts.
* OtherNetworksSupported, using separate executables
* built to run as daemon for days, weeks, ever... 

MLdonkey is a peer-to-peer file-sharing client completely written 
in Objective-Caml, that can be used to access the eDonkey2000, 
BitTorrent, Overnet, Direct Connect and Soulseek networks. It supports
downloads from multiple sources and corruption detection, complex search
requests, chat with friends, internationalization, history of search results,
etc...

%package client
Group: Networking/File transfer
Summary: Graphical frontend for mldonkey based on GTK
License: GPL

%description client
The GTK interface for mldonkey provides a convenient way of managing            
all mldonkey operations. It gives details about conected servers,               
downloaded files, friends and lets one search for files in a pleasing           
way.

%prep
%setup -q

%build
cd config
autoconf
cd ../
./configure --enable-largefile \
	    --sysconfdir=%_sysconfdir/mldonkey \
            --sharedstatedir=%_localstatedir/mldonkey \
            --localstatedir=%_localstatedir/mldonkey \
            --prefix=%_prefix \
	     --enable-gui=newgui2 \
	     --disable-rpath \
	     --enable-checks \
	     --enable-ocamlver=%(rpm -q --qf '%%{version}' ocaml) \
#
%make_build
%make_build utils
%__make make_torrent

%install
DONT_GPRINTIFY=1
export DONT_GPRINTIFY
%makeinstall_std

install -dm755 %buildroot%_bindir
install -dm755 %buildroot%_cachedir/%name
install -dm755 %buildroot%_libdir/mldonkey
install -dm755 %buildroot%_localstatedir/mldonkey/incoming
install -pm755 distrib/mldonkey_command %buildroot%_bindir/mldonkey_command
install -pm755 distrib/kill_mldonkey %buildroot%_bindir/kill_mldonkey
for util in copysources mld_hash get_range svg_converter subconv; do
    install -pm755 $util %buildroot%_bindir/$util ;
done
install -pm755 make_torrent %buildroot%_bindir/mldonkey_make_torrent
install -pm755 mlguistarter %buildroot%_bindir/mlguistarter
install -pm755 distrib/mldonkey_previewer %buildroot%_bindir/mldonkey_previewer

%__install -pD -m644 packages/rpm/%name-icon-16.png %buildroot/%_niconsdir/%name.png
%__install -pD -m644 packages/rpm/%name-icon-32.png %buildroot/%_miconsdir/%name.png
%__install -pD -m644 packages/rpm/%name-icon-48.png %buildroot/%_liconsdir/%name.png
desktop-file-install --dir=%buildroot%_desktopdir distrib/%name.desktop
install -dm755 %buildroot%_logdir/%name
install -pDm644 %SOURCE2 %buildroot%_logrotatedir/%name
install -pDm644 %SOURCE1 %buildroot%_unitdir/%name.service
install -pDm644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf
echo -e \
"temp_directory = \"%_var/cache/mldonkey\"\n"\
"incoming_directory = \"%_localstatedir/%name/incoming\"\n"\
"mldonkey_gui = \"%_bindir/mlgui\"\n"\
"mldonkey_bin = \"%_bindir/mldonkey\"\n"\
"log_file = \"%_logdir/mldonkey/mldonkey.log\"\n"\
> %buildroot%_localstatedir/%name/downloads.ini

%pre
getent group _%name >/dev/null || groupadd -r _%name
getent passwd _%name >/dev/null || \
    useradd -r -g _%name -d %_localstatedir/%name -s /sbin/nologin \
    -c "MLDonkey server" _%name


%files
%config(noreplace) %_sysconfdir/logrotate.d/mldonkey
%_unitdir/mldonkey.service
%_tmpfilesdir/%name.conf
%attr(750,_mldonkey,_mldonkey) %dir %_logdir/mldonkey
%attr(750,_mldonkey,_mldonkey) %dir %_cachedir/mldonkey
%attr(750,_mldonkey,_mldonkey) %dir %_localstatedir/mldonkey
%attr(770,_mldonkey,_mldonkey) %dir %_localstatedir/mldonkey/incoming
%config(noreplace) %_localstatedir/mldonkey/downloads.ini
%_bindir/mlnet
%_bindir/copysources
%_bindir/get_range
%_bindir/kill_mldonkey
%_bindir/mlbt
%_bindir/mld_hash
%_bindir/mldc
%_bindir/mldonkey_command
%_bindir/mldonkey
%_bindir/mlgnut
%_bindir/mlslsk
%_bindir/subconv
%_bindir/svg_converter
%_bindir/mldonkey_make_torrent

%files client
%doc  distrib/Authors.txt distrib/Bugs.txt distrib/ChangeLog distrib/Developers.txt Copying.txt
%_bindir/mlgui
%_bindir/mlnet+gui
%_bindir/mlbt+gui
%_bindir/mldc+gui
%_bindir/mldonkey+gui
%_bindir/mldonkey_gui
%_bindir/mlgnut+gui
%_bindir/mlslsk+gui
%_bindir/mlguistarter
%_bindir/mldonkey_previewer
%_desktopdir/%name.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Sun Oct 29 2017 Anton Farygin <rider@altlinux.ru> 3.1.6-alt1
- 3.1.6

* Wed Sep 26 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 3.1.0-alt1.2
- Fixed build

* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.1
- Fixed build

* Wed Jan 18 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 3.1.0-alt1
- 3.1.0
- build without gtk2 gui

* Mon Apr 18 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 3.0.0-alt5
- minor spec cleanup (repocop warn)

* Mon Apr 11 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 3.0.0-alt4
- convert debian menu to freedesktop
- spec cleanup

* Mon Apr 11 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 3.0.0-alt3
- fix build

* Sat Jun 27 2009 gray_graff <gray_graff@altlinux.org> 3.0.0-alt2
- fix repocop warning (pixmap-in-deprecated-location)

* Wed Jun 24 2009 gray_graff <gray_graff@altlinux.org> 3.0.0-alt1
- 3.0.0 (closes: 18503, 20379, 20380)

* Wed Jan 21 2009 L.A. Kostis <lakostis@altlinux.ru> 2.9.7-alt0.1
- 2.9.7.
- remove obsoleted macros.

* Tue Sep 23 2008 L.A. Kostis <lakostis@altlinux.ru> 2.9.6-alt0.1
- 2.9.6.

* Thu Jun 12 2008 L.A. Kostis <lakostis@altlinux.ru> 2.9.5-alt0.1
- 2.9.5.

* Sun Feb 10 2008 L.A. Kostis <lakostis@altlinux.ru> 2.9.3-alt0.1
- Version 2.9.3.
- disable build with exclusive ocaml 3.09.

* Sun Nov 04 2007 L.A. Kostis <lakostis@altlinux.ru> 2.9.2-alt0.1
- 2.9.2.

* Mon Aug 13 2007 L.A. Kostis <lakostis@altlinux.ru> 2.9.0-alt0.1
- 2.9.0.

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 2.8.6-alt0.1
- 2.8.6.

* Thu Apr 12 2007 L.A. Kostis <lakostis@altlinux.ru> 2.8.4-alt0.1
- 2.8.4.
- fix ocaml site-lib detection (ALT-specific patch).
- need more work:
   (firefox extension -> separate package)
   multi-user setup.

* Sat Dec 09 2006 L.A. Kostis <lakostis@altlinux.ru> 2.8.2-alt0.1
- 2.8.2 release.
- add patch for ED2K: Support for file's sizes >4GB
  (http://savannah.nongnu.org/patch/?5599). Tnx to gorev@ for info.
- disable firefox extension (TODO).

* Thu Oct 12 2006 L.A. Kostis <lakostis@altlinux.ru> 2.8.1-alt1
- 2.8.1.

* Sun Sep 17 2006 L.A. Kostis <lakostis@altlinux.ru> 2.8.0-alt1
- 2.8.0.
- update description.
- update requires for gear.
- update mlprogress patch.
- cleanup buildrequires & remove obsoleted apps.

* Sat Aug 05 2006 L.A. Kostis <lakostis@altlinux.ru> 2.7.7-alt1
- 2.7.7.

* Mon Jun 02 2006 LAKostis <lakostis at altlinux.org> 2.7.6-alt1
- 2.7.6;

* Sat May 20 2006 LAKostis <lakostis at altlinux.org> 2.7.5-alt2
- explicitly enable largefile support.

* Sat Apr 15 2006 LAKostis <lakostis at altlinux.org> 2.7.5-alt1
- 2.7.5;

* Sat Mar 25 2006 LAKostis <lakostis at altlinux.org> 2.7.4-alt1
- 2.7.4;
- close #5384;
- build with new ocaml.
- remove gcc-c++ from buildreq (it's optional now);
- strict verify-elf checking.

* Sun Feb 12 2006 LAKostis <lakostis at altlinux.org> 2.7.3-alt1
- 2.7.3.

* Sun Jan 15 2006 LAKostis <lakostis at altlinux.org> 2.7.2-alt1
- 2.7.2.

* Thu Nov 10 2005 LAKostis <lakostis at altlinux.org> 2.6.7-alt1
- 2.6.7.

* Fri Oct 21 2005 LAKostis <lakostis at altlinux.org> 2.6.5-alt0.1
- 2.6.5.
- still NMU :(

* Tue Sep 06 2005 LAKostis <lakostis at altlinux.org> 2.6.4-alt0.1
- 2.6.4.
- add README for firefox-plugin, change it's versioning.
- still NMU :(

* Fri Sep 02 2005 LAKostis <lakostis at altlinux.org> 2.6.3-alt0.3
- NMU.
- 2.6.3
- add newgui2 support.
- add firefox extension package.
- move all nonarch files to /usr/share/mldonkey.

* Tue Oct 05 2004 Nazar Yurpeak <phoenix@altlinux.org> 2.6-alt0.3
- CVS Sep 05 2004
- fixed #5178
- fixed #5244
- updated BuildRequires

* Fri Aug 20 2004 Nazar Yurpeak <phoenix@altlinux.org> 2.6-alt0.2
- 2.6.pre10

* Fri Aug 06 2004 Nazar Yurpeak <phoenix@altlinux.org> 2.6-alt0.1
- 2.6.pre6

* Sat May 15 2004 Nazar Yurpeak <phoenix@altlinux.org> 2.5.21-alt1
- 2.5.21

* Tue Feb 17 2004 Nazar Yurpeak <phoenix@altlinux.org> 2.5.12-alt1
- 2.5.12 CVS Feb 17 2004

* Fri Nov 14 2003 Nazar Yurpeak <phoenix@altlinux.org> 2.5.4-alt1
- 2.5.4

* Mon Oct 06 2003 Nazar Yurpeak <phoenix@altlinux.org> 2.5.3-alt2
- fixed BuildRequires

* Wed Jun 11 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.5.3-alt1
- new version

* Tue May 27 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.5.0-alt1
- new version

* Tue May 27 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.04.01-alt1
- new version
- added menu

* Mon Mar 31 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.04rc1-alt1
- 2.04rc1
- fixed Ocaml version

* Tue Feb 11 2003 Nazar Yurpeak <phoenix@altlinux.ru> 2.00-alt3
- removed Serial
- changed URL
- changed description
- changed mldonkey.sh
- removed make depend

* Mon Oct 28 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1:2.00-alt2
- spec cleanup

* Mon Oct 21 2002 Nazar Yurpeak <phoenix@altlinux.ru> 1:2.00-alt1
- realese 2.00 

