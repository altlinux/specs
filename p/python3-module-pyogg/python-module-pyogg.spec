Name: python3-module-pyogg
Version: 0.6.14
Release: alt1
Summary: Python bindings for Xiph.org Opus, Vorbis and FLAC and their Ogg container format

Group: Development/Python3
License: Unlicense
URL: https://github.com/TeamPyOgg/PyOgg/blob/master/LICENSE
Source: PyOgg-%{version}a1.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 02 2025
# optimized out: bash5 libgpg-error openssl-config python3 python3-base python3-dev python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-charset-normalizer python3-module-jaraco.collections python3-module-jaraco.context python3-module-jaraco.functools python3-module-jaraco.text python3-module-jinja2 python3-module-more-itertools python3-module-packaging python3-module-pkg_resources python3-module-py3dephell python3-module-sphinx python3-module-wheel sh5
BuildRequires: python3-module-genshi python3-module-pyproject-installer python3-module-setuptools

%description
PyOgg provides Python bindings for Xiph.org Opus, Vorbis and FLAC
audio file formats as well as their Ogg container format.

%prep
%setup -n PyOgg-%{version}a1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README*
%python3_sitelibdir/*

%changelog
* Thu Jan 02 2025 Fr. Br. George <george@altlinux.ru> 0.6.14-alt1
- Initial ALT build
