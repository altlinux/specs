%define name	podracer
%define version	1.4
%define release %mkrel 4

Name: podracer
Summary: A versatile podcast fetcher
Version: 1.4
Release: alt1

Source: http://prdownloads.sourceforge.net/podracer/%name-%version.tar.bz2
Patch0: podracer-1.4-alt-doc-fix-docdir.patch
Url: http://podracer.sourceforge.net/
License: BSD
Group: Networking/News
BuildArch: noarch

%description
Podracer is a podcast aggregator that gets the enclosures from your list of
podcast subscriptions and stores them in the location you specify. It
supports BitTorrent, HTTP, and FTP downloads, and runs best as a cron job to
automatically retrieve podcasts throughout the day.

%prep
%setup
%patch0 -p2

%build
#gcc $RPM_BUILD_OPTS timeout.c -o timeout
#chmod 755 timeout

%install
mkdir -p %buildroot/%_bindir
#cp timeout %buildroot/%_bindir
mkdir -p %buildroot/%_mandir/man1
#cp timeout.1.gz %buildroot/%_mandir/man1
cp %name %buildroot/%_bindir
mkdir -p %buildroot/%_sysconfdir
cp %name.conf %buildroot/%_sysconfdir
cp podracer.1.gz %buildroot/%_mandir/man1

%files
%doc CREDITS LICENSE README ChangeLog sample.subscriptions
%_bindir/%name
#%_bindir/timeout
%_mandir/man1/*
%config(noreplace) %_sysconfdir/%name.conf

%changelog
* Tue Aug 30 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4-alt1
- Initial build

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-4mdv2009.0
+ Revision: 259133
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4-3mdv2009.0
+ Revision: 247061
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.4-1mdv2008.1
+ Revision: 125490
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import podracer

* Wed Feb 22 2006 Austin Acton <austin@mandriva.org> 1.4-1mdk
- New release 1.4

* Sun Oct 9 2005 Austin Acton <austin@mandriva.org> 1.3-1mdk
- 1.3
- source URL

* Fri Aug 26 2005 Austin Acton <austin@mandriva.org> 1.2.2-1mdk
- initial package
