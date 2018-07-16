Name: oki4linux
Version: 2.1
Release: alt1.gst
License: GPL
Group: System/Configuration/Printing

Url: http://www.linuxprinting.org/download/printing/

# Source: http://www.linuxprinting.org/download/printing/%name-%version.tar.gz
Source: %name-%version.tar
Source1: oki4daemon.init
Source2: README.OKI-Winprinters
Source3: oki4daemon.service
Patch: oki4linux-2.0-daemon-mdk.patch
Patch1: oki4linux-2.1gst-LDFLAGS.patch

Summary: Drivers for Oki 4w, oki 400w and okipage 4w plus GDI winprinters
%description
A Linux / UNIX driver for the  okipage 4w, oki 400w and
okipage 4w plus GDI printers,

%prep
%setup
%patch0 -p1
%patch1 -p0

# some small corrections in the daemon script:
# - The daemon crashes with "setlogsock('unix');"
# - Correct the path for the driver
pushd src
  mv oki4daemon oki4daemon.pre
  sed "s/setlogsock('unix');/setlogsock('inet');/" oki4daemon.pre | sed "s:/usr/local/sbin/oki4drv:%_bindir/oki4drv:" > oki4daemon
popd

cp %SOURCE1 oki4daemon.init
cp %SOURCE2 README.OKI-Winprinters
cp %SOURCE3 oki4daemon.service

%build
pushd src
  make clean
%make CFLAGS="%optflags"
popd

%install
install -d %buildroot%_initdir/
install -d %buildroot%_bindir/
install -d %buildroot%_sbindir/
install -d %buildroot%_man1dir/

pushd src
  # Program files
  install -m0755 oki4drv %buildroot%_bindir
  install -m0755 oki4daemon %buildroot%_sbindir
  install -m0644 oki4drv.man %buildroot%_man1dir/oki4drv.1
popd

install -m0755 oki4daemon.init %buildroot%_initdir/

%post
%post_service oki4daemon

%postun
%preun_service oki4daemon

%files
%doc README.OKI-Winprinters COPYING ChangeLog README
%doc doc samples src/README.oki4daemon src/align.ps
%_initdir/oki4daemon.init
%_sbindir/oki4daemon
%_bindir/oki4drv
%_man1dir/oki4drv.1*

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 2.1-alt1.gst
- Initial build for ALT

