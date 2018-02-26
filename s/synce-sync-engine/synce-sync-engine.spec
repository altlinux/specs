BuildRequires(pre): rpm-build-python
%define orig_name sync-engine
%define python_noarch %_libexecdir/python%__python_version/site-packages

Name: synce-%orig_name
Version: 0.12
Release: alt1.1.1
Summary: Synce sync engine
License: GPLv2
Group: Communications
Packager: Mobile Development Team <mobile@packages.altlinux.org>
Url: http://www.synce.org
Source0: %orig_name-%version.tar.gz
Source1: synce-config.xml
Patch: sync-engine-defaultconf.patch

BuildRequires: python-module-Pyrex python-module-vobject

%description
SynCE sync engine

%package -n libopensync-plugin-synce
Group: Communications
Summary: Synce plugin for libopensync
Requires: synce-sync-engine = %version-%release
Requires: libopensync-plugin-python >= 0.35
Requires: libopensync-plugin-vformat >= 0.35
Serial: 1

%description -n libopensync-plugin-synce
This plugin allows applications using OpenSync to synchronise to and from
Windows CE and PockectPC based devices.
This plugin is functional, but NOT STABLE.


%prep
%setup -q -n %orig_name-%version
#%patch -p0

# change parametrs in default config
#sed -i -e 's,\(xterm -e msynctool --sync wm5sync\),xterm -e msynctool --sync synce,g' config/config.xml
sed -i -e 's,\(<OpensyncXMLFormat>OS20</OpensyncXMLFormat>\),<OpensyncXMLFormat>OS30</OpensyncXMLFormat>,g' config/syncengine.conf.xml

# Change python package path to normal on 'tools' folder
sed -i -e "#sys.path.insert(0,#d" tools/*.py

%build
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --optimize=2

mkdir -p %buildroot%_datadir/opensync-1.0/defaults
rm -fr %buildroot%python_sitelibdir/plugins
  
install -D plugins/synce-opensync-plugin-3x.py %buildroot%_libdir/opensync-1.0/python-plugins/synce-opensync-plugin-3x.py
install -D config/org.synce.SyncEngine.service %buildroot%_datadir/dbus-1/services/org.synce.SyncEngine.service
install -D config/syncengine.conf.xml %buildroot%_sysconfdir/syncengine.conf.xml

  
# make defaults file
cat > %buildroot%_datadir/opensync-1.0/defaults/synce-opensync-plugin << 'EOF'
<config>
 	<contact></contact>
	<todos></todos>
	<calendar></calendar>
	<file>/My Documents/</file>
</config>
EOF

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_noarch/* %buildroot%python_sitelibdir/
%endif

%files
%doc CHANGELOG
%config(noreplace) %_sysconfdir/syncengine.conf.xml
%_bindir/*.py
%_bindir/sync-engine
%python_sitelibdir/SyncEngine/
%python_sitelibdir/*.egg-info/
#%_datadir/%name/*
%_datadir/dbus-1/services/org.synce.SyncEngine.service

%files -n libopensync-plugin-synce
%doc plugins/synce-opensync-plugin-3x.README
%_libdir/opensync-1.0/python-plugins/synce-opensync-plugin-3x.py
%_datadir/opensync-1.0/defaults/synce-opensync-plugin
%exclude %_libdir/opensync-1.0/python-plugins/*pyc
%exclude %_libdir/opensync-1.0/python-plugins/*pyo
%exclude %_datadir/doc/sync-engine

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt1.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1.1
- Rebuilt with python 2.6

* Mon Oct 13 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12

* Sun Mar 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.11-alt7
- cleanup spec
- rebuild with python-2.5
- change OpensyncXMLFormat to OS30 for OpenSync 0.3x XML schemas in synce-config.xml
- add description for libopensync-plugin-synce
- change License
- add Packager
- build for Sisyphus

* Tue Feb 05 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt6
- remove noarch
- patch config.py to use default config.xml
- pack default config.xml

* Tue Feb 05 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt5
- add serial to fix update of libopensync-plugin-synce

* Mon Feb 04 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt4
- fix default path to opensync-1.0 (thanks to maverik@)

* Thu Jan 31 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt3
- build experimental libopensync-plugin-synce (opensync >= 0.30).
  See synce-opensync-plugin-3x.README

* Wed Jan 30 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt2
- fix requirements

* Tue Jan 29 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt1
- 0.11

* Sat May 26 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt1
- built for ALT Linux

