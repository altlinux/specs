%define _unpackaged_files_terminate_build 1
%define oname canto_next

Name: canto-next
Version: 0.9.7
Release: alt1.1

Summary: The next generation Canto RSS daemon.
License: GPLv2
Group: Networking/News
Url: http://codezen.org/canto-ng/
# https://github.com/themoken/canto-next.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Requires: python3-module-%name


%description
This is the RSS backend for Canto clients.

Canto is an Atom/RSS feed reader for the console that is meant to be
quick, concise, and colorful. It's meant to allow you to crank through
feeds like you've never cranked before by providing a minimal, yet
information packed interface. No navigating menus. No dense blocks of
unreadable white text. An interface with almost infinite customization
and extensibility using the excellent Python programming language.

%package -n python3-module-%name
Summary: Python module for %name
Group: Development/Python3

%description -n python3-module-%name
This is the RSS backend for Canto clients.

Canto is an Atom/RSS feed reader for the console that is meant to be
quick, concise, and colorful. It's meant to allow you to crank through
feeds like you've never cranked before by providing a minimal, yet
information packed interface. No navigating menus. No dense blocks of
unreadable white text. An interface with almost infinite customization
and extensibility using the excellent Python programming language.

This package contains python3 module for %name.

%package -n python3-module-%name-tests
Summary: Tests for %name
Group: Development/Python3

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/tests/

%description -n python3-module-%name-tests
This is the RSS backend for Canto clients.

Canto is an Atom/RSS feed reader for the console that is meant to be
quick, concise, and colorful. It's meant to allow you to crank through
feeds like you've never cranked before by providing a minimal, yet
information packed interface. No navigating menus. No dense blocks of
unreadable white text. An interface with almost infinite customization
and extensibility using the excellent Python programming language.

This package contains tests for %name.

%package -n python3-module-%name-plugins
Summary: Python module for %name
Group: Development/Python3
Requires: %name

%description -n python3-module-%name-plugins
This is the RSS backend for Canto clients.

Canto is an Atom/RSS feed reader for the console that is meant to be
quick, concise, and colorful. It's meant to allow you to crank through
feeds like you've never cranked before by providing a minimal, yet
information packed interface. No navigating menus. No dense blocks of
unreadable white text. An interface with almost infinite customization
and extensibility using the excellent Python programming language.

This package contains plugins for %name.

%prep
%setup

for i in `ls plugins`; do
sed -i '1s|^|#!/usr/bin/python3|' plugins/$i
done

%build
%python3_build_debug

%install
%python3_install

mv tests/ %buildroot%python3_sitelibdir/%oname/

%files
%doc COPYING README.md
%_bindir/canto-daemon
%_bindir/canto-remote
%_man1dir/canto-*
%_libexecdir/systemd/user/canto-daemon.service

%files -n python3-module-%name
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%oname/*.py
%python3_sitelibdir/%oname/__pycache__/

%files -n python3-module-%name-tests
%python3_sitelibdir/%oname/tests/

%files -n python3-module-%name-plugins
%_libexecdir/canto/plugins/


%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.9.7-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.7-alt1
- Version updated to 0.9.7
- porting on python3

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt1.rc1.git20140903.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.rc1.git20140903.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.rc1.git20140903
- Initial build for Sisyphus

