Name:		squidclam
Version:	0.23
Release:	alt1
Summary:	Redirect program for squid antivirus scanning
Group:		System/Servers
License:	GPL
#http://squidclam.sourceforge.net/
URL:		http://sourceforge.net/projects/squidclam
Packager: 	Alexey Shentzev <ashen@altlinux.ru>
Source0:	%name-%version.tar.gz
BuildRequires:	libcurl-devel libclamav-devel
Requires:	squid curl clamav

Patch0: squidclam-altlinux.patch


%description
squidclam is going to be a program to scan files served to win32
machines by a squid proxy. It hast du be fast and small to get
this job done. Also it has to be secure to not weaken the server
system.
At the moment squidclam is pretty small, scans files for viruses 
and is doing it's job pretty well for me.

%prep
%setup -q
%patch0 -p1

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT/
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/
mkdir -p $RPM_BUILD_ROOT%_sbindir/
install sample.conf $RPM_BUILD_ROOT%_sysconfdir/squidclam.conf
install src/squidclam $RPM_BUILD_ROOT%_sbindir/
mkdir -p $RPM_BUILD_ROOT%_docdir/%name
install antivir.php $RPM_BUILD_ROOT%_docdir/%name/

%clean
rm -rf $RPM_BUILD_ROOT

%post

%preun

%postun

%files
%defattr(0644,root,root,0755)
%doc Changelog README TODO
%doc antivir.php
%config(noreplace) %_sysconfdir/squidclam.conf
%attr(0755,root,root) %_sbindir/squidclam

%changelog
* Fri Jan 11 2008 Alexey Shentzev <ashen@altlinux.ru> 0.23-alt1
- first build for ALT Linux

