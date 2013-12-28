Name: vifm
Version: 0.7.6
Release: alt1

Summary: Two pane file manager with vi-like keybindings.
License: GPL
Group: File tools 
Url: http://vifm.sourceforge.net/ 

Source: %{name}-%{version}.tar.gz

# Automatically added by buildreq on Thu Jul 21 2005
BuildRequires: gcc-c++ libncursesw-devel libstdc++-devel libtinfo-devel samba-common

%description
Vifm is a ncurses based file manager with vi like keybindings,
which also borrows some useful ideas from mutt. If you use vi, vifm
gives you complete keyboard control over your files without having
to learn a new set of commands.

%prep
%setup -q -n %name

%build
#autoreconf -fisv
%configure
%make_build

%install
%makeinstall

%files

%_bindir/*
%_datadir/vifm
%_man1dir/*
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Sat Dec 28 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.6-alt1
- Update to lastest version with lots of improvements

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3-alt0.1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jul 21 2005 Nick S. Grechukh <gns@altlinux.ru> 0.3-alt0.1
initial release for Sisyphus


