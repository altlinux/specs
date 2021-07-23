%define oname vcversioner

Name: python3-module-%oname
Version: 2.16.0.0
Release: alt3
Summary: Use version control tags to discover version numbers
License: ISCL
Group: Development/Python3
Url: https://pypi.python.org/pypi/vcversioner/

# https://github.com/habnabit/vcversioner.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: git-core
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname

%description
Elevator pitch: you can write a setup.py with no version information
specified, and vcversioner will find a recent, properly-formatted VCS
tag and extract a version from it.

It's much more convenient to be able to use your version control
system's tagging mechanism to derive a version number than to have to
duplicate that information all over the place. I eventually ended up
copy-pasting the same code into a couple different setup.py files just
to avoid duplicating version information. But, copy-pasting is dumb and
unit testing setup.py files is hard. This code got factored out into
vcversioner.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAl"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
py.test3 -vv

%files
%doc COPYING *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 2.16.0.0-alt3
- Drop python2 support.

* Tue Jul 06 2021 Grigory Ustinov <grenka@altlinux.org> 2.16.0.0-alt2
- Fixed FTBFS.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.16.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.16.0.0-alt1
- Updated to upstream version 2.16.0.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.14.0.0-alt2.git20140715.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 2.14.0.0-alt2.git20140715
- cleanup buildreq

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0.0-alt1.git20140715
- Initial build for Sisyphus
