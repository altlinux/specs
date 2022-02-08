Name: libgpg-error
Version: 1.44
Release: alt1

Group: System/Libraries
Summary: Error library for GnuPG and related projects
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://www.gnupg.org/

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%set_verify_elf_method strict

Source: %name-%version.tar

Patch0: libgpg-error-1.29-multilib.patch
Patch1: 0001-Fix-LFS-on-32-bit-systems.patch
Patch2: 0002-ALT-version-is-not-beta.patch

BuildRequires: makeinfo
BuildRequires: gettext-tools

%package devel
Summary: Development files for the %name package
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group: Development/C
Requires: %name = %version-%release

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%description devel
This package contains files needed to develop
applications using the GnuPG error library.

%prep
%setup -q
%autopatch -p1

cat > doc/version.texi <<EOF
@set UPDATED $(LANG=C date -u -r doc/gpgrt.texi +'%%d %%B %%Y')
@set UPDATED-MONTH $(LANG=C date -u -r doc/gpgrt.texi +'%%B %%Y')
@set EDITION %version
@set VERSION %version
EOF

# Let the autoreconf sync po.m4 and po/Makefile.in.in .
rm -f -- m4/po.m4 po/Makefile.in.in

%build
%autoreconf
%configure \
	--disable-static \
	--with-pic
%make_build

%install
%makeinstall_std

# relocate shared libraries from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/libgpg-error.so; do
        t=$(readlink -v "$f")
        ln -rsnf %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%find_lang %name

%check
%make check

%files -f %name.lang
/%_lib/lib*.so.*
%_bindir/gpg-error
%_datadir/libgpg-error/
%doc AUTHORS NEWS README

%files devel
%_bindir/*-config
%_bindir/yat2m
%_libdir/*.so
%_includedir/*
%_aclocaldir/*
%_man1dir/gpgrt-config.1.*
%_infodir/gpgrt.*
%_pkgconfigdir/*.pc
%_datadir/common-lisp/source/gpg-error

%changelog
* Tue Feb 08 2022 Alexey Gladkov <legion@altlinux.ru> 1.44-alt1
- New version (1.44).

* Sat Nov 20 2021 Alexey Gladkov <legion@altlinux.ru> 1.43-alt1
- New version (1.43).

* Wed Jun 23 2021 Alexey Gladkov <legion@altlinux.ru> 1.42-alt1
- New version (1.42).

* Thu Dec 31 2020 Alexey Gladkov <legion@altlinux.ru> 1.41-alt4
- Removed the suffix from the version completely.

* Wed Dec 30 2020 Alexey Gladkov <legion@altlinux.ru> 1.41-alt3
- Marked version as not beta.

* Sat Dec 26 2020 Alexey Gladkov <legion@altlinux.ru> 1.41-alt2
- Updated Licence tag.
- Disabled static library.
- Rebased to upstream git history.
- Uncompressed source tarball.
- Hardened build checks.
- Fixed build dependencies.
- Fixed libgpg-error.so symlink.

* Wed Dec 23 2020 Paul Wolneykien <manowar@altlinux.org> 1.41-alt1
- Freshed up to v1.41.

* Mon Mar 25 2019 Paul Wolneykien <manowar@altlinux.org> 1.36-alt1
- Freshed up to version 1.36.
- Get rid of %%ubt.
- Added gpg-error.pc for pkgconfig.

* Thu Jun 14 2018 Sergey V Turchin <zerg@altlinux.org> 1.31-alt1
- new version

* Thu Apr 19 2018 Sergey V Turchin <zerg@altlinux.org> 1.29-alt1
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 1.27-alt1
- new version

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1.1
- NMU: added BR: texinfo

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 1.20-alt1
- new version

* Wed Jun 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.19-alt1
- 1.19
- relocate shared libraries from %_libdir/ to /%_lib/.

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.17-alt0.M70P.1
- built for M70P

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.17-alt1
- new version

* Thu Jun 19 2014 Sergey V Turchin <zerg@altlinux.org> 1.13-alt0.M70P.1
- built for M70P

* Thu Jun 05 2014 Sergey V Turchin <zerg@altlinux.org> 1.13-alt1
- new version

* Thu Jun 05 2014 Sergey V Turchin <zerg@altlinux.org> 1.12-alt0.M70P.1
- built for M70P

* Thu Dec 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.12-alt1
- new version

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 1.11-alt1
- new version

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.10-alt2
- add old versioned symbols to library

* Fri Feb 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.10-alt1
- new version
- clean version script

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.9-alt1
- new version

* Mon Jun 07 2010 Sergey V Turchin <zerg@altlinux.org> 1.8-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 1.8-alt1
- new version

* Mon Apr 27 2009 Sergey V Turchin <zerg@altlinux.org> 1.7-alt1
- new version
- remove deprecated macroses from specfile
- built static library

* Tue Sep 16 2008 Sergey V Turchin <zerg at altlinux dot org> 1.6-alt1
- new version

* Tue Dec 26 2006 Sergey V Turchin <zerg at altlinux dot org> 1.5-alt1
- new version

* Fri Sep 15 2006 Sergey V Turchin <zerg at altlinux dot org> 1.4-alt1
- new version

* Fri Apr 14 2006 Sergey V Turchin <zerg at altlinux dot org> 1.3-alt1
- new version

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 1.1-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- new version

* Mon Apr 05 2004 Sergey V Turchin <zerg at altlinux dot org> 0.7-alt1
- rebuild

* Wed Mar 24 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.7-alt0.1
- New upstream release
- Spec cleanup
- Added /usr/bin/gpg-error to the filelist
- Brushed up descriptions

* Thu Feb 05 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt2
- rebuild

* Mon Feb 02 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version
- don't build static libs by default

* Thu Sep 04 2003 Sergey V Turchin <zerg at altlinux dot org> 0.4-alt1
- initial spec
