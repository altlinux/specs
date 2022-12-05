## SPEC file for Perl module PAR::Packer

%define real_name PAR-Packer

Name: perl-PAR-Packer
Version: 1.057
Release: alt1

Summary: Perl module to generate stand-alone executables and ".par" archives

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/PAR-Packer/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Aug 04 2019
# optimized out: gem-power-assert glibc-kernheaders-generic glibc-kernheaders-x86 less libcrypt-devel perl perl-Archive-Zip perl-CPAN-Meta-Requirements perl-Compress-Raw-Zlib perl-Digest-SHA perl-Encode perl-IO-Compress perl-IPC-Cmd perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Term-Cap perl-Unicode-Normalize perl-devel perl-parent perl-podlators python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: dpkg perl-CPAN-Meta perl-ExtUtils-CBuilder perl-Getopt-ArgvFile perl-IPC-Run3 perl-Module-ScanDeps perl-PAR perl-PAR-Dist perl-Pod-Perldoc perl-prefork perl-unicore

# This module require App/Packer/Backend/DemoPack.pm and App/Packer/Frontend/ModuleInfo.pm modules
# which should be created by application
%add_findreq_skiplist */App/Packer/PAR.pm

%description
Perl module PAR::Packer is a part of the PAR toolkit.
PAR-Packer is the PAR component that can generate
stand-alone executables and ".par" archives.

%package scripts
Summary: PAR:Packer scripts
Group: Development/Perl
Requires: %name = %version-%release

%description scripts
Perl module PAR::Packer is a part of the PAR toolkit.
PAR-Packer is the PAR component that can generate
stand-alone executables and ".par" archives.

This package contains supplimentary scripts to generate
PAR archives.


%prep
%setup -q -n %real_name-%version

# Fix for parallel build:
sed -e 's#MY::postamble#MY::depend#' -i Makefile.PL

%build
rm -f t/90-rt129312.t

%perl_vendor_build

%install
%perl_vendor_install

mv -- %buildroot%_bindir/pp %buildroot%_bindir/par-pp

%files
%doc README Changes
%perl_vendor_privlib/PAR*
%perl_vendor_privlib/App/Packer*
%perl_vendor_privlib/pp.pm

%files scripts
%_bindir/*
%_man1dir/*


%changelog
* Mon Dec 05 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.057-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.054-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.052-alt1
- New version

* Tue May 05 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.050-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.049-alt1
- New version

* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.048-alt1
- New version

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.047-alt1.1
- rebuild with new perl 5.28.1

* Sat Aug 25 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.047-alt1
- New version

* Sat Aug 18 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.046-alt1
- New version

* Tue Jun 19 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.045-alt2
- Fix build in the parallel BTE

* Sun Jun 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.045-alt1
- New version

* Sat Apr 07 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.043-alt1
- New version

* Fri Mar 09 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.041-alt4
- Initial build for ALT Linux Sisyphus
