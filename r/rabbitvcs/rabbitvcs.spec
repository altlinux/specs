%define _unpackaged_files_terminate_build 1
Name:    rabbitvcs
Version: 0.19
Release: alt2

Summary: Graphical user interface to version control systems.
License: GPLv2+
Group:   Development/Other
URL:     http://rabbitvcs.org

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-pygobject3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
RabbitVCS is a set of graphical tools written to provide simple and
straightforward access to the version control systems you use.

%package core
Summary: Common package of RabbitVCS
Group:   Development/Other
Requires: meld

%description core
Contains files shared between the RabbitVCS extensions.

%package -n python3-module-rabbitvcs
Summary: Graphical user interface to version control systems
Group:   Development/Other
Requires: %name-core = %version-%release
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
Requires: %name-core = %version-%release
Requires: python3-module-rabbitvcs = %version-%release

%description cli
A command line command to use RabbitVCS

%package caja
Summary: Caja extension for RabbitVCS
Group:   Development/Other
# caja needs python3 for plugins
Requires: python3-module-rabbitvcs = %{version}-%{release}
Requires: python3-module-dbus
Requires: python3-module-caja
Requires: /usr/bin/caja

%description caja
An extension for Caja to allow better integration with the
source control system.

%package nautilus
Summary: Nautilus extension for RabbitVCS
Group:   Development/Other
# nautilus needs python3 for plugins
Requires: python3-module-rabbitvcs = %version-%release
Requires: python3-module-dbus
Requires: nautilus-python
Requires: nautilus

%description    nautilus
An extension for Nautilus to allow better integration with the
source control system.

%package nemo
Summary: Nemo extension for RabbitVCS
Group:   Development/Other
# nemo needs python3 for plugins
Requires: python3-module-rabbitvcs = %version-%release
Requires: python3-module-dbus
Requires: nemo-python
Requires: nemo

%description nemo
An extension for Nemo to allow better integration with the
source control system.

%prep
%setup

%build
%pyproject_build

%install
#mkdir -p %buildroot%python3_sitelibdir/python3-module-rabbitvcs
%pyproject_install
install -p -m0755 clients/cli/rabbitvcs -D %buildroot%_bindir/rabbitvcs
install -p -m0644 clients/caja/RabbitVCS.py -D %buildroot%_datadir/caja-python/extensions/RabbitVCS.py
install -p -m0644 clients/nautilus/RabbitVCS.py -D %buildroot%_datadir/nautilus-python/extensions/RabbitVCS.py
install -p -m0644 clients/nemo/RabbitVCS.py -D %buildroot%_datadir/nemo-python/extensions/RabbitVCS.py
rm -f %buildroot%_defaultdocdir/rabbitvcs/*
rm -rf %buildroot%python3_sitelibdir/rabbitvcs/tests

%find_lang RabbitVCS

%files -f RabbitVCS.lang core
%_datadir/rabbitvcs/
%_datadir/icons/hicolor/16x16/actions/rabbitvcs-push.png
%_datadir/icons/hicolor/scalable/*/*.svg

%files -n python3-module-rabbitvcs
%python3_sitelibdir/rabbitvcs
%python3_sitelibdir/rabbitvcs-*.dist-info

%files cli
%_bindir/rabbitvcs

%files caja
%_datadir/caja-python/extensions/*.py*

%files nautilus
%_datadir/nautilus-python/extensions/*.py*

%files nemo
%_datadir/nemo-python/extensions/*.py*

%changelog
* Sun Apr 07 2024 Andrey Cherepanov <cas@altlinux.org> 0.19-alt2
- Fixied module name.
- Used %%pyproject_build.
- Required /usr/bin/caja insead of caja package.

* Wed Mar 27 2024 Kirill Izmestev <felixz@altlinux.org> 0.19-alt1
- Initial build for Sisyphus (ALT #30354).
