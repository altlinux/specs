Name: ntfsdoc
Version: 0.5
Release: alt2
Summary: NTFS filesystem documentation
License: FDL
Group: Books/Computer books
URL: http://linux-ntfs.sf.net/
Packager: Andrey Rahmatullin <wrar@altlinux.ru>
BuildArch: noarch

Source0: %name-%version.tar.bz2
# http://linux-ntfs.sourceforge.net/info/ntfs.html
Source1: ntfsfaq.tar.bz2
Patch0: %name-0.5-alt-faq-link.patch

%description
The Linux-NTFS project (http://linux-ntfs.sf.net/) aims to bring full support
for the NTFS filesystem to the Linux operating system. Linux-NTFS currently
consists of a static library and utilities. 

This package contains linux NTFS project documentation.

%prep
%setup -q -n %name-%version
%setup -T -D -a 1
%__mv *.png *.css style/
%__mv ntfs*.html help/
%patch0 -p1

%install
%__mkdir_p %buildroot%_docdir/%name-%version
%__cp -ar * %buildroot%_docdir/%name-%version/

%files
%dir %_docdir/%name-%version/
%doc %_docdir/%name-%version/*

%changelog
* Tue Apr 19 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.5-alt2
- add Russian NTFS FAQ
- add FAQs in other languages

* Wed Nov 17 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.5-alt1
- 0.5
- change Packager:
- fix License:
- add NTFS FAQ

* Fri Jun 20 2004 Albert R. Valiev <darkstar at altlinux.ru> 0.4-alt1
- Initial build

