# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: mp3blaster
Version: 3.2.5
Release: alt1

Group: Sound
Summary: An interactive text-console based mp3 player

License: GPLv2
Url: http://mp3blaster.sourceforge.net
Packager: Slava Semushin <php-coder@altlinux.ru>

Source: http://easynews.dl.sourceforge.net/sourceforge/mp3blaster/mp3blaster-%version.tar.gz

Patch1: mp3blaster-3.2.0-alt-id3cyr.patch
Patch2: mp3blaster-3.2.0-alt-id3show.patch
Patch3: mp3blaster-alt-makefile-system_getopt.patch

BuildRequires: gcc-c++ libncurses-devel libstdc++-devel

%description
Mp3blaster is an audio player with a user-friendly interface that will run
on any text console. The interface is built using ncurses, and features all
common audio player controls. The playlist editor is very flexible and allows
nested groups (albums). Supported audio media: mp3, ogg vorbis, wav, sid and
streaming mp3 over HTTP.

%prep
%setup
%patch1 -p1

# remove own getopt version
%patch3 -p2
rm -fv -- src/getopt*

%build
%autoreconf
%configure
%make_build --silent --no-print-directory

%install
%makeinstall_std --silent --no-print-directory

%files
%doc AUTHORS ChangeLog CREDITS README TODO
%_bindir/mp3blaster
%_bindir/mp3tag
%_bindir/splay
%_bindir/nmixer
%_datadir/%name/
%_man1dir/mp3blaster.1.*
%_man1dir/nmixer.1.*
%_man1dir/splay.1.*

%changelog
* Sun Apr 12 2009 Slava Semushin <php-coder@altlinux.ru> 3.2.5-alt1
- Updated to 3.2.5
- New maintainer
- Updated Url tag
- Updated Summary field
- More proper License tag
- Exclude useless COPYING, INSTALL and NEWS files from package
- Include CREDITS file to package
- Directory /usr/share/mp3blaster now belongs to package
- Enabled _unpackaged_files_terminate_build

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.2.0-alt9.1
- Rebuilt with libstdc++.so.6.
- Remove gcc3.3-c++ and libstdc++3.3-devel from BuildReq.

* Wed May 12 2004 Nick S. Grechukh <gns@altlinux.ru> 3.2.0-alt9
- spec cleaned as for alt-packaging

* Wed May 12 2004 Nick S. Grechukh <gns@altlinux.ru> 3.2.0-alt7
- fixed packager

* Tue May 10 2004 Nick S. Grechukh <gns@altlinux.ru> 3.2.0-alt6
- added buldreq
- fixed building on sisyphus - explicit req gcc3.3

* Wed Feb 12 2004 Nick S. Grechukh <ngrechukh@ua.fm> 3.2.0-alt2
- applied id3show.patch

* Wed Jan 28 2004 Nick S. Grechukh <ngrechukh@ua.fm> 3.2.0-alt2
- applied own id3cyr.patch for correct display id3 with ascii>127.

* Mon Jan 26 2004 Nick S. Grechukh <ngrechukh@ua.fm> 3.2.0-alt1
- first build for Sisyphus
