%define _name virtkey
%define ver_major 0.63

Name: python-module-%_name
Version: %ver_major.0
Release: alt1.1

Summary: Python extension for emulating keypresses and getting the keyboard geometry from the xserver
License: LGPLv3+
Group: Development/Python
Url: https://launchpad.net/python-virtkey

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: http://launchpad.net/python-virtkey/%ver_major/%version/+download/%_name-%version.tar.gz

#BuildPreReq: python-devel python-module-setuptools rpm-build-python
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils fontconfig glib2-devel libX11-devel libXi-devel libcairo-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-server pkg-config python-base python-devel python-modules python-modules-compiler python-modules-email python3 python3-base xorg-inputproto-devel xorg-kbproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXtst-devel libgtk+2-devel libxkbfile-devel python3-devel rpm-build-python3

#BuildRequires: libX11-devel libXtst-devel libxkbfile-devel libgtk+2-devel
# for python3
#BuildRequires: rpm-build-python3 python3-devel

%description
virtkey is a python extension for emulating keypresses and
getting the keyboard geometry from the xserver.

%package -n python3-module-%_name
Summary: Python3 extension for emulating keypresses and getting the keyboard geometry from the xserver
License: LGPLv3+
Group: Development/Python3

%description -n python3-module-%_name
virtkey is a python3 extension for emulating keypresses and
getting the keyboard geometry from the xserver.

%prep
%setup -n %_name-%version
%setup -D -c -n %_name-%version
mv %_name-%version py3build

%build
PYTHON=%__python %python_build

pushd py3build
%python3_build
popd

%install
PYTHON=%__python %python_install

pushd py3build
%python3_install
popd

%files
%python_sitelibdir/%_name.so
%python_sitelibdir/%{_name}*.egg-info
%doc AUTHORS docs/* NEWS README

%files -n python3-module-%_name
%python3_sitelibdir/%_name.*.so
%python3_sitelibdir/%{_name}*.egg-info


%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.63.0-alt1.1
- NMU: Use buildreq for BR.

* Sat Oct 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.63.0-alt1
- 0.63.0
- new python3-module-virtkey subpackage

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.60.0-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.60.0-alt1.1
- Rebuild with Python-2.7

* Wed Oct 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.60.0-alt1
- Initial build in Sisyphus
