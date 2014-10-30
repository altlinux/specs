Name: mp3splt
Version: 2.6.1b
Release: alt1

Summary: utility to split mp3, ogg and flac files without decoding
License: GPLv2+
Group: Sound
Url: http://mp3splt.sourceforge.net/mp3splt_page/home.php
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar.gz

BuildRequires: libmp3splt-devel >= 0.9.1b

%description
Mp3Splt is a command line utility to split mp3, ogg and flac files
selecting a begin and an end time position, without decoding. It's very
useful to split large mp3/ogg to make smaller files or to split entire
albums to obtain original tracks. If you want to split an album, you can
select split points and filenames manually or you can get them
automatically from CDDB (internet or a local file) or from .cue files.
Supports also automatic silence split, that can be used also to adjust
cddb/cue splitpoints. You can extract tracks from Mp3Wrap or AlbumWrap
files in few seconds.

%prep
%setup

%build
%configure --enable-oggsplt_symlink \
	--enable-flacsplt_symlink
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/flacsplt
%_bindir/oggsplt
%_man1dir/%name.1*
%_man1dir/flacsplt.1.*
%_man1dir/oggsplt.1.*

%changelog
* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 2.6.1b-alt1
- 2.6.1b

* Thu Dec 12 2013 Yuri N. Sedunov <aris@altlinux.org> 2.6-alt1
- 2.6

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jun 14 2009 Alex V. Myltsev <avm@altlinux.ru> 2.2.5-alt1
- New version.

* Sun Aug 12 2007 Alex V. Myltsev <avm@altlinux.ru> 2.2-alt1.rc1
- Initial build for Sisyphus.

