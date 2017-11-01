Name: novnc
Version: 0.6.2
Release: alt1
Summary: VNC client using HTML5 (Web Sockets, Canvas) with encryption support
Requires: python-module-websockify

Group: Development/Python
License: GPLv3
Url: https://github.com/kanaka/noVNC
Source: %name-%version.tar

Patch2: novnc-0.4-manpage.patch
BuildArch: noarch
BuildRequires: python-devel

%description
Websocket implementation of VNC client

%prep
%setup
%patch2 -p1

%build
%install
mkdir -p %buildroot%_datadir/novnc/utils
install -m 644 *html %buildroot%_datadir/novnc
#provide an index file to prevent default directory browsing
install -m 644 vnc.html %buildroot%_datadir/novnc/index.html

mkdir -p %buildroot%_datadir/novnc/include/
install -m 644 include/*.*  %buildroot%_datadir/novnc/include
mkdir -p %buildroot%_datadir/novnc/images
install -m 644 images/*.*  %buildroot%_datadir/novnc/images

mkdir -p %buildroot%_bindir
install utils/launch.sh  %buildroot%_bindir/novnc_server

mkdir -p %buildroot%_man1dir/
install -m 644 docs/novnc_server.1 %buildroot%_man1dir/

%files
%doc README.md LICENSE.txt

%_datadir/novnc
%_bindir/novnc_server
%_man1dir/novnc_server.1*

%changelog
* Wed Nov 01 2017 Lenar Shakirov <snejok@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.1-alt1
- 0.5.1
- cleanup spec

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4-alt1
- First build for ALT (based on Fedora 0.4-9.fc21.src)

