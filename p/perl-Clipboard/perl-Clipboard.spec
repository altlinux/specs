%define _unpackaged_files_terminate_build 1
BuildRequires: perl-podlators
%define module Clipboard
%define m_distro Clipboard
%define m_name Clipboard
%define m_author_id unknown
%define _enable_test 1

Name: perl-Clipboard
Version: 0.21
Release: alt1

Summary: Cliboard - Copy and Paste with any OS

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/S/SH/SHLOMIF/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Tue Feb 08 2011 (-bb)
BuildRequires: perl-Module-Install xclip

%description
None.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %name = %EVR

%description scripts
scripts for %name


%prep
%setup -q -n %{module}-%{version}
rm -f lib/Clipboard/MacPasteboard.pm
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%doc Changes README
%perl_vendor_privlib/Clipboard/*
%perl_vendor_privlib/Clipboard.pm

%files scripts
%_bindir/*
%_man1dir/*


%changelog
* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sun Feb 03 2019 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Thu Jan 31 2019 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Wed Jan 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- fixed unpackaged files

* Tue Feb 08 2011 Denis Smirnov <mithraen@altlinux.ru> 0.13-alt1
- 0.13

* Tue Oct 27 2009 Denis Smirnov <mithraen@altlinux.ru> 0.09-alt1
- initial build for ALT Linux Sisyphus

