%define sname oslo.config

%def_with python3

Name:       python-module-%sname
Version:    3.17.1
Release:    alt1
Summary:    OpenStack common configuration library

Group:      Development/Python
License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    %name-%version.tar

Patch0001: 0001-add-usr-share-project-dist.conf-to-the-default-confi.patch

BuildArch:  noarch
Provides: python-module-oslo-config = %EVR
Obsoletes: python-module-oslo-config < %EVR
%py_provides oslo

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-netaddr >= 0.7.13
BuildRequires: python-module-stevedore >= 1.16.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-rfc3986 >= 0.2.2
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-mock >= 2.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.3
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-argparse
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-netaddr >= 0.7.13
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-stevedore >= 1.5.0
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%if_with python3
%package -n python3-module-%sname
Summary:    OpenStack common configuration library
Group: Development/Python3
Provides: python3-module-oslo-config = %EVR
%py3_provides oslo

%description -n python3-module-%sname
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.
%endif

%package doc
Summary:    Documentation for OpenStack common configuration library
Group: Development/Documentation
Provides: python-module-oslo-config-doc = %EVR
Obsoletes: python-module-oslo-config-doc < %EVR

%description doc
Documentation for the oslo-config library.

%prep
%setup

%patch0001 -p1

# Remove bundled egg-info
#rm -rf %{sname}.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
# generate html docs
python setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/oslo-config-generator \
   %buildroot%_bindir/python3-oslo-config-generator
popd
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


#%check

%files
%doc README.rst
%_bindir/oslo-config-generator
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%_bindir/python3-oslo-config-generator
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE doc/build/html

%changelog
* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 3.17.1-alt1
- 3.17.1

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.17.0-alt1
- 3.17.0

* Fri Apr 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.9.0-alt1
- 3.9.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Mon Feb 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0
- rename from python-module-oslo-config to python-module-oslo.config
- add python3 package

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2.1-alt1
- First build for ALT
