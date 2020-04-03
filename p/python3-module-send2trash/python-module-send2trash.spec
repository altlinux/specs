%define oname send2trash

Name: python3-module-%oname
Version: 1.5.0.0.2.1c32
Release: alt3

Summary: Python library to natively send files to Trash
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/hsoft/send2trash

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# git://git.altlinux.org/gears/p/python-module-send2trash.git
Source: %name-%version-%release.tar

%description
Send2Trash is a small package that sends files to the Trash
natively and on all platforms.

%prep
%setup -n %name-%version-%release

%build
%python3_build_debug

%install
%python3_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info


%changelog
* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5.0.0.2.1c32-alt3
- Build for python2 disabled.

* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.0.0.2.1c32-alt2
- NMU: build python3-module-send2trash

* Fri Jan 04 2019 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.0.2.1c32-alt1
- 1.5.0-2-g1c32d47.
