Name: kodos
Version: 2.4.9
Release: alt1.1.1
Summary: Visual regular expression editor

Group: Editors
# No version specified.
License: GPL+
Url: http://kodos.sourceforge.net/
Source0: http://download.sourceforge.net/kodos/kodos-%version.tar.gz
Source1: kodos.desktop

Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildArch: noarch
BuildRequires: python-devel, desktop-file-utils

Requires: python-module-PyQt

%description
Kodos is a visual regular expression editor and debugger written in Python.

%prep
%setup -q

%build
%python_build

%install
%python_install -O1
rm -f $RPM_BUILD_ROOT%python_sitelibdir/kodos/py2exe*
chmod 0755 $RPM_BUILD_ROOT%python_sitelibdir/kodos/kodos.py
mv $RPM_BUILD_ROOT%_bindir/kodos.py $RPM_BUILD_ROOT%_bindir/kodos
mkdir -p -m 0755 \
    $RPM_BUILD_ROOT%_datadir/pixmaps \
    $RPM_BUILD_ROOT%_datadir/applications
install -m 0644 images/kodos_icon.png $RPM_BUILD_ROOT%_datadir/pixmaps/
desktop-file-install \
    --vendor fedora \
    --dir $RPM_BUILD_ROOT%_datadir/applications \
    %SOURCE1

%files
%doc CHANGELOG.txt LICENSE.txt
%_bindir/*
%_datadir/kodos
%python_sitelibdir/*
%_datadir/applications/*
%_datadir/pixmaps/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.9-alt1.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.9-alt1.1
- Rebuilt with python 2.6

* Tue Nov 18 2008 Ilya Mashkin <oddity@altlinux.ru> 2.4.9-alt1
- Initial Build for ALT Linux

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.9-5
- fix license tag

* Sat Jun 16 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4.9-4
- Remove leftover useless Requires.

* Sun Jun 10 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4.9-3
- Don't add X-Fedora to desktop-file-install
- Don't run update-desktop-database, since there's no MimeType to worry about

* Sun Mar 11 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4.9-2
- BR desktop-file-utils
- Set permissions correctly to appease rpmlint

* Mon Jan 29 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.4.9-1
- Initial packaging for Extras.
