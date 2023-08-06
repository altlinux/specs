# Spec file for Perl module AnyEvent::HTTP::LWP::UserAgent

Name: perl-AnyEvent-HTTP-LWP-UserAgent
Version: 0.10
Release: alt2

Summary: Perl module AnyEvent::HTTP::LWP::UserAgent

%define real_name AnyEvent-HTTP-LWP-UserAgent

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/AnyEvent-HTTP-LWP-UserAgent/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses perl-devel


# Automatically added by buildreq on Sat Jul 29 2023
# optimized out: libgpg-error perl perl-AnyEvent perl-CGI perl-CPAN-Meta-Requirements perl-Clone perl-Encode perl-Guard perl-HTML-Parser perl-HTTP-Date perl-HTTP-Message perl-IO-AIO perl-IO-Socket-IP perl-JSON-PP perl-Module-Load perl-Parse-CPAN-Meta perl-Test-SharedFork perl-Try-Tiny perl-URI perl-common-sense perl-devel perl-parent python-modules python2-base python3-base sh4
BuildRequires: perl-AnyEvent-AIO perl-AnyEvent-HTTP perl-CPAN-Meta perl-EV perl-HTTP-Cookies perl-HTTP-Server-Simple perl-Test-TCP perl-libwww

%description
Perl module AnyEvent:HTTP::LWP::UserAgent provides an
LWP::UserAgent interface but works using AnyEvent::HTTP

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%exclude /.perl.req
%perl_vendor_privlib/AnyEvent/HTTP/LWP/UserAgent*

%changelog
* Sat Jul 29 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.10-alt2
- Update build requirements

* Sat Oct 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt1
- Initial build for ALT Linux Sisyphus
