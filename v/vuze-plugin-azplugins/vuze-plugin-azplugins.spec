# vim: set ft=spec: -*- rpm-spec -*-

%define plugin_id azplugins
%define plugin_version 2.1.6

Name: vuze-plugin-%plugin_id
Version: %plugin_version
Release: alt1

Summary: Vuze Core Plugins
Group: Networking/File transfer
License: GPL
Url: http://azureus.sourceforge.net/plugin_details.php?plugin=%plugin_id

BuildArch: noarch

Packager: Sir Raorn <raorn@altlinux.ru>

Obsoletes: azureus-plugin-%plugin_id
Provides: azureus-plugin-%plugin_id = %version-%release
PreReq: vuze

Source: %plugin_id-%version.tar
Patch: %plugin_id-%version-%release.patch

# Automatically added by buildreq on Tue Jan 29 2008 (-bi)
BuildRequires: ant jpackage-1.6-compat vuze eclipse-swt

BuildRequires: /proc

%description
This contains the Tracker Web Templates and IRC Client plugins.

Tracker web pages can be customised by extracting them from the
plugin JAR file and placing them in a directory called "web" under
the Azureus user-data directory.

When extracting them ensure that the prefix directory hierarchy of
"org/gudy/azureus2/ui/tracker/templates" is *removed* leaving, for
example, "index.tmpl" in the "web" directory.

%prep
%setup -n %plugin_id-%version
%patch -p1

%build
ant -lib %_datadir/azureus:%_javadir:%_libdir/java -Dsource.dir=. -Dplugin.version=%plugin_version makejar

%install
mkdir -p %buildroot%_datadir/azureus/plugins/%plugin_id
install -p -m644 *.jar %buildroot%_datadir/azureus/plugins/%plugin_id/

%files
%_datadir/azureus/plugins/%plugin_id

%changelog
* Sun Jan 11 2009 Sir Raorn <raorn@altlinux.ru> 2.1.6-alt1
- [2.1.6]
- Renamed to vuze-plugin-azplugins

* Tue Jan 29 2008 Sir Raorn <raorn@altlinux.ru> 2.1.4-alt1
- Initial build

