%global pypi_name clikit

Name: python3-module-%pypi_name
Summary: Utilities to build beautiful and testable CLIs
Version: 0.6.2
Release: alt1
License: MIT
Group: Development/Python3
Url: https://github.com/sdispater/clikit
Source0: %pypi_name-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build

%description
CliKit is a group of utilities to build beautiful and testable command
line interfaces. This is at the core of Cleo.

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
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py?.??.egg-info/

%changelog
* Thu May 05 2022 Ilya Mashkin <oddity@altlinux.ru> 0.6.2-alt1
- Build for Sisyphus

* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.6.2-1
- Update to version 0.6.2.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.4.2-1
- Update to version 0.4.2.

* Sun Dec 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.4.1-1
- Update to version 0.4.1.

* Fri Nov 15 2019 Fabio Valentini <decathorpe@gmail.com> - 0.4.0-1
- Update to version 0.4.0.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuilt for Python 3.8

* Sun May 12 2019 Fabio Valentini <decathorpe@gmail.com> - 0.2.4-1
- Update to version 0.2.4.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Initial package.

