## SPEC file for Perl module Archive::Tar::Wrapper

Name: perl-Archive-Tar-Wrapper
Version: 0.42
Release: alt1

Summary: Perl wrapper around the 'tar' utility

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Archive-Tar-Wrapper/

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

%define real_name Archive-Tar-Wrapper
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Mon Feb 09 2026
# optimized out: libgpg-error libnss-systemd perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-devel perl-parent python-modules python2-base python3 python3-base sh5
BuildRequires: libnss-mymachines perl-CPAN-Meta perl-File-Which perl-IPC-Run perl-Log-Log4perl

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
* Mon Feb 09 2026 Nikolay A. Fetisov <naf@altlinux.org> 0.42-alt1
- New version

* Wed May 29 2024 Nikolay A. Fetisov <naf@altlinux.org> 0.40-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.38-alt1
- New version

* Mon Aug 26 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.37-alt1
- New version

* Thu Apr 18 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.36-alt1
- New version

* Fri Aug 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.33-alt1
- New version

* Mon Jul 02 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.30-alt1
- New version

* Sun Jun 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.27-alt1
- New version

* Mon Jun 11 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.26-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.23-alt1
- New version

* Thu Oct 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.21-alt1
- New version

* Thu Oct 02 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- New version

* Wed Sep 17 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt3
- Rising release to override package from Autoimports/Sisyphus repository

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt1
- Initial build for ALT Linux Sisyphus

