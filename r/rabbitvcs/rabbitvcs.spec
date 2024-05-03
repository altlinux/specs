%define _unpackaged_files_terminate_build 1
%def_enable check

Name:    rabbitvcs
Version: 0.19.0.21.git6f2da1b
Release: alt1

Summary: Graphical user interface to version control systems
License: GPLv2+
Group:   Development/Other
URL:     http://rabbitvcs.org
VCS:     https://github.com/rabbitvcs/rabbitvcs

Source: %name-%version.tar
# Fix broken tagging which appeares after some refactoring in dulwich module
# upstream(c477828).
Patch0: .gear/rabbitvcs-0.19-alt-fix-tagging.patch
Patch1: .gear/rabbitvcs-0.19-alt-fix-unittest.patch
# Python v3.12 requires raw strings in regexp to avoid SyntaxWarning
Patch2: .gear/rabbitvcs-0.19-alt-regexp-raw-strings-py312.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_enabled check
BuildRequires: nautilus-python
BuildRequires: python3-module-dbus
BuildRequires: python3-module-configobj
BuildRequires: python3-module-pysvn
BuildRequires: python3-module-pytest
%endif

%description
RabbitVCS is a set of graphical tools written to provide simple and
straightforward access to the version control systems you use.

%package data
Summary: Common package of RabbitVCS
Group:   Development/Other
Requires: meld
Provides: %name-data = %EVR
Obsoletes: %name-core < %EVR

%description data
Contains files shared between the RabbitVCS extensions.

%package -n python3-module-rabbitvcs
Summary: Graphical user interface to version control systems
Group:   Development/Other
Requires: %name-data = %version-%release
Requires: python3-module-configobj
Requires: python3-module-dulwich
Requires: python3-module-pygobject3
Requires: python3-module-simplejson
Requires: python3-modules-tkinter

%description -n python3-module-rabbitvcs
RabbitVCS is a set of graphical tools written to provide simple
and straightforward access to the version control systems you use.

%package cli
Summary: CLI extension for RabbitVCS
Group:   Development/Other
BuildArch: noarch
Requires: %name-data = %version-%release
Requires: python3-module-rabbitvcs = %version-%release

%description cli
A command line command to use RabbitVCS

%package caja
Summary: Caja extension for RabbitVCS
Group:   Development/Other
Requires: python3-module-%name = %{version}-%{release}
Requires: python3-module-dbus
Requires: python3-module-caja
Requires: /usr/bin/caja

%description caja
An extension for Caja to allow better integration with the
source control system.

%package nautilus
Summary: Nautilus extension for RabbitVCS
Group:   Development/Other
Requires: python3-module-%name = %version-%release
Requires: python3-module-dbus
Requires: nautilus-python
Requires: nautilus
Requires: libgtk4-gir
Requires: libnautilus-gir

%description nautilus
An extension for Nautilus to allow better integration with the
source control system.

%package nemo
Summary: Nemo extension for RabbitVCS
Group:   Development/Other
Requires: python3-module-%name = %version-%release
Requires: python3-module-dbus
Requires: nemo-python
Requires: nemo
Requires: libgtk+3-gir
Requires: libnemo-gir

%description nemo
An extension for Nemo to allow better integration with the
source control system.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%pyproject_build

%install
%pyproject_install
install -p -m0755 clients/cli/%name -D %buildroot%_bindir/%name
install -p -m0644 clients/caja/RabbitVCS.py -D %buildroot%_datadir/caja-python/extensions/RabbitVCS.py
install -p -m0644 clients/nautilus/RabbitVCS.py -D %buildroot%_datadir/nautilus-python/extensions/RabbitVCS.py
install -p -m0644 clients/nemo/RabbitVCS.py -D %buildroot%_datadir/nemo-python/extensions/RabbitVCS.py

# Remove /usr/share/doc/rabbitvcs/{AUTHORS,MAINTAINERS} cause we pack
# required texts (including license) through doc section below.
rm -v %buildroot%_defaultdocdir/%name/*

%find_lang RabbitVCS

%check
# TODO: Repair second from existant test classes RabbitVCSPySvnTest
# runner could not find configspec.ini and failing.
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 %name/tests/test_rabbitvcs.py::RabbitVCSTest

%files -f RabbitVCS.lang data
%doc AUTHORS COPYING MAINTAINERS README.md
%dir %_datadir/%name
%config(noreplace) %_datadir/%name/configspec.ini
%dir %_iconsdir/hicolor/16x16/actions
%_iconsdir/hicolor/16x16/actions/%name-push.png
%dir %_iconsdir/hicolor/scalable/actions
%dir %_iconsdir/hicolor/scalable/emblems
%_iconsdir/hicolor/scalable/*/*.svg

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-*.dist-info
%exclude %python3_sitelibdir/%name/tests

%files cli
%_bindir/%name

%files caja
%dir %_datadir/caja-python
%dir %_datadir/caja-python/extensions
%_datadir/caja-python/extensions/*.py

%files nautilus
%_datadir/nautilus-python/extensions/*.py

%files nemo
%_datadir/nemo-python/extensions/*.py

%changelog
* Thu May 02 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.19.0.21.git6f2da1b-alt1
- Build new version from git ref 6f2da1b for Sisyphus:
  + Fixed remove staged files from working tree (Closes: #50050)
- Requirements for Nemo and Nautilus file managers(ALT#50048, ALT#50049)
- Fix tag create (Closes: #50051)
- Unittests fixes:
  + getlocale() more preferable for our version
  + namespace extension(-s) moved to project root
  + Nautilus v4.0 required actually
- Suppress SyntaxWarning in regexp processing(appeared in Python 3.12)

* Sun Apr 07 2024 Andrey Cherepanov <cas@altlinux.org> 0.19-alt2
- Fixied module name.
- Used %%pyproject_build.
- Required /usr/bin/caja insead of caja package.

* Wed Mar 27 2024 Kirill Izmestev <felixz@altlinux.org> 0.19-alt1
- Initial build for Sisyphus (ALT #30354).
