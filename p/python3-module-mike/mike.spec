Name: python3-module-mike
Version: 1.1.2
Release: alt1

Summary: Deploy multiple versions of your MkDocs

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mike

Source: mike-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 17 2022
# optimized out: libgpg-error python3 python3-base python3-dev python3-module-Pygments python3-module-docutils python3-module-filelock python3-module-packaging python3-module-pep517 python3-module-pkg_resources python3-module-platformdirs python3-module-pyparsing python3-module-six python3-module-system-seed-wheels python3-module-tomli sh4
BuildRequires: python3-module-build python3-module-flit python3-module-setuptools python3-module-virtualenv python3-module-wheel

%description
Mike is a Python utility to easily deploy multiple versions of your
MkDocs-powered docs to a Git branch, suitable for deploying to Github
via gh-pages. To see an example of this in action, take a look at the
documentation for bfg9000.The parsing module is an alternative approach
to creating and executing

%prep
%setup -n mike-%version

%build
python3 -m build -n

%install
pip3 install --ignore-installed --root=%buildroot --no-deps dist/mike-%version-py3-none-any.whl

%files
%doc *.md
%python3_sitelibdir/*
%_bindir/*

%changelog
* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 1.1.1-alt1
- Initial build for ALT
