Name: pywinery
Version: 0.3.2
Release: alt2

Summary: PyWinery is a graphical, easy and simple wine-prefix manager
License: GPLv3
Group: Emulators
Url: https://github.com/ergoithz/pywinery.git
Packager: Konstantin Artyushkin <akv@altlinux.org>

BuildArch:noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pygobject3-devel


%description
PyWinery is a graphical, easy and simple wine-prefix manager which allows
you to launch apps, explore and manage configuration of separate prefixes,
graphically and faster than setting variables on linux shell.

%prep
%setup

sed -i 's|python|&3|' $(find ./ -name '%name' -type f)
sed -i 's|#!.*python.*|#!/usr/bin/env python3|' $(find ./ -name '*.py')

%build
pushd branches/0.3
%python3_build
popd

%install
pushd branches/0.3
%python3_install
popd

%files
%_bindir/%name
%python3_sitelibdir/%name-*.egg-info
%python3_sitelibdir/%name/*
%_desktopdir/%name.desktop
%_datadir/%name/*


%changelog
* Tue Mar 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.2-alt2
- Porting to python3.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1.qa1
- NMU: applied repocop patch

* Tue Sep 13 2016 Konstantin Artyushkin <akv@altlinux.org> 0.3.2-alt1
- new version

