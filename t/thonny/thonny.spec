Name: thonny
Version: 5.0.0
Release: alt1
License: MIT
Summary: Python IDE for beginners
Group: Development/Python3
BuildArch: noarch
Url: https://github.com/thonny/thonny

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-uv-build

Requires: python3-module-astroid python3-module-jedi python3-module-pylint python3-module-mypy
Requires: python3-module-asttokens

%description
Thonny is a Python IDE meant for learning programming.

%package -n python3-module-%name
Group: Development/Python3
Summary: Supplemental module for %name

%description -n python3-module-%name
Thonny is a Python IDE meant for learning programming.

%prep
%setup
# Remove vendoring libraries
rm -rf \
  thonny/plugins/circuitpython \
  thonny/plugins/esp \
  thonny/plugins/ev3 \
  thonny/plugins/microbit \
  thonny/plugins/micropython \
  thonny/plugins/prime_inventor \
  thonny/plugins/rp2040 \
  thonny/plugins/rpi_pico \
  thonny/vendored_libs 

%build
%pyproject_build

%install
%pyproject_install
install -D packaging/linux/org.thonny.Thonny.appdata.xml %buildroot%_datadir/appdata/org.thonny.Thonny.appdata.xml
install -D packaging/linux/org.thonny.Thonny.desktop %buildroot%_desktopdir/org.thonny.Thonny.desktop
install -D packaging/linux/thonny.1 %buildroot%_man1dir/thonny.1
for f in packaging/icons/%name-*x*.png; do
	size=`echo $f | cut -d- -f2 | cut -d. -f1`
	install -D -m 644 $f %buildroot%_datadir/icons/hicolor/$size/apps/%name.png
done

%files
%doc licenses
%doc *.rst
%_bindir/*
%_datadir/appdata/*
%_iconsdir/*/*/*/*
%_desktopdir/*
%_man1dir/*

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Fri Oct 16 2026 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version (ALT #44839).
- New URL https://github.com/thonny/thonny.
- Built using pyproject macros.
- Built without vendoring libraries and micropython plugins.
- Required python3-module-asttokens (ALT #44130).

* Thu Oct 21 2021 Ildar Mulyukov <ildar@altlinux.ru> 3.3.14-alt1
- new version

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 3.2.3-alt1
- Autobuild version bump to 3.2.3

* Mon Aug 06 2018 Fr. Br. George <george@altlinux.ru> 2.1.21-alt2
- Fix requires

* Fri Aug 03 2018 Fr. Br. George <george@altlinux.ru> 2.1.21-alt1
- Autobuild version bump to 2.1.21

