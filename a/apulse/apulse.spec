Name: apulse
Version: 0.1.7
Release: alt1

Summary: PulseAudio emulation for ALSA
License: MIT, LGPLv2.1+
Group: System/Libraries

Url: https://github.com/i-rinat/apulse
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Source100: %name.watch

# Automatically added by buildreq on Tue Sep 23 2014
# optimized out: cmake-modules libstdc++-devel pkg-config
BuildRequires: cmake gcc-c++ glib2-devel libalsa-devel

%description
PulseAudio emulation for ALSA.  Usage:

$ apulse <program-name> [parameters]

%prep
%setup
%patch -p1

%build
%cmake_insource -DAPULSEPATH=%_libdir/apulse
%make_build # VERBOSE=1

%install
%makeinstall_std
%find_lang %name

%ifarch x86_64
sed 's!/lib64/!/lib/!g' < %buildroot%_bindir/apulse > %buildroot%_bindir/i586-apulse
chmod 0755 %buildroot%_bindir/i586-apulse
%endif

%files -f %name.lang
%_bindir/apulse

%ifarch x86_64
%_bindir/i586-apulse
%endif
%_libdir/apulse/

%changelog
* Thu Jan 14 2016 Denis Smirnov <mithraen@altlinux.ru> 0.1.7-alt1
- new version 0.1.7

* Fri Jun 19 2015 Denis Smirnov <mithraen@altlinux.ru> 0.1.6-alt1
- new version 0.1.6

* Fri Dec 19 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.5-alt1
- new version 0.1.5

* Thu Nov 20 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Tue Oct 21 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.3-alt1
- new version 0.1.3
- really disable debug output

* Sun Oct 19 2014 Michael Shigorin <mike@altlinux.org> 0.1.2-alt2
- *disable* debug output

* Wed Oct 08 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Thu Oct 02 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.1-alt1
- 0.1.1

* Wed Sep 24 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.0-alt2
- minor spec cleanup (thanks to mike@)
- add i586-apulse to x86_64 builds (for use with i586-apulse)

* Tue Sep 23 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.0-alt1
- first build for Sisyphus
