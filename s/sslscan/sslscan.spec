Name: sslscan
Version: 1.10.2
Release: alt1
Summary: Security assessment tool for SSL
Group: Security/Networking
#Special exception to allow linking against the OpenSSL libraries
License: GPLv3+ with exceptions
Url: http://www.dinotools.org/tag/sslscan.html
# https://github.com/DinoTools/sslscan/archive/%version.tar.gz
Source0: %name-%version.tar

BuildRequires: libssl-devel

%description
SSLScan queries SSL services, such as HTTPS, in order to determine the
ciphers that are supported. SSLScan is designed to be easy, lean and
fast. The output includes preferred ciphers of the SSL service, the
certificate and is in Text and XML formats.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc Changelog README.md LICENSE TODO
%_bindir/%name
%_mandir/man1/%name.1*

%changelog
* Mon May 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.10.2-alt1
- Initial build.
