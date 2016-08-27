Name: lessjs
Version: 2.5.1
Release: alt1

Summary: Less.js The dynamic stylesheet language

# cssmin.js is licensed under BSD license
# everything else is ASL 2.0
License: ASL 2.0 and BSD

Group: Development/Tools
Url: http://lesscss.org

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/less/less.js/archive/v%version.tar.gz
Source: %name-%version.tar

# Use /usr/share paths instead of /usr/lib
# Remove pre-built files from the dist/ directory

BuildRequires: node
Requires: node

%description
LESS extends CSS with dynamic behavior such as variables, mixins,
operations and functions. LESS runs on both the client-side (Chrome,
Safari, Firefox) and server-side, with Node.js and Rhino.

%prep
%setup
%__subst "s|../lib/less-node|../share/%name/less-node|g" bin/lessc

%build
# Nothing to be built, we're just carrying around flat files

# TODO
#check
#make_build test

%install
install -D bin/lessc %buildroot%_bindir/lessc
mkdir -p %buildroot%_datadir/%name/
cp -rp lib/* %buildroot%_datadir/%name/

%files
%doc LICENSE README.md
%_bindir/lessc
%_datadir/%name/

%changelog
* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1 (with rpmrb script)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- cleanup spec

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 1.3.1-alt1
- Initial release for Sisyphus (based on Fedora)
