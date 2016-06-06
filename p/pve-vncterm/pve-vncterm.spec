%define sname vncterm

Name: pve-%sname
Summary: VNC Terminal Emulator
Version: 1.2
Release: alt1
License: GPLv2
Group: Networking/WWW
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %sname.tar.xz
Source1: libvncserver-memcpy.patch
Patch0: %sname-alt.patch
Patch1: %sname-gnutls.patch


# Automatically added by buildreq on Mon Mar 21 2016
# optimized out: libp11-kit perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators xz
BuildRequires: libgnutls-devel libjpeg-devel perl-Pod-Usage zlib-devel

%description
With vncterm you can start commands and export its standard input and
output to any VNC client (simulating a xterm Terminal).

%prep
%setup -q -n %sname
%patch0 -p1
%patch1 -p1

cp %SOURCE1 vncpatches/

%build
make %sname
make %sname.1

%install
install -pD -m0755 %sname %buildroot%_bindir/%sname
install -pD -m0644 %sname.1 %buildroot%_man1dir/%sname.1
install -pD -m0644 VncViewer.jar %buildroot%_datadir/%sname/VncViewer.jar

%files
%_bindir/%sname
%_datadir/%sname
%_man1dir/%sname.1*

%changelog
* Mon Mar 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- initial release

