Name: gip
Version: 1.7.0
Release: alt3
Summary: Internet Protocol Calculator for Gnome

Group: Networking/Other
License: GPL
Url: http://code.google.com/p/gip/

Source: %name-%version.tar
Patch1: %name-%version-ubuntu.patch
Patch2: %name-%version-c++11.patch
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libgtkmm2-devel intltool gcc-c++

%description
Gip is an application for making IP address based calculations.
For example, it can display IP addresses in binary format.
It is also possible to calculate subnets.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
export LIBDIR=lib
./build.sh --prefix %_prefix

%install
mkdir -p %buildroot%_prefix
export LIBDIR=lib
./build.sh --install --prefix %buildroot%_prefix
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%doc AUTHORS ChangeLog COPYING

%changelog
* Thu Jul 07 2016 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt3
- applied patches to FTBFS.
- removed icons (Closes: #32253)

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.7.0-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Feb 07 2011 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt2
- fixed %%files section (do not include debuginfo files)

* Thu Oct 21 2010 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt1
- initial build

