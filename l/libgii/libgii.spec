Name: libgii
Version: 1.0.2
Release: alt3.qa2
Packager: Fr. Br. George <george@altlinux.ru>
Summary: A flexible library for input handling (General Input Interface)

License:	GPL
Group: System/Libraries
URL: http://www.ggi-project.org/
Source:	http://www.ggi-project.org/ftp/ggi/v2.1/%name-%version.src.tar.bz2

# Automatically added by buildreq on Tue Dec 09 2008
BuildRequires: imake libICE-devel libXext-devel libXt-devel libXxf86dga-devel xorg-cf-files

%description
LibGII is an input library developed by the GGI Project
(http://www.ggi-project.org). Its design philosophy is similar to
LibGGI, which deals with graphics output.

LibGII is based on the concept of input streams, which virtualize
access to the underlying input drivers. Events from various input
devices are abstracted into easy-to-use structures. LibGII also allows
the application to join streams together, receiving input from an
arbitrary combination of devices.

LibGII is a separate component from LibGGI, although LibGGI depends on
LibGII for input purposes. (LibGGI's input functions are simply
wrappers for LibGII functions.)

%package devel
Summary: development part of %name
Group: Development/C
Requires: %name = %version-%release

%description devel
development files for %name

%package devel-static
Summary: development part of %name, static version
Group: Development/C
Requires: %name = %version-%release

%description devel-static
development files for %name

%prep
%setup -q 

%build
%undefine __libtoolize
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall

%files
%doc ChangeLog* FAQ INSTALL INSTALL.autoconf NEWS README doc/README*
%config(noreplace) %_sysconfdir/ggi/*
%_bindir/*
%dir %_libdir/ggi
%dir %_libdir/ggi/filter
%dir %_libdir/ggi/input
%_libdir/ggi/*/*.so
%_libdir/*.so.*
%_mandir/man?/*

%files devel
%_includedir/*
#_libdir/ggi/*/*.la
%_libdir/*.so
#_libdir/*.la

%files devel-static
%_libdir/libgii.a
%_libdir/libgg.a

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3.qa2
- Removed bad RPATH

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Dec 09 2008 Fr. Br. George <george@altlinux.ru> 1.0.2-alt3
- Fix build

* Tue May 27 2008 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- Minor directory packaging fix

* Sun Jun 03 2007 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Resurrect from orphaned
- New version

* Wed Dec 29 2004 Stanislav Ievlev <inger@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 06 2004 Stanislav Ievlev <inger@altlinux.org> 0.8.6-alt1
- 0.8.6

* Tue Jan 13 2004 Stanislav Ievlev <inger@altlinux.org> 0.8.4-alt1
- 0.8.4

* Tue Dec 02 2003 Stanislav Ievlev <inger@altlinux.org> 0.8.3-alt1.1
- rebuild without .la files. As I understand, we also don't need .la
  files for plugins, 'cause all libraries don't use lt_dlopen()

* Tue Apr 15 2003 Stanislav Ievlev <inger@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Fri Feb 28 2003 Stanislav Ievlev <inger@altlinux.ru> 0.8.2-alt2
- fix ldconfig usage according packaging policy

* Tue Feb 25 2003 Stanislav Ievlev <inger@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Sep 26 2002 Stanislav Ievlev <inger@altlinux.ru> 0.8.1-alt2
- rebuild with gcc3

* Mon Sep 17 2001 Stanislav Ievlev <inger@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Fri Jul 27 2001 Stanislav Ievlev <inger@altlinux.ru> 0.8-alt1
- 0.8

* Wed Jul 04 2001 Stanislav Ievlev <inger@altlinux.ru> 0.7-alt1
- Initial release for ALT Linux
