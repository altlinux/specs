Name: mingw32-pkg-config
Version: 0.25
Release: alt1

Summary: A library management system used for cross-compiling for %_mingw32_target target

License: GPL v2 or later
Group: Development/Other
Url: http://www.mingw.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pkgconfig.freedesktop.org/releases/pkg-config-%version.tar
Patch: pkg-config-dnl.patch

BuildRequires: rpm-build-mingw32

BuildRequires: mingw32-filesystem >= 38

# NB: This must be left in.
Requires: mingw32-filesystem >= 38
# Because we will not install the pkg.m4 package
Requires: pkg-config

%description
The pkg-config program is used to retrieve information about installed
libraries in the system. It is typically used to compile and link
against one or more libraries.
This version is used for cross-compiling for %_mingw32_target target.

%prep
%setup -n pkg-config-%version
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
  --prefix=%prefix \
  --program-prefix=%_mingw32_target- \
  --with-pc-path=%_mingw32_libdir/pkgconfig:%_mingw32_datadir/pkgconfig

%make_build all || make all

%install
%makeinstall_std

# These files conflict with ordinary pkg-config.
rm -rf %buildroot%_mandir
rm -rf %buildroot%_datadir

%files
%_bindir/%_mingw32_target-pkg-config

%changelog
* Fri Mar 25 2011 Vitaly Lipatov <lav@altlinux.ru> 0.25-alt1
- initial build for ALT Linux Sisyphus (thanks, SUSE)

