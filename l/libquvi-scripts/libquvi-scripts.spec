%define _name quvi
%define ver_major 0.4

Name: lib%_name-scripts
Version: %ver_major.10
Release: alt1

Summary: Lua scripts for parsing the media details
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://downloads.sourceforge.net/project/%name/%ver_major/%name-%version.tar.xz
Patch: %name-0.4.4-alt-pkgconfig.patch

BuildArch: noarch
BuildRequires: quvi

%description
%name contains the embedded lua scripts that libquvi uses for parsing
the media details. Some additional utility scripts are also included.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files needed for building applications against
%name.

%prep
%setup -q
%patch

%build
%autoreconf
%configure
%make_build

%check
#%%make check

%install
%make DESTDIR=%buildroot install

%files
%_datadir/%name/
%_man7dir/%name.*
%doc NEWS README AUTHORS

%files devel
%_datadir/pkgconfig/*.pc

%changelog
* Thu Nov 22 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.10-alt1
- 0.4.10

* Sat Oct 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.9-alt1
- 0.4.9

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.8-alt1
- 0.4.8

* Thu Jul 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.7-alt1
- 0.4.7

* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.6-alt1
- 0.4.6

* Sat May 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- first build for Sisyphus
