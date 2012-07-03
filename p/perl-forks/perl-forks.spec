%define dist forks
Name: perl-%dist
Version: 0.34
Release: alt2

Summary: Drop-in replacement for Perl threads using fork()
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Acme-Damn perl-Attribute-Handlers perl-Devel-Symdump perl-List-MoreUtils perl-Sys-SigAction perl-devel perl-threads

%description
The forks.pm module is a drop-in replacement for threads.pm.  It has the
same syntax as the threads.pm module (it even takes over its namespace).

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/forks*
%perl_vendor_autolib/forks
%perl_vendor_archlib/threads

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.34-alt2
- rebuilt for perl-5.14

* Sun Jan 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt1
- initial build for ALT Linux Sisyphus
