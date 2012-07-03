%define dist PostScript-Simple
Name: perl-%dist
Version: 0.07
Release: alt1.1

Summary: Produce PostScript files from Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MC/MCNEWTON/PostScript-Simple-0.07.tar.gz
Packager: Eugene Ostapets <eostapets@altlinux.ru>

BuildArch: noarch

# Automatically added by buildreq on Tue Jul 26 2005
BuildRequires: perl-devel

%description
PostScript::Simple allows you to have a simple method of writing PostScript
files from Perl. It has graphics primitives that allow lines, curves, circles,
polygons and boxes to be drawn. Text can be added to the page using standard
PostScript fonts.


%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/PostScript*


%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Tue Jul 26 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.06-alt1
- initial revision

