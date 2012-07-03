%define rname	TabMixPlus
%define cid 	\{dc572301-7619-498c-a57d-39143191b318\}
%define ciddir  %firefox_noarch_extensionsdir/%cid

Summary:	Tab Mix Plus extensions for Firefox
Name:		firefox-TabMixPlus
Version:	0.4.0.1
Release:	alt1
Source0:	%rname-%version.xpi
License:	GPL
Group:		Networking/WWW
URL:		http://tmp.garyr.net

BuildArch:      noarch
BuildRequires(pre):     rpm-build-firefox
BuildRequires:  unzip

Conflicts: firefox-tabbrowser-extensions 

%description 	
Tab browsing with an added boost.

%prep
%setup -c

%install
mkdir -p %buildroot/%ciddir
cp -r * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
    [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi
	
%files
%ciddir

%changelog
* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.0.1-alt1
- 0.4.0.1

* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 0.3.8.6-alt3
- Rebuilt with firefox 9.0.1

* Thu Oct 13 2011 Alexey Gladkov <legion@altlinux.ru> 0.3.8.6-alt2
- Rebuilt with firefox 7.0.1

* Tue Aug 02 2011 Alexey Gladkov <legion@altlinux.ru> 0.3.8.6-alt1
- 0.3.8.6

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.8.5-alt1
- 0.3.8.5

* Tue Sep 28 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3.8.4-alt1
- 0.3.8.4

* Thu Oct 22 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.8.2-alt1
- 0.3.8.2

* Tue Aug 18 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.8.1-alt1
- 0.3.8.1

* Fri Jun 05 2009 Alexey Gladkov <legion@altlinux.ru> 0.3.7.3-alt2
- Rebuild for Firefox 3.5

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.7.3-alt1
- 0.3.7.3

* Fri Oct 17 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.7.2-alt1
- 0.3.7.2

* Mon Jul 28 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.7-alt0.pre080728
- build devel version 0.3.7pre.080728

* Thu Jul 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.3.6.1-alt1.080416
- build devel version 0.3.6.1.080416

* Wed Sep 19 2007 Alexey Shabalin <shaba@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.3.5.2-alt1
- 0.3.5.2

* Mon Nov 27 2006 Alexey Shabalin <shaba@altlinux.ru> 0.3.5-alt1
- 0.3.5
- set noarch
- remove obsoleted macros

* Mon Sep 25 2006 Alexey Shabalin <shaba@altlinux.ru> 0.3.0.5-alt2.1
- rebuild with firefox 1.5.0.7

* Thu Aug 24 2006 Alexey Shabalin <shaba@altlinux.ru> 0.3.0.5-alt2
- rebuild with firefox 1.5.0.6

* Thu Jun 15 2006 Alexey Gladkov <legion@altlinux.ru> 0.3.0.5-alt1.1.1
- NMU: rebuild with firefox 1.5.0.4

* Mon May 15 2006 Alexey Gladkov <legion@altlinux.ru> 0.3.0.5-alt1.1
- NMU: rebuild with firefox 1.5.0.3

* Tue Mar 14 2006 Alexey Shabalin <shaba@altlinux.ru> 0.3.0.5-alt1
- update 0.3.0.5
- change URL home page

* Thu Mar 02 2006 Alexey Shabalin <shaba@altlinux.ru> 0.3.0.4-alt1
- update 0.3.0.4

* Mon Feb 20 2006 Alexey Gladkov <legion@altlinux.ru> 0.3.0.2-alt2
- NMU: rebuild with firefox 1.5.0.1

* Mon Feb 06 2006 Alexey Shabalin <shaba@altlinux.ru> 0.3.0.2-alt1
- update 0.3.0.2
- with russian locale

* Thu Jan 19 2006 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- update 0.3
- no russian locale

* Mon Dec 19 2005 Alexey Gladkov <legion@altlinux.ru> 0.2.5.2-alt2.1
- rebuild with firefox-1.5
- spec changes:
  * BuildRequires fix;
  * ghost file added;
  * new macros was used to fix multiarch problem.

* Thu Nov 24 2005 Alexey Shabalin <shaba@altlinux.ru> 0.2.5.2-alt2
- fix cid

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.2.5.2-alt1
- update 0.2.5.2

* Tue Nov 15 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.3.1-alt1.1
- rebuild with firefox-1.0.7 .

* Thu Aug 18 2005 Alexey Shabalin <shaba@altlinux.ru> 0.2.3.1-alt1
- first build for ALT Linux.
