Name:		xrun
Version:	0.01
Release:	alt1
Summary:	Run an arbitrary program until X server dies
Source:		%name-%version.tar
Group:		System/X11
License:	GPLv3

# Automatically added by buildreq on Thu Aug 30 2012
# optimized out: perl-Encode perl-Locale-gettext xorg-xproto-devel
BuildRequires: help2man libX11-devel

%description
XRun is an X client that runs an arbitrary program,
and kill it when a connection to X server is lost.


%prep
%setup

%build
%make

%install
install -D -m755 %name %buildroot%_bindir/%name
install -D %name.man %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/*



%changelog
* Fri Aug 31 2012 Fr. Br. George <george@altlinux.ru> 0.01-alt1
- Initial build from scratch

