Name: enchant
Version: 1.6.0
Release: alt3
Summary: An Enchanting Spell Checking Program
Group: Text tools
License: LGPL
URL: http://www.abisource.com/projects/enchant

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires:  lib%name = %version-%release

Source: http://www.abisource.com/downloads/enchant/%version/%name-%version.tar.gz
Source1: %name-spell

BuildRequires: gcc-c++ glib2-devel libdbus-glib-devel libhunspell-devel

%description
This package contains simple programs that wrap other spell checking backends,
including an Ispell compatible script.

%package -n lib%name
Summary: An Enchanting Spell Checking Library
Group: System/Libraries

%description -n lib%name
A library that wraps other spell checking backends.

%package -n lib%name-devel
Summary: Support files necessary to compile applications with libenchant.
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Libraries, headers, and support files necessary to compile applications
using libenchant.

%prep
%setup -q

%build
%autoreconf
%configure \
	--with-myspell-dir=%_datadir/myspell \
	--disable-aspell \
	--disable-ispell \
	--disable-zemberek \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

install -m755 %SOURCE1 %buildroot%_bindir/

cat <<EOF >%buildroot%_datadir/%name/%name.ordering
*:myspell
EOF

mkdir -p %buildroot%_altdir
cat <<EOF >%buildroot%_altdir/%name
%_bindir/spell	%_bindir/%name-spell	60
EOF

%files
%_altdir/%name
%_bindir/*
%_man1dir/*

%files -n lib%name
%doc AUTHORS COPYING.LIB README
%_libdir/*.so.*
%dir %_libdir/%name
%_libdir/%name/*.so*
%_datadir/%name

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Fri Mar 11 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt3
- rebuild for debuginfo

* Wed Nov 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt2
- dropped version script

* Mon May 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Fri Jan 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt2
- disabled zemberek (closes: #22614)

* Wed Jun 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed Jun 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt2
- disabled aspell (closes: #20278)

* Fri Apr 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.2-alt1
- 1.4.2
- disabled ispell

* Wed Sep 27 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.0-alt0.1
- Updated to 1.3.0

* Sat Jun 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.6-alt0.1
- Release 1.2.6

* Tue Apr 25 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.5-alt0.1
- Updated to 1.2.5
- Major spec cleanup in conformance to ALT spec conventions
- Updated alternatives format
- Somewhat better English here and there in descriptions

* Wed Dec 14 2005 Vital Khilko <vk@altlinux.ru> 1.2.0-alt2
- #8617

* Fri Dec 09 2005 Vital Khilko <vk@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Mon Apr 04 2005 Vital Khilko <vk@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Mon Nov 24 2003 Vital Khilko <vk@altlinux.ru> 1.1.1-alt1
- adapted for ALT Linux
- added alternatives for enchant-ispell script

* Sun Aug 24 2003 Rui Miguel Seabra <rms@1407.org>
- update spec to current stat of affairs
- building from source rpm is now aware of --with and --without flags:
- --without aspell --without ispell --without myspell --with uspell

* Wed Jul 16 2003 Rui Miguel Seabra <rms@1407.org>
- take advantage of environment rpm macros

* Sun Jul 13 2003 Dom Lachowicz <cinamod@hotmail.com>
- Initial version
