%define  git_commit 3704cdd

Name: 	 kiwix
Version: 0.9
Release: alt0.rc3.git%git_commit
Summary: Kiwix is an offline reader for Web content like Wikipedia

License: GPLv3
Group: 	 Office
URL: 	 http://www.kiwix.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  kiwix-%version.tar

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

%description
Kiwix is an offline reader for Web content. It's especially intended to
make Wikipedia available offline. Kiwix manages to do that by reading
ZIM files, a highly compressed open format with additional meta-data.

%prep
%setup -q
# Prepare environment for automake
touch NEWS
mv CHANGELOG ChangeLog

%build
%add_optflags -I/usr/include/nspr
%autoreconf
%configure --disable-android \
	   --with-gecko-sdk=%_libdir/xulrunner-devel \
	   --with-aria2=%_bindir/aria2
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog COPYING AUTHORS README
%_sysconfdir/*
%_bindir/*
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
* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 0.9-alt0.rc3.git3704cdd
- Initial build in Sisyphus
