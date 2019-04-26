# $Id: python-module-launchpadlib.spec $
# -*- coding: utf-8 -*-
Name: python-module-launchpadlib
Version: 1.10.6
Release: alt1

%setup_python_module launchpadlib

Summary: Script Launchpad through its web services interfaces.  Officially supported.
License: gpl3
Group: Development/Python

Url: https://launchpad.net/launchpadlib
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: rpm-build-licenses

Requires: python%_python_version(lazr.uri)
Requires: python%_python_version(lazr.restfulclient)

%add_python_req_skip lazr

%description
launchpadlib is a standalone Python library for scripting Launchpad through
its web services interface.  It is the officially supported bindings to the
Launchpad web service, but there may be third party bindings that provide
scriptability for other languages.

This module is built for python %_python_version

%package -n python-module-launchpadlib-tests
Summary: launchpadlib tests
Group: Development/Other
Requires: %name = %version-%release
#Requires: python#_python_version(bzrlib.tests)

%description -n python-module-launchpadlib-tests
This package contain tools and test suites for testing launchpadlib.


%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/launchpadlib/
%exclude %python_sitelibdir/launchpadlib/tests
%python_sitelibdir/*.egg-info
%doc HACKING.txt README.txt

%files -n python-module-launchpadlib-tests
%dir %python_sitelibdir/launchpadlib
%python_sitelibdir/launchpadlib/tests

%changelog
* Tue Mar 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.10.6-alt1
- Initial build
