Name: libfilteraudio
Version: 0.0.0
Release: alt0.612c5a102550

Summary: Lightweight audio filtering library made from webrtc code

License: MIT
Group: Networking/Instant messaging
Url: https://github.com/irungentoo/filter_audio

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/irungentoo/filter_audio
Source: %name-%version.tar

#manually removed: python3 ruby ruby-stdlibs
# Automatically added by buildreq on Sun Jun 07 2015
# optimized out: python3-base
BuildRequires: libdb4-devel

%description
Lightweight audio filtering library made from webrtc code.

%package devel
Summary: Header files for the %name library
Group: Development/C++
Requires: %name = %version-%release

%description devel
Lightweight audio filtering library made from webrtc code.

This package contains the header files.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_lib
rm -f %buildroot%_libdir/%name.a

%files
%_libdir/%name.so.0*

%files devel
%_libdir/%name.so
%_includedir/filter_audio.h
%_pkgconfigdir/filteraudio.pc

%changelog
* Sun Jun 07 2015 Vitaly Lipatov <lav@altlinux.ru> 0.0.0-alt0.612c5a102550
- initial build for ALT Linux Sisyphus
