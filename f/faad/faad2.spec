%define soversion 2

Name: faad
Version: 2.7
Release: alt4

Packager: Pavlov Konstantin <thresh@altlinux.ru>
Summary: FAAD is a Freeware Advanced Audio Decoder
License: GPL
Group: Sound
Url: http://www.audiocoding.com

Patch1: faad2-alt-fix-no-ext-segfault.patch
Patch2: faad2-alt-make-mp4ff-shared.patch

Source: http://prdownloads.sourceforge.net/faac/%{name}2-%version.tar.bz2

%define libsndfile_ver 1.0.5

Requires: lib%name%soversion = %version-%release

BuildPreReq: libsndfile >= %libsndfile_ver

BuildRequires: gcc-c++ glib-devel gtk+-devel id3lib-devel
BuildRequires: libstdc++-devel libxmms-devel zlib-devel

%description
FAAD is a LC, MAIN and LTP profile MPEG2 and MPEG-4 AAC decoder.

%package -n lib%name%soversion
Summary: Freeware Advanced Audio Decoder (FAAD) libraries
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n lib%name%soversion
This package contains Freeware Advanced Audio Decoder (FAAD) shared
libraries.

%package -n lib%name-devel
Summary: Development files for the FAAD AAC decoder libraries
Group: Development/C++
Requires: lib%name%soversion = %version-%release
Requires: libsndfile-devel >= %libsndfile_ver

%description -n lib%name-devel
This package provides header files development libraries and
documentation for lib%name.

%package -n xmms-in-faad
Summary: FAAD input plugin for XMMS
Group: Sound
Requires: lib%name%soversion = %version-%release
Requires: xmms
Provides: xmms-input-faad = %version-%release
Obsoletes: xmms-input-faad <= %version-%release

%description -n xmms-in-faad
This package provides input plugin allowing XMMS to read .aac and .mp4
files.

%prep
%setup -q -n %{name}2-%version

%patch1 -p2
%patch2 -p2

find ./ -type f -name "Makefile*" -print0 | \
xargs -r0 %__subst 's,^\(CFLAGS\),AM_\1,g
		    s,^\(LDFLAGS\),AM_\1,g
		    s,^[[:blank:]*],\t,' --

%define _xmms_input_plugin_dir %(xmms-config --input-plugin-dir)

%build
%add_optflags %optflags_shared
#%_buildshell ./bootstrap
autoreconf -isfv
%configure --disable-static \
	    --without-drm \
	    --with-xmms

%make_build

%install
%make_install DESTDIR=%buildroot install

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files
%_bindir/*
#%_man1dir/*

%files -n lib%name%soversion
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README TODO

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n xmms-in-faad
%_xmms_input_plugin_dir/*
%doc plugins/xmms/{AUTHORS,ChangeLog,NEWS,README,TODO}

%changelog
* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt4
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt3
- Rebuilt for soname set-versions

* Wed Aug 12 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.7-alt2
- made libmp4ff shared and installable (sbolshakov@).

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.7-alt1
- 2.7 release.
- Remove unneeded ldconfig calls.
- libfaad package renamed to libfaad2.

* Tue Apr 08 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.6.1-alt4
- Disable DRM support: fixes #14873.

* Tue Mar 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.6.1-alt3
- Fix #8750.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.6.1-alt2
- Fix #13893: renamed xmms-input-faad to xmms-in-faad.

* Tue Nov 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.6.1-alt1
- 2.6.1 release.

* Mon Oct 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.6-alt1
- 2.6 release. 

* Tue Jul 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt3.20040923
- Tuned buildrequires.

* Tue Jul 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0-alt2.20040923
- Added gcc4 patch.

* Thu Jan 27 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt1.2_20040923
- libfaad do not more provides libmp4v2.

* Tue Jan 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt1.1_20040923
- updated to 20040923 cvs snapshot.

* Mon May 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt1
- 2.0 release.

* Mon Dec 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt0.7rc3
- install more headers so that libfaad{,-devel} will provide
  libmp4v2{,-devel}.

* Mon Dec 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt0.6rc3
- do not package .la files.

* Thu Nov 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0-alt0.5rc3
- 2.0rc3.

* Sat Jun 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1-alt1
- First build for Sisyphus.

