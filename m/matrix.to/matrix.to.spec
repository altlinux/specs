Name: matrix.to
Version: 1.2.17
Release: alt1

Summary: A simple URL redirecting service for the Matrix ecosystem

License: Apache-2.0
Group: Networking/WWW
Url: https://github.com/matrix-org/matrix.to

# Source-url: https://github.com/matrix-org/matrix.to/archive/%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from
# etersoft-build-utils
Source1: %name-development-%version.tar

BuildArch: noarch

AutoReq: no
AutoProv: no

BuildRequires: /usr/bin/node

%description
A simple stateless privacy-protecting URL redirecting service for the
Matrix.org ecosystem which lets users share links to Matrix entities
without being tied to a specific app.

%prep
%setup -a1

%build
node scripts/build.js

%install
mkdir -p %buildroot/var/www/html/
cp -a build %buildroot/var/www/html/%name/

%files
/var/www/html/%name/

%changelog
* Thu Apr 02 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.17-alt1
- initial build for ALT Sisyphus

