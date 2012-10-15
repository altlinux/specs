# -*- coding: utf-8 -*-
Name: python-module-bzr-stats
Version: 0.1.0
Release: alt1

%setup_python_module bzr-stats

Summary: Simple statistics plugin for Bazaar.
License: gpl2
Group: Development/Python

Url: https://launchpad.net/bzr-stats
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: rpm-build-licenses

%description
Simple statistics plugin for Bazaar. At the moment it can display
statistics about the committers that have contributed to a project.

This module is built for python %__python_version

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/bzrlib/plugins/stats
%python_sitelibdir/*.egg-info
%doc NEWS

%changelog
* Mon Oct 15 2012 Anatoly Kitaikin <cetus@altlinux.org> 0.1.0-alt1
- First build.

