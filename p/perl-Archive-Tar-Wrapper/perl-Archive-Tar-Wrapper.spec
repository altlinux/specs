## SPEC file for Perl module Archive::Tar::Wrapper

Name: perl-Archive-Tar-Wrapper
Version: 0.21
Release: alt1

Summary: Perl wrapper around the 'tar' utility

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Archive-Tar-Wrapper/
#URL: https://github.com/mschilli/archive-tar-wrapper-perl

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Archive-Tar-Wrapper
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Sep 14 2014
BuildRequires: perl-File-Which perl-IPC-Run perl-Log-Log4perl perl-devel

%description
Archive::Tar::Wrapper is an API wrapper around the 'tar' command
line utility. It never stores anything in memory, but works on
temporary directory structures on disk instead. It provides a
mapping between the logical paths in the tarball and the 'real'
files in the temporary directory on disk.

%prep
%setup  -n %real_name-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Archive*


%changelog
* Thu Oct 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.21-alt1
- New version

* Thu Oct 02 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- New version

* Wed Sep 17 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt3
- Rising release to override package from Autoimports/Sisyphus repository

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt1
- Initial build for ALT Linux Sisyphus

