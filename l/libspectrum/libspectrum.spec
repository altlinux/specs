Name:          libspectrum
Version:       1.4.5
Release:       alt0.1
Summary:       ZX Spectrum emulation shared library
License:       GPLv2
Group:         Emulators
Url:           https://sourceforge.net/projects/fuse-emulator/
Vcs:           https://git.code.sf.net/p/fuse-emulator/libspectrum
Packager:      ZX Spectrum Development Team <spectrum@packages.altlinux.org>

Source:        %name-%version.tar
# libbzip2: support for certain compressed files.
BuildRequires: bzlib-devel
# libaudiofile: support for loading from .wav files.
BuildRequires: libaudiofile-devel
# zlib: support for compressed RZX files.
BuildRequires: zlib-devel
# libgcrypt: the ability to digitally sign RZX files (note that Fuse requires version 1.1.42 or later).
BuildRequires: libgcrypt-devel
BuildRequires: glib2-devel
BuildRequires: libgpg-error-devel
BuildRequires: pkgconfig
BuildRequires: gcc-c++

%package       devel
Summary:       ZX Spectrum emulation library, header files
Group:         Emulators
Requires:      %name = %version-%release

%description
libspectrum is a library which is designed to make the input and
output of ZX Spectrum emulator files slightly easier than it would be
otherwise. It should hopefully compile and run on Unix-based systems,
Win32 and Mac OS X.

%description devel
libspectrum is a library which is designed to make the input and
output of ZX Spectrum emulator files slightly easier than it would be
otherwise. It should hopefully compile and run on Unix-based systems,
Win32 and Mac OS X.

This package contains header files for %name.

%prep
%setup
# for 1.4.4 TODO
sed "s/1.4.4/1.4.5/" -i ./configure.ac

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%_man3dir/*

%files devel
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_includedir/%name.h

%changelog
* Fri Dec 11 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.5-alt0.1
- ^ 1.4.1 -> 1.4.5[gamma]
- + support for bzlib, libaudiofile, and zlib

* Thu Dec 06 2018 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- Removed sources from gear.
- Bump to 1.4.1.

* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.qa1
- NMU: rebuilt with libgcrypt.so.11 -> libgcrypt.so.20.

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Sat Dec 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2
- NMU: new version 1.0.0
- release alt2 to resolve accidental conflict with autoimports

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.3.0.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Fri Jan 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.0.1-alt2
- cleanup spec

* Sun May 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3.0.1-alt1
- new version 0.3.0.1 (with rpmrb script)

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- NMU: new version (GTK2)

* Tue Sep 30 2003 Alexey Tourbin <at@altlinux.ru> 0.2.0-alt1
- initial revision
