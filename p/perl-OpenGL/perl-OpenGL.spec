%define _unpackaged_files_terminate_build 1

Name: perl-OpenGL
Epoch: 1
Version: 0.7004
Release: alt1

Summary: Perl bindings to OpenGL API
Group: Development/Perl
License: Perl

Url: %CPAN OpenGL
VCS: git+https://github.com/Perl-GPU/pogl.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel libGLUT-devel libXi-devel libXmu-devel libXext-devel libstdc++-devel gcc-c++
# for tests to run
BuildRequires: xvfb-run

%description
%summary

%prep
%setup -q
%patch -p1
# one-off scripts (for dev use?) as of 0.7004
rm test.pl
rm genvars.pl isosurf.pl menutest.pl oga.pl

# even with xvfb-run, "OpenGL GLX extension not supported by display ':0'"
rm -f t/shader.t

%build
%perl_vendor_build
#xvfb-run -a make test

%install
%perl_vendor_install

%files
%perl_vendor_archlib/OpenGL*
%perl_vendor_autolib/OpenGL*
%doc Changes TODO README COPYRIGHT KNOWN_PROBLEMS SUPPORTS

%changelog
* Fri Apr 04 2025 Igor Vlasenko <viy@altlinux.org> 1:0.7004-alt1
- New version 0.7004.

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 1:0.70-alt3
- removed Array.pod (conflicts with perl-OpenGL-Array)

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.70-alt2.1
- rebuild with new perl 5.28.1

* Wed Oct 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.70-alt2
- NMU: rebuilt with libGLUT.

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
