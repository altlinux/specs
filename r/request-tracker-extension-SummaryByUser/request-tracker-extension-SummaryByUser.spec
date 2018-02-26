%define module RT-Extension-SummaryByUser
%define m_distro RT-Extension-SummaryByUser
%define m_name RT::Extension::SummaryByUser
%define m_author_id unknown

Name: request-tracker-extension-SummaryByUser
Version: 0.04
Release: alt1

Summary: portlets to show ticket counters per user

License: GPL or Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 31 2010 (-bi)
BuildRequires: perl-devel

%description
This extension ships with OwnerSummary and RequestorSummary portlets you
can use in a dashboard and/or RT at glance. Summary can be displayed not
only by user, but by users' organization or other fields. For example
RequestorSummary portlet displays summary by requestors' organization.
Read more about this below in "CONFIGURATION" section.

%prep
%setup
%build
%perl_vendor_build

%install
mkdir -p %buildroot%_libexecdir/rt/local/plugins/%module/
cp -rp lib %buildroot%_libexecdir/rt/local/plugins/%module/

%files
%_libexecdir/rt/local/plugins/%module

%changelog
* Thu Apr 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.04-alt1
- Initial build for Sisyphus
