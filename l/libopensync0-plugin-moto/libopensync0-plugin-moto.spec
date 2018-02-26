%define orig_name libopensync-plugin-moto
Name: libopensync0-plugin-moto
Version: 0.22
Release: alt2.1.1

Summary: Motorola Synchronization Plug-In for OpenSync
License: GPL v2 or later
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %orig_name-%version.tar.bz2
Patch0:         libopensync-plugin-moto-mototool_fix.diff
Patch1:         libopensync-plugin-moto-fix-alarm-trigger.diff
Patch2:         libopensync-plugin-moto-fix-mototool-segfault.diff
Patch3:         libopensync-plugin-moto-fix-path-detection.diff

Requires: libopensync0 = %version
Requires: python-module-opensync0 python-module-dateutil python-module-pybluez libopensync0-plugin-python
# Conflicts: %orig_name

%description
This plug-in allows applications using OpenSync to synchronize to and
from Motorola cellphones which doesn't support SyncML via Obex (e.g.
Razr V3(i), L7, V635).

%prep
%setup -q -n %orig_name-%version
%patch0
%patch1
%patch2
%patch3

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/opensync/python-plugins/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/opensync/defaults/
cp motosync.py $RPM_BUILD_ROOT/%{_libdir}/opensync/python-plugins/ 
cp moto-sync $RPM_BUILD_ROOT/%{_datadir}/opensync/defaults/
cp mototool $RPM_BUILD_ROOT/%{_bindir}/

%files
%doc AUTHORS COPYING README
%{_bindir}/mototool
%{_libdir}/opensync/python-plugins/motosync.py
%{_datadir}/opensync/defaults/moto-sync

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.22-alt2.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt2.1
- Rebuilt with python 2.6

* Fri Oct 17 2008 Andriy Stepanov <stanv@altlinux.ru> 0.22-alt2
- Stable version.
