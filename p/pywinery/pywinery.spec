Name: pywinery
Version: 0.3.3
Release: alt1

Summary: PyWinery is a graphical, easy and simple wine-prefix manager

License: GPLv3
Group: Emulators
Url: https://github.com/ergoithz/pywinery

Packager: Konstantin Artyushkin <akv@altlinux.org>

# Source-url: https://github.com/ergoithz/pywinery/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch:noarch

BuildRequires(pre): rpm-build-python3
# FIXME: AttributeError: 'gi.repository.Gtk' object has no attribute 'Container'
# typelib(gtk) provided both libgtk+3-gir and libgtk+4-gir
BuildRequires: libgtk+3-gir
BuildRequires: python3-module-pygobject3

# TODO: gi.require_version("Gtk", "3.0")
Conflicts: libgtk+4-gir

%description
PyWinery is a graphical, easy and simple wine-prefix manager which allows
you to launch apps, explore and manage configuration of separate prefixes,
graphically and faster than setting variables on linux shell.

%prep
%setup
mv branches/0.3/* .
sed -i 's|python|&3|' $(find ./ -name '%name' -type f)
sed -i 's|#!.*python.*|#!/usr/bin/env python3|' $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%_bindir/%name
%python3_sitelibdir/%name-*.egg-info
%python3_sitelibdir/%name/*
%_desktopdir/%name.desktop
%_datadir/%name/*


%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt1
- NMU: new version (0.3.3) with rpmgs script
- NMU: switch to tarball from github, cleanup spec

* Tue Mar 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.2-alt2
- Porting to python3.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1.qa1
- NMU: applied repocop patch

* Tue Sep 13 2016 Konstantin Artyushkin <akv@altlinux.org> 0.3.2-alt1
- new version

