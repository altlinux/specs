Name: perl-OpenGL
Epoch: 1
Version: 0.70
Release: alt1.1.1

Summary: Perl bindings to OpenGL API
Group: Development/Perl
License: Perl

Url: %CPAN OpenGL
# Cloned from git://pogl.git.sourceforge.net/gitroot/pogl/pogl
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel libfreeglut-devel libXi-devel libXmu-devel libXext-devel libstdc++-devel gcc-c++

%description
%summary

%prep
%setup -q
%patch -p1
rm test.pl

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/OpenGL*
%perl_vendor_autolib/OpenGL*
%doc TODO CHANGES README COPYRIGHT KNOWN_PROBLEMS Release_Notes SUPPORTS

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.70-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.70-alt1.1
- rebuild with new perl 5.24.1

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.70-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.6704-alt2.1
- rebuild with new perl 5.22.0

* Wed Nov 25 2015 Vladimir Lettiev <crux@altlinux.ru> 0.6704-alt2
- fix build with mesa 11.0.6

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.6704-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.6703-alt1.1
- rebuild with new perl 5.20.1

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.6703-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt2
- rebuilt for perl-5.16

* Fri Jun 22 2012 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt1
- initial build
