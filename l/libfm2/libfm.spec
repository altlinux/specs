#%%set_automake_version 1.11

Name: 	 libfm2
Version: 1.2.0
Release: alt0.rc1.1

Summary: GIO-based library for file manager-like programs
License: GPL
Group:   System/Libraries
Url: 	 http://pcmanfm.sourceforge.net/

Source:  %name-%version.tar.gz

BuildPreReq: rpm-build-xdg
BuildRequires: intltool libmenu-cache-devel gtk-doc
BuildRequires: libdbus-glib-devel libudisks2-devel
BuildRequires: libgtk+3-devel
BuildRequires: vala >= 0.13.0
BuildRequires: libexif-devel
BuildRequires: libxslt-devel

Conflicts: libfm

%description
LibFM is a GIO-based library used to develop file manager-like programs.
It is developed as the core of next generation PCManFM and takes care of
all file-related operations such as copy & paste, drag & drop, file
associations or thumbnail support. By utilizing glib/gio and gvfs, libfm
can access remote filesystems supported by gvfs.

%package devel
Summary: Development files for %{name}
Group:   Development/Other
Conflicts: libfm-devel

%description devel
This package contains files needed to build libfm-dependent applications

%prep
%setup
sed -ri '/AM_INIT_AUTOMAKE/s,-Werror,\0 -Wno-portability,' configure.ac
%autoreconf

%build
%configure \
    --disable-static \
    --disable-silent-rules \
    --enable-largefile \
    --enable-gtk-doc \
    --with-gtk=3 \
    --enable-udisks \
    --sysconfdir=/etc

%make_build

# FIXME: tilda versions don't work with RPM in general
sed -i 's,\~[a-z0-9]*,,g' libfm*.pc

%install
%makeinstall_std
%find_lang libfm

# Remove pkgconfig for gtk2
rm -f %buildroot%_pkgconfigdir/libfm-gtk.pc

# Remove unnecessary files
rm -f %buildroot%_libdir/libfm/modules/*.la

%files -f libfm.lang
%_xdgconfigdir/*
%_bindir/*
%_libdir/*.so.*
%_libdir/libfm/modules/*.so

%_xdgmimedir/packages/*
%_datadir/libfm/
%_desktopdir/*
%doc %_man1dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%doc %_datadir/gtk-doc/html/libfm/*

%changelog
* Fri Mar 07 2014 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt0.rc1.1
- Build libfm 1.2.0 as separate package
