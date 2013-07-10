Name: kde4-selinux
Version: 0.2.3
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - SELinux Utils
License: GPLv2

Source: %name-%version.tar

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++
BuildRequires: libselinux-devel
BuildRequires: kde4base-workspace-devel libEGL-devel

%description
SELinux utils for the K Desktop Environment.


%prep
%setup -q

%build
%K4cmake
%K4make

%install
%K4install

%files
%_K4lib/mandatoryattributesplugin.so
%_K4srv/mandatoryattributesplugin.desktop
%_K4lib/kwin4_effect_seframe.so
%_K4srv/kwin/seframeeffect.desktop

%changelog
* Wed Jul 10 2013 Timur Aitov <timonbl4@altlinux.org> 0.2.3-alt1
- fix utf8

* Mon Jun 24 2013 Timur Aitov <timonbl4@altlinux.org> 0.2.2-alt1
- fix seframeeffect

* Fri Jun 21 2013 Timur Aitov <timonbl4@altlinux.org> 0.2.1-alt1
- seframeeffect: enabled by default

* Wed Jun 19 2013 Timur Aitov <timonbl4@altlinux.org> 0.2-alt2
- add BuildRequires

* Wed Jun 19 2013 Timur Aitov <timonbl4@altlinux.org> 0.2-alt1
- add seframe kwin effect

* Mon Apr 29 2013 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- Initial build

