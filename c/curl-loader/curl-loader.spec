Summary: An HTTP and FTP simulating application load
Name: curl-loader
Version: 0.56
Release: alt2
Url: http://curl-loader.sourceforge.net/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: Networking/WWW

BuildRequires: libssl-devel zlib-devel libevent-devel libcurl-devel libcares-devel


%description
curl-loader (also known as "omes-nik" and "davilka") is an open-source
tool written in C-language, simulating application load and application
behavior of thousands and tens of thousand HTTP/HTTPS and FTP/FTPS
clients, each with its own source IP-address. In contrast to other
tools curl-loader is using real C-written client protocol stacks,
namely, HTTP and FTP stacks of libcurl and TLS/SSL of openssl,
and simulates user behavior with support for login and authentication
flavors.

The goal of the project is to deliver a powerful and flexible
open-source testing solution as a real alternative to Spirent 
Avalanche and IXIA IxLoad.

%prep
%setup

%build
mkdir obj
%make

%install
%makeinstall_std


%files
%_bindir/curl-loader
%_man1dir/curl-loader.1*
%_man5dir/curl-loader-config.5*
%doc doc/* conf-examples

%changelog
* Mon Feb 29 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.56-alt2
- Rebuilded to fix man pages archiving method.

* Sat Feb 16 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.56-alt1
- Initial build

