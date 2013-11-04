Name: SoundTouch
Version: 1.7.1
Release: alt1

Summary: SoundTouch audio processing library
License: LGPLv2.1
Group: System/Libraries

Url: http://www.surina.net/soundtouch/
Packager: Nazarov Denis <nenderus@altlinux.org>
Source: http://www.surina.net/soundtouch/soundtouch-%version.tar.gz

BuildRequires: gcc-c++

%description
SoundTouch is an open-source audio processing library that allows changing the sound
tempo, pitch and playback rate parameters independently from each other, i.e.:
 - Sound tempo can be increased or decreased while maintaining the original pitch 
 - Sound pitch can be increased or decreased while maintaining the original tempo 
 - Change playback rate that affects both tempo and pitch at the same time 
 - Choose any combination of tempo/pitch/rate

%package -n lib%name
Summary: SoundTouch audio processing library
Group: System/Libraries
Conflicts: libsoundtouch

%description -n lib%name
SoundTouch is an open-source audio processing library that allows changing the sound
tempo, pitch and playback rate parameters independently from each other, i.e.:
 - Sound tempo can be increased or decreased while maintaining the original pitch 
 - Sound pitch can be increased or decreased while maintaining the original tempo 
 - Change playback rate that affects both tempo and pitch at the same time 
 - Choose any combination of tempo/pitch/rate

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %version-%release
Conflicts: libsoundtouch-devel

%description -n lib%name-devel
Contains libraries and header files for developing applications that use %name.

%package -n soundstretch
Summary: SoundStretch Audio Processing Utility
Group: Sound
Requires: lib%name = %version-%release
Conflicts: libsoundtouch

%description -n soundstretch
SoundStretch is a command-line program that performs SoundTouch library effects
on WAV audio files. The program is a source code example how SoundTouch library
routines can be used to process sound in other programs, but it can be used as
a stand-alone audio processing tool as well.

%prep
%setup -n soundtouch

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%prefix/doc
%__rm -rf %buildroot%_libdir/lib%name.la

%files -n lib%name
%doc COPYING.TXT README.html
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/soundtouch
%_includedir/soundtouch/*.h
%_pkgconfigdir/soundtouch.pc
%_libdir/lib%name.so
%_aclocaldir/soundtouch.m4

%files -n soundstretch
%_bindir/soundstretch

%changelog
* Tue Nov 05 2013 Nazarov Denis <nenderus@altlinux.org> 1.7.1-alt1
- Initial build for ALT Linux
