Name: libmpc3
Version: 1.1.0
Release: alt1

Summary: C library for multiple precision complex arithmetic
License: LGPLv3+, GFDL
Group: System/Libraries
Url: http://multiprecision.org/

# http://multiprecision.org/mpc/download/mpc-%version.tar.gz
Source: mpc-%version.tar

BuildRequires: libgmp-devel libmpfr-devel

Provides: libmpc = %version-%release

%description
The GNU MPC library is a C library for the arithmetic of complex numbers
with arbitrarily high precision and correct rounding of the result.
It is built upon and follows the same principles as MPFR.

%package -n libmpc-devel
Summary: Header files for the GNU MPC library
Group: Development/C
Requires: %name = %version-%release

%description -n libmpc-devel
Header files for the GNU MPC library.

%prep
%setup -n mpc-%version
rm m4/{lt*,libtool}.m4

%build
%autoreconf
export EGREP=egrep
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%files
%doc AUTHORS NEWS README
%_libdir/libmpc.so.*

%files -n libmpc-devel
%_libdir/libmpc.so
%_includedir/mpc.h
%_infodir/mpc.info*

%changelog
* Wed Jan 17 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0.

* Wed May 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.3-alt1
- Updated to 1.0.3.

* Tue Sep 16 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2-alt1
- Updated to 1.0.2.

* Wed Sep 25 2013 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- Updated to 1.0.1 (closes: #29363).

* Thu Jun 07 2012 Dmitry V. Levin <ldv@altlinux.org> 0.9-alt2
- Rebuilt with libgmp10 and libmpfr4 (closes: #27416).

* Mon Sep 19 2011 Alexey Tourbin <at@altlinux.ru> 0.9-alt1
- 0.9
- enabled check

* Wed Oct 20 2010 Kirill A. Shutemov <kas@altlinux.org> 0.8.2-alt1
- 0.8.2

* Sun Mar 21 2010 Kirill A. Shutemov <kas@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux Sisyphus

