%define oname send2trash
%def_with check

Name: python3-module-%oname
Version: 1.8.0
Release: alt1

Summary: Python library to natively send files to Trash
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/hsoft/send2trash
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-flake8
%endif

%filter_from_requires /python3(Foundation)/d
%filter_from_requires /python3(pythoncom)/d
%filter_from_requires /python3(pywintypes)/d
%filter_from_requires /python3(win32.*)/d


# git://git.altlinux.org/gears/p/python-module-send2trash.git
Source: %name-%version.tar

%description
Send2Trash is a small package that sends files to the Trash
natively and on all platforms.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%doc LICENSE README.rst
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/Send2Trash-*.dist-info

%changelog
* Tue Dec 06 2022 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- new version 1.8.0
- enabled tests

* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5.0.0.2.1c32-alt3
- Build for python2 disabled.

* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.0.0.2.1c32-alt2
- NMU: build python3-module-send2trash

* Fri Jan 04 2019 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.0.2.1c32-alt1
- 1.5.0-2-g1c32d47.
