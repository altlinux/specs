Name: obshutdown
Version: 0.1
Release: alt3
Summary: Openbox shutdown manager
Summary(ru_RU.UTF-8): Управеление сеансом openbox
License: GPL
Group: Graphical desktop/Other
Url: https://github.com/panjandrum
Packager: Konstantin Artyushkin <akv@altlinux.org>
Source: %name-%version.tar.gz
BuildRequires: libgtk+2-devel libcairo-devel automake

%description
Openbox shutdown manager
%description -l ru_RU.UTF-8
Управеление сеансом openbox
%prep
%setup

%build
%add_optflags -fgnu89-inline
%autoreconf
%configure 
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING README
%_bindir/%name
%_datadir/%name/*

%changelog
* Wed May 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt3
- NMU: fixed build with new toolchain.

* Sun Nov 08 2015 Konstantin Artyushkin <akv@altlinux.org> 0.1-alt2
- initial build for ALT Linux Sisyphus

