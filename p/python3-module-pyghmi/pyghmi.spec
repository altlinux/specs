%define _unpackaged_files_terminate_build 1
%define oname pyghmi

%def_with check
%def_with docs

Name:           python3-module-pyghmi
Version:        1.5.63
Release:        alt1

Summary:        Python General Hardware Management Initiative (IPMI and others)

Group:          Development/Python3
License:        Apache-2.0
URL:            https://pypi.org/project/pyghmi

Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr
%if_with docs
BuildRequires:  python3-module-sphinx
BuildRequires:  python3-module-openstackdocstheme
BuildRequires:  python3-module-dateutil
%endif

%if_with check
BuildRequires: python3-module-stestr
BuildRequires: python3-module-oslotest
%endif

%description
This is a pure python implementation of the IPMI protocol.

%if_with docs
%package doc
Summary: Documentation for pyghmi
Group: Development/Documentation

%description doc
Documentation for pyghmi.
%endif

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup

# Remove bundled egg-info
rm -rf pyghmi.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
pushd %buildroot%_bindir
for i in $(ls); do
       sed -i 's|python|python3|g' $i
       sed -i 's|python33|python3|g' $i
       sed -i 's|tox|tox.py3|g' $i
done
popd

%check
%__python3 -m stestr run --slowest

%files
%doc README LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%_bindir/fakebmc
%_bindir/pyghmicons
%_bindir/pyghmiutil
%_bindir/virshbmc
%exclude %python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc html
%endif

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Mon Sep 25 2023 Anton Vyatkin <toni@altlinux.org> 1.5.63-alt1
- new version 1.5.63

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.19-alt1
- Build new version.

* Tue Sep 15 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.18-alt1
- Build new version.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.16-alt1
- Build new version.

* Fri Jul 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.15-alt1
- Build new version.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.3-alt1
- Build new version.
- Fix license.
- Fix url.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt2
- Build with docs.

* Tue Oct 29 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.
- Build with python3 instead of python2.

* Thu Jun 22 2017 Lenar Shakirov <snejok@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 0.5.9-alt1
- First build for ALT (based on Fedora 0.5.9-3.fc23.src
