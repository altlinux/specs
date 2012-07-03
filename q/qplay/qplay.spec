Name: qplay  
Version: 0.7.3
Release: alt0.1

Summary: console MP3/Ogg player
License: GPL
Group: Sound 
Url: http://www.qplay.org/ 

Source: %{name}-%{version}.tar.bz2

# Automatically added by buildreq on Thu Jul 21 2005
BuildRequires: libncurses-devel libtinfo-devel samba-common

%description
qplay is a console music player that features a user-friendly inferface for managing a play- and queue-list and a module-like system for adding new file formats. It uses familiar vim key bindings. The playlist can be played in sequence or in shuffle mode while an extra queuelist has highest priority so that you can determine which song will be played next before returning back to sequence or shuffle mode. It also features efficient sort and randomization, custom key bindings, external control support, and support for MP3, Ogg, M3U, and FTP streams.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS
%_bindir/*
%_man1dir/*

%changelog
* Thu Jul 21 2005 Nick S. Grechukh <gns@altlinux.ru> 0.7.3-alt0.1
initial release for Sisyphus


