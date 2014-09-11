Name: liblockfile
Version: 1.09
Release: alt1

Summary: NFS-safe locking library, includes dotlockfile program
License: LGPL v2+ (library), GPL v2+ (dotlockfile)
URL: http://www.t2-project.org/packages/liblockfile.html
Group: System/Libraries

#http://ftp.debian.org/debian/pool/main/libl/liblockfile/%{name}_%version.orig.tar.gz
Source: %name-%version.tar

%description
Liblockfile is a shared library with NFS-safe locking functions. It
includes the command-line utility ``dotlockfile''.

%package devel
Summary: Header files for liblockfile library
License: LGPL v2+
Group: Development/C
Requires: %name = %version-%release

%description devel
This is a development package for liblockfile. It includes headers and
documentation.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-shared \
	--with-mailgroup

%make

%install
install -d %buildroot{%_libdir,%_bindir,%_includedir,%_mandir/man{1,3}}

%make_install install \
	MAILGROUP=%(id -gn) \
	ROOT=%buildroot

ln -sf $(basename %buildroot%_libdir/liblockfile.so.1.*) %buildroot%_libdir/liblockfile.so.1

%files
%doc COPYRIGHT README
%_bindir/dotlockfile
%_libdir/liblockfile.so.*.*
%ghost %_libdir/liblockfile.so.1
%_man1dir/dotlockfile.1*

%files devel
%_libdir/liblockfile.so
%_includedir/lockfile.h
%_includedir/maillock.h
%_man3dir/lockfile_create.3*
%_man3dir/maillock.3*

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.09-alt1
- Version 1.09

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.08-alt3.qa1
- NMU: rebuilt for debuginfo.

* Thu Oct 21 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.08-alt3
- Rebuild for soname-set versions

* Wed Dec 03 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.08-alt2
- Remove obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 29 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.08-alt1
- Initial build for ALT Linux (spec from PLD)
