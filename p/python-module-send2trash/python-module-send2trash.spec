Name: python-module-send2trash
Version: 1.5.0.0.2.1c32
Release: alt2

Summary: Python library to natively send files to Trash
Group: Development/Python
License: BSD-3-Clause
Url: https://github.com/hsoft/send2trash
BuildArch: noarch

%def_with python3
%setup_python_module send2trash

# git://git.altlinux.org/gears/p/python-module-send2trash.git
Source: %name-%version-%release.tar

%description
Send2Trash is a small package that sends files to the Trash
natively and on all platforms.

%if_with python3
%package -n python3-module-%modulename
Group: Development/Python3
Summary: Python library to natively send files to Trash
BuildRequires(pre): rpm-build-python3 rpm-build-intro

%description -n python3-module-%modulename
Send2Trash is a small package that sends files to the Trash
natively and on all platforms.

%endif

%prep
%setup -n %name-%version-%release

%python3_dirsetup

%build
%python_build
%python3_dirbuild

%install
%python_install
%python3_dirinstall

%files
%python_sitelibdir/*
%doc CHANGES.rst LICENSE README.rst

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif


%changelog
* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.0.0.2.1c32-alt2
- NMU: build python3-module-send2trash

* Fri Jan 04 2019 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.0.2.1c32-alt1
- 1.5.0-2-g1c32d47.
