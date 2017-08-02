Name: enlightenment-module-desksanity
Version: 1.1.0
Release: alt2.git.6.g4de6a6e

Summary: desksanity module for the Enlightenment window manager
License: BSD
Group: Graphical desktop/Enlightenment
Url: https://git.enlightenment.org/enlightenment/modules/desksanity.git

# GIT https://git.enlightenment.org/enlightenment/modules/desksanity.git
Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 02 2016
# optimized out: efl-libs efl-libs-devel elementary-data enlightenment fontconfig gnome-icon-theme gnu-config icon-theme-hicolor libelementary-devel libgpg-error libjson-c pkg-config terminology
BuildRequires: enlightenment-devel

Requires: enlightenment

%description
desksanity module for the Enlightenment window manager

%prep
%setup

%build
./autogen.sh \

%make_build

%install
%makeinstall_std

%files
%_libdir/enlightenment/modules/desksanity
%doc AUTHORS COPYING NEWS README

%changelog
* Tue Aug 01 2017 Ildar Mulyukov <ildar@altlinux.ru> 1.1.0-alt2.git.6.g4de6a6e
- new GIT snapshot

* Fri Oct 28 2016 Ildar Mulyukov <ildar@altlinux.ru> 1.1.0-alt1.1
- rebuild with new E

* Wed Mar 02 2016 Ildar Mulyukov <ildar@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus

