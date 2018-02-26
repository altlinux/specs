%define dist Devel-ptkdb
Name: perl-%dist
Version: 1.1092
Release: alt1.1

Summary: Perl debugger using a Tk GUI
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

# Automatically added by buildreq on Sun Oct 18 2009
BuildRequires: perl-Tk perl-devel

%description
ptkdb is a debugger for perl that uses perl-Tk for a user interface.
It features pushbutton controls for run, step-in, step-out, return,
controls for breakpoints, expression evaluation and package browsing.  

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Devel*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1092-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 18 2009 Grigory Batalov <bga@altlinux.ru> 1.1092-alt1
- New upstream release.

* Mon Aug 02 2004 Alexey Tourbin <at@altlinux.ru> 1.1091-alt1
- initial revision
- no-cpan.patch: do not try to install Tk with CPAN
