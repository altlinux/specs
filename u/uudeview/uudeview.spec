Name: uudeview
Version: 0.5.20
Release: alt11

Summary: smart uuenc/xxenc/base64 encoder/decoder
License: GPL-2.0-only
Group: Text tools

Url: https://github.com/hannob/uudeview
Vcs: https://github.com/hannob/uudeview.git
Source: %name-%version.tar

BuildRequires: sendmail-common tcl-devel tk-devel
BuildRequires: zlib-devel

Summary(ru_RU.UTF-8): быстрый кодер/декодер uuenc/xxenc/base64

%description
Smart multi-file multi-part decoder for uuencoded,
xxencoded, Base64 and BinHex encoded files. Also
includes a similarly powerful encoder.

%description -l ru_RU.UTF-8
"Умный" декодер для файлов uuenc/xxenc/base64/BinHex.
Также включает кодер с аналогичными характеристиками.

%package -n xdeview
Summary: uudeview for X
Group: Text tools

%description -n xdeview
%summary

%package -n libuu
Summary: %name shared library
Group: System/Libraries

%description -n libuu
%summary

%package -n libuu-devel
Summary: Header files for %name shared library
Group: Development/C
Requires: libuu = %EVR

%description -n libuu-devel
%summary

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure --enable-tcl=%_libdir
%make_build

%install
%makeinstall_std

%files
%_bindir/minews
%_bindir/uudeview
%_bindir/uuenview
%_man1dir/uudeview*
%_man1dir/uuenview*
%doc HISTORY INSTALL README.md

%files -n xdeview
%_bindir/uuwish
%_bindir/xdeview
%_man1dir/xdeview*
%_man1dir/uuwish*

%files -n libuu
%_libdir/libuu.so.*

%files -n libuu-devel
%_includedir/*.h
%_libdir/libuu.so

%changelog
* Fri May 15 2026 Alexey Shabalin <shaba@altlinux.org> 0.5.20-alt11
- Build from upstream git, drop carried patches.
- Drop -doc subpackage.

* Tue Mar 26 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5.20-alt10
- Fixed FTBFS: built with system zlib.

* Sat Apr 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.20-alt9
- NMU: fixed build.

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5.20-alt8.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Sat Mar 08 2014 Michael Shigorin <mike@altlinux.org> 0.5.20-alt8
- tweaked libuu summary line (closes: #27441)

* Sat Jan 18 2014 Michael Shigorin <mike@altlinux.org> 0.5.20-alt7
- oops, work around weird FTBFS on x86_64 (base_libs broke)

* Wed Jan 15 2014 Michael Shigorin <mike@altlinux.org> 0.5.20-alt6
- separate xdeview subpackage to avoid pulling libX11 & co
  into regular-rescue.iso but still to provide a nice utility
- added Russian description, converted Summary: to UTF-8
- dropped Packager: as a matter of fact (thank you vvk@!)

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.20-alt5.1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for uudeview-doc

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5.20-alt5.1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.20-alt5.1
- Rebuilt for soname set-versions

* Fri Oct 23 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.20-alt5
- Add libuu and libuu-devel packages.

* Fri Apr 17 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.20-alt4
- Revert uudeview-0.5.20-unknown_filename_fix.patch (Closes: #5976)

* Wed Aug 13 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.20-alt3
- Security fix: CVE-2008-2266
- Pull in source patches from Debian:
  + Fix temporary file issue (CVE-2004-2265, CVE-2008-2266, DEB#222275)
  + Update uudeview man page, include uuwish man page
  + Don't force overwrite mode if auto-rename enabled, DEB#378076
- Drop uudeview-0.5.20-mkstemp.patch

* Thu Mar 13 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.20-alt2
- Rebuild with libtcl8.5

* Fri Nov 03 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.20-alt1
- Updated to 0.5.20
- uudeview.patch splitted to separate patches
  + uudeview-0.5.20-unknown_filename_fix.patch
  + uudeview-0.5.20-mkstemp.patch
  + other patches unneeded now
- Minor spec cleanup

* Tue Mar 16 2004 Egor S. Orlov <oes@altlinux.ru> 0.5.19-alt2
- Added OpenPKG patch

* Tue Oct 14 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.19-alt1
- New version

* Tue Oct 14 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.18-alt4
- fixed changelog entry

* Mon Oct 13 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.18-alt2
- fixed doc dependency bug

* Thu Sep 25 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.18-alt1
- Initial spec
