%define dist Privileges-Drop
Name: perl-%dist
Version: 1.03
Release: alt1

Summary: A module to make it simple to drop all privileges, even POSIX groups.
License: GPL or Artistic
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar

BuildArch: noarch

BuildRequires: perl-devel perl-Module-Build

%description
This module tries to simplify the process of dropping privileges. This
can be useful when your Perl program needs to bind to privileged ports,
etc. This module is much like Proc::UID, except that it's implemented in
pure Perl.

%prep
%setup -q -n %dist-%version

%build
%if "%(logger -d -u /dev/log -p user.debug test &>/dev/null || echo no)" == "no"
: syslog not available
%def_without test
%endif

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README MANIFEST* ChangeLog examples
%perl_vendor_privlib/Privileges*

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Tue Nov 16 2010 Michael A. Kangin <prividen@altlinux.org> 1.01-alt2
- Remove man3dir macro

* Sun Sep 19 2010 Michael A. Kangin <prividen@altlinux.org> 1.01-alt1
- Initial release for Sisyphus

