## SPEC file for Perl module App::Cmd

Name: perl-App-Cmd
Version: 0.317
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

# Automatically added by buildreq on Fri Apr 20 2012
# optimized out: perl-Data-OptList perl-List-MoreUtils perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Runtime perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Check perl-Params-Util perl-Params-Validate perl-Sub-Exporter perl-Sub-Install perl-Try-Tiny perl-devel
BuildRequires: perl-Capture-Tiny perl-Class-Load perl-Getopt-Long-Descriptive perl-IO-TieCombine perl-IPC-Cmd perl-Module-Pluggable perl-String-RewritePrefix perl-Test-Fatal perl-parent

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
* Fri Apr 20 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.317-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.314-alt1
- Initial build for ALT Linux Sisyphus

