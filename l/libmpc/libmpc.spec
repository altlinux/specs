Name: libmpc
Version: 0.9
Release: alt2

Summary: Complex floating-point library with high precision and exact rounding
License: LGPLv2.1+
Group: System/Libraries
Url: http://multiprecision.org/

# http://multiprecision.org/mpc/download/mpc-%version.tar.gz
Source: mpc-%version.tar

BuildRequires: libgmp-devel libmpfr-devel

%description
The MPC library is a C library for the arithmetic of complex numbers
with arbitrarily high precision and correct rounding of the result.
It is built upon and follows the same principles as MPFR.

%package devel
Summary: Header files for MPC library
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for MPC library.

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

%files devel
%_libdir/libmpc.so
%_includedir/mpc.h
%_infodir/mpc.info*

%changelog
* Thu Jun 07 2012 Dmitry V. Levin <ldv@altlinux.org> 0.9-alt2
- Rebuilt with libgmp10 and libmpfr4 (closes: #27416).

* Mon Sep 19 2011 Alexey Tourbin <at@altlinux.ru> 0.9-alt1
- 0.9
- enabled check

* Wed Oct 20 2010 Kirill A. Shutemov <kas@altlinux.org> 0.8.2-alt1
- 0.8.2

* Sun Mar 21 2010 Kirill A. Shutemov <kas@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux Sisyphus

