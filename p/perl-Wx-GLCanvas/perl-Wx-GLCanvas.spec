Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Class/Accessor/Fast.pm) perl(ExtUtils/MY_Metafile.pm) perl(Math/Trig.pm) perl(OpenGL.pm) perl-podlators
# END SourceDeps(oneline)
#
%add_findreq_skiplist %{perl_vendor_archlib}/Wx/DemoModules/*
%add_findprov_skiplist %{perl_vendor_archlib}/Wx/DemoModules/*
%add_findreq_skiplist %{perl_vendor_archlib}/Wx/*
%add_findprov_skiplist %{perl_vendor_archlib}/Wx/*
BuildRequires: libGL-devel libGLU-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Wx-GLCanvas
Version:        0.09
Release:        alt2_28
Summary:        Interface to wxWidgets' OpenGL canvas
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Wx-GLCanvas
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/Wx-GLCanvas-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Alien/wxWidgets.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Wx/build/MakeMaker.pm)
BuildRequires:  libwxGTK3.0-devel

%if 0%{?with_tests}
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Wx.pm)
BuildRequires:  perl(Wx/ScrolledWindow.pm)
%endif



Source44: import.info

%description
A wrapper for wxWidgets' wxGLCanvas, used to display OpenGL graphics.

%prep
%setup -q -n Wx-GLCanvas-%{version}
rm -rf wx

chmod -x Changes README.txt

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags} -I/usr/include/wx-3.0"
%make_build

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%if 0%{?with_tests}
%check
DISPLAY=:0.0 make test
%endif

%files
%doc Changes README.txt
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Wx*

%changelog
* Thu Oct 21 2021 Igor Vlasenko <viy@altlinux.org> 0.09-alt2_28
- build with wxGTK3.0

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2_17
- rebuild with new perl 5.28.1

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_17
- update to new release by fcimport

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_15.1
- rebuild with new perl 5.26.1

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_15
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_12
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_11.1
- rebuild with new perl 5.24.1

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_11
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_10
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_9.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_9
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_6.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_4
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_3
- moved to Sisyphus for Slic3r (by dd@ request)

