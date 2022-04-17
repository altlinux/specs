Name: python3-module-verspec
Version: 0.1.0
Release: alt1

Summary: Library for handling software versions and specifiers

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/verspec/

Source: verspec-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 17 2022
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-Pygments python3-module-docutils python3-module-filelock python3-module-packaging python3-module-pep517 python3-module-pkg_resources python3-module-platformdirs python3-module-pyparsing python3-module-six python3-module-system-seed-wheels python3-module-tomli sh4
BuildRequires: python3-module-build python3-module-flit python3-module-setuptools python3-module-virtualenv python3-module-wheel

%description
verspec is a Python library for handling software versions and specifiers,
adapted from the packaging package.

%prep
%setup -n verspec-%version

%build
python3 -m build -w -n

%install
pip3 install --ignore-installed --root=%buildroot --no-deps dist/verspec-%version-py3-none-any.whl

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.1.0-alt1
- Initial build for ALT
