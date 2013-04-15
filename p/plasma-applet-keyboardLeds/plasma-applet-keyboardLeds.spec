Name: plasma-applet-keyboardLeds
Version: 0.1
Release: alt1.r951154.qa1

Summary: Keyboard LEDs indicator plasma applet
License: GPLv2+
Group: Graphical desktop/KDE

Url: http://kde.org

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): kde-common-devel
BuildPreReq: gcc-c++ kde4libs-devel

%description
This applet shows keyboard LEDs states.

%prep
%setup

%build
%K4build

%install
%K4install

%files
%_libdir/kde4/*.so
%_K4apps/desktoptheme/default/widgets/*
%_K4srv/%name.desktop

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt1.r951154.qa1
- NMU: rebuilt for debuginfo.

* Sat May 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.1-alt1.r951154
- initial build

