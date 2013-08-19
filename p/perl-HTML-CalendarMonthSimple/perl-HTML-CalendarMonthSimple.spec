%define module HTML-CalendarMonthSimple
%define m_distro HTML-CalendarMonthSimple
%define m_name HTML::CalendarMonthSimple
%define m_author_id unknown
%define _enable_test 1

Name: perl-HTML-CalendarMonthSimple
Version: 1.25
Release: alt1

Summary: Perl Module for Generating HTML Calendars

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

BuildRequires: perl-Date-Calc perl-devel

%description
HTML::CalendarMonthSimple is a Perl module for generating,
manipulating, and printing a HTML calendar grid for a specified month.
It is intended as a faster and easier-to-use alternative to
HTML::CalendarMonth.

This module requires the Date::Calc module, which is available from
CPAN if you don't already have it.

%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTML/*

%changelog
* Tue Aug 20 2013 Evgenii Terechkov <evg@altlinux.org> 1.25-alt1
- initial build for ALT Linux Sisyphus

