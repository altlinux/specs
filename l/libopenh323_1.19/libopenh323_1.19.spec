%define origname libopenh323
Name: libopenh323_1.19
Version: 1.19.0.1
Release: alt8

Summary: OpenH323 Library

License: MPL
Group: System/Libraries
Url: http://openh323.sf.net/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: openh323-%version.tar.bz2

Patch: libopenh323.ixjlib.patch

Obsoletes: openh323_1
Conflicts: %origname

# Automatically added by buildreq on Sun Feb 06 2005
BuildRequires: gcc-c++ hostinfo libSDL_sound-devel libexpat-devel libldap-devel
BuildRequires: libsasl2-devel libssl-devel libstdc++-devel

BuildPreReq: libpw1.11-devel libspeex-devel

%set_verify_elf_method textrel=relaxed

%description
This is a Open Source class library for the development of
applications that wish to use the H.323 protocol for multi-media
communications over packet based networks.

%description -l ru_RU.KOI8-R
Это библитека классов с открытыми исходниками для разработки
приложений, которым необходимо использование протокола H.323
для мультимедийного обмена информацией через сети с пакетной
передачей.

%package devel
Summary: OpenH323 development files
Summary(ru_RU.KOI8-R):	Файлы для разработки с OpenH323
Group: Development/C
Requires: %name = %version
Requires: libldap-devel
Requires: libSDL_sound-devel
Requires: libexpat-devel
Obsoletes: openh323_1-devel
Conflicts: %origname-devel

%description devel
Header files and libraries for developing applications that use
OpenH323.

%description devel -l ru_RU.KOI8-R
Заголовочные файлы и библиотеки для разработки приложений,
использующих OpenH323.

%prep
%setup -qn openh323-%version
%patch -p2

%build
%configure --enable-localspeex \
	--enable-shared=yes \
	--enable-static=no \
	--disable-h460
%make_build

%install
%makeinstall_std
install -m644 openh323u.mak.alt %buildroot/%_datadir/openh323/openh323u.mak

#fix doc perms
chmod a+r *.txt *.htm

cd %buildroot/%_libdir
ln -s libh323*.so libopenh323.so

%files
%doc *.txt mpl-1.0.htm
%_libdir/lib*.so.*
%_libdir/pwlib
# for buggy make
%_libdir/*.so

%files devel
%_libdir/*.so
%_includedir/*
%_datadir/openh323

%changelog
* Fri Jul 08 2011 Denis Smirnov <mithraen@altlinux.ru> 1.19.0.1-alt8
- add %_libdir/libopenh323.so

* Wed May 25 2011 Denis Smirnov <mithraen@altlinux.ru> 1.19.0.1-alt7
- rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.19.0.1-alt6
- rebuild with new openssl

* Mon Nov 17 2008 Denis Smirnov <mithraen@altlinux.ru> 1.19.0.1-alt5
- cleanup spec
- remove post/postun ldconfig

* Wed Oct 17 2007 Denis Smirnov <mithraen@altlinux.ru> 1.19.0.1-alt4
- remove #include <linux/compiler.h> from ixjlid.h (Kirill A. Shutemov)

* Mon Mar 05 2007 Denis Smirnov <mithraen@altlinux.ru> 1.19.0.1-alt3
- rebuild with libpw 1.11 cvs

* Thu Sep 21 2006 Denis Smirnov <mithraen@altlinux.ru> 1.19.0.1-alt2
- mak-file fix

* Mon Sep 18 2006 Denis Smirnov <mithraen@altlinux.ru> 1.19.0.1-alt1
- New version

* Tue Jan 10 2006 Denis Ovsienko <pilot@altlinux.ru> 1.15.6-alt1
- forked Vitaly Lipatov's package to make gnomemeeting 1.2.2 work

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.17.1-alt1
- new version (from FC3)
