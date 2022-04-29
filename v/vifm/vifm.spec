Name: vifm
Version: 0.12
Release: alt1

Summary: Two pane file manager with vi-like keybindings
License: GPLv2
Group: File tools
Url: http://vifm.sourceforge.net/

Source: %name-%version.tar.bz2

BuildRequires: gcc-c++ libncursesw-devel groff  libcfile-devel

%description
Vifm is a ncurses based file manager with vi like keybindings,
which also borrows some useful ideas from mutt. If you use vi, vifm
gives you complete keyboard control over your files without having
to learn a new set of commands.

%prep
%setup
sed -i 's/#!\/usr\/bin\/env perl/#!\/usr\/bin\/perl/' src/vifm-convert-dircolors

%build
#autoreconf
#configure \
#    --enable-werror
%configure \
	--with-curses \
	--with-libmagic \
	--without-gtk \
	--disable-developer

%make_build

%install
%makeinstall_std

%files
%doc AUTHORS BUGS COPYING ChangeLog FAQ NEWS README TODO
%exclude /usr/share/doc/%name
%_bindir/*
%_datadir/%name
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_sysconfdir/%name/colors/Default-256.%name
%_man1dir/*
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Fri Apr 29 2022 Ilya Mashkin <oddity@altlinux.ru> 0.12-alt1
- 0.12

* Fri Sep 25 2020 Grigory Ustinov <grenka@altlinux.org> 0.11-alt1
- Build new version.

* Sat Dec 21 2019 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt2
- Fix python shebang.

* Tue Jul 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt1
- Build new version.

* Tue Nov 20 2018 Grigory Ustinov <grenka@altlinux.org> 0.10-alt1
- Build new version.

* Thu Mar 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt1
- Build new version.

* Fri Dec 15 2017 Grigory Ustinov <grenka@altlinux.org> 0.9-alt1
- Build new version.
  fix missing groff dependency.
  (Closes: 27873)

* Sat Dec 28 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.7.6-alt1
- Update to lastest version with lots of improvements

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3-alt0.1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jul 21 2005 Nick S. Grechukh <gns@altlinux.ru> 0.3-alt0.1
initial release for Sisyphus
