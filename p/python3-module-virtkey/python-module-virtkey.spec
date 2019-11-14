%define _name virtkey
%define ver_major 0.63

Name: python3-module-%_name
Version: %ver_major.0
Release: alt2

Summary: Python extension for emulating keypresses and getting the keyboard geometry from the xserver
License: LGPLv3+
Group: Development/Python3
Url: https://launchpad.net/python-virtkey

Source: http://launchpad.net/python-virtkey/%ver_major/%version/+download/%_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: libXtst-devel libgtk+2-devel libxkbfile-devel python3-devel


%description
virtkey is a python extension for emulating keypresses and
getting the keyboard geometry from the xserver.

%prep
%setup -n %_name-%version
%setup -D -c -n %_name-%version

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS docs/* NEWS README
%python3_sitelibdir/%_name.*.so
%python3_sitelibdir/%{_name}*.egg-info


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.63.0-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.63.0-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.63.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

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
