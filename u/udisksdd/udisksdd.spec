%define _unpackaged_files_terminate_build 1

Name:    udisksdd
Version: 0.2
Release: alt1

Summary: a dd(1) drop-in replacement that makes use of udisks(8)

License: GPL-2.0-or-later
Group:   System/Configuration/Hardware
URL:     https://github.com/bonktree/udisksdd

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(dbus)

Source: %name-%version.tar

%package -n python3-module-%name
Summary: Python 3 package for udisksdd
Group: Development/Python3
BuildArch: noarch

%description
This utility is intended to be called with CLI arguments suitable for dd(1).
Its only job is to request a file descriptor to a block device which is
unavailable to be opened for reading or writing directly and to pass it to
dd(1).

This utility only depends on Python 3, its standard library and dbus-python.

%description -n python3-module-%name
This package contains python3(udisksdd). The package can be used in a
standalone fashion, but the main way to use it is via udd(1).

%prep
%setup

%build
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
[ -e setup.py ] && rm -f ./setup.py
echo 'import setuptools; setuptools.setup()' > setup.py
%python3_build

%install
%python3_install

%files
%doc README.md
%_bindir/udd

%files -n python3-module-%name
%doc README.md
%python3_sitelibdir/udisksdd
%python3_sitelibdir/*.egg-info

%changelog
* Sat Jan 15 2022 Arseny Maslennikov <arseny@altlinux.org> 0.2-alt1
- 0.1 -> 0.2.

* Sat Apr 10 2021 Arseny Maslennikov <arseny@altlinux.org> 0.1-alt1
- Initial build for ALT Sisyphus.
