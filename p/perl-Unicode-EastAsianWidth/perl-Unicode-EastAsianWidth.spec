%define dist Unicode-EastAsianWidth
Name: perl-%dist
Version: 1.33
Release: alt1

Summary: East Asian Width properties
License: CC0 1.0 Universal
Group: Development/Perl
BuildArch: noarch

Url: %CPAN %dist
# http://search.cpan.org/CPAN/authors/id/A/AU/AUDREYT/%dist-%version.tar.gz
Source: %dist-%version.tar
BuildRequires: perl-devel

%description
This perl module provide user-defined Unicode properties that deal
with width status of East Asian characters, as specified in
<http://www.unicode.org/unicode/reports/tr11/>.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Unicode/

%changelog
* Fri Nov 01 2013 Dmitry V. Levin <ldv@altlinux.org> 1.33-alt1
- Initial revision.
