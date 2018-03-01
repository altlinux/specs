Name:    blink-qt
Version: 3.0.3
Release: alt1

Summary: Blink SIP Client
License: GPLv3+
Group:   Other
URL:     http://icanblink.com/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: libvncserver-devel
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-application >= 2.0.0
BuildRequires: python-module-cjson
BuildRequires: python-module-Cython
BuildRequires: python-module-enum34
BuildRequires: python-module-eventlib
BuildRequires: python-module-gnutls
BuildRequires: python-module-google-api-client >= 1.6.5
BuildRequires: python-module-lxml
BuildRequires: python-module-oauth2client
BuildRequires: python-module-PyQt5 >= 5.0
BuildRequires: python-module-sipsimple >= 3.0.0
BuildRequires: python-module-twisted-core
BuildRequires: python-module-zope.interface

%py_requires service_identity twisted.names

Source:  %name-%version.tar

%description
Fully featured, easy to use SIP client with a Qt based UI Blink is a
fully featured SIP client written in Python and built on top of SIP
SIMPLE client SDK with a Qt based user interface. Blink provides real
time applications based on SIP and related protocols for Audio, Video,
Instant Messaging, File Transfers, Desktop Sharing and Presence.

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%doc README LICENSE TODO
%_bindir/blink
%_datadir/blink
%python_sitelibdir/blink/
%python_sitelibdir/*.egg-info

%changelog
* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- Initial build in Sisyphus
