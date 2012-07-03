Summary:	Program for adjusting soundcard mixers (OSS only). 
Name:		umix
Version:	1.0.2
Release:	alt3
License:	GPL
Url:		http://umix.sf.net/
Group:		Sound
Source:		%name-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>
# Automatically added by buildreq on Tue Mar 15 2005
BuildRequires: glibc-devel-static libncurses-devel libtinfo-devel

%description
Umix is a program for adjusting soundcard volumes and other
features in soundcard mixers. You can control your volumes, balances and
recording sources flexibly from the command line or with a ncurses
user interface with familiar vi/emacs keybindings. Umix supports multiple 
mixer devices. All settings can be saved and loaded from a file.

Unfortunately, Umix can not operate with ALSA, only with OSS.
Modprobe snd-mixer-oss for OSS mixer support.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/umix
%_man1dir/umix.1*
%doc AUTHORS ChangeLog NEWS README TODO

%changelog
* Tue Aug 25 2009 Fr. Br. George <george@altlinux.ru> 1.0.2-alt3
- No ALSA support is here, add a warning

* Tue Sep 23 2008 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- Fix broken build

* Tue Mar 15 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.2-alt1
- First build for ALT Linux.

