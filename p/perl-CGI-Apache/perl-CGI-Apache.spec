Name:    perl-CGI-Apache
Version: 1.01
Release: alt1

Summary: CGI::Apache - Backward compatibility module for CGI.pm
License: Perl
Group:   Development/Perl
URL:     https://perldoc.perl.org/5.16.1/CGI::Apache.txt

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-CGI

BuildArch: noarch

Source: %name-%version.tar

%description
%{summary}.

%prep
%setup

%install
install -Dpm0644 CGI::Apache.pm %buildroot%perl_vendor_privlib/CGI/Apache.pm

%files
%perl_vendor_privlib/CGI/Apache.pm

%changelog
* Sat Jul 31 2021 Andrey Cherepanov <cas@altlinux.org> 1.01-alt1
- Initial build for Sisyphus.
