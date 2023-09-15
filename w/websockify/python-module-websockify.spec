
Name: websockify
Version: 0.11.0
Release: alt1
Summary: WebSocket to TCP proxy/bridge
Group: Networking/Other

License: BSD-2-Clause AND LGPL-3.0-only AND MPL-2.0 AND BSD-3-Clause
Url: https://github.com/novnc/websockify
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
websockify was formerly named wsproxy and was part of the
noVNC project.

At the most basic level, websockify just translates WebSockets traffic
to normal socket traffic. Websockify accepts the WebSockets handshake,
parses it, and then begins forwarding traffic between the client and
the target in both directions.

%package -n python3-module-%name
Summary: WSGI based adapter for the Websockets protocol
Group: Development/Python3
Provides: %name = %EVR

%description -n python3-module-%name
websockify was formerly named wsproxy and was part of the
noVNC project.

At the most basic level, websockify just translates WebSockets traffic
to normal socket traffic. Websockify accepts the WebSockets handshake,
parses it, and then begins forwarding traffic between the client and
the target in both directions.

%prep
%setup

# remove unwanted shebang
sed -i '1 { /^#!/ d }' websockify/websocket*.py

%build
%python3_build

%install
%python3_install

rm -Rf %buildroot%_datadir/%name
mkdir -p %buildroot%_man1dir
install -m 644 docs/websockify.1 %buildroot%_man1dir

%files -n python3-module-%name
%doc COPYING README.md CHANGES.txt
%python3_sitelibdir/*
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Fri Sep 15 2023 Alexey Shabalin <shaba@altlinux.org> 0.11.0-alt1
- 0.11.0
- drop python2 package

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt2
- add python2 package

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Mar 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-2.fc21.src)

