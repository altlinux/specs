Name:           novnc
Version:        0.4
Release:        alt1
Summary:        VNC client using HTML5 (Web Sockets, Canvas) with encryption support
Requires:       python-module-websockify

Group:		Development/Python
License:        GPLv3
URL:            https://github.com/kanaka/noVNC
Source0:        https://github.com/downloads/kanaka/noVNC/novnc-%{version}.tar.gz

Patch1:         novnc-0.4-call-websockify.patch
Patch2:         novnc-0.4-manpage.patch
BuildArch:      noarch
BuildRequires:  python-devel

%description
Websocket implementation of VNC client

%prep
%setup
%patch1 -p1
%patch2 -p1

%build


%install
mkdir -p %{buildroot}/%{_usr}/share/novnc/utils
install -m 444 *html %{buildroot}/%{_usr}/share/novnc
#provide an index file to prevent default directory browsing
install -m 444 vnc.html %{buildroot}/%{_usr}/share/novnc/index.html

mkdir -p %{buildroot}/%{_usr}/share/novnc/include/
install -m 444 include/*.*  %{buildroot}/%{_usr}/share/novnc/include
mkdir -p %{buildroot}/%{_usr}/share/novnc/images
install -m 444 images/*.*  %{buildroot}/%{_usr}/share/novnc/images

mkdir -p %{buildroot}/%{_bindir}
install utils/launch.sh  %{buildroot}/%{_bindir}/novnc_server

mkdir -p %{buildroot}%{_mandir}/man1/
install -m 444 docs/novnc_server.1 %{buildroot}%{_mandir}/man1/

%{__install} -d %{buildroot}%{_sysconfdir}/sysconfig

%files
%doc README.md LICENSE.txt

%dir %{_usr}/share/novnc
%{_usr}/share/novnc/*.*
%dir %{_usr}/share/novnc/include
%{_usr}/share/novnc/include/*
%dir %{_usr}/share/novnc/images
%{_usr}/share/novnc/images/*
%{_bindir}/novnc_server
%{_mandir}/man1/novnc_server.1*

%changelog
* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4-alt1
- First build for ALT (based on Fedora 0.4-9.fc21.src)

