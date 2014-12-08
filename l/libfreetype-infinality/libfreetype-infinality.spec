%define freetypemajorversion 6

Name: libfreetype-infinality
Version: 2.5.4
Release: alt1

Summary: A free and portable font rendering engine with patches from http://www.infinality.net
License: FTL or GPLv2+
Group: System/Libraries
Url: http://www.freetype.org/
Packager: Vladimir Didenko <cow@altlinux.ru>

Source0: %name-%version.tar

Source91: infinality-settings.sh
Source92: README.infinality

Patch1: freetype-2.4.10-rh-enable-valid.patch
Patch2: freetype-2.5.4-upstream-20141207.patch
# Infinality patches. Now we use bohoomil upstream:
# https://github.com/bohoomil/fontconfig-ultimate/
Patch90:freetype-2.5.4-bohoomil-ftsmooth-20141207.patch
Patch91: freetype-2.5.4-bohoomil-infinality-20141207.patch

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
%patch90 -p1
%patch91 -p1

%build
%add_optflags -fno-strict-aliasing
%define libdir %{_libdir}/%name
%configure %{subst_enable static} \
    --libdir=%libdir

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

mkdir -p %buildroot%_sysconfdir/X11/profile.d
install -pm755 %SOURCE91 %buildroot%_sysconfdir/X11/profile.d/

%define docdir %{_docdir}/%name-%version
mkdir -p %buildroot%docdir
cp -a docs/{FTL.TXT,LICENSE.TXT,CHANGES} %buildroot%docdir/
pushd %buildroot%docdir
    bzip2 -9 CHANGES 
popd
cp %SOURCE91 %buildroot%docdir
cp %SOURCE92 %buildroot%docdir
cp %PATCH91 %buildroot%docdir

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
%config %_sysconfdir/X11/profile.d/infinality-settings.sh
%config %ld_so_conf

%changelog
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
