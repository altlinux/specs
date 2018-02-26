Name: libpaper
Version: 1.1.24
Release: alt4

Summary: Library and tools for handling papersize

License: GPL
Group: System/Libraries
Url: http://packages.qa.debian.org/libp/libpaper.html

Source: %name-%version.tar

Patch: libpaper-1.1.20-fedora-automake_1.10.patch
Patch1: libpaper-1.1.23-fedora-debianbug475683.patch
Patch2: libpaper-fedora-useglibcfallback.patch

# Automatically added by buildreq on Sun Jan 08 2006
BuildRequires: gcc-c++ libstdc++-devel

%description
The paper library and accompanying files are intended to provide a simple
way for applications to take actions based on a system- or user-specified
paper size.  This release is quite minimal, its purpose being to provide
really basic functions (obtaining the system paper name and getting
the height and width of a given kond of paper) that applications can
immediately integrate.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure --disable-static
# Disable rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make

%install
%make_install install \
	DESTDIR=%buildroot
rm %buildroot%_libdir/*.la
mkdir -p %buildroot%_sysconfdir
echo '# Simply write the paper name. See papersize(5) for possible values' > %buildroot%_sysconfdir/papersize
mkdir -p %buildroot%_sysconfdir/libpaper.d
for i in cs da de es fr gl hu it ja nl pt_BR sv tr uk vi; do
    mkdir -p %buildroot%_datadir/locale/$i/LC_MESSAGES/;
    msgfmt debian/po/$i.po -o %buildroot%_datadir/locale/$i/LC_MESSAGES/%name.mo;
done
%find_lang %name

%files -f %name.lang
%doc README
%config(noreplace) %_sysconfdir/papersize
%dir %_sysconfdir/libpaper.d
%_bindir/paperconf
%_libdir/libpaper.so.*
%_sbindir/paperconfig
%_man1dir/*
%_man5dir/*
%_man8dir/*

%files devel
%_libdir/libpaper.so
%_includedir/paper.h
%_man3dir/*

%changelog
* Wed Sep 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.24-alt4
- steal Fedora patches for proper papersize setting (ALT #26176)

* Mon Aug 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.24-alt3
- firsttime script added

* Mon Aug 29 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.24-alt2
- set paper to A4 if not set

* Fri Mar 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.24-alt1
- 1.1.24

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.23-alt1.qa2
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.23-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libpaper
  * postun_ldconfig for libpaper
  * postclean-05-filetriggers for spec file

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.23-alt1
- new version 1.1.23 (with rpmrb script)

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.21-alt0.1
- new version 1.1.21 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.20-alt0.1
- new version 1.1.20 (with rpmrb script)

* Sun Jan 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt0.1
- initial build for ALT Linux Sisyphus
