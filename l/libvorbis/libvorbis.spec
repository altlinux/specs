Name: libvorbis
Version: 1.3.3
Release: alt1

Summary: The Vorbis General Audio Compression Codec
Summary(ru_RU.UTF-8): Аудиокодек Vorbis
License: BSD-style
Group: System/Libraries
Url: http://www.xiph.org/vorbis/
# http://downloads.xiph.org/releases/vorbis/%name-%version.tar.bz2
Source: %name-%version.tar
Patch1: libvorbis-1.3.2-alt-export-symbols.patch
Patch2: libvorbis-1.3.2-alt-add-needed.patch
Patch3: libvorbis-1.3.3-alt-aclocal.patch

BuildRequires: libogg-devel

%def_disable static

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

%description -l ru_RU.UTF-8
Ogg Vorbis - это полностью открытый и свободный формат для сжатия звука.

%package devel
Summary: Development files for libvorbis
Group: Development/C
PreReq: %name = %version-%release
Requires: libogg-devel

%description devel
The libvorbis-devel package contains the header files and documentation
needed to develop applications with libvorbis.

%description devel -l ru_RU.UTF-8
В этом пакете находятся файлы, необходимые для использования libvorbis
в разработке приложений.

%package devel-static
Summary: Static libraries for libvorbis
Group: Development/C
PreReq: %name-devel = %version-%release
Requires: libogg-devel-static

%description devel-static
This package contains development libraries required for packaging
statically linked libvorbis-based software.

%description devel-static -l ru_RU.UTF-8
В этом пакете находятся статические библиотеки, необходимые
для использования libvorbis в разработке статических приложений.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
for f in m4/*.m4; do
	[ ! -f "%_datadir/aclocal/${f##*/}" ] ||
		rm -fv "$f"
done
# restrict lists of global symbols exported by libraries
sed -n 's/^extern[[:space:]]\+[^(]*[[:space:]]\**\([a-z][^()[:space:]]\+\)[[:space:]]*(.*/\1/p' \
	include/vorbis/*.h > lib/libvorbis.sym
# extra symbols required by packages
cat >> lib/libvorbis.sym <<'EOF'
vorbis_window
_ilog
EOF
sort -u -o lib/libvorbis.sym{,}

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std
%define docdir %_docdir/%name-%version
install -pm644 AUTHORS CHANGES COPYING %buildroot%docdir/
%set_verify_elf_method strict

%check
%make_build -k check

%files
%_libdir/*.so.*
%dir %docdir
%docdir/[A-Z]*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_datadir/aclocal/*
%dir %docdir
%docdir/[a-z]*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Feb 15 2012 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt1
- Updated to 1.3.3.

* Sun Dec 11 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt2
- Fixed RPATH issues.

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2.

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.
- Restricted lists of global symbols exported by libraries.

* Tue Aug 18 2009 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- Updated to 1.2.3.

* Wed May 14 2008 Igor Zubkov <icesik@altlinux.org> 1.2.0-alt3
- CVE-2008-1419 (patch from upstream)
- CVE-2008-1420 (patch from upstream)
- CVE-2008-1423 (patch from upstream)

* Fri Aug 03 2007 Igor Zubkov <icesik@altlinux.org> 1.2.0-alt2.1
- fix requires

* Thu Aug 02 2007 Igor Zubkov <icesik@altlinux.org> 1.2.0-alt2
- CVE-2007-4029

* Thu Aug 02 2007 Igor Zubkov <icesik@altlinux.org> 1.2.0-alt1
- 1.1.2 -> 1.2.0

* Tue Jun 26 2007 Igor Zubkov <icesik@altlinux.org> 1.1.2-alt3
- fix CVE-2007-3106 (patch from upstream)

* Fri Dec 01 2006 Igor Zubkov <icesik@altlinux.org> 1.1.2-alt2
- bump release

* Sun Jan 01 2006 Igor Zubkov <icesik@altlinux.ru> 1.1.2-alt1
- 1.1.2
- remove hack maded from #7660

* Wed Aug 17 2005 Grigory Batalov <bga@altlinux.ru> 1.1.1-alt2
- Move C headers to %_includedir/vorbis and make links from there.

* Thu Jul 07 2005 Andrey Astafiev <andrei@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sat Sep 25 2004 Andrey Astafiev <andrei@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Jan 22 2004 Andrey Astafiev <andrei@altlinux.ru> 1.0update.1-alt3
- Fixed BuildRequires.

* Tue Dec 02 2003 Alexey Tourbin <at@altlinux.ru> 1.0update.1-alt2
- Do not package .la files.
- Do not package %name-devel-static by default.
- Aggressive optimization disabled (partially).

* Sat Nov 22 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0update.1-alt1
- 1.0.1

* Thu Oct 31 2002 Rider <rider@altlinux.ru> 1.0release-alt2
- rebuild (gcc 3.2)

* Tue Jul 30 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0release-alt1
- 1.0
- building doesn't requires libogg-devel-static.
- some temprorary changes to avoid using Serial.

* Thu Jan 03 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0rc3-alt1
- 1.0rc3

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0rc2-alt2
- Fixed license tag.
- Relocated documentation, a bit more specfile cleanup.

* Thu Sep 27 2001 Andrey Astafiev <andrei@altlinux.ru> 1.0rc2-alt1
- spec cleanup.

* Sat Sep 22 2001 Michael Shigorin <mike@lic145.kiev.ua>
- built for ALTLinux.

* Sat Oct 21 2000 Jack Moffitt <jack@icecast.org>
- initial spec file created.
