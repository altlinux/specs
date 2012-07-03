Name: dxpc
Summary: Differential X Protocol Compressor
Url: http://www.vigor.nu/dxpc/
Group: System/X11
License: BSD
Version: 3.9.2
Release: alt1

Source: %name-%version.tgz

# Automatically added by buildreq on Thu Nov 30 2006
BuildRequires: gcc-c++ libXt-devel liblzo2-devel xorg-cf-files

%description
dxpc is an X protocol compressor designed to improve the speed of
X11 applications run over low-bandwidth links (such as dialup PPP
connections).

%prep
%setup

%build
%configure --with-x
%make_build

%install
%makeinstall prefix=%buildroot/usr man1dir=%buildroot/%_man1dir

%files
%_bindir/*
%_man1dir/*
%doc README

%changelog
* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 3.9.2-alt1
- Autobuild version bump to 3.9.2

* Wed Jun 03 2009 Fr. Br. George <george@altlinux.ru> 3.9.1-alt1
- Version up

* Thu Nov 30 2006 Fr. Br. George <george@altlinux.ru> 3.9.0-alt1
- Initial build from OpenPKG

