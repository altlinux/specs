%define  modulename glymur
%def_with check

Name:    python3-module-%modulename
Version: 0.9.9
Release: alt1

Summary: Python interface to OpenJPEG library for reading and writing JPEG 2000 images.

License: MIT
Group:   Development/Python3
URL:     https://github.com/quintusdias/glymur

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-lxml
BuildRequires: python3-module-scikit-image
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
[ -e setup.py ] && rm -f ./setup.py
echo 'import setuptools; setuptools.setup()' > setup.py
%python3_build

%install
%python3_install

# don't install tests in such directory please
rm -rf %buildroot%python3_sitelibdir/tests

%check
py.test3

%files
%doc README.md CHANGES.txt LICENSE.txt
%_bindir/jp2dump
%_bindir/tiff2jp2
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Fri Mar 25 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.9-alt1
- Automatically updated to 0.9.9.

* Mon Mar 14 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.8-alt1
- Automatically updated to 0.9.8.

* Sat Feb 05 2022 Grigory Ustinov <grenka@altlinux.org> 0.9.7-alt1
- Automatically updated to 0.9.7.

* Tue Nov 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.6-alt1
- Automatically updated to 0.9.6.

* Tue Sep 07 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.4-alt1
- Automatically updated to 0.9.4.

* Thu Jan 14 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.3-alt1
- Automatically updated to 0.9.3.

* Wed Sep 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus.
