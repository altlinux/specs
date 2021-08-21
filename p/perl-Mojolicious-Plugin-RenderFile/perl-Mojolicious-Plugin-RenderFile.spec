%define _unpackaged_files_terminate_build 1

Name: perl-Mojolicious-Plugin-RenderFile
Version: 0.12
Release: alt2
Summary: Mojolicious plugin allowing customization to force file download
# See lib/Mojolicious/Plugin/RenderFile.pm
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Mojolicious-Plugin-RenderFile/
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(Encode.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Spec/Functions.pm)
BuildRequires: perl(lib.pm)
BuildRequires: perl(Mojo/Base.pm)
BuildRequires: perl(Mojo/Util.pm)
BuildRequires: perl(Mojolicious/Lite.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(Test/Mojo.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(utf8.pm)
BuildRequires: perl(warnings.pm)

%description
Mojolicious::Plugin::RenderFile is a Mojolicious plugin that makes it
easy to provide files for download. It also allows customization of
the HTTP headers sent to the client.

%prep
%setup
# This test only works properly with Mojo 5.78+:
# https://github.com/koorchik/Mojolicious-Plugin-RenderFile/commit/0dfa997
rm t/multibyte_filename.t

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -f %buildroot%perl_vendorlib/Mojolicious/Plugin/README.pod

%files
%doc Changes
%perl_vendorlib/Mojolicious/Plugin*

%changelog
* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt2
- NMU: drop BR python2 module

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.12-alt1
- initial build for ALT
