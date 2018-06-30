## SPEC file for Perl module File::Find::Object::Rule

Name: perl-File-Find-Object-Rule
Version: 0.0309
Release: alt1

Summary: alternative interface to File::Find::Object

License: %perl_license
Group: Development/Perl

%define real_name File-Find-Object-Rule
URL: http://search.cpan.org/dist/File-Find-Object-Rule/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses


# Automatically added by buildreq on Sun Jun 03 2018
# optimized out: perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Class-XSAccessor perl-Devel-Symdump perl-Encode perl-File-Find-Rule perl-HTML-Parser perl-JSON-PP perl-Module-Metadata perl-Number-Compare perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Text-Glob perl-devel perl-parent perl-podlators python-base python-modules python3 python3-base python3-module-zope ruby
BuildRequires: perl-File-Find-Object perl-File-Find-Rule-Perl perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module File::Find::Object::Rule is a friendlier interface
to File::Find::Object . It allows you to build rules which
specify the desired files and directories.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File/Find/Object/Rule*
%_bindir/findorule
%_man1dir/findorule*

%changelog
* Sat Jun 30 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.0309-alt1
- New version

* Sun Jun 03 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.0307-alt1
- New version

* Sun Sep 18 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.0306-alt3
- New version

* Mon Sep 08 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.0305-alt3
- Rising release to override package from Autoimports/Sisyphus repository

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.0305-alt1
- Initial build
