# $Id: python-module-bzrtools.spec 138 2004-03-26 23:17:36Z cray $
# -*- coding: utf-8 -*-
Name: python-module-bzrtools
Version: 2.5
Release: alt1

%setup_python_module bzrtools

Summary: Bzrtools is plugin providing a collection of utilities for bzr.
License: gpl2plus
Group: Development/Other

Url: http://bazaar-vcs.org/BzrTools/
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed Jan 14 2004
#BuildRequires: libapr1-devel libaprutil1-devel libsubversion-devel

%description
Bzrtools is plugin providing a collection of utilities for bzr.

This module is built for python %__python_version

%package -n python-module-bzrtools-tests
Summary: Bzrtools plugin tests
Group: Development/Other

Requires: %name = %version-%release

%description -n python-module-bzrtools-tests
This package contain tools and test suites for testing bzrtools.


%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/bzrlib/plugins/%modulename/
%exclude %python_sitelibdir/bzrlib/plugins/%modulename/tests
%python_sitelibdir/*.egg-info
%doc AUTHORS CREDITS INSTALL NEWS* PACKAGERS README* TODO*

%files -n python-module-bzrtools-tests
%dir %python_sitelibdir/bzrlib/plugins/%modulename/
%python_sitelibdir/bzrlib/plugins/%modulename/tests

%changelog
* Fri Mar 09 2012 Anatoly Kitaikin <cetus@altlinux.org> 2.5-alt1
- 2.5 release
- create python-module-bzrtools-tests subpackage

* Tue Jan 17 2012 Anatoly Kitaykin <cetus@altlinux.org> 2.4.1-alt1
- 2.4.1 release

* Wed Nov 30 2011 Anatoly Kitaykin <cetus@altlinux.org> 2.3.0-alt1
- Initial build


