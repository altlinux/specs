Name:           python3-module-pyghmi
Version:        1.5.3
Release:        alt1

Summary:        Python General Hardware Management Initiative (IPMI and others)

Group:          Development/Python3
License:        Apache-2.0
URL:            https://pypi.org/project/pyghmi

Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-module-pbr
BuildRequires:  python3-module-sphinx
BuildRequires:  python3-module-openstackdocstheme

%description
This is a pure python implementation of the IPMI protocol.

%package doc
Summary: Documentation for pyghmi
Group: Development/Documentation

%description doc
Documentation for pyghmi.

%prep
%setup

# Remove bundled egg-info
rm -rf pyghmi.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python3_build

python3 setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python3_install
pushd %buildroot%_bindir
for i in $(ls); do
       sed -i 's|python|python3|g' $i
       sed -i 's|python33|python3|g' $i
       sed -i 's|tox|tox.py3|g' $i
done
popd

%files
%doc README LICENSE
%python3_sitelibdir/pyghmi
%python3_sitelibdir/*.egg-info
%_bindir/fakebmc
%_bindir/pyghmicons
%_bindir/pyghmiutil
%_bindir/virshbmc

%files doc
%doc doc/build/html

%changelog
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
