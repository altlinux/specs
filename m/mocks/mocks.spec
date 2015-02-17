Name: mocks
Version: 0.0.2
Release: alt1
Summary: My Own soCKs Server
License: GPLv2
Group: Networking/Other
Url: http://sourceforge.net/projects/mocks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%description
MOCKS is a small, easy configurable, RFC1928 compliant SOCKS 5 server
for Linux and Linux-like systems. MOCKS supports upstream proxy and
IP-based client filtering rules.

%prep
%setup

rm -f %name

%build
./build

%install
install -d %buildroot%_bindir
install -m755 %name %buildroot%_bindir/

%files
%doc CHANGELOG README TODO
%_bindir/*

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus

