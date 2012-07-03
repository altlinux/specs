%define module RT-Authen-ExternalAuth
%define m_distro RT-Authen-ExternalAuth
%define m_name RT::Authen::ExternalAuth
%define m_author_id unknown
%define _enable_test 1

Name: request-tracker-extension-externalauth
Version: 0.08
Release: alt1

Summary: External Authentication for Request Tracker

License: GPLv2
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

BuildArch: noarch
Source: %m_distro-%version.tar

# Automatically added by buildreq on Tue Aug 25 2009 (-bi)
BuildRequires: perl-CGI perl-DBI perl-devel perl-ldap

%description
Allows authentication from any LDAP or DBI-supported data source. Also allows
the use of a browser cookie to implement Single Sign-On with other web code
using a DBI authentication backend.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%add_findreq_skiplist /usr/lib/rt/local/plugins/RT-Authen-ExternalAuth/lib/RT/User_Vendor.pm
%add_findreq_skiplist /usr/lib/rt/local/plugins/RT-Authen-ExternalAuth/lib/RT/Authen/ExternalAuth.pm
%add_findreq_skiplist /usr/lib/rt/local/plugins/RT-Authen-ExternalAuth/lib/RT/Authen/ExternalAuth/DBI.pm

%install
mkdir -p %buildroot%_libexecdir/rt/local/plugins/%module/
cp -rp html lib %buildroot%_libexecdir/rt/local/plugins/%module/

%files
%_libexecdir/rt/local/plugins/%module
%doc etc/RT_SiteConfig.pm

%changelog
* Mon Aug 31 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.08-alt1
- Initial build for Sisyphus
