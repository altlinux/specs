# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pod2man gcc-c++ pkgconfig(libpcre) pkgconfig(libpcrecpp)
# END SourceDeps(oneline)
Name:           cclive
Version:        0.7.16
Release:        alt1.1
Summary:        Command line video extraction utility
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group:          Video
License:        GPLv3+
URL:            http://cclive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

BuildRequires: boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel libquvi-devel libcurl-devel pcre-devel chrpath
Source44: import.info

%description
cclive is a command line video extraction utility similar to clive but with
lower requirements. Its features are few and essential. Supports Youtube,
Googlevideo, Break, Liveleak, Sevenload, Evisortv and Dailymotion.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc COPYING README 
%{_bindir}/%{name}
%{_bindir}/ccl
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.7.16-alt1.1
- rebuild with boost 1.57.0

* Tue Sep 09 2014 Ilya Mashkin <oddity@altlinux.ru> 0.7.16-alt1
- 0.7.16

* Fri Sep 05 2014 Ilya Mashkin <oddity@altlinux.ru> 0.7.11-alt2
- build for Sisyphus

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.11-alt1_4
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.11-alt1_3
- update to new release by fcimport

* Mon Jan 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.11-alt1_1
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.10-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.9-alt2_3
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.9-alt2_2
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.9-alt2_1
- rebuild with new libquvi

* Sat May 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.9-alt1_1
- converted for Sisyphus

