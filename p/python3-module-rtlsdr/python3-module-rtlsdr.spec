# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename rtlsdr

Name: python3-module-%modulename
Version: 0.4.0
Release: alt1

Summary: A Python 3 wrapper for librtlsdr (a driver for Realtek RTL2832U based SDR's)
License: GPL-3.0-only
Group: Development/Python3
URL: https://github.com/roger-/pyrtlsdr
VCS: https://github.com/roger-/pyrtlsdr
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup
%autopatch -p1

#chmod 644 rtlsdr/rtlsdrtcp/base.py

find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%_bindir/python3|'

%build
%pyproject_build

%install
%pyproject_install

# remove unpackaged files
rm -vr %buildroot%python3_sitelibdir/doc/source/

%files
%doc README.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/py%modulename-%version.dist-info

%changelog
* Mon Mar 09 2026 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Tue Aug 15 2023 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

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
