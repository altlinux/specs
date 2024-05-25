%define oldname python-uinput

Name: python3-module-uinput
Version: 1.0.1
Release: alt1

Summary: Pythonic API to the Linux uinput kernel module

License: GPLv3
Group: Development/Python3
URL: https://pypi.org/project/python-uinput
VCS: https://github.com/pyinput/python-uinput

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: rdma-core-devel
BuildRequires: libudev-devel

# https://github.com/tuomasjjrasanen/python-uinput/issues/16
# setup.py parses /usr/include/linux/input.h
BuildRequires: glibc-kernheaders-generic

%description
Python-uinput is Python interface to the Linux uinput kernel module
which allows attaching userspace device drivers into kernel.

%prep
%setup

# Use unversioned .so
%__subst "s/libudev.so.0/libudev.so/" setup.py

# Hack off distutils dependency
sed -i 's/distutils.sysconfig as //' src/__init__.py

%build
%pyproject_build

%install
%pyproject_install

chmod a-x examples/*

%files
%doc COPYING examples
%python3_sitelibdir/python_uinput-%version.dist-info
%python3_sitelibdir/_libsuinput.*.so
%python3_sitelibdir/uinput/

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Build new version.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 0.11.2-alt2
- Dropped dependency on distutils.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 0.11.2-alt1
- Build new version.

* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt7
- Fixed build for python3.10.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt6
- Drop python2 support.

* Thu May 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt5
- build for ALT Sisyphus (with python2 support)

* Fri Apr 19 2019 Cronbuild Service <cronbuild@altlinux.org> 0.10.1-alt4_21
- rebuild to get rid of unmets

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt3_21
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt3_20
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt3_18
- update to new release by fcimport

* Sat May 05 2018 Cronbuild Service <cronbuild@altlinux.org> 0.10.1-alt3_17
- rebuild to get rid of unmets

* Thu Mar 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_17
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_16
- update to new release by fcimport

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_15
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_10
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt2_9
- update to new release by fcimport

* Sat Apr 09 2016 Cronbuild Service <cronbuild@altlinux.org> 0.10.1-alt2_8
- rebuild to get rid of unmets

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_8
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_6
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_4
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_2
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_4
- update to new release by fcimport

* Mon Apr 01 2013 Cronbuild Service <cronbuild@altlinux.org> 0.9-alt2_3
- rebuild to get rid of unmets

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_3
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_2
- initial fc import

