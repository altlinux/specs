Name: liblinebreak
Version: 2.1
Release: alt1

Summary:  Line breaking in a Unicode sequence
License: BSD
Group:  Development/C
Url: http://vimgadgets.cvs.sourceforge.net/vimgadgets/common/tools/linebreak/
Source0: %name-%version.tar
Source1: %name.watch

%package devel
Summary: Libraries for %name
Summary(ru_RU.UTF-8): Динамические библиотеки для %name
Group: Development/C

%description
Implementation of the line breaking algorithm as described in Unicode
5.0.0 Standard Annex 14.

%description devel
Implementation of the line breaking algorithm as described in Unicode
5.0.0 Standard Annex 14.

You should install this package if you wish to develop 
applications that utilize %name.


%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%makeinstall

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENCE NEWS README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so


%changelog
* Tue Oct 15 2013 Anton Farygin <rider@altlinux.ru> 2.1-alt1
- new version

* Fri Mar 21 2008 Anton Farygin <rider@altlinux.ru> 0.9.6-alt1
- first build for Sisyphus

