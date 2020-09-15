# -*- coding: utf-8 -*-
%define _unpackaged_files_terminate_build 1
%def_with python3

Name: python3-module-brz-colo
Version: 0.4.0
Release: alt2

Summary: Colocated branches in Bazaar using present technology
License: GPL-2.0+
Group: Development/Python
Url: https://launchpad.net/bzr-colo
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %name-%version.tar
Patch0: %name-%version-lp-bzr-colo.patch
Patch1: %name-%version-alt-breezy.patch

BuildRequires(pre): rpm-build-python3

%description
In order to provide a faster and simpler working model, this plugin tries
to support a configuration similar to git and Mercurial's colocated branches,
where there is a single working tree that can be switched between multiple
branches that all co-exist in the same directory. This working model is
entirely possible using Bazaar's existing technology, and this plugin aims to
make it as simple as possible to use that model.

This module is built for python %__python_version

%package tests
Summary: brz-colo tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contain tools and test suites for testing brz-colo

%prep
%setup -n %name-%version
%patch0 -p1
%patch1 -p1

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir

%files
%python3_sitelibdir/breezy/plugins/colo
%exclude %python3_sitelibdir/breezy/plugins/colo/tests
%python3_sitelibdir/*.egg-info
%doc NEWS.txt TODO.txt

%files tests
%python3_sitelibdir/breezy/plugins/colo/tests

%changelog
* Fri Sep 11 2020 Anatoly Kitaykin <cetus@altlinux.org> 0.4.0-alt2
- Upstream typo fixes
- Breezy support patch
- Python3 build

* Wed Jan 23 2013 Anatoly Kitaikin <cetus@altlinux.org> 0.4.0-alt1
- Initial build
