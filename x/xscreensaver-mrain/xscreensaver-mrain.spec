Name: xscreensaver-mrain
Version: 1.0.0
Release: alt1
Summary: A screen saver Matrix Rain for the X window system
License: GPL
Group: Graphical desktop/Other
Url: http://sourceforge.net/projects/mrain/

Packager: Denis Pynkin <dans@altlinux.org>

Source: %name-%version.tar
Source1: %name.xss
Source2: %name.desktop

BuildRequires: gcc-c++
BuildRequires: glibc-kernheaders libGL-devel
BuildRequires: rpm-build-xscreensaver

%description
A Matrix Rain is a classic matrix screensaver, which can capture a video 
from your web-camera and display video like the "matrix-style" in real time.


%prep
%setup -q

%build
%make

%install
mkdir -p %buildroot{%xss_ad_dir,%xss_hack_dir,%_man6dir,%_desktopdir}
install -m 755 out/mrain %buildroot/%xss_hack_dir/
install -m 644 nix/manpage.1 %buildroot/%_man6dir/mrain.6
install -m 644 %SOURCE1 %buildroot%xss_ad_dir/mrain.xss
install -m 644 %SOURCE2 %buildroot%_desktopdir/mrain.desktop

%files
%doc license
%xss_ad_dir/mrain.xss
%xss_hack_dir/mrain
%_desktopdir/mrain.desktop
%_man6dir/*

%changelog
* Wed Feb 15 2012 Denis Pynkin <dans@altlinux.org> 1.0.0-alt1
- Initial version for ALTLinux
