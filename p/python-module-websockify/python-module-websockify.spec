Name: python-module-websockify
Version: 0.8.0
Release: alt1
Summary: WSGI based adapter for the Websockets protocol
Group: Development/Python

License: LGPLv3
Url: https://github.com/kanaka/websockify
Source0: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
Python WSGI based adapter for the Websockets protocol

%prep
%setup

# remove unwanted shebang
sed -i '1 { /^#!/ d }' websockify/websocket*.py
# drop unneeded executable bit
chmod -x include/web-socket-js/web_socket.js

%build
%python_build

%install
%python_install

%files
%doc LICENSE.txt README.md CHANGES.txt
%python_sitelibdir/*
%_bindir/websockify
%_datadir/websockify

%changelog
* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Mar 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-2.fc21.src)

