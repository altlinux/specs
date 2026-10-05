Name: evolution-etesync
Version: 1.1.2
Release: alt1

Summary: EteSync backend for Evolution and Evolution Data Server

License: LGPL-2.1-or-later
Group: Networking/Mail
Url: https://gitlab.gnome.org/GNOME/evolution-etesync

# Source-url: https://gitlab.gnome.org/GNOME/evolution-etesync/-/archive/%version/evolution-etesync-%version.tar.gz
Source: %name-%version.tar
# pass seconds, not milliseconds, to notes CREATED/LAST-MODIFIED
# https://gitlab.gnome.org/GNOME/evolution-etesync/-/merge_requests/9
Patch: evolution-etesync-notes-time-seconds.patch

# etebase keeps mtime as int64_t milliseconds, the code stores it in time_t:
# on 32-bit time_t it overflows and fails to build (incompatible pointer type)
ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake intltool
BuildRequires: evolution-data-server-devel >= 3.34.0
BuildRequires: evolution-devel >= 3.34.0
BuildRequires: libgtk+3-devel
BuildRequires: libetebase-devel

%description
This package provides an EteSync backend for Evolution Data Server and
an Evolution module to configure EteSync accounts. EteSync is a secure,
end-to-end encrypted and privacy respecting sync for contacts and
calendars (address books, calendars and task lists).

%prep
%setup
%patch -p1

%build
# keep upstream RPATH: modules link to the private libevolution-etesync.so
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
%find_lang %name

%files -f %name.lang
%doc README.md NEWS
%_libdir/%name/
%_libdir/evolution-data-server/addressbook-backends/libebookbackendetesync.so
%_libdir/evolution-data-server/calendar-backends/libecalbackendetesync.so
%_libdir/evolution-data-server/registry-modules/module-etesync-backend.so
%_libdir/evolution-data-server/credential-modules/module-etesync-credentials.so
%_libdir/evolution/modules/module-etesync-configuration.so
%_datadir/metainfo/org.gnome.Evolution-etesync.metainfo.xml

%changelog
* Mon Oct 05 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for Sisyphus
