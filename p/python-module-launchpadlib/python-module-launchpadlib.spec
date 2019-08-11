%define _unpackaged_files_terminate_build 1
%def_with python3

Name: python-module-launchpadlib
Version: 1.10.7
Release: alt2
%setup_python_module launchpadlib
Summary: Script Launchpad through its web services interfaces.  Officially supported.
License: gpl3
Group: Development/Python
Url: https://launchpad.net/launchpadlib
Packager: Anatoly Kitaikin <cetus@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses

%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

Requires: python%_python_version(lazr.uri)
Requires: python%_python_version(lazr.restfulclient)

%add_python_req_skip lazr

%py_provides launchpadlib

%description
launchpadlib is a standalone Python library for scripting Launchpad through
its web services interface.  It is the officially supported bindings to the
Launchpad web service, but there may be third party bindings that provide
scriptability for other languages.

This module is built for python %_python_version

%package tests
Summary: launchpadlib tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contain tools and test suites for testing launchpadlib.

%if_with python3
%package -n python3-module-launchpadlib
Summary: Script Launchpad through its web services interfaces.  Officially supported.
Group: Development/Python3

%py3_provides launchpadlib

%description -n python3-module-launchpadlib
launchpadlib is a standalone Python library for scripting Launchpad through
its web services interface.  It is the officially supported bindings to the
Launchpad web service, but there may be third party bindings that provide
scriptability for other languages.

This module is built for python %_python_version

%package -n python3-module-launchpadlib-tests
Summary: launchpadlib tests
Group: Development/Python3
Requires: python3-module-launchpadlib = %version-%release

%description -n python3-module-launchpadlib-tests
This package contain tools and test suites for testing launchpadlib.

%endif

%prep
%setup -q
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc HACKING.txt README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/launchpadlib/tests

%files tests
%python_sitelibdir/launchpadlib/tests

%if_with python3

%files -n python3-module-launchpadlib
%doc HACKING.txt README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/launchpadlib/tests

%files -n python3-module-launchpadlib-tests
%python3_sitelibdir/launchpadlib/tests

%endif

%changelog
* Sun Aug 11 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.10.7-alt2
- Requirements fix

* Fri Aug 09 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.10.7-alt1
- Release 1.10.7

* Sun Jul 21 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.10.6-alt2
- Python3 support added

* Tue Mar 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.10.6-alt1
- Initial build
