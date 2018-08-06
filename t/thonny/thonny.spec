Name: thonny
Version: 2.1.21
Release: alt2
License: MIT
Summary: Python IDE for beginners
Source: %name-%version.tar.gz
Group: Development/Python3
BuildArch:	noarch
URL:	https://thonny.org/
Requires: python3-module-%name = %version-%release

# Automatically added by buildreq on Fri Aug 03 2018
# optimized out: python-base python-modules python3 python3-base python3-dev python3-module-pkg_resources sh3
BuildRequires: python3-module-setuptools

%description
Thonny is a Python IDE meant for learning programming.

%package -n python3-module-%name
Group: Development/Python3
Summary: Supplemental module for %name

%description -n python3-module-%name
Thonny is a Python IDE meant for learning programming.

%prep
%setup

%build
%python3_build

%install
%python3_install
install -D packaging/linux/org.thonny.Thonny.appdata.xml %buildroot%_datadir/appdata/org.thonny.Thonny.appdata.xml
install -D packaging/linux/org.thonny.Thonny.desktop %buildroot%_desktopdir/org.thonny.Thonny.desktop
install -D packaging/linux/thonny.1 %buildroot%_man1dir/thonny.1

%files
%doc licenses
%doc *rst
%_bindir/*
%_datadir/appdata/*
%_desktopdir/*
%_man1dir/*

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Mon Aug 06 2018 Fr. Br. George <george@altlinux.ru> 2.1.21-alt2
- Fix requires

* Fri Aug 03 2018 Fr. Br. George <george@altlinux.ru> 2.1.21-alt1
- Autobuild version bump to 2.1.21

