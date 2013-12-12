%define api_ver 0

Name: libmp3splt
Version: 0.9.0
Release: alt1

Summary: library for mp3splt, a mp3/ogg/flac splitter
License: GPLv2+
Group: System/Libraries
Url: http://mp3splt.sourceforge.net/mp3splt_page/home.php
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar.gz
BuildRequires: libltdl-devel libpcre-devel libmad-devel libogg-devel
BuildRequires: libvorbis-devel libid3tag-devel libflac-devel
BuildRequires: doxygen graphviz

%description
Core library for mp3splt, a mp3/ogg/glac splitter.

%package devel
Summary: development files for libmp3splt
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for libmp3splt.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

%find_lang %name%api_ver

%files -f %name%api_ver.lang
%_libdir/%name.so.*
%dir %_libdir/%name%api_ver
%_libdir/%name%api_ver/*.so*
%exclude %_libdir/%name%api_ver/*.la

%files devel
%_libdir/%name.so
%_includedir/%name/
%_pkgconfigdir/*.pc
%_datadir/doc/%name/

%changelog
* Thu Dec 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0
- removed obsolete patches
- flac support enabled

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5.6-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jan 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1.1
- rebuild for set:provides by request of mithraen

* Wed Jan 14 2009 Alexander Myltsev <avm@altlinux.ru> 0.5.6-alt1
- New version.

* Sun Aug 12 2007 Alex V. Myltsev <avm@altlinux.ru> 0.4-alt1.rc1
- Initial build for Sisyphus.

