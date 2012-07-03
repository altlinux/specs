%define m_distro pip
Name: perl-pip
Version: 1.19
Release: alt1
Summary: The Perl Installation Program, for scripted and third-party distribution installation

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/pip/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-libwww perl-File-pushd perl-PAR-Dist perl-LWP-Online perl-Test-Script perl-CPAN perl-Archive-Zip perl-CPAN-Inject perl-Params-Util perl-File-Which perl-Archive-Tar perl-IO-Zlib perl-URI

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/pip
%perl_vendor_privlib/Module/P5Z.pm
%perl_vendor_privlib/Module/Plan/*
%perl_vendor_privlib/pip*
%doc Changes README 

%changelog
* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.19-alt1
- New version 1.19

* Sun Nov 21 2010 Vladimir Lettiev <crux@altlinux.ru> 1.18-alt2
- Dropped man3 pages

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.18-alt1
- New version 1.18

* Wed Jan 27 2010 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- initial build
