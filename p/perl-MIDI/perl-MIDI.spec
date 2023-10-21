%define _unpackaged_files_terminate_build 1
%define module MIDI
%define origname %module-Perl

Name: perl-%module
Version: 0.84
Release: alt1

Summary: %{module} module for perl
License: GPL or Artistic
Group: Development/Perl

Source0: http://www.cpan.org/authors/id/C/CO/CONKLIN/%{module}-Perl-%{version}.tar.gz
BuildArch: noarch

Packager: Afanasov Dmitry <ender@altlinux.org>

# Automatically added by buildreq on Tue Aug 19 2003
BuildRequires: perl-devel

%description
%{module} module for perl

# if you're very sensitive to MIDI file size then
# build with --define 'comment ""'	// mike

%prep
%setup -q -n %{module}-Perl-%{version}
%ifdef comment
%__subst 's/\"\$0 at \" \. scalar(localtime)/"%comment"/' lib/MIDI/Simple.pm
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog
%perl_vendor_privlib/MIDI*

%changelog
* Sat Oct 21 2023 Igor Vlasenko <viy@altlinux.org> 0.84-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 05 2008 Afanasov Dmitry <ender@altlinux.org> 0.81-alt1
- 0.81 release

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.8-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Aug 19 2003 Michael Shigorin <mike@altlinux.ru> 0.8-alt1
- built for ALT Linux

