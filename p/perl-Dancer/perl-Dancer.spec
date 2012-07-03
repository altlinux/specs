Name: perl-Dancer
Version: 1.3095
Release: alt1
Summary: lightweight yet powerful web application framework

Group: Development/Perl
License: Perl
Url: %CPAN Dancer

BuildArch: noarch
# Cloned from git://github.com/sukria/Dancer.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel perl-Encode perl-MIME-Types perl-HTTP-Body perl-URI perl-HTTP-Server-Simple-PSGI perl-Plack perl-YAML perl-Clone perl-podlators perl-Try-Tiny
Requires: perl-Clone

%description
This project is inspired by  Ruby's Sinatra framework: a framework for
building web applications with minimal-effort, allowing a simple webapp
to be created with very few lines of code, but allowing the flexibility
to scale to much more complex applications.

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/dancer
%_man1dir/dancer.1*
%perl_vendor_privlib/Dancer*
%doc TODO LICENSE CHANGES README

%changelog
* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3095-alt1
- New version 1.3095

* Sat Dec 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3091-alt1
- New version 1.3091

* Thu Dec 15 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3090-alt1
- New version 1.3090

* Mon Dec 05 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3080-alt1
- New version 1.3080

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3071-alt1
- New version 1.3071 (security release)

* Tue Jul 26 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3070-alt1
- New version 1.3070

* Sat May 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3051-alt1
- New version 1.3051.
- Security fix merged upstream

* Thu May 26 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3050-alt1
- New version 1.3050

* Sun Apr 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3030-alt1
- New version 1.3030
- Security: fixed directory traversal flaw

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 1.2005-alt1
- New version 1.2005

* Tue Nov 23 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2000-alt1
- 1.2000, the first major stable community release
- Patch applied to fix test

* Fri Nov 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1901-alt2
- Fixed generation of man1 pages

* Sun Sep 26 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1901-alt1
- New version 1.1901

* Sun Sep 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1811-alt1
- New version 1.1811

* Sun Aug 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1809-alt1
- initial build
