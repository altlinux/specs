# $Id: python-module-bzr-webdav.spec $
# -*- coding: utf-8 -*-
Name: python-module-bzr-webdav
Version: 2.5.0
Release: alt2

%setup_python_module bzr-webdav

Summary: Implementation of WebDAV for bzr http transports.
License: gpl3
Group: Development/Python

Url: https://launchpad.net/bzr-webdav
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar

BuildPreReq: rpm-build-licenses

%description
Implementation of WebDAV for bzr http transports.
 Allows write access to DAV-enabled web servers by registering http+webdav and https+webdav as protocols recognized by bzr

A Transport which complement http transport by implementing partially the WebDAV protocol to push files.
 This enables remote push operations.
 It requires:
 - to be installed as a plugin for bzr
 - a DAV enabled web server

It has been (and is still) tested against Apache 2.x.

This module is built for python %_python_version

%package -n python-module-bzr-webdav-tests
Summary: bzr-webdav plugin tests
Group: Development/Other
Requires: %name = %version-%release
Requires: python%_python_version(bzrlib.tests)

%description -n python-module-bzr-webdav-tests
This package contain tools and test suites for testing bzr-webdav.


%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir

%files
%python_sitelibdir/bzrlib/plugins/webdav
%exclude %python_sitelibdir/bzrlib/plugins/webdav/tests
%python_sitelibdir/*.egg-info
%doc NOTES TODO

%files -n python-module-bzr-webdav-tests
%dir %python_sitelibdir/bzrlib/plugins/webdav
%python_sitelibdir/bzrlib/plugins/webdav/tests

%changelog
* Mon Oct 15 2012 Anatoly Kitaykin <cetus@altlinux.org> 2.5.0-alt2
- don't use resigned upstream tags, change gear rules

* Mon Oct 15 2012 Anatoly Kitaykin <cetus@altlinux.org> 2.5.0-alt1
- 2.5.0 release

