Name:       rosa-crypto-tool
Version:    0.1.5
Release:    alt2

Summary:    Program for working with electronic digital signatures
Group:      Text tools
License:    BSD
URL:        https://abf.io/uxteam/rosa-crypto-tool-devel.git
BuildArch:  noarch

Source0:    %name-%version.tar
Patch:      %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Requires: python3-module-pyudev-pyqt5 >= 0.21.0


%description
Program for working with electronic digital signatures.

%prep
%setup -q
%patch -p1


## py2 -> py3
sed -i 's|, unicode=True||' src/rosa_crypto_tool.py

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name '*.py' -o -name '%name' \))
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build

%install
%python3_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%doc %_defaultdocdir/%name/help.pdf
%python3_sitelibdir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg


%changelog
* Mon Nov 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt2
- python2 -> python3

* Wed Nov 02 2016 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- New version

* Tue Oct 04 2016 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt0.1.beta
- New beta version
- Added executable and desktop files

* Sun Aug 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.0.8-alt1
- Initial build in Sisyphus

