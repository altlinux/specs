%define  git_commit 8389ecb

Name: 	 kiwix
Version: 0.9
Release: alt0.rc4.1.git%git_commit
Summary: Kiwix is an offline reader for Web content like Wikipedia

License: GPLv3
Group: 	 Office
URL: 	 http://www.kiwix.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
Source1: %name.desktop

# Fix build with xulrunner 27.x (see https://bugzilla.mozilla.org/show_bug.cgi?id=951984#c7)
Patch1:  %name-build-with-xulrunner-27.patch

BuildRequires: aria2 >= 1.18.3
BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libcryptopp-devel
BuildRequires: libctpp-devel
BuildRequires: libicu-devel
BuildRequires: liblzma-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libpugixml-devel
BuildRequires: libssl-devel
BuildRequires: libuuid-devel
BuildRequires: libxapian-devel
BuildRequires: libzim-devel
BuildRequires: python-modules
BuildRequires: xapian-core
BuildRequires: xulrunner-devel >= 27.0
BuildRequires: zlib-devel

BuildRequires: zip
BuildRequires: wget
BuildRequires: bc

Requires: aria2 >= 1.18.3

%description
Kiwix is an offline reader for Web content. It's especially intended to
make Wikipedia available offline. Kiwix manages to do that by reading
ZIM files, a highly compressed open format with additional meta-data.

%prep
%setup -q

%patch1 -p1

# Prepare environment for automake
touch NEWS
mv CHANGELOG ChangeLog
# Copy localized desktop file
cp -f %SOURCE1 desktop/%name.desktop

%build
%add_optflags -I/usr/include/nspr
%autoreconf
%configure --disable-android \
	   --with-gecko-sdk=%_libdir/xulrunner-devel
%make_build

%install
%makeinstall_std
# Put main executable file in /usr/bin
ln -s %_libdir/%name/%name %buildroot%_bindir/%name

%files
%doc ChangeLog COPYING AUTHORS README
%_sysconfdir/*
%_bindir/kiwix**
%_libdir/kiwix/*
%_desktopdir/%name.desktop
%_datadir/application-registry/%name.applications
%_datadir/%name
%doc %_man1dir/*
%doc %_mandir/fr/man1/*
%_xdgmimedir/packages/%name.xml
%_iconsdir/%name
%_pixmapsdir/*

%changelog
* Fri Feb 14 2014 Andrey Cherepanov <cas@altlinux.org> 0.9-alt0.rc4.1.git8389ecb
- Update version from upstream
- Rebuild with new xulrunner

* Tue Jan 21 2014 Andrey Cherepanov <cas@altlinux.org> 0.9-alt0.rc3.git3704cdd.2
- Remove deprecated fix for bad aria2c binary name

* Mon Jan 20 2014 Andrey Cherepanov <cas@altlinux.org> 0.9-alt0.rc3.git3704cdd.1
- Put main executable file in /usr/bin
- Add aria2 as required program
- Fix hardcoded path to aria2c
- Add Russian localization to desktop file

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 0.9-alt0.rc3.git3704cdd
- Initial build in Sisyphus
