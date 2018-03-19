# BEGIN SourceDeps(oneline):
BuildRequires: perl(CGI/Simple.pm) perl(ExtUtils/MakeMaker.pm) perl(HTML/Tiny.pm) perl(HTTP/Response.pm) perl(LWP/UserAgent.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.99
%define module_name Captcha-reCaptcha
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.99
Release: alt2
Summary: A Perl implementation of the reCAPTCHA API
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/S/SU/SUNNYP/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
reCAPTCHA version 1 is a hybrid mechanical turk and captcha that allows visitors
who complete the captcha to assist in the digitization of books.

From http://recaptcha.net/learnmore.html:

    reCAPTCHA improves the process of digitizing books by sending words that
    cannot be read by computers to the Web in the form of CAPTCHAs for
    humans to decipher. More specifically, each word that cannot be read
    correctly by OCR is placed on an image and used as a CAPTCHA. This is
    possible because most OCR programs alert you when a word cannot be read
    correctly.

version 1 of Perl implementation is modelled on the PHP interface that can be
found here:

http://recaptcha.net/plugins/php/

To use reCAPTCHA you need to register your site here:

https://www.google.com/recaptcha/admin/create


Version 2 is a new and eaasy to solve captcha that is
"easy for humans to solve, but hard for 'bots' and other malicious software"
%prep
%setup -q -n %{module_name}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README TODO examples
%perl_vendor_privlib/C*

%changelog
* Mon Mar 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.99-alt2
- to Sisyphus as perl-Captcha-reCAPTCHA replacement

* Thu Sep 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- initial import by package builder

