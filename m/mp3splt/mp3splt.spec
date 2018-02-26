Name: mp3splt
Version: 2.2.5
Release: alt1

Summary: utility to split mp3 and ogg files without decoding
License: GPLv2 or later
Group: Sound
Url: http://mp3splt.sourceforge.net/mp3splt_page/home.php
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sun Aug 12 2007
BuildRequires: libmp3splt-devel

%description
Mp3Splt is a utility to split mp3 and ogg files selecting a begin and
an end time position, without decoding. It's very useful to split
large mp3/ogg to make smaller files or to split entire albums to
obtain original tracks. If you want to split an album, you can select
split points and filenames manually or you can get them automatically
from CDDB (internet or a local file) or from .cue files. Supports also
automatic silence split, that can be used also to adjust cddb/cue
splitpoints. You can extract tracks from Mp3Wrap or AlbumWrap files in
few seconds.

%prep
%setup

%build
%configure --with-mp3splt-includes=%_includedir/libmp3splt
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sun Jun 14 2009 Alex V. Myltsev <avm@altlinux.ru> 2.2.5-alt1
- New version.

* Sun Aug 12 2007 Alex V. Myltsev <avm@altlinux.ru> 2.2-alt1.rc1
- Initial build for Sisyphus.

