Name: python-module-send2trash
Version: 1.5.0.0.2.1c32
Release: alt1

Summary: Python library to natively send files to Trash
Group: Development/Python
License: BSD-3-Clause
Url: https://github.com/hsoft/send2trash
BuildArch: noarch

%setup_python_module send2trash

# git://git.altlinux.org/gears/p/python-module-send2trash.git
Source: %name-%version-%release.tar

%description
Send2Trash is a small package that sends files to the Trash
natively and on all platforms.

%prep
%setup -n %name-%version-%release

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%doc CHANGES.rst LICENSE README.rst

%changelog
* Fri Jan 04 2019 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.0.2.1c32-alt1
- 1.5.0-2-g1c32d47.
