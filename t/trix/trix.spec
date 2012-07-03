Name: trix
Version: 0.94
Release: alt1
Group: Networking/Instant messaging
Summary: Vypress compatible intranet chat
License: GPL

Packager: Alexander Borovsky <partizan@altlinux.ru>

Source: %{name}-%version.tar.bz2

Requires: %{get_dep libqt3} 

# Automatically added by buildreq on Sun Dec 14 2008
BuildRequires: gcc-c++ imake libXt-devel libjpeg-devel libpng-devel libqt3-devel xorg-cf-files

%description 
TriX is a serverless text chat, dedicated to using in small home or 
office LAN's, that runs on Linux using Qt/X11 library. It is compatible 
with Vypress Chat(TM) for Windows. 

%prep
%setup -q -n %name-%version

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"

%__aclocal
%__automake --add-missing --gnu
%__autoconf

%configure \
	--disable-rpath \
	--with-pic \
	--disable-debug \
  --with-Qt-dir=%_libdir/qt3
%make_build

%install
%makeinstall

%files
%defattr(0644,root,root,0755)
%doc README COPYING INSTALL 
%attr(0755,root,root) %_bindir/%name
%_datadir/%name

%changelog
* Sun Dec 14 2008 Alexander Borovsky <partizan@altlinux.ru> 0.94-alt1
- 0.94

* Sat Feb  2 2008 Alexander Borovsky <partizan@altlinux.ru> 0.93-alt1
- Upgraded to 0.93

* Sun Dec  2 2007 Alexander Borovsky <partizan@altlinux.ru> 0.92-alt1
- Upgraded to 0.92

* Sun Dec 03 2006 Alexander Borovsky <partizan@altlinux.ru> 0.90-alt1
- New version

* Wed Oct 18 2006 Alexander Borovsky <partizan@altlinux.ru> 0.88-alt0.test2
- New version

* Mon Oct 16 2006 Alexander Borovsky <partizan@altlinux.ru> 0.85-alt1
- First build for Sisyphus

