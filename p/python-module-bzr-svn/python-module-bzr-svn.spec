# $Id: python-module-bzr-svn.spec 138 2004-03-26 23:17:36Z cray $
# -*- coding: utf-8 -*-
Name: python-module-bzr-svn
Version: 1.2.1
Release: alt1

%setup_python_module bzr-svn

Summary: Python bindings for the Subversion version control system that are aimed to be complete, fast and feel native to Python programmers.
License: %gpl2plus
Group: Development/Other

Url: https://launchpad.net/bzr-svn/
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar.gz

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Jan 14 2004
#BuildRequires: libapr1-devel libaprutil1-devel libsubversion-devel

%description
Python bindings for the Subversion version control system that are
aimed to be complete, fast and feel native to Python programmers.

Bindings are provided for the working copy, client, delta, remote
access and repository APIs. A hookable server side implementation
of the custom Subversion protocol (svn_ra) is also provided.

Subvertpy covers more of the APIs than python-svn. It provides a
more "Pythonic" API than python-subversion, which wraps the Subversion
C API pretty much directly. Neither provide a hookable server-side.

This module is built for python %__python_version

%package -n python-module-bzr-svn-tests
Summary: Bzr-svn plugin tests
Group: Development/Other

Requires: %name = %version-%release

%description -n python-module-bzr-svn-tests
This package contain tools and test suites for testing bzr-svn.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/bzrlib/plugins/svn/
%exclude %python_sitelibdir/bzrlib/plugins/svn/tests
%python_sitelibdir/*.egg-info
%doc AUTHORS FAQ HACKING INSTALL NEWS README TODO

%files -n python-module-bzr-svn-tests
%dir %python_sitelibdir/bzrlib/plugins/svn
%python_sitelibdir/bzrlib/plugins/svn/tests

%changelog
* Fri Mar 16 2012 Anatoly Kitaykin <cetus@altlinux.org> 1.2.1-alt1
- 1.2.1 release
- subpackage python-module-bzr-svn-tests

* Wed Nov 30 2011 Anatoly Kitaikin <cetus@altlinux.org> 1.1.1-alt1
- New release

* Sat Oct 29 2011 Anatoly Kitaikin <cetus@altlinux.org> 1.1.0-alt1
- Initial revision
