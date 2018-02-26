Name: liblinebreak
Version: 0.9.6
Release: alt1

Summary:  Line breaking in a Unicode sequence
License: BSD
Group:  Development/C
Url: http://vimgadgets.cvs.sourceforge.net/vimgadgets/common/tools/linebreak/
Source0: %name-%version.tar

%package -n %name-devel-static
Summary: Static libraries for %name
Summary(ru_RU.UTF-8): Статические библиотеки для %name
Group: Development/C

%description
Implementation of the line breaking algorithm as described in Unicode
5.0.0 Standard Annex 14.

%description -n %name-devel-static
Implementation of the line breaking algorithm as described in Unicode
5.0.0 Standard Annex 14.

You should install this package if you wish to develop statically linked
applications that utilize %name.


%prep
%setup -q

%build
%make_build CFG=Release CFLAGS="-fPIC"

%install

install -Dm644 ReleaseDir/%name.a %buildroot/%_libdir/%name.a
install -Dm644 linebreak.h  %buildroot/%_includedir/linebreak.h

%files -n %name-devel-static
%_libdir/*.a
%_includedir/*

%changelog
* Fri Mar 21 2008 Anton Farygin <rider@altlinux.ru> 0.9.6-alt1
- first build for Sisyphus

