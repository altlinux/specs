%define module WWW-Blog-Identify

Name: perl-%module
Version: 0.06
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: WWW::Blog::Identify - Identify blogging tools based on URL and content
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/WWW/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Aug 06 2008
BuildRequires: perl-devel

%description
WWW::Blog::Identify - Identify blogging tools based on URL and content.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/WWW

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Aug 06 2008 Victor Forsyuk <force@altlinux.org> 0.06-alt1
- Initial build.
