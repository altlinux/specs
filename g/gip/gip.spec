Name: gip
Version: 1.7.0
Release: alt2
Summary: Internet Protocol Calculator for Gnome

Group: Networking/Other
License: GPL
Url: http://code.google.com/p/gip/

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libgtkmm2-devel intltool gcc-c++

%description
Gip is an application for making IP address based calculations.
For example, it can display IP addresses in binary format.
It is also possible to calculate subnets.

%prep
%setup -q

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
%_niconsdir/calc.png
%_liconsdir/calc.png
%_datadir/mime/packages/%name.xml
%doc AUTHORS ChangeLog COPYING

%changelog
* Mon Feb 07 2011 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt2
- fixed %%files section (do not include debuginfo files)

* Thu Oct 21 2010 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt1
- initial build

