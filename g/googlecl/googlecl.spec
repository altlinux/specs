Name: googlecl
Version: 0.9.13
Release: alt2

Summary: GoogleCL brings Google services to the command line
License: Apache License 2.0
Group: Development/Python3
Url: http://code.google.com/p/googlecl/
BuildArch: noarch

Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires %name


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

%package -n python3-module-%name
Summary: GoogleCL brings Google services to the command line
Group: Development/Python3

%description -n python3-module-%name
GoogleCL brings Google services to the command line.

This package contains python3 module for %name.

%prep
%setup -q
%patch0 -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%__python3 setup.py install --skip-build --root %buildroot
mkdir -p %buildroot/%_man1dir/
install -p man/google.1 %buildroot/%_man1dir/

%files
%doc README.config README.txt
%_bindir/google
%_man1dir/*

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.13-alt2
- porting on python3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.13-alt1.1.qa1
- NMU: applied repocop patch

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

