Name: vifm
Version: 0.3
Release: alt0.1

Summary: file manager with vi-like keybindings. 
License: GPL
Group: File tools 
Url: http://vifm.sourceforge.net/ 

Source: %{name}-%{version}.tar.gz

# Automatically added by buildreq on Thu Jul 21 2005
BuildRequires: gcc-c++ libncurses-devel libstdc++-devel libtinfo-devel samba-common

%description
Vifm is a ncurses based file manager with vi like keybindings. If you use vi, vifm gives you complete keyboard control over your files without having to learn a new set of commands.

%prep
%setup -q -n %name

%build
autoreconf -fisv
%configure
%make_build

%install
%makeinstall

%files

%_bindir/*
%_datadir/vifm

%changelog
* Thu Jul 21 2005 Nick S. Grechukh <gns@altlinux.ru> 0.3-alt0.1
initial release for Sisyphus


