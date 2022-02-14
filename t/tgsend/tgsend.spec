Name: tgsend
Version: 1.3.4
Release: alt3
License: GPL-2.0-or-later and BSD-3-Clause
Group: Networking/WWW
Summary: Simple Telegram bot sender
Requires: libssl-devel
Requires: libssl1.1

Buildrequires(pre): rpm-build-fpc
BuildRequires: fpc upx lazarus libssl1.1

ExclusiveArch: %ix86 x86_64

Source: tgsend-%version.tgz

%description
Simple Telegram bot message/file console sender

%prep
%setup -q
sed -i 's/openssl,/ssl_openssl,/' tgsend.lpr
sed -i 's/x09@altlinux.org/shevtsov.anton@gmail.com/' tgsend.lpr


%build
%_bindir/lazbuild --verbose synapse/laz_synapse.lpk
%_bindir/fpc  -MObjFPC -Scgi -CX -Cg -Os3 -XX -l -vewnhibq -Fu./synapse/lib/%fpc_arch -Fu%_libdir/lazarus/packager/units/%fpc_arch -Fu./ -o./%name -Fr%_libdir/fpc/msg/errore.msg %name.lpr

%_bindir/upx %_builddir/%name-%version/tgsend

%install
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_defaultdocdir/%name-%version

install -m 755 tgsend %buildroot%_bindir
install -m 644 tgsend.conf %buildroot%_sysconfdir/tgsend.conf.example

%files
%doc CREDITS
%_bindir/tgsend
%_sysconfdir/tgsend.conf.example

%changelog
* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 1.3.4-alt3
- Compress executable.

* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 1.3.4-alt2
- Initial build in Sisyphus
- Fix bogus changelog date strings

* Sat Feb 12 2022 Anton Shevtsov <shevtsov.anton@gmail.com> 1.3.4-alt1
- upgrade Synapse library

* Tue Dec 17 2019  Anton Shevtsov <x09@altlinux.org> 1.3.3-alt1
- Fix Synapse library for ALT p9 build
- Change license to GPL-2.0-or-later and BSD-3-Clause

* Thu Dec 5 2019 Anton Shevtsov <x09@altlinux.org> 1.3.2-alt1
- Help page fixed

* Tue Nov 26 2019 Anton Shevtsov <x09@altlinux.org> 1.3.1-alt1
- Initial build
