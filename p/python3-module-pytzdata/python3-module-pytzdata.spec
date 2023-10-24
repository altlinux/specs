%global pypi_name pytzdata

Name: python3-module-%pypi_name
Version: 2020.1
Release: alt1.1
Group: Development/Python3
License: MIT
Summary: Timezone database for Python
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: https://github.com/sdispater/%pypi_name
Source0: %pypi_name-%version.tar.gz
Patch: remove-distutils-for-python-3.12.patch
BuildArch: noarch

BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build

%description
The Olson timezone database for Python.

%prep

%setup -n %pypi_name-%version
%patch -p2
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
[ -e setup.py ] && rm -f ./setup.py
echo 'import setuptools; setuptools.setup()' > setup.py
%build
%python3_build

%install
%python3_install



%files
%doc README.rst
%python3_sitelibdir/%pypi_name-0.0.0-py?.??.egg-info
%python3_sitelibdir/%pypi_name


%changelog
* Tue Oct 24 2023 Grigory Ustinov <grenka@altlinux.org> 2020.1-alt1.1
- NMU: dropped dependency on distutils.

* Thu May 05 2022 Ilya Mashkin <oddity@altlinux.ru> 2020.1-alt1
- Build for Sisyphus

* Sun Dec 12 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1-5
- Converted SPEC to 201x-era guidelines.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2020.1-3
- Rebuilt for Python 3.10

* Mon Dec 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2020.1-1
- Updated to version 2020.1.

* Wed Jun 24 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3-2
- Added python3-setuptools to build requirements.

* Thu Jun 18 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 2019.3-1
- Initial SPEC release.
