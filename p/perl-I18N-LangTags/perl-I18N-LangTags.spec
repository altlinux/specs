%define dist I18N-LangTags
Name: perl-%dist
Version: 0.35
Release: alt3

Summary: Functions for dealing with RFC3066-style language tags
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: %name-0.35-dist-5.12.3.patch

BuildArch: noarch

# Automatically added by buildreq on Fri Feb 04 2011
BuildRequires: perl-devel

%description
Language tags are a formalism, described in RFC 3066 (obsoleting
1766), for declaring what language form (language and possibly
dialect) a given chunk of information is in.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog
%perl_vendor_privlib/I18N*

%changelog
* Fri Feb 04 2011 Alexey Tourbin <at@altlinux.ru> 0.35-alt3
- updated from perl-5.12.3

* Fri Jul 24 2009 Alexey Tourbin <at@altlinux.ru> 0.35-alt2
- rebuilt

* Thu Dec 09 2004 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- initial revision (split perl-i18n)
