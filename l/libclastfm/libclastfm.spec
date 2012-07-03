Name:		libclastfm
Version:	0.5
Release:	alt1.git.968af0ab
Summary:	Unofficial C-API for the Last.fm web service

Group:		System/Libraries
License:	GPLv2+
URL:		http://liblastfm.sourceforge.net
Source0:	%name-%version.tar
Packager:	Egor Glukhov <kaman@altlinux.org>

BuildRequires: libcurl-devel

%description
%name is an unofficial C-API for the Last.fm web service 
written with libcurl. libclastfm supports much more than 
basic scrobble submission. You can send shouts, fetch album covers 
and much more. 

%package devel
Summary: Development files for %{name}
Group:	 Development/C
Requires: %name = %version-%release

%description devel
This package contains the development files for %{name}.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README
%_libdir/*.so.*

%files devel
%_includedir/clastfm.h
%_libdir/*.so
%_pkgconfigdir/libclastfm.pc

%changelog
* Fri Apr 20 2012 Egor Glukhov <kaman@altlinux.org> 0.5-alt1.git.968af0ab
- Initial build for Sisyphus

* Sun Mar 06 2011 Matias De lellis <mati86dl@gmail.com> 0.4-1
- Libclastfm 0.4 - Initial release.
