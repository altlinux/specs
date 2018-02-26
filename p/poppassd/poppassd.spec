%define		__pamdir	%_sysconfdir/pam.d/
%define		__xinetdir	%_sysconfdir/xinetd.d/

Summary:	Eudora Poppassd modified to support PAM
Name:		poppassd
Version:	1.8.5
Release:	alt1
License:	GPL
Group:		System/Servers
Source0:	http://echelon.pl/pubs/%{name}-%{version}.tar.gz
Source1:	%{name}.pam
Source2:	%{name}.xinetd
URL:		http://echelon.pl/pubs/poppassd.html

# Automatically added by buildreq on Wed Feb 07 2007
BuildRequires: libpam-devel

PreReq:		xinetd

%description
Poppassd-ceti is a Qualcomm password changer daemon with PAM support
and several other improvements. This program is intended to be a
secure way to change system passwords via the Web. Methods that
involve calling SUID programs directly from the Web are especially
avoided. Poppassd strictly isolates the Web interface from actual
password manipulations. The program contains no known security bugs
that could be reported since it was released several years ago. This
version uses PAM, which means you can do anything PAM can. Currently,
there are PAM modules for almost all known authentication methods
available.

%prep
%setup -q

%build
%__make

%install
%__mkdir_p %buildroot/{%_sbindir,%_sysconfdir}
%__mkdir_p %buildroot/{%__pamdir,%__xinetdir}
%__install %name %buildroot/%_sbindir/
%__install -m 640 %SOURCE1 %buildroot/%__pamdir/%name
%__install -m 640 %SOURCE2 %buildroot/%__xinetdir/%name

%files
%doc README COPYING
%attr(2711,root,shadow) %_sbindir/%name
%attr(640,root,shadow) %config(noreplace) %__pamdir/%name
%attr(640,root,root) %config(noreplace) %__xinetdir/%name

%changelog
* Wed Feb 07 2007 Serhii Hlodin <hlodin@altlinux.ru> 1.8.5-alt1
- Initial build 
