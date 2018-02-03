# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ularn
Version:        1.5p4
Release:        alt2_28
Summary:        Simple roguelike game

Group:          Games/Other
License:        GPL+
URL:            http://www.ularn.org
Source0:        http://downloads.sourceforge.net/ularn/Ularn-1.5ishPL4.tar.gz
Source1:        config.sh.in
Source2:        ularn.desktop
Source3:        ularn.png
Patch0:         ularn-build.patch
Patch1:         ularn-euid.patch
Patch2:         ularn-datadir.patch
Patch3:         ularn-drop-setgid.patch

BuildRequires:  libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
BuildRequires:  desktop-file-utils
Requires:       ncompress
Requires(post): coreutils
Requires(postun): coreutils
Source44: import.info

%description
A text-based roguelike game based on the original Larn.  Travel through
dungeons collecting weapons, killing monsters, in order to find and sell the
Eye of Larn to save your sick daughter.

%prep
%setup -q -n Ularn

# The configure script for this package is interactive.  However, it
# produces a config.sh script that can be customized if necessary.
# a pre-built config.sh script is used to avoid running an interactive
# configure script, but still must be customized slightly.
sed -e 's#@bindir@#%{_bindir}#' \
        -e 's#@datadir@#%{_datadir}#' \
        -e 's#@var@#%{_var}#' < %{SOURCE1} > config.sh
chmod +x config.h.SH
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# Keep track of where we are.  Some of the configuration scripts change
# the current working directory.
builddir=`pwd`
. ./config.h.SH
${builddir}/Makefile.u.SH
cd ${builddir}
mv Makefile.u Makefile
CC="gcc $RPM_OPT_FLAGS" make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_var}/games
touch $RPM_BUILD_ROOT/%{_var}/games/Ularn-scoreboard

desktop-file-install \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/

%files
%attr(2711,root,games) %{_bindir}/Ularn
%{_datadir}/%{name}
%config(noreplace) %attr (0664,root,games) %{_var}/games/Ularn-scoreboard
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%doc README README.spoilers GPL CHANGES.text Ularnopts


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_28
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_27
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_25
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_24
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_23
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_22
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_21
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_20
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_19
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_18
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt2_17
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt1_17
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.5p4-alt1_16
- converted from Fedora by srpmconvert script

