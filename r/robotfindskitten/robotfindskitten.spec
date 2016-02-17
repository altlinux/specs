# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libncurses-devel
# END SourceDeps(oneline)
Name:		robotfindskitten
Version:	1.7320508.406
Release:	alt2_12
Summary:	A game/zen simulation. You are robot. Your job is to find kitten.

Group:		Games/Other
License:	GPLv2+
URL:		http://robotfindskitten.org
Source0:        http://robotfindskitten.org/download/POSIX/robotfindskitten-1.7320508.406.tar.gz
# Submitted to upstream development list for consideration
Patch0:		robotfindskitten-1.7320508.406-info-direntry.patch

BuildRequires:	ncurses-devel glibc-devel texinfo
Requires(post):	info
Requires(preun): info
Source44: import.info

%description
In this game, you are robot (#). Your job is to find kitten. This task
is complicated by the existence of various things which are not kitten.
Robot must touch items to determine if they are kitten or not. The game
ends when robotfindskitten.

%prep
%setup -q
%patch0 -p1 -b .info-direntry


%build
%configure
make %{?_smp_mflags}
# rebuild the info page to include the patched-in direntry
rm -f doc/robotfindskitten.info
make -C doc robotfindskitten.info


%install
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
ln -sf ../games/robotfindskitten $RPM_BUILD_ROOT/%{_bindir}/robotfindskitten
# make install creates this, but we don't need it
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir


%files
%doc AUTHORS BUGS ChangeLog COPYING NEWS README
%{_bindir}/robotfindskitten
%{_prefix}/games/robotfindskitten
%{_datadir}/info/robotfindskitten.info*
%{_datadir}/man/man6/robotfindskitten.6*

%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt2_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt2_6
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt2_5
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt1_5
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.7320508.406-alt1_4
- converted from Fedora by srpmconvert script

