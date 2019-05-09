%define oldname python-uinput

%def_with python3

Name: python-module-uinput
Version: 0.10.1
Release: alt5

Summary: Pythonic API to the Linux uinput kernel module

License: GPLv3
Group: Development/Python
Url: http://pypi.python.org/pypi/python-uinput/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://pypi.python.org/packages/source/p/%oldname/%oldname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python rpm-build-python3 rpm-build-intro
BuildRequires: rdma-core-devel
BuildRequires: libudev-devel
BuildRequires: python-dev python3-devel

# https://github.com/tuomasjjrasanen/python-uinput/issues/16
# setup.py parses /usr/include/linux/input.h
BuildRequires: glibc-kernheaders-generic

%description
Python-uinput is Python interface to the Linux uinput kernel module
which allows attaching userspace device drivers into kernel.

%package -n python3-module-uinput
Group: Development/Python
Summary: Pythonic API to the Linux uinput kernel module

%description -n python3-module-uinput
Python-uinput is Python interface to the Linux uinput kernel module
which allows attaching userspace device drivers into kernel.

%prep
%setup

# Use unversioned .so
%__subst "s/libudev.so.0/libudev.so/" setup.py


# https://github.com/tuomasjjrasanen/python-uinput/issues/16
# use correct input file
[ -s /usr/include/linux/input-event-codes.h ] && \
    %__subst "s/input.h/input-event-codes.h/" setup.py

%python3_dirsetup
#find . -name '*.py' | xargs sed -i '1s|^#!python|#!%__python3|'

%build
%python_build
%python3_dirbuild

%install
%python_install
%python3_dirinstall

chmod a-x examples/*

%files
%doc COPYING NEWS README examples
%python_sitelibdir/python_uinput-%version-py?.?.egg-info
%python_sitelibdir/_libsuinput.so
%python_sitelibdir/uinput/

%if_with python3
%files -n python3-module-uinput
%doc COPYING NEWS README examples
%python3_sitelibdir/python_uinput-%version-py?.?.egg-info
%python3_sitelibdir/_libsuinput.*.so
%python3_sitelibdir/uinput/
%endif

%changelog
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

