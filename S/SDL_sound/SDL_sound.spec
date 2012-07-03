Name: SDL_sound
Version: 1.0.3
Release: alt3.2
%define lib_name lib%name

Summary: An abstract soundfile decoder
License: LGPLv2+
Group: System/Libraries
URL: http://icculus.org/SDL_sound/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
# http://icculus.org/SDL_sound/downloads/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-1.0.3-autotools.patch

# Automatically added by buildreq on Fri Nov 19 2010
BuildRequires: doxygen libSDL-devel libflac-devel libmikmod-devel libmodplug-devel libspeex-devel libvorbis-devel libphysfs-devel
%ifnarch %arm
BuildRequires: libsmpeg-devel
%endif

%package -n %lib_name
Summary: An abstract soundfile decoder
Group: System/Libraries
Provides: %name = %version-%release

%package -n %lib_name-devel
Summary: Header files and more to develop SDL_sound applications
Group: Development/C
Requires: %lib_name = %version-%release
Provides: %name-devel = %version-%release

%package -n %lib_name-devel-static
Summary: Static libraries for develop SDL_sound applications
Group: Development/C
Requires: %lib_name-devel = %version-%release

%description
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3.  It is meant to make
the programmer's sound playback tasks simpler.  The programmer
gives SDL_sound a filename, or feeds it data directly from one of
many sources, and then reads the decoded waveform data back at her
leisure.  If resource constraints are a concern, SDL_sound can process
sound data in programmer-specified blocks.  Alternately, SDL_sound
can decode a whole sound file and hand back a single pointer to the
whole waveform.  SDL_sound can also handle sample rate, audio format,
and channel conversion on-the-fly and behind-the-scenes, if the
programmer desires.

%description -n %lib_name
SDL_sound is a library that handles the decoding of several popular
sound file formats, such as .WAV and .MP3.  It is meant to make
the programmer's sound playback tasks simpler.  The programmer
gives SDL_sound a filename, or feeds it data directly from one of
many sources, and then reads the decoded waveform data back at her
leisure.  If resource constraints are a concern, SDL_sound can process
sound data in programmer-specified blocks.  Alternately, SDL_sound
can decode a whole sound file and hand back a single pointer to the
whole waveform.  SDL_sound can also handle sample rate, audio format,
and channel conversion on-the-fly and behind-the-scenes, if the
programmer desires.

%description -n %lib_name-devel
Header files and more to develop SDL_sound applications.

%description -n %lib_name-devel-static
Static library for develop SDL_sound applications.

%prep
%setup
%patch -p1

%build
%add_optflags -I%_includedir/smpeg
%autoreconf
%configure

%make_build
doxygen

%install
%makeinstall_std
mkdir -p %buildroot%_man3dir
cp -a docs/man/man3/* %buildroot%_man3dir/
pushd %buildroot%_man3dir
mv actual.3 Sound_Sample::actual.3
mv author.3 Sound_DecoderInfo::author.3
mv buffer.3 Sound_Sample::buffer.3
mv buffer_size.3 Sound_Sameple::buffer_size.3
mv channels.3 Sound_AudioInfo::channels.3
mv decoder.3 Sound_Sample::decoder.3
mv description.3 Sound_DecoderInfo::description.3
mv desired.3 Sound_Sample::desired.3
mv extensions.3 Sound_DecoderInfo::extensions.3
mv flags.3 Sound_Sample::flags.3
mv format.3 Sound_AudioInfo::format.3
mv major.3 Sound_Version::major.3
mv minor.3 Sound_Version::minor.3
mv opaque.3 Sound_Sample::opaque.3
mv patch.3 Sound_Version::patch.3
mv rate.3 Sound_AudioInfo::rate.3
mv url.3 Sound_DecoderInfo::url.3
popd

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
cp -a CHANGELOG COPYING CREDITS README docs/html %buildroot%docdir/


%files -n %lib_name
%_bindir/*
%_libdir/*.so.*
%docdir
%exclude %docdir/html

%files -n %lib_name-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*
%dir %docdir
%docdir/html

%changelog
* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt3.2
- Rebuilt for debuginfo

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt3.1
- Rebuilt with libphysfs 2.0.2

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt3
- Fixed linkage, dropped static subpackage.
- Fixed interpackage dependencies.
- Fixed packaging of documentation.
- Updated build requirements.
- Updated package descriptions.
- Enabled FLAC support.

* Thu Apr 23 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.3-alt2
- Delete obsoleted post_ldconfig and postun_ldconfig
- Remove /usr/share/man/man3/major.3.gz and
  /usr/share/man/man3/minor.3.gz (ALT #19718)

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.3-alt1
- New version
- Convert spec to UTF-8

* Wed Jan 24 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.1-alt2
- Delete self-obsolete

* Mon Jan 22 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.1-alt1
- Delete /usr/share/man/man3/buffer (for fix #10696)

* Fri Feb 17 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.1-alt0
- initial build
