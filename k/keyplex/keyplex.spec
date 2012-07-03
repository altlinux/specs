# Spec file for keyplex utility

Name: keyplex
 
Version: 0.2
Release: alt1
    
Summary: keyboard multiplexer for X11 terminals

License: %bsdstyle
Group: Terminals
URL: http://sourceforge.net/projects/keyplex/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0: %name-0.2-alt-default_terminal.patch

AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Feb 04 2009
BuildRequires: imake libSM-devel libX11-devel xorg-cf-files

%description
Keyplex is a keyboard multiplexer for X11 terminals. It will
spawn a number of terminals, and when it has focus it relays
all keystrokes and mouse-button2 (paste) to them.

%prep
%setup
%patch0

%build
%configure
%make_build

%install
%make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc COPYING
# Empty files:
#%%doc ChangeLog AUTHORS News
%_bindir/%name

%changelog
* Wed Feb 04 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.2-alt1
- Initial build for ALT Linux Sisyphus
