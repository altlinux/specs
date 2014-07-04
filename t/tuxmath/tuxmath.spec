# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/makensis gcc-c++ libxml2-devel pkgconfig(cairo) pkgconfig(libxml-2.0)
# END SourceDeps(oneline)
Name:           tuxmath
Version:        2.0.1
Release:        alt2_6
Summary:        Educational math tutor for children

Group:          Games/Other
License:        GPLv3+ and CC-BY and OFL
URL:            http://tux4kids.alioth.debian.org/
Source0:        https://alioth.debian.org/frs/download.php/3272/%{name}_w_fonts-%{version}.tar.gz
Patch0:	        tuxmath_w_fonts-2.0.1-scandir.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_pango-devel
BuildRequires:  libSDL_net-devel
BuildRequires:  librsvg-devel
BuildRequires:	t4k_common-devel
Source44: import.info

%description
TuxMath is an educational math tutor for children. It features several
different types of gameplay, at a variety of difficulty levels.


%prep
%setup -q -n %{name}_w_fonts-%{version}
# remove unneeded font files
rm -f data/fonts/*.ttf
%patch0 -p1

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
%find_lang %{name}

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop


%files -f %{name}.lang
%doc doc/changelog doc/GPL_VERSIONS doc/COPYING_GPL3 doc/README_DATA_LICENSES doc/README doc/TODO doc/OFL
%{_bindir}/%{name}*
%{_bindir}/generate_lesson
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_2
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- update to new release by fcimport

* Fri Oct 28 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- use fedora versions

* Tue Aug 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_0
- new version; manual update (#26080); note the patch

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_2
- rebuild with new librsvg

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_2
- converted from Fedora by srpmconvert script

