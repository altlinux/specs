%define  git_commit 3704cdd

Name: 	 kiwix
Version: 0.9
Release: alt0.rc3.git%git_commit.1
Summary: Kiwix is an offline reader for Web content like Wikipedia

License: GPLv3
Group: 	 Office
URL: 	 http://www.kiwix.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  %name-%version.tar
Source1: %name.desktop

BuildRequires: aria2
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
BuildRequires: xulrunner-devel
BuildRequires: zlib-devel

BuildRequires: zip
BuildRequires: wget
BuildRequires: bc

Requires: aria2

%description
Kiwix is an offline reader for Web content. It's especially intended to
make Wikipedia available offline. Kiwix manages to do that by reading
ZIM files, a highly compressed open format with additional meta-data.

%prep
%setup -q
# Prepare environment for automake
touch NEWS
mv CHANGELOG ChangeLog
# Copy localized desktop file
cp -f %SOURCE1 desktop/%name.desktop
# Fix hardcoded path to aria2c
subst 's/"aria2c"/"aria2"/' kiwix/chrome/content/main/js/content.js

%build
%add_optflags -I/usr/include/nspr
%autoreconf
%configure --disable-android \
	   --with-gecko-sdk=%_libdir/xulrunner-devel \
	   --with-aria2=%_bindir/aria2
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
* Mon Jan 20 2014 Andrey Cherepanov <cas@altlinux.org> 0.9-alt0.rc3.git3704cdd.1
- Put main executable file in /usr/bin
- Add aria2 as required program
- Fix hardcoded path to aria2c
- Add Russian localization to desktop file

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 0.9-alt0.rc3.git3704cdd
- Initial build in Sisyphus
