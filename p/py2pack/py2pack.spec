%define oldname python-py2pack

#doesn't support python3 at this time
%global with_python3 0

%define mod_name py2pack

Name: py2pack
Version: 0.4.4
Release: alt2

Summary: Generate distribution packages from Python packages on PyPI

Url: http://github.com/saschpe/py2pack
License: GPLv2
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/p/%mod_name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools python-module-jinja2

Requires: python-module-py2pack = %version-%release

%if 0%{?with_python3}
BuildRequires: python3-dev-devel
BuildRequires: python3-module-jinja2 python-module-jinja2-tests
%endif # with_python3
Source44: import.info

%description
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%package -n python-module-py2pack
Summary: General purpose template engine
Group: Development/Python

%description -n python-module-py2pack
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%if 0%{?with_python3}
%package -n python3-module-py2pack
Summary: General purpose template engine
Group: Development/Python
#Requires: python3-module-argparse
#Requires: python3-module-jinja2 python3-module-jinja2-tests

%description -n python3-module-py2pack
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.
%endif #with_python3

%prep
%setup -n %mod_name-%version
%__subst "s|man/man1|share/man/man1|g" setup.py

%if 0%{?with_python3}
rm -rf %_builddir/python3-%oldname-%version-%release
cp -a . %_builddir/python3-%oldname-%version-%release
find %_builddir/python3-%oldname-%version-%release -name '*.py' | xargs sed -i '1s|^#!python|#!%__python3|'
%endif # with_python3

find -name '*.py' | xargs sed -i '1s|^#!python|#!%__python|'

%build
%python_build

%if 0%{?with_python3}
pushd %_builddir/python3-%oldname-%version-%release
%python_build
popd
%endif # with_python3

%install
%python_install

%if 0%{?with_python3}
pushd %_builddir/python3-%oldname-%version-%release
%python3_install
popd
%endif # with_python3

%files
%_bindir/%mod_name
%_man1dir/%mod_name.*

%files -n python-module-py2pack
%_docdir/%name
%python_sitelibdir_noarch/%{mod_name}*

%if 0%{?with_python3}
%files -n python3-module-py2pack
%_docdir/%oldname
%_man1dir/%mod_name.*
%_bindir/%mod_name
%python3_sitelibdir_noarch/%{mod_name}*
%endif # with_python3

%changelog
* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt2
- initial build for ALT Linux Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_4
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_3
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_2
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.17-alt1_4
- update to new release by fcimport

* Sun Dec 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.17-alt1_3
- initial fc import

