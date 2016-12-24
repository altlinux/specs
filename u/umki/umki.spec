# This spec is backported to ALTLinux p7 automatically by rpmbph script. Do not edit it.
#
%define appname smartcar
Name: umki
Version: 1.10
Release: alt1
Summary: Frontend to UMKI - Radio Controlled Robotic Construction Set
License: GPL
Group: Education
Url: http://umki.vinforika.ru/

Source: %name-%version.tar
Source1: %{name}.desktop
Source2: %{appname}.svg
Source3: %{appname}-16x16.png
Source4: %{appname}-32x32.png
Source5: %{appname}-48x48.png

BuildRequires: libqt4-devel libqwt-devel gcc-c++ desktop-file-utils qt4-serialport-devel

%description
UMKI in Russian stands for Radio Controlled Robotic Construction Set,
Innovative. It helps children to design robots and learn to control
them.

%package docs
Summary: Documentation for %name
Group: Education
BuildArch: noarch

%description docs
Documentation for UMKI, which in Russian stands for Radio Controlled
Robotic Construction Set, Innovative. It helps children to design
robots and learn to control them.

%prep
%setup -q

%build
cd smartcar_linux
qmake-qt4 smartcar.pro
make clean
make
cd -

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_sysconfdir/%appname
mkdir -p %buildroot%_datadir/%appname
mkdir -p %buildroot%_datadir/applications
mkdir -p %buildroot%_datadir/pixmaps
mkdir -p %buildroot%_miconsdir/
mkdir -p %buildroot%_niconsdir/
mkdir -p %buildroot%_liconsdir/

cd smartcar_linux
install -p -m755 %appname %buildroot%_bindir/
install -p -m644 smart.ini %buildroot%_sysconfdir/%appname
install -p -m644 ../Vehicle/zst.jpg %buildroot%_datadir/%appname
desktop-file-install --dir=%buildroot%_datadir/applications %SOURCE1
install -p -m644 %SOURCE2 %buildroot%_datadir/pixmaps
install -p -m644 %SOURCE3 %buildroot%_miconsdir/%{appname}.png
install -p -m644 %SOURCE4 %buildroot%_niconsdir/%{appname}.png
install -p -m644 %SOURCE5 %buildroot%_liconsdir/%{appname}.png

%files
%doc readme
%_bindir/%appname
%_sysconfdir/%appname
%_datadir/%appname
%_datadir/applications/%{name}.desktop
%_datadir/pixmaps/%{appname}.svg
%_miconsdir/%{appname}.png
%_niconsdir/%{appname}.png
%_liconsdir/%{appname}.png

%files docs
%doc docum

%changelog
* Sat Dec 24 2016 Dmitry Derjavin <dd@altlinux.org> 1.10-alt1
- 1.10.

* Fri Jan 22 2016 Dmitry Derjavin <dd@altlinux.org> 1.8-alt1
- kumir2 support review.

* Wed May 27 2015 Dmitry Derjavin <dd@altlinux.org> 1.7-alt1
- Forward port of 1.7 from p7 branch based development.

* Tue Feb 03 2015 Dmitry Derjavin <dd@altlinux.org> 1.3-alt1
- 1.3.

* Fri Sep 12 2014 Dmitry Derjavin <dd@altlinux.org> 1.2-alt1
- 1.2;
- png icons added.

* Tue Sep 02 2014 Dmitry Derjavin <dd@altlinux.org> 1.1-alt2
- SVG icon added;
- .desktop file cleaned up.

* Tue Sep 02 2014 Dmitry Derjavin <dd@altlinux.org> 1.1-alt1
- 1.1;
- shorter description in .desktop file.

* Fri Feb 14 2014 Dmitry Derjavin <dd@altlinux.org> 1.0-alt1
- Initial ALTLinux build.

