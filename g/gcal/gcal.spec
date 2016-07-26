# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/less /usr/bin/perl /usr/bin/pg /usr/sbin/zdump texinfo
# END SourceDeps(oneline)
%global gcalmantag 4

Name:		gcal
Version:	4
Release:	alt1_3
Summary:	GNU Gregorian calendar program

Group:		Text tools
License:	GPLv3+
URL:		http://www.gnu.org/software/gcal/
Source0:	ftp://ftp.gnu.org/gnu/gcal/%{name}-%{version}.tar.xz
# The man pages are not shipped in tarball but reside in the git repository.
# To fetch the man pages, do:
# $ gcalmantag=3.6
# $ git archive --format=tar v${gcalmantag} -- doc/en/man | \
#     gzip -c > gcal-man-v${gcalmantag}.tar.gz
Source1:	gcal-man-v%{gcalmantag}.tar.gz
BuildRequires: gettext gettext-tools gettext-tools-python libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
Requires(post): info info-install
Requires(preun): info info-install

# Gnulib is granted exception of "no bundled libraries" packaging guideline:
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides: bundled(gnulib)
Source44: import.info

%description
Gcal is a program for calculating and printing calendars.  Gcal
displays hybrid and proleptic Julian and Gregorian calendar sheets.
It also displays holiday lists for many countries around the globe.

%prep
%setup -q
tar xf %{SOURCE1}


%build
CFLAGS="%{optflags}"
export CFLAGS
%configure
make %{?_smp_mflags}


%check
make check


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -dm 755 %{buildroot}%{_mandir}/man1
install -pm 644 doc/en/man/*.1 %{buildroot}%{_mandir}/man1
rm -f %{buildroot}%{_datadir}/%{name}/Makefile.in
rm -f %{buildroot}%{_infodir}/dir
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS BUGS COPYING LIMITATIONS NEWS README THANKS TODO
%{_bindir}/gcal
%{_bindir}/gcal2txt
%{_bindir}/tcal
%{_bindir}/txt2gcal
%{_datadir}/gcal/
%{_infodir}/*.info*
%{_mandir}/man1/*.1*

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 4-alt1_3
- update to new release by fcimport

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 4-alt1_2.1
- NMU: added BR: texinfo

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.3-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.3-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_4
- update to new release by fcimport

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_2
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.6-alt2_4
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_4
- update to new release by fcimport

* Thu Jun 09 2011 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_3
- new version

