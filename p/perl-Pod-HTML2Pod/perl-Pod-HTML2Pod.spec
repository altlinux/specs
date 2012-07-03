%define dist Pod-HTML2Pod
Name: perl-%dist
Version: 4.05
Release: alt2

Summary: Translate HTML into POD
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-HTML-Tree perl-devel

%description
Translate HTML into POD, the Plain Old Documentation format.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%_bindir/html2pod
%perl_vendor_privlib/Pod

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 4.05-alt2
- rebuilt

* Fri Mar 11 2005 Alexey Tourbin <at@altlinux.ru> 4.05-alt1
- 4.04 -> 4.05 (just rebundling; no code changes)
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.04-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Aug 25 2004 Alexey Tourbin <at@altlinux.ru> 4.04-alt1
- initial revision (html2pod is needed to build netpbm man pages)
