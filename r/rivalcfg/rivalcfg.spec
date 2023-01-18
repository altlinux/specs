Name:       rivalcfg
Version:    4.8.0
Release:    alt1

Summary:    Configure SteelSeries Rival gaming mice
License:    WTFPL
Group:      System/Configuration/Hardware
Url:        https://github.com/flozz/rivalcfg

Packager:   L.A. Kostis <lakostis@altlinux.org>
BuildArch:  noarch

Source0:    %name-%version.tar
Patch:      %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools


%description
rivalcfg is a small CLI utility program that allows you to configure
SteelSeries Rival gaming mice on Linux.

%prep
%setup
%patch -p1

sed -i 's|#!/usr/bin/env python|&3|' setup.py

%build
CFLAGS="%optflags" %__python3 setup.py build

%install
%__python3 setup.py install --root %buildroot --record=INSTALLED_FILES

mkdir -p %buildroot%_udevrulesdir
touch %buildroot%_udevrulesdir/99-steelseries-rival.rules

cat << EOF > %buildroot%_bindir/%name
#!/usr/bin/env python3

from rivalcfg import __main__

__main__.main()
EOF

%files -f INSTALLED_FILES
%doc README* LICENSE* CHANGELOG.* doc/{env,faq}.rst
%dir %python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name
%exclude %python3_sitelibdir_noarch/%name-%{version}*
%ghost %_udevrulesdir/*.rules


%changelog
* Wed Jan 18 2023 L.A. Kostis <lakostis@altlinux.ru> 4.8.0-alt1
- 4.8.0.

* Fri Sep 23 2022 L.A. Kostis <lakostis@altlinux.ru> 4.7.0-alt1
- 4.7.0.

* Sun Jul 18 2021 L.A. Kostis <lakostis@altlinux.ru> 4.3.0-alt1
- 4.3.0.
- Remove documentation (will add later).

* Thu Nov 05 2020 L.A. Kostis <lakostis@altlinux.ru> 4.1.0-alt1
- 4.1.0.
- Record udev rules as ghost file.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 3.7.0-alt1
- 3.7.0.
- Fix License tag.

* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.6.0-alt2
- Porting on python3.

* Fri Sep 13 2019 L.A. Kostis <lakostis@altlinux.ru> 3.6.0-alt1
- 3.6.0.

* Sat Jan 12 2019 L.A. Kostis <lakostis@altlinux.ru> 3.4.0-alt1
- Updated to 3.4.0:
  + runscript: update.
  + rival95: re-applied.

* Thu Oct 26 2017 L.A. Kostis <lakostis@altlinux.ru> 2.6.0-alt3.gitd0c3ec2
- .spec cleanup (based on repocop suggestions).

* Tue Oct 24 2017 L.A. Kostis <lakostis@altlinux.ru> 2.6.0-alt2.gitd0c3ec2
- rival95: experimental support of Rival 95.

* Tue Oct 24 2017 L.A. Kostis <lakostis@altlinux.ru> 2.6.0-alt1.gitd0c3ec2
- d0c3ec2 GIT.
- initial build for ALTLinux.
