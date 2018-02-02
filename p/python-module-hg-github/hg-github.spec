%def_disable check

%define oname hg-github
Name: python-module-%oname
Version: 0.1.5
Release: alt2.git20140713.1
Summary: A Mercurial extension for working with GitHub repositories
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/hg-github/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/stephenmcd/hg-github.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-setuptools mercurial

Requires: mercurial
%py_provides hggithub

%description
hg-github is a Mercurial extension that wraps hg-git, and supports a
work-flow where repositories are hosted on Bitbucket and mirrored on
GitHub. This work-flow normally requires adding Git paths to each
repository's config file, and creating Mercurial bookmarks pointing to
the GitHub repository's branch name. hg-github takes care of these for
you automatically.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc AUTHORS *.rst docs/*.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.5-alt2.git20140713.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 0.1.5-alt2.git20140713
- Disabled tests and unnecessary dependents

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140713
- Initial build for Sisyphus

