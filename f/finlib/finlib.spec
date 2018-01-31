%def_disable static

Name: finlib
Version: 2.36.5
Release: alt1

Summary: Fast indexing library
License: LGPLv2+
Group: System/Libraries
Url: http://corpora.fi.muni.cz/noske/src/finlib/finlib-2.28.2.tar.gz
Packager: Kirill Maslinsky <kirill@altlinux.org>
BuildRequires: gcc-c++ libicu-devel


Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
Fast Indexing Library

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%prep
%setup
%patch -p1

%build
autoreconf -iv
%configure %{subst_enable static} --with-icu
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README NEWS
%_libdir/*.so.*
%_bindir/*

%files devel
%_includedir/%name/*.hh
%_libdir/*.so

%if_enabled static
%files devel-static
%_libdir/lib%name.a
%endif

%changelog
* Wed Jan 31 2018 Kirill Maslinsky <kirill@altlinux.org> 2.36.5-alt1
- 2.36.5

* Tue Oct 18 2016 Kirill Maslinsky <kirill@altlinux.org> 2.35.2-alt1
- 2.35.2

* Mon Feb 15 2016 Kirill Maslinsky <kirill@altlinux.org> 2.33.1-alt2
- rebuilt with libicu 5.6

* Sat Dec 05 2015 Kirill Maslinsky <kirill@altlinux.org> 2.33.1-alt1
- 2.33.1

* Wed Mar 18 2015 Kirill Maslinsky <kirill@altlinux.org> 2.28.2-alt1
- 2.28.2

* Wed Oct 02 2013 Kirill Maslinsky <kirill@altlinux.org> 2.19.3-alt1
- 2.19.3

* Tue Apr 10 2012 Kirill Maslinsky <kirill@altlinux.org> 2.11-alt1
- Initial build for Sisyphus

