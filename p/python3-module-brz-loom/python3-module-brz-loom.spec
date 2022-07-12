# -*- coding: utf-8 -*-
%define _unpackaged_files_terminate_build 1
%def_with python3

Name: python3-module-brz-loom
Version: 3.0.0
Release: alt1

Summary: Loom, a plugin for breezy to assist in developing focused patches
License: GPL-2.0
Group: Development/Python
#Url: https://launchpad.net/brz-loom
Url:https://github.com/breezy-team/breezy-loom.git
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Loom is a Breezy plugin that helps you to manage and develop patches.

It is similar to tools such as Quilt, Stacked Git and Mercurial Queues. However,
it also gives you the full power of version control when managing your stack of 
patches. This makes collaboration just as easy as if you were working with a
normal Bazaar/Breezy branch. Using Loom, you can roll back, annotate, push and
pull the stack you're building.

This module is built for python %__python_version

%package tests
Summary: brz-loom tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contain tools and test suites for testing brz-loom

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir

%files
%python3_sitelibdir/breezy/plugins/loom
%exclude %python3_sitelibdir/breezy/plugins/loom/tests
%python3_sitelibdir/*.egg-info
%doc CONTRIBUTORS HOWTO NEWS README.rst TODO

%files tests
%python3_sitelibdir/breezy/plugins/loom/tests

%changelog
* Tue Jul 12 2022 Anatoly Kitaykin <cetus@altlinux.org> 3.0.0-alt1
- Initial build
