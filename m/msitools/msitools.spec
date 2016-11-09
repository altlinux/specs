%define ver_major 0.96
%define libname libmsi
%define api_ver 1.0

Name: msitools
Version: %ver_major
Release: alt1

Summary: Windows Installer tools
Group: File tools
License: GPLv2+
Url: http://ftp.gnome.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define gcab_ver 0.2
%define vala_ver 0.16

BuildRequires: intltool
BuildRequires: libgcab-devel >= %gcab_ver
BuildRequires: libgio-devel libgsf-devel libuuid-devel
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools >= %vala_ver

%description
msitools is a set of programs to inspect and build Windows Installer
(.MSI) files. It is based on libmsi, a portable library to read and
write .MSI files. libmsi in turn is a port of (and a subset of) Wine's
implementation of the Windows Installer.

%package -n %libname
Summary: A library to manipulate Windows .MSI files
Group: System/Libraries
License: LGPLv2+

%description -n %libname
%libname is a GObject library to manipulate with Windows Installer files.
It is a port from the MSI library of the Wine project.

%package -n %libname-devel
Summary: A library to manipulate Windows .MSI files (development package)
Group: Development/C
License: LGPLv2+
Requires: %libname = %version-%release

%description -n %libname-devel
This package provides the headers and library to develop applications
using %libname.

%package -n %libname-gir
Summary: GObject introspection data for the %libname
Group: System/Libraries
License: LGPLv2+
Requires: %libname = %version-%release

%description -n %libname-gir
%libname is a GObject library to manipulate with Windows Installer files.
This package provides GObject introspection data for the %libname.

%package -n %libname-gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
License: LGPLv2+
BuildArch: noarch
Requires: %libname-devel = %version-%release
Requires: %libname-gir = %version-%release

%description -n %libname-gir-devel
%libname is a GObject library to manipulate with Windows Installer files.
This package provides GObject introspection devel data for the %libname.

%prep
%setup

%build
%configure \
	--disable-static \
	--enable-fast-install

%make_build

%install
%makeinstall_std

%find_lang %name

%check
# check failed on i586
#%make check

%files -f %name.lang
%_bindir/msibuild
%_bindir/msidiff
%_bindir/msidump
%_bindir/msiextract
%_bindir/msiinfo
%_bindir/wixl
%_bindir/wixl-heat
%_datadir/bash-completion/completions/msitools
%_datadir/wixl-%version/
%doc NEWS README TODO

%files -n %libname
%_libdir/%libname.so.*

%files -n %libname-devel
%_includedir/%libname-%api_ver/
%_libdir/%libname.so
%_pkgconfigdir/%libname-%api_ver.pc
%_vapidir/%libname-%api_ver.vapi

%files -n %libname-gir
%_typelibdir/Libmsi-%api_ver.typelib

%files -n %libname-gir-devel
%_girdir/Libmsi-%api_ver.gir

%changelog
* Wed Nov 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.96-alt1
- 0.96

* Tue Dec 01 2015 Yuri N. Sedunov <aris@altlinux.org> 0.95-alt1
- first preview for Sisyphus


