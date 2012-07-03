%define dist Curses-UI
Name: perl-%dist
Version: 0.9609
Release: alt1

Summary: A curses based OO user interface framework
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Curses perl-Module-Install perl-Term-ReadKey perl-Test-Pod

%description
Curses::UI is an object-oriented user interface framework for Perl.
It contains basic widgets (like buttons and text areas), more
"advanced" widgets (like UI tabs and a fully-functional basic text
editor), and some higher-level classes like pre-fab error dialogues.

%prep
%setup -q -n %dist-%version

%build
export COLUMNS=80 LINES=25
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
%dir	%perl_vendor_privlib/Curses
%dir	%perl_vendor_privlib/Curses/UI
	%perl_vendor_privlib/Curses/UI.pm
	%perl_vendor_privlib/Curses/UI/*.pm
%doc	%perl_vendor_privlib/Curses/UI/*.pod
	%perl_vendor_privlib/Curses/UI/Dialog
	%perl_vendor_privlib/Curses/UI/Language

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.9609-alt1
- 0.9607 -> 0.9609
- rebuilt as plain src.rpm

* Wed Jul 22 2009 Alexey Tourbin <at@altlinux.ru> 0.96.07-alt1
- 0.9602 -> 0.9607

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 0.96.02-alt1
- 0.95 -> 0.9602

* Tue Dec 28 2004 Alexey Tourbin <at@altlinux.ru> 0.95-alt1
- initial revision
