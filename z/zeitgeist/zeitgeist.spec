%define major 0.9
%define _noarchpkgconfigdir %_datadir/pkgconfig

Name: zeitgeist
Version: %major.0.1
Release: alt1

Summary: Framework providing Desktop activity awareness

Group: Office
License: LGPLv3+ and LGPLv3
# zeitgeist/loggers/iso_strptime.py is LGPLv3 and the rest LGPLv3+
Url: https://launchpad.net/zeitgeist

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://launchpad.net/%name/%major/%version/+download/%name-%version.tar

Patch: %name-link.patch

# can't do buildreq correctly
BuildRequires: python-devel python-module-rdflib
BuildRequires: raptor
BuildRequires: gettext, perl-XML-Parser, intltool
BuildRequires: gcc-c++ glib2-devel libsqlite3-devel libgio-devel libdbus-devel libxapian-devel
# for autoreconf
BuildRequires: gettext-tools

%description
Zeitgeist is a service which logs the users's activities and events (files
opened, websites visites, conversations hold with other people, etc.) and makes
relevant information available to other applications.

Note that this package only contains the daemon, which you can use
together with several different user interfaces.

%prep
%setup
%patch -p2

%build
#autoreconf
%configure
%make_build

%install
%makeinstall_std
# pkgconfigdir=%_noarchpkgconfigdir
rm -rf %buildroot%_prefix/doc/

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/zeitgeist-daemon
%_datadir/%name/
#_pkgconfigdir/zeitgeist-daemon.pc
%_libexecdir/%name-fts
%python_sitelibdir_noarch/zeitgeist/
%_datadir/dbus-1/services/org.gnome.zeitgeist.service
%_datadir/dbus-1/services/org.gnome.zeitgeist.fts.service
%_man1dir/zeitgeist-*.*

%changelog
* Sun Jun 10 2012 Vitaly Lipatov <lav@altlinux.ru> 0.9.0.1-alt1
- new version 0.9.0.1 (with rpmrb script)

* Tue Jan 24 2012 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.2-alt1.1
- Rebuild with Python-2.7

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Aug 06 2010 Deji Akingunola <dakingun@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 15 2010 Deji Akingunola <dakingun@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3.1-1
- Update to 0.3.3.1 to fix datasource_registry bug (BZ #586238)

* Wed Apr 21 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.3-1
- Update to 0.3.3

* Wed Jan 20 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Thu Jan 14 2010 Deji Akingunola <dakingun@gmail.com> - 0.3.1-1
- Add missing requires (Package reviews)
- Update license tag (Package reviews)
- Update to latest release

* Tue Dec 01 2009 Deji Akingunola <dakingun@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Wed Nov 04 2009 Deji Akingunola <dakingun@gmail.com> - 0.2.1-1
- Initial Fedora packaging
