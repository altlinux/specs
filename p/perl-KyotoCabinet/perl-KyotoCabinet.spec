Name: perl-KyotoCabinet
Version: 1.18
Release: alt3
Summary: a straightforward implementation of DBM

Group: Development/Perl
License: GPLv3
Url: http://fallabs.com/kyotocabinet/perlpkg/

Source: kyotocabinet-perl-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: libkyotocabinet-devel perl-devel

%description
%summary

%prep
%setup -q -n kyotocabinet-perl-%version

%build
%perl_vendor_build LIBS='-lkyotocabinet'

%install
%perl_vendor_install

rm %buildroot%perl_vendor_archlib/*.pl

%files
%doc COPYING README
%perl_vendor_archlib/KyotoCabinet*
%perl_vendor_autolib/KyotoCabinet

%changelog
* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 1.18-alt3
- Rebuilt for perl-5.14

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.18-alt2
- Rebuild

* Tue Jul 12 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.18-alt1
- New version 1.18

* Thu Jun 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.17-alt1
- New version 1.17

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- New version 1.16

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 1.15-alt1
- initial build

