Name: vobcopy
Version: 1.2.0
Release: alt2

Summary: Copy DVD videos to the hard disk
Summary(ru_RU.UTF-8): Копирует содержимое DVD на диск
License: GPLv2+
Group: Video
URL: http://vobcopy.org/

Source0: http://vobcopy.org/download/%name-%version.tar.bz2

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Sep 19 2009
BuildRequires: libdvdread-devel

%description
vobcopy copies DVD .vob files to harddisk, decrypting (if you have libdvdcss installed)
them on the way (thanks to libdvdread and libdvdcss) and merges them into file(s) with
the name extracted from the DVD. It checks for enough free space on the destination
drive and compares the ripped size to the size on DVD (in case the size is wrong the files keep
the .partial ending ). vobcopy without any options will copy the first title into files of
2GB size into the current working directory. There is one drawback though: at the moment
vobcopy doesn't deal with multi-angle-dvd's. But since these are rather sparse this
shouldn't matter much. Mirroring of a dvd's VIDEO_TS is also possible.

%description -l ru_RU.UTF-8
vobcopy копирует *.vob-файлы с DVD на жесткий диск, дешифруя их на
лету (если у вас установлена libdvdcss) и записывет их в файлы в
имена, взятые с DVD-диска.

%prep
%setup -q

%build
%make_build CFLAGS+="%optflags"

%install
install -pD -m 755 vobcopy %buildroot%_bindir/vobcopy
install -pD -m 644 vobcopy.1 %buildroot%_man1dir/vobcopy.1
install -pD -m 644 vobcopy.1.de %buildroot%_mandir/de/man1/vobcopy.1

%files
%doc Changelog README Release-Notes TODO
%_bindir/vobcopy
%_man1dir/vobcopy.*
%_mandir/de/man1/vobcopy.*

%changelog
* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 1.2.0-alt2
- rebuild

* Fri Jul 31 2009 Igor Zubkov <icesik@altlinux.org> 1.2.0-alt1
- 1.1.2 -> 1.2.0

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 1.1.2-alt1
- 1.1.1 -> 1.1.2

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 1.1.1-alt1
- 1.1.0 -> 1.1.1

* Mon Jan 14 2008 Igor Zubkov <icesik@altlinux.org> 1.1.0-alt1
- 1.0.1 -> 1.1.0 (CVE-2007-5718)
- Update Url
- use %%opflags for build

* Tue Jun 05 2007 Slava Semushin <php-coder@altlinux.ru> 1.0.1-alt0
- Updated to 1.0.1
- Fixed bad encoding specification in Summary (#5126)
- Spec cleanup:
  + Added full url to Source tag
  + Set packager tag to previous maintainer
  + Formatted %%description
  + s/%%setup -qn %%name-%%version/%%setup/
  + Don't use macros for install command
  + Use %%_man1dir macros
  + Don't package COPYING file with GPL license
  + Removed tabs from %%changelog

* Tue Oct 05 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.13-alt1.1
- Rebuilt with libdvdread.so.3.

* Thu Apr 01 2004 Egor S. Orlov <oes@altlinux.ru> 0.5.13-alt1
- new version

* Tue Nov 18 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.9-alt1
- new version

* Wed Sep 10 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.8-alt0.1
- New version

* Wed Jul 30 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.7-alt0.1
- Initial build for ALT

* Sat Mar 15 2003 GЖtz Waschk <goetz@plf.zarb.org> 0.5.7-1plf
- new version

* Sun Feb  9 2003 GЖtz Waschk <goetz@plf.zarb.org> 0.5.6-1plf
- new version

* Tue Nov  5 2002 GЖtz Waschk <waschk@informatik.uni-rostock.de> 0.5.5-1plf
- new version

* Mon Sep 23 2002 GЖtz Waschk <waschk@informatik.uni-rostock.de> 0.5.4-1plf
- new version

* Sun Jul 21 2002 GЖtz Waschk <waschk@informatik.uni-rostock.de> 0.5.2-1plf
- new version

* Wed Jul 17 2002 GЖtz Waschk <waschk@informatik.uni-rostock.de> 0.5.1-1plf
- 0.5.1

* Fri Apr 26 2002 GЖtz Waschk <waschk@linux-mandrake.com> 0.4.3-1plf
- 0.4.3

* Sun Mar 24 2002 GЖtz Waschk <waschk@linux-mandrake.com> 0.4.2-1plf
- new version

* Sun Feb 24 2002 GЖtz Waschk <waschk@linux-mandrake.com> 0.4.1-2plf
- rebuild to fix Vendor again :-(

* Wed Feb 20 2002 GЖtz Waschk <waschk@linux-mandrake.com> 0.4.1-1plf
- 0.4.1
- drop patch

* Sun Feb 17 2002 GЖtz Waschk <waschk@linux-mandrake.com> 0.4.0-2plf
- rebuild for right vendor tag

* Sat Feb 16 2002 GЖtz Waschk <waschk@linux-mandrake.com> 0.4.0-1plf
- patch to make it compile with libdvdread 0.9.2
- new version

* Wed Jan 23 2002 GЖtz Waschk <waschk@linux-mandrake.com> 0.3.0-1plf
- initial package
