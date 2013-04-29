Name: kde4-selinux
Version: 0.1
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - SELinux Utils
License: GPLv2

Source: %name-%version.tar

BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++
BuildRequires: libselinux-devel

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

%changelog
* Mon Apr 29 2013 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- Initial build

