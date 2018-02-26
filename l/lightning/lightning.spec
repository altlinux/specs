Name: lightning
Version: 1.2
Release: alt1

Summary: GNU Lightning is a library for dynamic code generation
License: LGPLv2+
Group: Development/Other
ExclusiveArch: %ix86 ppc sparc
Url: http://www.gnu.org/software/lightning/lightning.html
# ftp://ftp.gnu.org/gnu/lightning/lightning-%version.tar.gz
Source: %name-%version.tar

%description
GNU lightning is a library to aid in making portable programs
that compile assembly code at run time.  Unlike other dynamic
code generation systems, which are usually either inefficient or
non-portable, GNU lightning is both retargetable and very fast.

%prep
%setup
rm doc/*.info*

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%files
%_bindir/*
%_includedir/*
%_datadir/%name
%_datadir/aclocal/*
%_infodir/*.info*
%_man1dir/*
%doc AUTHORS README NEWS THANKS

%changelog
* Sun Mar 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Updated to 1.2.
- Cleaned up specfile.

* Sun Sep 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt2
- NMU: fix spec name, update Url, fix Source path, change to tar.bz2
- add Packager

* Tue Dec 16 2003 Ott Alex <ott@altlinux.ru> 1.1.2-alt1
- New release

* Sun Nov 09 2003 Ott Alex <ott@altlinux.ru> 1.1.1-alt1
- New release

* Sun Jul 13 2003 Ott Alex <ott@altlinux.ru> 1.1-alt1
- Initial release


