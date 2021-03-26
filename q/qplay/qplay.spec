Name: qplay
Version: 0.7.3
Release: alt0.2

Summary: console MP3/Ogg player
License: GPLv2
Group: Sound
Url: http://www.qplay.org/

Source: %{name}-%{version}.tar.bz2

# Automatically added by buildreq on Thu Jul 21 2005
BuildRequires: libncurses-devel libtinfo-devel samba-common

%description
qplay is a console music player that features a user-friendly inferface
for managing a play- and queue-list and a module-like system for adding new file
formats. It uses familiar vim key bindings. The playlist can be played
in sequence or in shuffle mode while an extra queuelist has highest priority so
that you can determine which song will be played next before returning back
to sequence or shuffle mode. It also features efficient sort and randomization,
custom key bindings, external control support, and support for MP3, Ogg, M3U,
and FTP streams.

%prep
%setup

%build
%add_optflags -fcommon
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS
%_bindir/*
%_man1dir/*

%changelog
* Fri Mar 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.3-alt0.2
- Fixed FTBFS with -fcommon.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.3-alt0.1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jul 21 2005 Nick S. Grechukh <gns@altlinux.ru> 0.7.3-alt0.1
initial release for Sisyphus


