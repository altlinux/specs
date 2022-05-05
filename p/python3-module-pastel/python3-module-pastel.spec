%global pypi_name pastel

Name: python3-module-%pypi_name
Summary: Bring colors to your terminal
Version: 0.2.0
Release: alt1
License: MIT
Group: Development/Python3
Url: https://github.com/sdispater/pastel
Source0: %pypi_name-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>
# do not install the "tests" package
Patch0: 00-dont-install-tests.patch

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build

%description
Pastel is a simple library to help you colorize strings in your
terminal.

It comes bundled with predefined styles:

- info: green
- comment: yellow
- question: black on cyan
- error: white on red

Features:

- Use predefined styles or add you own.
- Disable colors all together by calling with_colors(False).
- Automatically disables colors if the output is not a TTY.
- Used in cleo.

%prep
%setup -n %pypi_name-%version
%patch0 -p1
# https://bugzilla.altlinux.org/show_bug.cgi?id=39907
#[ -e setup.py ] && rm -f ./setup.py
#echo 'import setuptools; setuptools.setup()' > setup.py
%build
%python3_build

%install
%python3_install

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

%files
%doc README.rst LICENSE

%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py?.??.egg-info/

%changelog
* Thu May 05 2022 Ilya Mashkin <oddity@altlinux.ru> 0.2.0-alt1
- Build for Sisyphus

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-1
- Update to version 0.2.0.
- Enable running test suite.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.8

* Sat Aug 10 2019 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-1
- Initial package.

