Name: madplay
Version: 0.15.2b
Release: alt2

Summary: High quality MPEG audio decoder
Summary(ru_RU.CP1251): Декодер аудиофайлов формата MPEG
License: GPL
Group: Sound
Url: http://mad.sourceforge.net/

Packager: Andrey Astafiev <andrei@altlinux.ru>

Source: http://download.sourceforge.net/%name/%name-%version.tar.bz2

Provides: mad = %version
Obsoletes: mad

PreReq: libmad >= 0.15.1
PreReq: libid3tag >= 0.15.1
BuildPreReq: libid3tag-devel >= 0.15.1
BuildPreReq: libmad-devel >= 0.15.1

# Automatically added by buildreq on Thu Mar 04 2004
BuildRequires: esound-devel gcc-c++ hostinfo libaudiofile-devel libid3tag-devel
BuildRequires: libmad-devel libstdc++-devel zlib-devel

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2 extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

%description -l ru_RU.CP1251
MAD - это высокачественный декодер аудиофайлов формата MPEG.
Сейчас поддерживаются MPEG-1, расширение MPEG-2 для низких битрейтов,
а также так называемый формат MPEG 2.5. Полностью реализованы все три
уровня сжатия звука (Layer I, Layer II и Layer III, известный как MP3).

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%find_lang %name

%files -f %name.lang
%_bindir/*
%_mandir/man?/*
%doc CHANGES README INSTALL CREDITS COPYRIGHT TODO VERSION

%changelog
* Thu Mar 04 2004 Andrey Astafiev <andrei@altlinux.ru> 0.15.2b-alt2
- 0.15.2b
- Renamed from mad to madplay.

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt2
- Building fix: required libid3tag and libmad of version 0.15.0b.

* Fri Jun 06 2003 Andrey Astafiev <andrei@altlinux.ru> 0.15.0b-alt1
- 0.15.0b.
- Libraries libid3tag and libmad moved to packages with corresponding names.

* Sat Mar 15 2003 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt4
- Library libid3tag moved to separate binary package.

* Sun Oct 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.14.2b-alt3
- rebuild with gcc-3.2
- Packager tag added.

* Tue Feb 12 2002 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt2
- Packager field fixed.

* Fri Nov 09 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.2b-alt1
- 0.14.2b

* Tue Oct 23 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.1b-alt1
- 0.14.1b

* Fri Oct 19 2001 Andrey Astafiev <andrei@altlinux.ru> 0.14.0b-alt1
- 0.14.0b

* Mon Sep 03 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.13.0b-alt2
- Blind minor specfile cleanup.

* Mon Sep 3 2001 Andrey Astafiev <andrei@altlinux.ru> 0.13.0b-alt1
- First version of RPM package
