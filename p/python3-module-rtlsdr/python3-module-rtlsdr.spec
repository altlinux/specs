%define modulename rtlsdr

Name: python3-module-%modulename
Version: 0.2.92
Release: alt1

Summary: A Python 3 wrapper for librtlsdr (a driver for Realtek RTL2832U based SDR's)
License: GPLv3
Group: Development/Python3
URL: https://github.com/roger-/pyrtlsdr

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup
%autopatch -p1

rm -rf pyrtlsdr.egg-info
chmod 644 rtlsdr/rtlsdrtcp/base.py

find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%_bindir/python3|'

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
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
