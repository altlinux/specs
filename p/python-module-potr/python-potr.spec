Name: python-module-potr
Version: 1.0.1
Release: alt1.1.1
Summary: Python Off-The-Record encryption
Group: Development/Python
License: LGPLv3+
Url: http://python-otr.pentabarf.de
BuildArch: noarch
Source: python-potr-%version.zip

BuildRequires(pre): rpm-build-python3 unzip

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 unzip

#BuildRequires: python-module-distribute  python-devel
#BuildRequires: python3-module-distribute python3-devel

%description
This is a pure Python OTR implementation; it does not bind to libotr.

%package -n python3-module-potr
Group: Development/Python
Summary: %summary
%description -n python3-module-potr
This is a pure Python OTR implementation; it does not bind to libotr.

%prep
%setup -n python-potr-%version

%build
cp -a . ../python3
%python_build
cd ../python3 && %python3_build

%install
%python_install
cd ../python3 && %python3_install

%files
%doc src/tools/convertkey.py CHANGELOG PKG-INFO
%python_sitelibdir_noarch/*

%files -n python3-module-potr
%doc src/tools/convertkey.py CHANGELOG PKG-INFO
%python3_sitelibdir_noarch/*

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.1
- NMU: Use buildreq for BR.

* Mon Feb 02 2015 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Autobuild version bump to 1.0.0

* Thu Mar 27 2014 Fr. Br. George <george@altlinux.ru> 0.9.9-alt1
- Initial build from scratch

