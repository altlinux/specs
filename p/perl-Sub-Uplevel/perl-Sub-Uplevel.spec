%define dist Sub-Uplevel
Name: perl-%dist
Version: 0.22
Release: alt1
Epoch: 1

Summary: Run a function in a higher stack frame
License: GPL or Artistic
Group: Development/Perl

URL: http://www.cpan.org
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: perl-Module-Build

%description
Like Tcl's uplevel() function, but not quite so dangerous.  The idea
is just to fool caller().  All the really naughty bits of Tcl's uplevel()
are avoided.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
%dir	%perl_vendor_privlib/Sub
	%perl_vendor_privlib/Sub/Uplevel.pm
%doc	%perl_vendor_privlib/Sub/Uplevel.pod

%changelog
* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1:0.22-alt1
- 0.1901 -> 0.22

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1901-alt2
- fix directory ownership violation

* Thu Jun 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1901-alt1
- new version 0.1901 (with rpmrb script) - fix bug #15976
- update buildreq

* Tue Jun 07 2005 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- first build for ALT Linux Sisyphus
