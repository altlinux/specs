%define _name libquvi-scripts
%define ver_major 0.9
%define snapshot 20131012

Name: %_name%ver_major
Version: %ver_major.%snapshot
Release: alt1

Summary: Lua scripts for parsing the media details
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://downloads.sourceforge.net/project/%_name/%ver_major/%_name-%version.tar.xz
Patch: %_name-0.9.20130903-alt-pkgconfig.patch

BuildArch: noarch
# for tests
#BuildRequires: libquvi%ver_major-devel

%description
%name contains the embedded lua scripts that libquvi uses for parsing
the media details. Some additional utility scripts are also included.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files needed for building applications against
%name

%prep
%setup -n %_name-%version
#%%patch
subst 's@\(^pkgconfigdir[[:space:]]=[[:space:]]\$(\)libdir\()/pkgconfig\)@\1datadir\2@' Makefile.*

%build
# Autoconf version 2.69 or higher is required
#%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
#%%make check

%files
%_datadir/%_name/
%_man7dir/%_name.*
%_man7dir/quvi-modules-3rdparty.7.*
%_man7dir/quvi-modules.7.*
%doc NEWS README AUTHORS

%files devel
%_datadir/pkgconfig/*.pc

%changelog
* Fri Oct 25 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.20131012-alt1
- official snapshot

* Tue Sep 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.20130903-alt1
- first build for Sisyphus

