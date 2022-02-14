%define oname nose2

Name: python3-module-%oname
Version: 0.11.0
Release: alt1

Summary: A unittest-based testing framework for python that makes writing and running tests easier

Group: Development/Python3
License: LGPL
Url: https://github.com/nose-devs/nose2

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage

%description
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as much
as is reasonably possible without resorting to too much magic.

%prep
%setup
sed -i "s|man/man1|share/man/man1|g" setup.py

%build
%python3_build

%install
%python3_install

rm -f %buildroot%_bindir/nosetests

%files
%doc AUTHORS README.rst
%_bindir/nose2
%_bindir/nose2-3*
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Feb 14 2022 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- New version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt2
- Drop python2 support.

* Thu Jan 28 2021 Andrey Cherepanov <cas@altlinux.org> 0.10.0-alt1
- New version.

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- New version.

* Thu Apr 04 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- New version.

* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.4-alt1
- New version.
- Build from upstream tag.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 22 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.5-alt1
- Initial build in Sisyphus
