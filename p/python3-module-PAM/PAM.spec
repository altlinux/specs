%define oname pam

Name:       python3-module-PAM
Version:    2.0.2
Release:    alt1.1

Summary:    PAM bindings for Python

License:    MIT
Group:      Development/Python3
Url:        https://github.com/FirefighterBlu3/python-pam

Source0:    %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname

%description
PAM (Pluggable Authentication Module) bindings for Python.

%prep
%setup
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
[ -e setup.py ] && rm -f ./setup.py
echo 'import setuptools; setuptools.setup()' > setup.py

%build
%python3_build

%install
%python3_install

%check
# needs display

%files
%doc LICENSE README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/python_%oname-%version-py%_python3_version.egg-info

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri May 20 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Automatically updated to 2.0.2.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt3
- drop unused BR: python3-module-pip

* Thu Jul 15 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.4-alt2
- Drop python2 support.

* Thu Jul 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.4-alt1
- Build new version.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.3-alt2
- NMU: Rebuild with python3.7.

* Fri May 04 2018 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- New version (switch to fork from David Ford)
- Add Python 3 package
- Make package noarch

* Fri Mar 01 2013 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt2
- Rename package to python-module-PAM

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt1
- Initial release for Sisyphus (based on Fedora)
