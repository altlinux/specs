# -*- coding: utf-8 -*-
Name: python-module-bzr-colo
Version: 0.4.0
Release: alt1

%setup_python_module bzr-colo

Summary: Colocated branches in Bazaar using present technology
License: gpl2
Group: Development/Python

Url: https://launchpad.net/sample
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: rpm-build-licenses

%description
In order to provide a faster and simpler working model, this plugin tries
to support a configuration similar to git and Mercurial's colocated branches,
where there is a single working tree that can be switched between multiple
branches that all co-exist in the same directory. This working model is
entirely possible using Bazaar's existing technology, and this plugin aims to
make it as simple as possible to use that model.

This module is built for python %__python_version

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/bzrlib/plugins/colo
%python_sitelibdir/*.egg-info
%doc NEWS.txt TODO.txt

%changelog
* Wed Jan 23 2013 Anatoly Kitaikin <cetus@altlinux.org> 0.4.0-alt1
- Initial build
