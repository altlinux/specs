# vim: set ft=spec: -*- rpm-spec -*-

%def_without check
%def_without python3

Name: breezy
Version: 3.0.0
Release: alt1

Summary: Breezy is a fork of decentralized revision control system Bazaar
License: %gpl2plus
Group: Development/Other

Url: https://github.com/breezy-team/breezy.git
Packager: Anatoly Kitaykin <cetus@altlinux.ru>

Source: %name-%version.tar

Patch0: %name-%version.patch

Conflicts: %name-doc < %version
Conflicts: bzr-git-remote

BuildRequires(pre): rpm-build-licenses

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-six
BuildRequires: python3-module-Cython
BuildRequires: python3-module-configobj

%else
BuildRequires(pre): rpm-build-python
BuildRequires: python-dev
BuildRequires: python-module-six
BuildRequires: python-module-Cython
BuildRequires: python-module-configobj

%endif

%if_with check
#python2
BuildRequires: python-modules
BuildRequires: python-module-six
BuildRequires: python-module-setuptools
BuildRequires: python-module-configobj
BuildRequires: python-module-dulwich
BuildRequires: python-module-sphinx
#BuildRequires: python-module-sphinx[contrib]-epytext
BuildRequires: python-module-Cython
BuildRequires: python-module-Pyrex
#python3
BuildRequires: python3-module-docutils
BuildRequires: python3-module-paramiko
BuildRequires: python3-module-testtools
BuildRequires: python3-module-subunit
BuildRequires: python3-module-dulwich
BuildRequires: python3-module-subunit
BuildRequires: python3-module-configobj
BuildRequires: python3-module-six
%endif

%if_with python3
%add_python3_req_skip lazr

%else
%add_python_req_skip lazr

%endif

%description
Breezy (or brz) is a distributed version control system that is powerful, friendly, and scalable.
Breezy is a fork of the Bazaar version control system.
By default, Breezy provides support for both the Bazaar and Git file formats.

%if_with python3
%package -n python3-module-breezy-tests
Summary: Tools for testing Bazaar
Group: Development/Other
#BuildArch: noarch

Requires: %name = %version-%release
Provides: brz-selftest = %version-%release

%description -n python3-module-breezy-tests
This package contain tools and test suites for testing Bazaar.

%else
%package -n python-module-breezy-tests
Summary: Tools for testing Bazaar
Group: Development/Other
#BuildArch: noarch

Requires: %name = %version-%release
Provides: brz-selftest = %version-%release

%description -n python-module-breezy-tests
This package contain tools and test suites for testing Bazaar.

%endif

%package doc
Summary: %name documentation and examples
Group: Development/Other
BuildArch: noarch

Conflicts: %name < %version

%description doc
Bazaar is a decentralized revision control system. This
package contain documentation and examples for using Bazaar.

%prep
%setup
#patch0 -p1

%build
%add_optflags -fno-strict-aliasing

%if_with python3
%python3_build

%else
%python_build

%endif

%install
#define _compress_method none

%if_with python3
%python3_install --install-data=%_datadir

%else
%python_install --install-data=%_datadir

%endif

%define breezy_docdir %_docdir/%name-%version

install -dm0755 %buildroot%breezy_docdir
install -m0644 BRANCH.TODO INSTALL NEWS README.rst README_BDIST_RPM TODO %buildroot%breezy_docdir
cp -a doc contrib %buildroot%breezy_docdir
# Hack! Need a subst in setup.py
cp -a breezy/locale %buildroot%_datadir
%find_lang %name

%check
%make_build check

%files -f %name.lang
%_bindir/*
%_man1dir/*

%if_with python3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/breezy/tests
%exclude %python3_sitelibdir/breezy/plugins/*/tests
%exclude %python3_sitelibdir/breezy/util/tests

%else
%python_sitelibdir/*
%exclude %python_sitelibdir/breezy/tests
%exclude %python_sitelibdir/breezy/plugins/*/tests
%exclude %python_sitelibdir/breezy/util/tests

%endif

%breezy_docdir
%exclude %breezy_docdir/doc
%exclude %breezy_docdir/contrib
#%%_datadir/locale/*/LC_MESSAGES/brz.mo

%if_with python3

%files -n python3-module-breezy-tests
%python3_sitelibdir/breezy/tests
%python3_sitelibdir/breezy/plugins/*/tests
%python3_sitelibdir/breezy/util/tests

%else

%files -n python-module-breezy-tests
%python_sitelibdir/breezy/tests
%python_sitelibdir/breezy/plugins/*/tests
%python_sitelibdir/breezy/util/tests

%endif

%files doc
%dir %breezy_docdir
%breezy_docdir/doc
%breezy_docdir/contrib

%changelog
* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 3.0.0-alt1
- Initial build

