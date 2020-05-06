# Spec file for perl-Time-Format

%define real_name Time-Format

Name: perl-Time-Format
Version: 1.16
Release: alt1

Summary: Easy-to-use date/time formatting
License: unrestricted
Group: Development/Perl

URL: https://metacpan.org/release//Time-Format/
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Manually added by Alexey Tourbin!
Requires: perl-Time-Format_XS

# Automatically added by buildreq on Thu Oct 18 2012
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Class-Load perl-Class-Singleton perl-Data-OptList perl-DateTime-Locale perl-DateTime-TimeZone perl-Encode perl-JSON-PP perl-List-MoreUtils perl-Math-Round perl-Module-Implementation perl-Module-Metadata perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Sub-Install perl-Try-Tiny perl-YAML-Syck perl-devel perl-parent perl-podlators
BuildRequires: perl-Date-Manip perl-DateTime perl-HTML-Parser perl-Module-Build perl-Time-Format_XS

%description
Time::Format provides a very easy way to format dates and times.
The formatting functions are tied to hash variables, so they can
be used inside strings as well as in ordinary expressions. The
formatting codes used are meant to be easy to remember, use, and
read.

# Skip tests inside hasher - unstable results leads to periodic rebuild failures
%ifdef __BTE
 %def_without test
%endif

%prep
%setup -q -n %real_name-%version

%build
rm -f t/xs_doc.t
rm -f t/xs_DateTime.t
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README quickref.txt
%perl_vendor_privlib/Time

%changelog
* Wed May 06 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.16-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.15-alt1
- New version

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.12-alt1
- New version

* Sun Feb 27 2011 Alexey Tourbin <at@altlinux.ru> 1.11-alt2
- fixed tests for Date::Manip
- added dependency on on perl-Time-Format_XS

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.11-alt1
- New version 1.11

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.09-alt1
- New version 1.09

* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt1
- Initial build for ALT Linux Sisyphus

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt0
- Initial build
