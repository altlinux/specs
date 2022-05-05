%global pypi_name pylev

Name: python3-module-%pypi_name
Summary: Liberally licensed, pure Python Levenshtein implementation
Version: 1.3.0
Release: alt1
License: BSD
Group: Development/Python3
Url: http://github.com/toastdriven/pylev
Source0: %pypi_name-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>
# Include LICENSE file from upstream repository
Source1: https://raw.githubusercontent.com/toastdriven/pylev/master/LICENSE

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build

%description
A pure Python Levenshtein implementation that's not freaking GPL'd.

Based off the Wikipedia code samples at
https://en.wikipedia.org/wiki/Levenshtein_distance.

%prep
%setup -n %pypi_name-%version

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

cp %SOURCE1 .

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/%pypi_name-%version-py?.??.egg-info

%changelog
* Thu May 05 2022 Ilya Mashkin <oddity@altlinux.ru> 1.3.0-alt1
- Build for Sisyphus

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-7
- Rebuilt for Python 3.9

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-4
- Rebuilt for Python 3.8

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 1.3.0-1
- Initial package.

