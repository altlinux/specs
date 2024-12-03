%define networkversion 0.2.0

Name: x125
Version: 0.2.3
Release: alt2
License: GPL
Group: System/Configuration/Printing

Url: http://sourceforge.net/projects/x125-linux/

# Source: http://heanet.dl.sourceforge.net/sourceforge/x125-linux/x125-drv-%version.tar.gz
# Source1: http://heanet.dl.sourceforge.net/sourceforge/x125-linux/x125-drv-network-%networkversion.tar.gz
Source: %name-drv-%version.tar
Source1: %name-drv-network-%networkversion.tar
Patch1: x125-ftbfs-gcc14.patch
Patch2: x125-network-ftbfs-gcc14.patch

Summary: A printer driver for the Lexmark X125 All-in-one printer/scanner/fax
%description
%summary

%prep
%setup -c -T -a0 -a1
pushd x125-drv-%version/src
%patch1 -p3
popd

pushd x125-drv-network-%networkversion/src
%patch2 -p3
popd

%build
pushd x125-drv-%version/src
%make CFLAGS="%optflags"
popd

pushd x125-drv-network-%networkversion/src
%make CFLAGS="%optflags"
popd

%install
install -d %buildroot%_bindir

install -m0755 x125-drv-%version/src/x125_cmyk %buildroot%_bindir/
install -m0755 x125-drv-%version/src/x125_cmyk_print.sh %buildroot%_bindir/
install -m0755 x125-drv-network-%networkversion/src/x125_network %buildroot%_bindir/

cp x125-drv-%version/README README.drv_x125
cp x125-drv-%version/FAQ FAQ.drv_x125
cp x125-drv-%version/ChangeLog ChangeLog.drv_x125
cp x125-drv-network-%networkversion/README README.drv_x125_network
cp x125-drv-network-%networkversion/FAQ FAQ.drv_x125_network
cp x125-drv-network-%networkversion/ChangeLog ChangeLog.drv_x125_network

%files
%doc README.* FAQ.* ChangeLog.*
%doc x125-drv-%version/LICENSE
%_bindir/*

%changelog
* Tue Dec 03 2024 Oleg Solovyov <mcpain@altlinux.org> 0.2.3-alt2
- fix ftbfs with gcc14

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.2.3-alt1
- Initial build for ALT

