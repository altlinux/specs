Name: googlecl
Version: 0.9.13
Release: alt1.1
Summary: GoogleCL brings Google services to the command line

Group: Development/Python
License: Apache License 2.0
Url: http://code.google.com/p/googlecl/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-dev

%description
GoogleCL brings Google services to the command line.
We currently support the following Google services:
Blogger
$ google blogger post --title "foo" "command line posting"
Calendar
$ google calendar add "Lunch with Jim at noon tomorrow"
Contacts
$ google contacts list name,email > contacts.csv
Docs
$ google docs edit --title "Shopping list"
Picasa
$ google picasa create --album "Cat Photos" ~/photos/cats/*.jpg
Youtube
$ google youtube post --category Education killer_robots.avi

%prep
%setup -q

%build
%python_build

%install
%__python setup.py install --skip-build --root %buildroot
mkdir -p %buildroot/%_man1dir/
install -p man/google.1 %buildroot/%_man1dir/

%files
%doc README.config README.txt
%_bindir/google
%python_sitelibdir/*
%_man1dir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.13-alt1.1
- Rebuild with Python-2.7

* Wed Apr 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.13-alt1
- 0.9.13 (svn r548)

* Thu Jan 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.12-alt1
- 0.9.11 (svn r537)

* Mon Oct 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.11-alt1
- 0.9.11 (svn r457)

* Fri Sep 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.10-alt1
- 0.9.10 (svn r401)

* Thu Jul 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1
- 0.9.9 (svn r360)

* Wed Jun 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt1
- 0.9.8 (svn r316)

* Sun Jun 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7-alt1
- 0.9.7 (svn r261)

* Fri Jun 18 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt1
- initial

