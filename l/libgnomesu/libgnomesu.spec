%define oname gnomesu
%define soname 0

Name: libgnomesu
Version: 2.0.10
Release: alt1

Url: https://github.com/openSUSE/libgnomesu
Vcs: https://github.com/openSUSE/libgnomesu

License: LGPL-2.1-or-later
Group: System/Libraries

Summary: GNOME su library and utility

Source: %name-%version.tar

BuildRequires: intltool glib2-devel pkgconfig(gtk+-3.0)
BuildRequires: libpam0-devel libgnomeui-devel

%description
Libgnomesu is a library for providing superuser privileges to GNOME
applications. It supports sudo, consolehelper, PAM and su.

%package devel
Summary: Development files for %name
Group: Development/C
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %name%soname
Group: System/Libraries
Summary: %name library
%description -n %name%soname
%name library.

%prep
%setup

%build
export SUID_CFLAGS="-fPIE"
export SUID_LDFLAGS="-pie"
export LDFLAGS="-Wl,--copy-dt-needed-entries"
mkdir m4
intltoolize -f
%autoreconf
%configure	\
	--disable-setuid-error \
	--disable-silent-rules
%make_build

%install
%makeinstall PAMDIR=%buildroot%_sysconfdir/pam.d

%find_lang %name --all-name

%files -f %name.lang
%doc README.md AUTHORS COPYING
%_sysconfdir/pam.d/%oname-pam
%_bindir/%oname
%_libexecdir/%{oname}*

%files devel
%_includedir/%name-1.0
%_pkgconfigdir/*.pc
%_libdir/%name.so

%files -n %name%soname
%_libdir/%name.so.%soname
%_libdir/%name.so.%{soname}.*

%changelog
* Tue Apr 28 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.0.10-alt1
- Initial build for ALT Linux.

