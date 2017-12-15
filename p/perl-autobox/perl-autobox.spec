##nQ SPEC file for Perl module autobox

Name: perl-autobox
Version: 2.85
Release: alt1.1

Summary: Perl interface to call methods on native types

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/autobox/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

%define real_name autobox
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Pod-Escapes perl-Pod-Simple perl-devel
BuildRequires: perl-Scope-Guard perl-Test-Pod

%description
The autobox pragma allows methods to be called on integers, floats,
strings, arrays, hashes, and code references in exactly the same
manner as blessed references.

The autoboxing is transparent: boxed values are not blessed into
their (user-defined) implementation class (unless the method elects
to bestow such a blessing) - they simply use its methods as though
they are.

autobox is lexically scoped, and bindings for an outer scope
can be overridden or countermanded in a nested scope.


%prep
%setup  -n %real_name-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/autobox*
%perl_vendor_autolib/autobox*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.85-alt1.1
- rebuild with new perl 5.26.1

* Sat Mar 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.85-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.84-alt1.1
- rebuild with new perl 5.24.1

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 2.84-alt1
- New version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.83-alt1.1
- rebuild with new perl 5.22.0

* Sun Jun 07 2015 Nikolay A. Fetisov <naf@altlinux.ru> 2.83-alt1
- New version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.82-alt1.1
- rebuild with new perl 5.20.1

* Wed Sep 10 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.82-alt1
- New version

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.79-alt2
- built for perl 5.18

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.79-alt1
- New version

* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.77-alt1
- New version

* Sun Nov 25 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.76-alt1
- New version

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.75-alt2
- rebuilt for perl-5.16

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 2.75-alt1
- Initial build for ALT Linux Sisyphus

