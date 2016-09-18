## SPEC file for Perl module File::Find::Object

Name: perl-File-Find-Object
Version: 0.3.0
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


# Automatically added by buildreq on Sat May 30 2015
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Class-XSAccessor perl-Devel-Symdump perl-Encode perl-File-Find-Object-Rule perl-JSON-PP perl-Module-Metadata perl-Number-Compare perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Text-Glob perl-Tie-RefHash perl-autodie perl-devel perl-parent perl-podlators
BuildRequires: perl-CPAN-Changes perl-HTML-Parser perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-Test-TrailingSpace

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
* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1:0.3.0-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1:0.2.13-alt1
- New version

* Mon Sep 08 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1:0.2.11-alt3
- Rising serial/release to override package from Autoimports/Sisyphus repository

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.11-alt1
- Initial build
