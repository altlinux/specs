## SPEC file for Perl module App::Cmd

Name: perl-App-Cmd
Version: 0.335
Release: alt1

Summary: Perl module to write CLI apps with less suffering

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/App-Cmd/
#URL: https://github.com/rjbs/app-cmd

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name App-Cmd
Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Thu Mar 18 2021
# optimized out: perl perl-CPAN-Meta-Requirements perl-Data-OptList perl-Encode perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Implementation perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Module-Runtime perl-Package-Stash perl-Package-Stash-XS perl-Params-Check perl-Params-Util perl-Params-Validate perl-Parse-CPAN-Meta perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage perl-Sub-Exporter perl-Sub-Install perl-Try-Tiny perl-devel perl-parent perl-podlators python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Capture-Tiny perl-Class-Load perl-Getopt-Long-Descriptive perl-IO-TieCombine perl-IPC-Cmd perl-Module-Pluggable perl-Pod-Perldoc perl-String-RewritePrefix perl-Test-Fatal perl-experimental

%description
Perl module App::Cmd is intended to make it easy to write complex
command-line applications without having to think about most of
the annoying things usually involved.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/App/Cmd*

%changelog
* Fri Jan 13 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.335-alt1
- New version

* Mon Jun 21 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.334-alt1
- New version

* Thu Mar 18 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.333-alt1
- New version

* Thu Jul 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.331-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.330-alt1
- New version

* Sat Sep 05 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.328-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.327-alt1
- New version

* Sat Jan 10 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.326-alt1
- New version

* Wed Oct 29 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.324-alt1
- New version

* Thu Feb 27 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.323-alt1
- New version

* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.320-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.318-alt1
- New version

* Fri Apr 20 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.317-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.314-alt1
- Initial build for ALT Linux Sisyphus

