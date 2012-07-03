%define module Alterator-Automate
%define m_distro Alterator-Automate
%define m_name Alterator::Automate
%define m_author_id unknown
%define _enable_test 0

Name: perl-Alterator-Automate
Version: 0.03
Release: alt1

Summary: Control host via web alterator from perl code

License: Artistic
Group: Development/Perl
Url: http://git.altlinux.org/people/boyarsh/packages/?p=perl-Alterator-Automate.git


BuildArch: noarch
Source: %m_distro-%version.tar

BuildRequires: perl-devel perl-LWP-Protocol-https

Requires: perl-LWP-Protocol-https

%description
Control host via web alterator from perl code for test purpose

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*


%changelog
* Tue Jul 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.03-alt1
- ldap users adding suport added

* Tue Jul 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.02-alt1
- netinst support added

* Fri Jul 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.01-alt1
- first build


