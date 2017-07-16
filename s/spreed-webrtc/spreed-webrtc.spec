Name: spreed-webrtc
Version: 0.29.6
Release: alt1

Summary: A WebRTC audio/video call and conferencing server
License: AGPLv3
Group: System/Servers
Url: https://github.com/strukturag/spreed-webrtc/

Source: %name-%version-%release.tar

BuildRequires: golang node
BuildRequires: golang(github.com/gorilla/mux) golang(github.com/gorilla/websocket)

%description
Spreed WebRTC implements a WebRTC audio/video call and conferencing server.

%prep
%setup

%build
[ ! -x autogen.sh ] || sh autogen.sh
%configure
%make_build DEB_BUILDING=1

%install
%makeinstall_std
find %buildroot%_datadir/spreed-webrtc-server -type f -print0 |xargs -0 chmod 0644
install -pm0644 -D spreed-webrtc.service %buildroot%_unitdir/%name.service
install -pm0640 -D server.conf.in %buildroot%_sysconfdir/%name.conf
install -pm0644 -D spreed-webrtc.sysconfig %buildroot%_sysconfdir/sysconfig/%name

%pre
/usr/sbin/groupadd -r -f _spreed &>/dev/null ||:
/usr/sbin/useradd -r -g _spreed -d %_datadir/spreed-webrtc-server/www -s /dev/null \
    -c "Spreed WebRTC" -M -n _spreed &>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md doc
%attr(0640,root,_spreed) %config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_sbindir/spreed-webrtc-server
%_datadir/spreed-webrtc-server

%changelog
* Sun Jul 16 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.29.6-alt1
- initial
