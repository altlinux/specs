%define dist MIME-Lite
Name: perl-MIME-Lite
Version: 3.028
Release: alt1

Summary: Low-calorie MIME generator
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: MIME-Lite-3.028-alt-req.patch

BuildArch: noarch
Requires: sendmail-common

# Automatically added by buildreq on Sun Nov 13 2011
BuildRequires: perl-Email-Date-Format perl-MIME-Types perl-MailTools perl-Test-Pod sendmail-common

%description
MIME::Lite is intended as a simple, standalone module for generating
(not parsing!) MIME messages... specifically, it allows you to output
a simple, decent single- or multi-part message with text or binary
attachments.  It does not require that you have the Mail:: or MIME::
modules installed, but will work with them if they are.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/MIME

%changelog
* Sun Nov 13 2011 Alexey Tourbin <at@altlinux.ru> 3.028-alt1
- 3.027 -> 3.028

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 3.027-alt1
- 3.023 -> 3.027

* Tue Nov 25 2008 Alexey Tourbin <at@altlinux.ru> 3.023-alt1
- 3.021 -> 3.023

* Tue Jun 17 2008 Alexey Tourbin <at@altlinux.ru> 3.021-alt1
- 3.01 -> 3.021

* Sun Aug 27 2006 Alexey Tourbin <at@altlinux.ru> 3.01-alt3
- sync debian libmime-lite-perl_3.01-7.diff.gz
- clarified perl dependencies by removing eval wraps
- added dependency on sendmail-common

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.01-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Jun 02 2004 Denis Smirnov <mithraen@altlinux.ru> 3.01-alt2
- Fixed summary and description

* Thu Jan 22 2004 Denis Smirnov <mithraen@altlinux.ru> 3.01-alt1
- Build for Sisyphus
