## SPEC file for Perl module PathTools
%define real_name PathTools

Name: perl-PathTools
#####  ATTENTION  ATTENTION  ATTENTION ATTENTION    ######
##### Parts of the module are included into perl-base ####
##### Module version MUST BE THE SAME as in perl-base ####
#####         CHECK IT BEFORE UPGRADING!              ####
Version: 3.62
#####  ATTENTION  ATTENTION  ATTENTION ATTENTION    ######
Release: alt2

Summary: Perl modules to work with file names

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/PathTools/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar


BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sun Dec 20 2015
# optimized out: perl-parent
BuildRequires: perl-Encode perl-devel

%description
PathTools is the combined distribution for the File::Spec and
Cwd modules.

File::Spec Perl module is designed to support operations commonly
performed on file specifications (usually called "file names",
but not to be confused with the contents of a file, or Perl's
file handles), such as concatenating several directory and file
names into a single path, or determining whether a path is
rooted.

NOTE: Basic PathTools functionality already included into
perl-base package, this package contains non-Unix File::Spec
modules.


#Cwd Perl module provides functions for determining the pathname
#of the current working directory. It is recommended that getcwd
#(or another *cwd() function) be used in all code to ensure
#portability.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# Parts of perl-base:
rm -f -- %buildroot%perl_vendor_archlib/File/Spec.pm
rm -f -- %buildroot%perl_vendor_archlib/File/Spec/Functions.pm
rm -f -- %buildroot%perl_vendor_archlib/File/Spec/Unix.pm
rm -f -- %buildroot%perl_vendor_archlib/File/Spec/AmigaOS.pm
rm -f -- %buildroot%perl_vendor_archlib/Cwd.pm
#rm -f -- %%buildroot%%perl_vendor_autolib/Cwd/Cwd.so
rm -rf -- %buildroot%perl_vendor_autolib

%files
%doc Changes README
%perl_vendor_archlib/File/Spec*


%changelog
* Sun Feb 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 3.62-alt2
- New version

* Sun Dec 20 2015 Nikolay A. Fetisov <naf@altlinux.ru> 3.56-alt1
- Initial build for ALT Linux Sisyphus
