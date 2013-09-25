Name: libmpc2
Version: 0.9
Release: alt3

Summary: C library for multiple precision complex arithmetic
License: LGPLv2.1+
Group: System/Legacy libraries
Url: http://multiprecision.org/

# http://multiprecision.org/mpc/download/mpc-%version.tar.gz
Source: mpc-%version.tar

BuildRequires: libgmp-devel libmpfr-devel

Provides: libmpc = %version-%release
Obsoletes: libmpc < %version-%release

%description
The MPC library is a C library for the arithmetic of complex numbers
with arbitrarily high precision and correct rounding of the result.
It is built upon and follows the same principles as MPFR.

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

%changelog
* Wed Sep 25 2013 Dmitry V. Levin <ldv@altlinux.org> 0.9-alt3
- Packaged libmpc2 compatibility library.

* Thu Jun 07 2012 Dmitry V. Levin <ldv@altlinux.org> 0.9-alt2
- Rebuilt with libgmp10 and libmpfr4 (closes: #27416).

* Mon Sep 19 2011 Alexey Tourbin <at@altlinux.ru> 0.9-alt1
- 0.9
- enabled check

* Wed Oct 20 2010 Kirill A. Shutemov <kas@altlinux.org> 0.8.2-alt1
- 0.8.2

* Sun Mar 21 2010 Kirill A. Shutemov <kas@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux Sisyphus

