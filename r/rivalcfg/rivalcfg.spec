%define git d0c3ec2

Name: rivalcfg
Version: 2.6.0
Release: alt3.git%git

Summary: Configure SteelSeries Rival gaming mice
License: DWTFYWTPL
Group: System/Configuration/Hardware
Url: https://github.com/flozz/rivalcfg
Source0: %name-d0c3ec2.tar
Patch: %name-%version-%release.patch

Packager: L.A. Kostis <lakostis@altlinux.org>

BuildArch: noarch

BuildRequires(pre): python-devel python-module-setuptools

%description
rivalcfg is a small CLI utility program that allows you to configure
SteelSeries Rival gaming mice on Linux.

%prep
%setup -q -n %name-d0c3ec2
%patch -p1

%build
CFLAGS="%optflags" python setup.py build

%install
python setup.py install --root %buildroot --record=INSTALLED_FILES
mkdir -p %buildroot%_udevrulesdir
install -m644 rivalcfg/data/99-steelseries-rival.rules %buildroot%_udevrulesdir/
cat << EOF > %buildroot%_bindir/%name
#!/usr/bin/env python

from rivalcfg import cli

cli.main()
EOF

%files -f INSTALLED_FILES
%doc README* LICENSE* doc/*.md
%exclude %python_sitelibdir_noarch/%name-%{version}*
%_udevrulesdir/*.rules

%changelog
* Thu Oct 26 2017 L.A. Kostis <lakostis@altlinux.ru> 2.6.0-alt3.gitd0c3ec2
- .spec cleanup (based on repocop suggestions).

* Tue Oct 24 2017 L.A. Kostis <lakostis@altlinux.ru> 2.6.0-alt2.gitd0c3ec2
- rival95: experimental support of Rival 95.

* Tue Oct 24 2017 L.A. Kostis <lakostis@altlinux.ru> 2.6.0-alt1.gitd0c3ec2
- d0c3ec2 GIT.
- initial build for ALTLinux.


