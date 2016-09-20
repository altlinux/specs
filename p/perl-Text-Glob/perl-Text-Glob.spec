%define _unpackaged_files_terminate_build 1
%define dist Text-Glob
Name: perl-%dist
Version: 0.10
Release: alt1

Summary: match globbing patterns against text
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RC/RCLAMP/Text-Glob-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 24 2011
BuildRequires: perl-Module-Build

%description
Text::Glob implements glob(3) style matching that can be used to match
against text, rather than fetching names from a filesystem.  If you
want to do full file globbing use the File::Glob module instead.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Text

%changelog
* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- 0.08 -> 0.09

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- 0.06 -> 0.08

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.06-alt1
- first build for ALT Linux Sisyphus
