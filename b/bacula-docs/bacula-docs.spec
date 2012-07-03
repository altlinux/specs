Name: bacula-docs
Version: 5.2.5
Release: alt1

License: AGPLv3
Summary: Network based backup program (documentation)
Group: Archiving/Backup
Url: http://www.bacula.org/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Source: docs-%version.tar
Source1: version.h

BuildArch: noarch
BuildRequires: latex2html tetex-dvips

%description
Bacula documentation

%prep
%setup -b 0 -n docs-%version
mkdir src
cp -a %SOURCE1 src

%configure --with-bacula=`pwd`

%build

make

%install

mkdir -p %buildroot%_datadir/%name
cp -a manuals/en/console/console %buildroot%_datadir/%name
cp -a manuals/en/console/console.pdf %buildroot%_datadir/%name
cp -a manuals/en/developers/developers %buildroot%_datadir/%name
cp -a manuals/en/developers/developers.pdf %buildroot%_datadir/%name
cp -a manuals/en/main/main %buildroot%_datadir/%name
cp -a manuals/en/main/main.pdf %buildroot%_datadir/%name
cp -a manuals/en/misc/misc %buildroot%_datadir/%name
cp -a manuals/en/misc/misc.pdf %buildroot%_datadir/%name
cp -a manuals/en/problems/problems %buildroot%_datadir/%name
cp -a manuals/en/problems/problems.pdf %buildroot%_datadir/%name
cp -a manuals/en/utility/utility %buildroot%_datadir/%name
cp -a manuals/en/utility/utility.pdf %buildroot%_datadir/%name

%files
%dir %attr(0755,root,root) %_datadir/%name
%_datadir/%name/*

%changelog
* Sat Jan 28 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.5-alt1
- 5.2.5

* Tue Jan 24 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.4-alt1
- 5.2.4

* Tue Dec 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.3-alt1
- 5.2.3

* Wed Dec 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.2.2-alt1
- 5.2.2

* Thu Aug 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.3-alt1
- 5.0.3
- mike@: fix docs-docs

* Thu May 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.2-alt1
- 5.0.2

* Sun Feb 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.1-alt1
- 5.0.1

* Mon Jan 25 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.0-alt1
- 5.0.0

* Tue Oct 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Tue Jul 21 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Wed Jun 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt2
- rebuild with bacula-3.0.1-alt2

* Thu Apr 30 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.1-alt1
- initial standalone split from bacula package
- 3.0.1
