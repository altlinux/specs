Name: lrzip
Version: 0.612
Release: alt1

Summary: Long Range ZIP or Lzma RZIP
License: GPLv2+
Group: File tools

URL: http://ck.kolivas.org/apps/lrzip/
Source: http://ck.kolivas.org/apps/lrzip/lrzip-%version.tar.bz2

# Automatically added by buildreq on Fri Mar 09 2012 (-bi)
BuildRequires: bzlib-devel doxygen gcc-c++ liblzo2-devel nasm perl-Pod-Parser zlib-devel

%description
This is a compression program optimised for large files. The larger the file
and the more memory you have, the better the compression advantage this will
provide, especially once the files are larger than 100MB. The advantage can
be chosen to be either size (much smaller than bzip2) or speed (much faster
than bzip2).

%package -n lib%name
Summary: Library to add lrzip compression and decompression to other applications
Group: System/Libraries

%description -n lib%name
liblrzip library allows you to add lrzip compression and decompression to other
applications with either simple lrzip_compress and lrzip_decompress functions
or fine control over all the options with low level functions.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains files needed for developing applications
that use lib%name.

%prep
%setup

%build
%configure --disable-static --disable-silent-rules
%make_build

%install
%makeinstall_std

install -pDm644 Lrzip.h %buildroot%_includedir/Lrzip.h

%files
%doc README README-NOT-BACKWARD-COMPATIBLE WHATS-NEW doc/lrzip.conf.example
%_bindir/lrunzip
%_bindir/lrzcat
%_bindir/lrzip
%_bindir/lrztar
%_bindir/lrzuntar
%_man1dir/*
%_man5dir/*
%exclude %_docdir/lrzip

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/*.so

%changelog
* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 0.612-alt1
- 0.612

* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 0.611-alt1
- 0.611

* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 0.610-alt1
- 0.610

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 0.608-alt1
- 0.608
  + NB: 0.607 fixed a rare unable-to-decompress corner case

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.606-alt1
- 0.606

* Mon Apr 25 2011 Victor Forsiuk <force@altlinux.org> 0.603-alt1
- 0.603

* Wed Mar 23 2011 Victor Forsiuk <force@altlinux.org> 0.600-alt1
- 0.600

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 0.46-alt1
- 0.46

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 0.45-alt1
- 0.45

* Fri Jan 15 2010 Victor Forsyuk <force@altlinux.org> 0.44-alt1
- 0.44

* Tue Dec 22 2009 Victor Forsyuk <force@altlinux.org> 0.42-alt1
- 0.42

* Fri Nov 27 2009 Victor Forsyuk <force@altlinux.org> 0.40-alt1
- Initial build.
