Name: libfreetype-infinality
Version: 2.8.0
Release: alt6

Summary: A free and portable font rendering engine with patches from http://www.infinality.net
License: FTL or GPLv2+
Group: System/Libraries
Url: http://www.freetype.org/
Packager: Vladimir Didenko <cow@altlinux.ru>

Source0: %name-%version.tar

Source91: infinality-settings.sh
Source92: xft-settings.sh
Source93: CHANGELOG

Patch1: freetype-2.7.0-alt-enable-valid.patch
Patch2: freetype-2.8-alt-export-compat-symbols.patch
Patch3: freetype-2.8.0-alt-ft_done_mm_var.patch
# Infinality patches. Now it is based on archfan upstream (looks like bohoomil
# has dropped infinality patches support)
# https://github.com/archfan/infinality_bundle
Patch91: freetype-2.8.0-archfan-infinality-20170614.patch
# Set default byte code interpreter to infinality version. Default "minimal"
# version still can be selected using FREETYPE_PROPERTIES environment variable
# in /etc/X11/profile.d/infinality-settings.sh config file.
Patch92: freetype-2.7.0-alt-default-interpreter.patch

Provides: freetype2-infinality = %version
Obsoletes: freetype2-infinality < %version

%def_disable static

BuildRequires: libX11-devel zlib-devel libpng-devel

%description
The FreeType engine is a free and portable TrueType font rendering
engine, developed to provide TrueType support for a variety of
platforms and environments.  FreeType is a library which can open
and manages font files as well as efficiently load, hint and render
individual glyphs.  FreeType is not a font server or a complete
text-rendering library.

This version is compiled with the Infinality patches. It transparently
overrides the system library using ld.so.conf.d mechanism.

%prep
%setup -n %name-%version

%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch91 -p1
%patch92 -p2

%build
%add_optflags -fno-strict-aliasing %(getconf LFS_CFLAGS)
%define libdir %{_libdir}/%name
%configure %{subst_enable static} \
    --libdir=%libdir --with-optimization=no

# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' builds/unix/libtool

%make_build

%install
%makeinstall_std

%define ld_so_conf %_sysconfdir/ld.so.conf.d/%name-%_arch.conf
ld_so_conf=%ld_so_conf
mkdir -p %buildroot${ld_so_conf%%/*}
echo %_libdir/%name > %buildroot%ld_so_conf
chmod 644 %buildroot%ld_so_conf
%filter_from_provides '/^libfreetype\.so\./d'
%filter_from_provides '/^debug/d'

mkdir -p %buildroot%_sysconfdir/X11/profile.d
install -pm755 %SOURCE91 %buildroot%_sysconfdir/X11/profile.d/
install -pm755 %SOURCE92 %buildroot%_sysconfdir/X11/profile.d/

%define docdir %{_docdir}/%name-%version
mkdir -p %buildroot%docdir
cp -a docs/{FTL.TXT,LICENSE.TXT,CHANGES} %buildroot%docdir/
pushd %buildroot%docdir
    bzip2 -9 CHANGES
popd
cp %SOURCE93 %buildroot%docdir

#remove devel data. Infinality package is not oriented on any development
rm -f %buildroot%_bindir/*-config
rm -f %buildroot%libdir/*.so
rm -f %buildroot%libdir/*.la
rm -fr %buildroot%_includedir/
rm -fr %buildroot%libdir/pkgconfig/
rm -f %buildroot%_datadir/aclocal/*.m4

%set_verify_elf_method strict

%files
%exclude %_mandir/
%docdir
%_libdir/%name/
%config(noreplace) %_sysconfdir/X11/profile.d/infinality-settings.sh
%config(noreplace) %_sysconfdir/X11/profile.d/xft-settings.sh
%config %ld_so_conf

%changelog
* Thu Feb 8 2018 Vladimir Didenko <cow@altlinux.ru> 2.8.0-alt6
- Temporary restore package to work-around problem with skia
- Backport FT_Done_MM_Var from freetype 2.9 (fixes problem with harfbuzz)

* Fri Feb 2 2018 Vladimir Didenko <cow@altlinux.ru> 2.8.0-alt5
- Make package noarch

* Wed Jan 17 2018 Vladimir Didenko <cow@altlinux.ru> 2.8.0-alt4
- Make package empty (prepare it for removing from the repo)

* Fri Sep 15 2017 Vladimir Didenko <cow@altlinux.ru> 2.8.0-alt3
- Added export of FT_Done_GlyphSlot symbol for libInventor.

* Wed Sep 13 2017 Vladimir Didenko <cow@altlinux.ru> 2.8.0-alt2
- Built with LFS support enabled

* Wed Jun 14 2017 Vladimir Didenko <cow@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue Jan 17 2017 Vladimir Didenko <cow@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Thu Sep 22 2016 Vladimir Didenko <cow@altlinux.ru> 2.7.0-alt3
- Set infinality as default hinting interpreter

* Wed Sep 21 2016 Vladimir Didenko <cow@altlinux.ru> 2.7.0-alt2
- Fix infinality patch

* Tue Sep 20 2016 Vladimir Didenko <cow@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Wed Apr 13 2016 Vladimir Didenko <cow@altlinux.ru> 2.6.3-alt2
- update infinality patch

* Sat Feb 20 2016 Vladimir Didenko <cow@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Tue Dec 8 2015 Vladimir Didenko <cow@altlinux.ru> 2.6.2-alt1
- 2.6.2
- use separate script to set xft settings
- don't set xft.dpi by default
- update infinality patch

* Mon Oct 5 2015 Vladimir Didenko <cow@altlinux.ru> 2.6.1-alt1
- 2.6.1
- Remove debug(libfreetype.so) from provides (closes: #31325)
- update infinality patch

* Thu Jun 11 2015 Vladimir Didenko <cow@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Jan 19 2015 Vladimir Didenko <cow@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Mon Dec 8 2014 Vladimir Didenko <cow@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Thu Jul 10 2014 Vladimir Didenko <cow@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Jun 24 2013 Dmitry V. Levin <ldv@altlinux.org> 2.4.12-alt2
- infinality-settings.sh: relocated from /etc/profile.d/ to
  /etc/X11/profile.d/ (closes: #29093).
- Reintroduced ld.so.conf.d based configuration (closes: #29095).

* Tue May 28 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.12-alt1
- 2.4.12

* Thu Feb 5 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt6
- Switched back to LD_PRELOAD because ld.so.conf.d solution
  breaks other packages building

* Thu Feb 5 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt5
- Use ld.so.conf.d instead LD_PRELOAD

* Thu Jan 24 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt4
- Fixed conflict with official debuginfo package
- Added missed doc files
- spec cleanup

* Thu Jan 17 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt3
- Include %_libdir/%name/ directory

* Thu Jan 17 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt2
- Fixed ld preload script to properly work on biarch systems

* Wed Jan 9 2013 Vladimir Didenko <cow@altlinux.ru> 2.4.11-alt1
- 2.4.11

* Fri Dec 21 2012 Vladimir Didenko <cow@altlinux.ru> 2.4.10-alt3
- Deleted devel packages

* Wed Dec 19 2012 Vladimir Didenko <cow@altlinux.ru> 2.4.10-alt2
- Removed dependency on official freetype package

* Mon Dec 10 2012 Vladimir Didenko <cow@altlinux.ru> 2.4.10-alt1
- Initial build
