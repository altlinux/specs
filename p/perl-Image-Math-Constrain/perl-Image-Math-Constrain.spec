## SPEC file for Perl module Image::Math::Constrain
## Used during tests of Imager

%define version    1.02
%define release    alt1

Name: perl-Image-Math-Constrain
Version: %version
Release: alt1.1

Summary: scaling math used in image size constraining
#Summary(ru_RU.UTF-8): 

License: %perl_license
Group: Development/Perl

%define real_name Image-Math-Constrain
URL: http://search.cpan.org/~adamk/%real_name/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses


%description
Perl module  Image::Math::Constrain implements the logic of 
constrain image sizes. Any module or script that does image 
size  constraining  or thumbnailing could use  it for doing 
common math operation.

#%%description -l ru_RU.UTF-8

%prep
%setup -q -n %real_name-%version

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%doc --no-dereference LICENSE
%perl_vendor_privlib/Image/Math/Constrain.pm
%exclude /.perl.req

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt1
- New version

* Tue Apr 25 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.01-alt1
- Initial build for ALT Linux

