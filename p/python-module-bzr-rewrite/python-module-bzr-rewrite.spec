# $Id: python-module-bzr-rewrite.spec $
# -*- coding: utf-8 -*-
Name: python-module-bzr-rewrite
Version: 0.6.3
Release: alt1

%setup_python_module bzr-rewrite

Summary: This plugin provides various commands for rewriting Bazaar revisions
License: gpl3
Group: Development/Python

Url: https://launchpad.net/bzr-rewrite
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Wed Jan 14 2004
#BuildRequires: libapr1-devel libaprutil1-devel libsubversion-devel

%description
This plugin provides various commands for rewriting Bazaar revisions in 
an automated fashion. 

It includes a 'bzr rebase' command, in the same fashion of the 
famous ``git rebase`` command.

This module is built for python %__python_version

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/bzrlib/plugins/rewrite
%python_sitelibdir/*.egg-info
%doc AUTHORS NEWS README

%changelog
* Tue Feb 28 2012 Anatoly Kitaikin <cetus@altlinux.org> 0.6.3-alt1
- new version

* Thu Dec 08 2011 Anatoly Kitaykin <cetus@altlinux.org> 0.6.2-alt1
- Initial build
