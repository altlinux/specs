## SPEC file for Perl module Module::Extract::Use

%define real_name Module-Extract-Use

Name: perl-Module-Extract-Use
Version: 1.043
Release: alt1

Summary: Perl module to pull out the modules a module explicitly uses

License: %artistic_license_v2
Group: Development/Perl

URL: http://search.cpan.org/dist/Module-Extract-Use/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Jan 21 2017
# optimized out: perl perl-Clone perl-Devel-Symdump perl-Encode perl-Exporter-Tiny perl-IO-String perl-List-MoreUtils perl-PPI perl-Params-Util perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel python-base python-modules python3-base
BuildRequires: perl-PPI-XS perl-Test-Manifest perl-Test-Output perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Module::Extract::Use extracts the names of the modules
used in a file using a static analysis. Since this module does not
run code, it cannot find dynamic uses of modules, such as eval
"require $class". It only reports modules that the file loads
directly. Modules loaded with parent or base, for instance, will
be in the import list for those pragmas but won't have separate
entries in the data this module returns.

%prep
%setup -q -n %real_name-%version

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/Artistic-2 %_docdir/%name/LICENSE) LICENSE

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.pod Changes
%doc --no-dereference LICENSE

%perl_vendor_privlib/Module/Extract/Use*

%changelog
* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.043-alt1
- New version

* Sat Jan 21 2017 Nikolay A. Fetisov <naf@altlinux.ru> 1.04-alt3
- Initial build for ALT Linux Sisyphus
