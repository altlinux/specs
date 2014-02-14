%define appname smartcar
Name: umki
Version: 1.0
Release: alt1
Summary: Frontend to UMKI - Radio Controlled Robotic Construction Set
License: GPL
Group: Education
Url: http://umki.vinforika.ru/

Source: %name-%version.tar
Source1: %{name}.desktop

BuildRequires: libqt4-devel gcc-c++ desktop-file-utils

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
make clean
qmake-qt4
make
cd -

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_sysconfdir/%appname
mkdir -p %buildroot%_datadir/%appname
mkdir -p %buildroot%_datadir/applications

cd smartcar_linux
install -p -m755 %appname %buildroot%_bindir/
install -p -m644 smart.ini %buildroot%_sysconfdir/%appname
install -p -m644 zst.jpg %buildroot%_datadir/%appname
desktop-file-install --dir=%buildroot%_datadir/applications %SOURCE1

%files
%doc readme
%_bindir/%appname
%_sysconfdir/%appname
%_datadir/%appname
%_datadir/applications/%{name}.desktop

%files docs
%doc docum

%changelog
* Fri Feb 14 2014 Dmitry Derjavin <dd@altlinux.org> 1.0-alt1
- Initial ALTLinux build.

