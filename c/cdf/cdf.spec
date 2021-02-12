%def_disable clang

Summary: colorized df
Name: cdf
Version: 0.2
Release: alt3
Source0: %{name}-%{version}.tar.gz
URL: http://bmp-plugins.berlios.de/misc/cdf/cdf.html
License: GPL-2.0+
Group: Monitoring

%description
cdf is a tool simular to df(1), but with colors support. Note that 
cdf is _not_ just df with colors and it doesn't compatible with df 
(however, compatiblity with df may be realized later).

%if_enabled clang
BuildRequires(pre): clang-devel
%endif

%prep
%setup -q

%build
export CFLAGS="$CFLAGS -fcommon"
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif

%configure
%make

%install
%makeinstall

%files
%_bindir/*
%doc README AUTHORS NEWS TODO

%changelog
* Fri Feb 12 2021 Leontiy Volodin <lvol@altlinux.org> 0.2-alt3
- Built with gcc10.

* Mon Jan 18 2021 Leontiy Volodin <lvol@altlinux.org> 0.2-alt2
- Built with clang.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Jan 27 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.2-alt1
- 0.2

* Thu Nov 04 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.1-alt1
- Implementation build

