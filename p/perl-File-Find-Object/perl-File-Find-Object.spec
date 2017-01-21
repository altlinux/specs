## SPEC file for Perl module File::Find::Object

Name: perl-File-Find-Object
Version: 0.3.2
Serial: 1
Release: alt1


Summary: an object oriented File::Find replacement

License: %perl_license
Group: Development/Perl

%define real_name File-Find-Object
URL: http://search.cpan.org/dist/File-Find-Object/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses


# Automatically added by buildreq on Sat Jan 21 2017
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-JSON-PP perl-Module-Metadata perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-devel perl-parent perl-podlators python-base python-modules python3-base
BuildRequires: perl-Class-XSAccessor perl-HTML-Parser perl-Module-Build

%description
Perl module File::Find::Object does the same job as File::Find
but works like an object and with an iterator. As File::Find
is not object oriented, one cannot perform multiple searches
in the same application. The second problem of File::Find is
its file processing: after starting its main loop, one cannot
easily wait for another event and so get the next result.

With File::Find::Object you can get the next file by calling
the next() function, but setting a callback is still possible.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File/Find/Object*

%changelog
* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.org> 1:0.3.2-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1:0.3.0-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1:0.2.13-alt1
- New version

* Mon Sep 08 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1:0.2.11-alt3
- Rising serial/release to override package from Autoimports/Sisyphus repository

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.11-alt1
- Initial build
