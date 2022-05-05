%global pypi_name cleo

Name: python3-module-%pypi_name
Summary: Create beautiful and testable command-line interfaces
Version: 0.8.1
Release: alt1
License: MIT
Group: Development/Python3
Url: https://github.com/sdispater/cleo
Source0: %pypi_name-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build

%description 
Create beautiful and testable command-line interfaces.

Cleo is mostly a higher level wrapper for CliKit, so a lot of the
components and utilities comes from it. Refer to its documentation for
more information.


%prep
%setup -n %pypi_name-%version
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
#[ -e setup.py ] && rm -f ./setup.py
#echo 'import setuptools; setuptools.setup()' > setup.py
%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py?.??.egg-info/

%changelog
* Thu May 05 2022 Ilya Mashkin <oddity@altlinux.ru> 0.8.1-alt1
- Build for Sisyphus

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.10

* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.1-1
- Update to version 0.8.1.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-3
- Rebuilt for Python 3.9

* Sun Dec 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.6-1
- Update to version 0.7.6.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-2
- Rebuilt for Python 3.8

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-1
- Initial package.

