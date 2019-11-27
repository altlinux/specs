Name: tgsend
Version: 1.3.1
Release: alt1
License: GPLv3
Group: Networking/WWW
Summary: Simple Telegram bot sender
Packager: Anton Shevtsov <x09@altlinux.org>
Requires: libssl-devel 

Buildrequires(pre): rpm-build-fpc 
BuildRequires: fpc upx lazarus

ExclusiveArch: %ix86 x86_64

Source: tgsend-1.3.1.tar

%description
Simple Telegram bot message/file console sender

%prep
%setup -q

%build
%_bindir/lazbuild --verbose synapse/laz_synapse.lpk
%_bindir/fpc  -MObjFPC -Scgi -CX -Cg -Os3 -XX -l -vewnhibq -Fu./synapse/lib/%fpc_arch -Fu%_libdir/lazarus/packager/units/%fpc_arch -Fu./ -o./%name -Fr%_libdir/fpc/msg/errore.msg %name.lpr

%_bindir/upx %_builddir/%name-%version/tgsend

%install
mkdir -p  %buildroot%_sysconfdir
mkdir -p  %buildroot%_bindir
install -m 755 tgsend %buildroot%_bindir
install -m 644 tgsend.conf %buildroot%_sysconfdir/tgsend.conf.example

%files
%_bindir/tgsend
%_sysconfdir/tgsend.conf.example

%changelog
* Thu Nov 26 2019 Anton Shevtsov <x09@altlinux.org> 1.3.1-alt1
- Initial build
