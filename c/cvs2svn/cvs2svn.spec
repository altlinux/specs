%def_without M24

%def_without check

%if_with M24
%define _release alt0.M24.1
%else
%define _release alt1
%endif

Name: cvs2svn
Version: 2.3.0
Release: %_release.1.1

Packager: Ilya Mashkin <oddity@altlinux.ru>

Summary: Convert CVS repositories to Subversion repositories
Summary(ru_RU.KOI8-R): Перенос репозитариев из CVS в Subversion
# see COPYING
License: Apache-style
Group: Development/Other
Url: http://cvs2svn.tigris.org/

Source0: http://cvs2svn.tigris.org/files/documents/1462/25036/%name-%version.tar.gz

BuildArch: noarch

BuildPreReq: python-devel = %__python_version
BuildRequires: python-modules-encodings

%if_enabled check
BuildRequires: subversion subversion-server-common
BuildRequires: cvs rcs python-module-egenix-mx-base python-modules-bsddb
%endif


%description
cvs2svn aims to allows you to convert a CVS repository to a Subversion one.
This work for complete conversion, not a synchronisation for each commit.

%description -l ru_RU.KOI8-R
cvs2svn предназначен для конвертирования репозитариев из CVS в Subversion.
Подразумевается окончательный перенос, а не синхронизация обновлений.

%prep
%setup -q

%build
%__python setup.py build

%if_enabled check
# is needed for testing
export LANG=en_US.UTF-8
%__python run-tests.py
%endif

%install
%__python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc BUGS CHANGES COMMITTERS COPYING HACKING README www

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.1
- Rebuilt with python 2.6

* Wed Oct 07 2009 Ilya Mashkin <oddity@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Jul 23 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 1.3.1-alt1.1
- Rebuilt with python-2.5.

* Tue Jun 20 2006 Grigory Batalov <bga@altlinux.ru> 1.3.1-alt1
- 1.3.1
- Enable tests.
- Clean build requirements up.

* Tue Sep 27 2005 Grigory Batalov <bga@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Mon Mar 21 2005 Grigory Batalov <bga@altlinux.ru> 1.2.1-alt1
- Rebuild for ALT Linux

* Thu Feb 03 2005 Michael Scherer <misc@mandrake.org> 1.1.0-1mdk
- New release 1.1.0

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.0.0-2mdk
- Rebuild for new python

* Thu Sep 02 2004 Michael Scherer <misc@mandrake.org> 1.0.0-1mdk
- 1.0.0, no longer svn and rpmbuildupdate aware

* Tue Aug 17 2004 Michael Scherer <misc@mandrake.org> 0.rev1326-1mdk
- New release 0.rev1326

* Thu Jul 29 2004 Michael Scherer <misc@mandrake.org> 0.rev1173-1mdk
- New release 0.rev1173

* Sat Jun 05 2004 Michael Scherer <misc@mandrake.org> 0.rev957-2mdk
- add python as BuildRequires ( python-base is not enough )

* Sun May 23 2004 Michael Scherer <misc@mandrake.org> 0.rev957-1mdk
- New release 0.rev957

* Wed Apr 28 2004 Michael Scherer <misc@mandrake.org> 0.rev923-1mdk
- New release 0.rev923

* Fri Apr  9 2004 Michael Scherer <misc@mandrake.org> 0.rev914-2mdk
- Update the spec file to be auto updateable with svn://

* Thu Apr 08 2004 Michael Scherer <misc@mandrake.org> 0.rev914-1mdk
- First package, based on work from David Summers <david@summersoft.fay.ar.us>
