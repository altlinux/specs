%define modulename rtlsdr

Name: python3-module-%modulename
Version: 0.2.93
Release: alt1

Summary: A Python 3 wrapper for librtlsdr (a driver for Realtek RTL2832U based SDR's)
License: GPLv3
Group: Development/Python3
URL: https://github.com/roger-/pyrtlsdr
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary

%prep
%setup
%autopatch -p1

#chmod 644 rtlsdr/rtlsdrtcp/base.py

find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%_bindir/python3|'

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/py%modulename-%version.dist-info

%changelog
* Mon Jun 12 2023 Anton Midyukov <antohami@altlinux.org> 0.2.93-alt1
- New version 0.2.93.

* Wed May 19 2021 Anton Midyukov <antohami@altlinux.org> 0.2.92-alt1
- new version 0.2.92
- python 3 version only

* Wed Mar 10 2021 Stanislav Levin <slev@altlinux.org> 0.2.91-alt2
- Made m2r optional.

* Fri Dec 28 2018 Anton Midyukov <antohami@altlinux.org> 0.2.91-alt1
- new version 0.2.91

* Mon Mar 26 2018 Anton Midyukov <antohami@altlinux.org> 0.2.7-alt2
- Fix buildrequires

* Sun Mar 18 2018 Anton Midyukov <antohami@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus
