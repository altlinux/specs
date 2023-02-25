Group: Video
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install perl(Proc/Simple.pm) perl(Tk.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: alevt
Version: 1.8.1
Release: alt1_1
Summary: Teletext decoder/browser
License: GPLv2
URL: https://gitlab.com/alevt/alevt
Source: https://gitlab.com/%{name}/%{name}/-/archive/v%{version}/alevt-v%{version}.tar.bz2
Source1: alevt.desktop
Patch0: alevt-1.6.2-pixmap.patch
Patch1: alevt-1.6.2-manpath.patch
Patch2: alevt-1.8.1-doublefont.patch
Patch3: alevt-1.6.2-zlib.patch
BuildRequires: gcc
BuildRequires: libX11-devel
BuildRequires: libpng-devel libpng17-tools
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools
Source44: import.info

%description
AleVT is a teletext/videotext decoder and browser for the
vbi (/dev/vbi) device and X11.  It features multiple windows,
a page cache, regexp searching, built-in manual, and more.
There's also a program to get the time from teletext and
one to capture teletext pages from scripts.


%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1 -b .pixmap
%patch1 -p1 -b .manpath
%patch2 -p1 -b .double
%patch3 -p1 -b .zlib

%build
CC="$CC -DVERSION=\\\"%{version}\\\""
# alevt does not have standard build system, so we populate OPT, 
# which is internal build variable to accommodate Fedora opt flags
# This will produce lot of garbage on output.
%make_build -e OPT="%{optflags}"


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

make USR_X11R6=%{_prefix} MAN=%{_mandir} rpm-install
desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%{_bindir}/alevt
%{_bindir}/alevt-date
%{_bindir}/alevt-cap
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/%{name}*
%{_datadir}/pixmaps/mini-alevt.xpm
%doc README.md CHANGELOG COPYRIGHT

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1.8.1-alt1_1
- update to new release by fcimport

* Tue Feb 08 2022 Ilya Mashkin <oddity@altlinux.ru> 1.8.1-alt1
- 1.8.1
- Update URL and License tags

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_29
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_27
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_26
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_25
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_24
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_23
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_22
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_21
- update to new release by fcimport

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt2_20.1
- Rebuilt with libpng15

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_20
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_16
- rebuild to get rid of #27020

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_16
- initial release by fcimport

