# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/a2x
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           cclive
Version:        0.9.3
Release:        alt2
Summary:        Command line video extraction utility
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group:          Video
License:        GPLv3+
URL:            http://cclive.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

#SuSE
Patch0:         cclive-0.9.3_iostream.patch
Patch1:         cclive-0.9.3_gcc5.patch
Patch2:         cclive-0.9.3_subdir.patch
Patch4:         cclive-0.9.3_boost1.67.patch
# gentoo (not used)
Patch3:         %name-0.9.3-gentoo-boost-ver-check.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  boost-filesystem-devel
BuildRequires:  boost-program_options-devel
BuildRequires:  libquvi-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.24
BuildRequires:  pkgconfig(libcurl) >= 7.18.0
BuildRequires:  pkgconfig(libpcre) >= 8.02
BuildRequires:  pkgconfig(libpcrecpp) >= 8.02

%description
cclive is a command line video extraction utility similar to clive but with
lower requirements. Its features are few and essential. Supports Youtube,
Googlevideo, Break, Liveleak, Sevenload, Evisortv and Dailymotion.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
# gentoo (not used)
#patch3 -p1

%ifarch %e2k
# lcc 1.25.20: cpp adds an extra space breaking this regex (mcst#6826)
sed -i 's,\^boost-lib-version,boost-lib-version,' m4/boost.m4
%endif

%build
export DATE=/bin/true
autoreconf -fiv
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%doc ChangeLog NEWS README
%{_bindir}/cclive
%{_bindir}/ccl
%{_man1dir}/cclive.1*

%changelog
* Wed Jan 26 2022 Michael Shigorin <mike@altlinux.org> 0.9.3-alt2
- E2K: workaround boost test's issue with lcc's cpp (mcst#6826)

* Mon Jan 24 2022 Igor Vlasenko <viy@altlinux.org> 0.9.3-alt1
- NMU: updated to 0.9.3, rebuilt with quvi 0.9, added SuSE patches

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.16-alt2.1
- NMU: rebuilt with boost-1.67.0

* Fri Sep 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.16-alt2
- Rebuilt with boost 1.65.0.

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

