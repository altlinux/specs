Name:     suite3270
Version:  3.5ga11
Release:  alt2

Summary:  Terminal emulation 3270
License:  BSD
Group:    Terminals
Url:      https://sourceforge.net/projects/x3270/files/x3270/3.5ga11/suite3270-3.5ga11-src.tgz/download

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildRequires: libX11-devel libXt-devel libXmu-devel libXaw-devel bdftopcf mkfontdir libncurses-devel libncursesw-devel tcl tcl-devel libssl-devel


%description
Terminal emulation suite for 3270 family terminals

%package docs
Summary: Terminal emulator 3270 docs
Group: Documentation
BuildArch: noarch

%description docs
Documentation for terminal emulator for 3270 family terminals.


%prep
%setup

%build
cd %name
%configure --enable-unix --with-fontdir=%_datadir/fonts/misc
%make_build

%install
cd %name
%makeinstall_std
%makeinstall_std install.man
mkdir -p %buildroot/%_docdir/%name-%version/
find . -name html -type d -exec cp -ar {} %buildroot/%_docdir/%name-%version/ \;


%files
%_bindir/*
%_man1dir/*
%_man5dir/*
%_sysconfdir/x3270
%_sysconfdir/x3270/ibm_hosts
%_datadir/fonts/misc*

%files docs
%_docdir/%name-%version/

%changelog
* Fri Oct 20 2017 Denis Medvedev <nbr@altlinux.org> 3.5ga11-alt2
- fix packaging of config dir and added noarch for documentaion.

* Fri Oct 20 2017 Denis Medvedev <nbr@altlinux.org> 3.5ga11-alt1
Initial sisyphus release
