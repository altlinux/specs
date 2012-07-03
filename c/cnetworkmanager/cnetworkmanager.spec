Name:           cnetworkmanager
Version:        0.21.1
Release:        alt1.1
Summary:        Command-line client for NetworkManager
License:        GPL v2 or later
Url:            http://vidner.net/martin/software/cnetworkmanager/
Group:          System/Configuration/Networking
BuildArch:      noarch

BuildRequires:	python-dev python-module-pygobject-devel python-module-dbus-devel
Requires:	NetworkManager >= 0.7.0
Provides:       NetworkManager-client

Source:         %{name}-%{version}.tar
Patch:		%{name}-%{version}-%{release}.patch

%description
Cnetworkmanager is a command-line client for NetworkManager, intended
to supplement and replace the GUI applets.

%prep
%setup
%patch -p0

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT 

%check
make check-nonm

%files
%defattr(-,root,root)
%doc README COPYING HACKING NEWS screenshots.html
%_sysconfdir/dbus-1/system.d/cnetworkmanager.conf
%_bindir/%name

%python_sitelibdir/networkmanager
%python_sitelibdir/dbusclient

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.21.1-alt1.1
- Rebuild with Python-2.7

* Wed Apr 28 2010 Mykola Grechukh <gns@altlinux.ru> 0.21.1-alt1
- first build to sisyphus
