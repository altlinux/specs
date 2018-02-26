Name: libmp3splt
Version: 0.5.6
Release: alt1.1

Summary: library for mp3splt, a mp3/ogg splitter
License: GPLv2 or later
Group: Sound
Url: http://mp3splt.sourceforge.net/mp3splt_page/home.php
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar
Source1: %name.ver
Patch0: %name-0.5-alt-cue-get-year.patch
Patch1: %name-0.5.6-alt-uninclude-ltdl.patch
Patch2: %name-0.5.6-alt-version-script.patch

BuildRequires: libltdl-devel libmad-devel libogg-devel libvorbis-devel libid3tag-devel

# mp3splt 2.2-alt1.rc1 was built with an RC version of libmp3splt,
# and this version does not maintain binary compatibility with it.
# Remove this clause when the soname is no longer libmp3splt.so.0.
Conflicts: mp3splt < 2.2.5-alt1

%description
Core library for mp3splt, a mp3/ogg splitter.

%package devel
Summary: development files for libmp3splt
Group: Development/C
Requires: %name = %version-%release, libvorbis-devel, libmad-devel

%description devel
Development files for libmp3splt.

%prep
%setup
autoreconf -fisv
%patch0 -p1 -z .cue-year
%patch1 -p2 -z .uninclude-ltdl
%patch2 -p2 -z .version-script
cp %SOURCE1 src/

%build
%configure \
	--disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/%name.so.*
%dir %_libdir/%name
%_libdir/%name/*.so*

%files devel
%_libdir/%name.so
%_includedir/%name
%_datadir/aclocal/mp3splt.m4

%changelog
* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1.1
- rebuild for set:provides by request of mithraen

* Wed Jan 14 2009 Alexander Myltsev <avm@altlinux.ru> 0.5.6-alt1
- New version.

* Sun Aug 12 2007 Alex V. Myltsev <avm@altlinux.ru> 0.4-alt1.rc1
- Initial build for Sisyphus.

