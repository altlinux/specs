Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: perl(FileHandle.pm) perl(Text/Wrap.pm) texinfo
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%global libchewing_python_dir %{python_sitelibdir}/libchewing

%global im_name_zh_TW 新酷音輸入法
%global name_zh_TW %{im_name_zh_TW}函式庫

Name:           libchewing
Version:        0.5.1
Release:        alt1_11
Summary:        Intelligent phonetic input method library for Traditional Chinese
Summary(zh_TW): %{name_zh_TW}

License:        LGPLv2+
URL:            http://chewing.csie.net/
Source0:        https://github.com/chewing/%{name}/archive/v%{version}.tar.gz
Source1:         https://raw.githubusercontent.com/chewing/%{name}/v%{version}/contrib/python/chewing.py

BuildRequires:  autoconf automake libtool makeinfo 
BuildRequires:  libsqlite3-devel
Requires: sqlite3
Requires(post): info info-install
Requires(preun): info info-install
Source44: import.info

%description
libchewing is an intelligent phonetic input method library for Chinese.

It provides the core algorithm and logic that can be used by various
input methods. The Chewing input method is a smart bopomofo phonetics
input method that is useful for inputting Mandarin Chinese.

%description -l zh_TW
%{name_zh_TW}提供實做了核心選字演算法，以便輸入法程式調用。

%{im_name_zh_TW}是一種智慧型注音/拼音猜字輸入法，透過智慧型的字庫分析、習慣記錄學習與預測分析，
使拼字輸入的人為選字機率降至最低，進而提升中文輸入、打字的效率。

%package -n %{name}-devel
Group: Development/Other
Summary:        Development files for libchewing
Summary(zh_TW): %{name_zh_TW}開發者套件
Requires:       %{name} = %{version}-%{release}

%description -n %{name}-devel
Headers and other files needed to develop applications using the %{name}
library.

%description -l zh_TW  -n %{name}-devel
%{name_zh_TW}開發者套件提供了開發%{im_name_zh_TW}相關程式所需的檔案，
像是標頭檔(header files)，以及函式庫。


%package -n python-module-libchewing
Group: System/Libraries
Summary:        Python binding for libchewing
Summary(zh_TW): %{name_zh_TW} python 綁定
BuildRequires:  python-devel
Requires:       %{name} = %{version}-%{release}
Requires:       python
%{?python_provide:%python_provide python2-%{name}}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}

%description -n python-module-libchewing
Python binding of libchewing.

%description -l zh_TW -n python-module-libchewing
%{name_zh_TW} python 綁定

%prep
%setup -q
mkdir -p contrib/python
cp -p %SOURCE1 contrib/python

%build
CFLAGS="%{optflags} -g -DLIBINSTDIR='%{_libdir}'"
autoreconf -ivf
%configure --disable-static
make V=1 RPM_CFLAGS="%{optflags}" %{_smp_mflags}

%install
make DESTDIR=%{buildroot} install INSTALL="install -p"
rm %{buildroot}%{_libdir}/libchewing.la

mkdir -p %{buildroot}%{libchewing_python_dir}
cp -p contrib/python/chewing.py %{buildroot}%{libchewing_python_dir}

mkdir -p %{buildroot}%{_libdir}/chewing
touch %{buildroot}%{libchewing_python_dir}/__init__.py

rm -f %{buildroot}/%{_infodir}/dir



%files
%doc README.md AUTHORS COPYING NEWS TODO
%{_datadir}/%{name}/*
%{_libdir}/*.so.*
%{_infodir}/%{name}.info.*

%files devel
%dir %{_includedir}/chewing
%{_includedir}/chewing/*
%{_libdir}/pkgconfig/chewing.pc
%{_libdir}/*.so

%files -n python-module-libchewing
%{libchewing_python_dir}

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_11
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_8
- update to new release by fcimport

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_5
- update to new version by fcimport

* Tue Jul 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt2
- Updated build dependencies

* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt1.1
- Rebuild with Python-2.7

* Sun Dec 19 2010 Ilya Mashkin <oddity@altlinux.ru> 0.3.2-alt1
- Build for ALT Linux

* Thu Sep 02 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-28
- Resolves: #625980
  Add padding to wch_t to ensure it's word aligned.

* Wed Mar 04 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-27
- Fix Dvorak Hsu 4th tone key (ibus google issue 755 comment 12,
  chewing google issue 10)
- Resolves: #555192

* Mon Feb 15 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-24
- Fix Hsu and Dvorak Hsu input (ibus google issue 755,
  chewing google issue 10)
- Resolves: #555192

* Mon Feb 15 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-23
- Fix Hsu and Dvorak Hsu input (ibus google issue 755,
  chewing google issue 10)
- Resolves: #555192

* Wed Feb 10 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-22
- Fix Hsu and Dvorak Hsu input (ibus google issue 755)
- Resolves: #555192

* Tue Feb 02 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-21
- Revised phrase choice from rear logic.
  Thus update phraseChoiceRearward.patch as phraseChoiceRearward.2.patch
- Resolves: #555192

* Fri Jan 21 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-20
- Resolves: #555192
- Fix for package wrangler.

* Tue Jan 19 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-18
- Resolves: #555192
- Fix for package wrangler.

* Tue Jan 05 2010 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-17
- Add zh_TW summary and description
- Split out python binding into a subpackage.
- Fix for package wrangler.

* Wed Sep 30 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-16
- Fix chewing Google issue 352:
  zuin_count in chewing_zuin_String( ChewingContext *ctx, int *zuin_count )
  does not count correctly.

* Mon Aug 03 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-15
- Fix [Bug 512108:issue 11] ibus-chewing crash the application
  by move cursor_orig to chewingio.c global.

* Thu Jul 30 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-14
- Fix [Bug 512108] ibus-chewing crash the application

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-12
- Rebuild to correct tags.

* Fri Jun 26 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-11
- Revise phraseChoiceRearward.patch so the cursor won't move to left
  when repeatly press down key.

* Wed May 20 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-10
- Need autoreconf and BuildRequires: pkgconfig to make changes in
  Makefile.am effective, thus actually fix [Bug 477960] libchewing multilib conflict.

* Mon May 18 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-9
- Possible Fix of Bug 501220 - RFE: edit last preedit character from end of line
  Chewing upstream does not handle if phrase choice rearward is enabled.

* Wed Apr 22 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-8
- Fix [Bug 496968] - libchewing-debuginfo does not contain sources.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-6
- Fix [Bug 486409] - Wrong python binding installed path
  Add BuildRequires:  python-devel

* Wed Feb 18 2009 Adam Jackson <ajax@redhat.com> 0.3.2-5
- Rerun autotools so changes to Makefile.am actually take effect.

* Fri Jan 23 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-4
- touch python-<ver>/site-packages/libchewing/__init__.py,
  So python thinks libchewing is a library.

* Thu Jan 14 2009 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-3
- Add python binding by copy python/chewing.py to
  <python_dir>/site_packages/libchewing

* Tue Dec 23 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-2
- [Bug 477690] libchewing multilib conflict
  Move /usr/share/chewing/fonetree.dat to corresponding libdir.

* Wed Dec 03 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.2-0
- Upstream update to 0.3.2.

* Wed Oct 08 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.1-0
- Upstream update.

* Wed Sep 17 2008 Ding-Yi Chen <dchen at redhat dot com> - 0.3.0.901-0
- Upstream update.

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.3.0-12
- fix license tag

* Tue Apr 22 2008 Caius Chance <cchance@redhat.com> - 0.3.0-11.fc10
- Resolves: rhbz195416 (Initial input mode between Chinese and English.)

* Wed Feb 13 2008 Caius Chance <cchance@redhat.com> - 0.3.0-10.fc9
- Rebuild for F9.

* Tue Jan 08 2008 Caius Chance <cchance@redhat.com> - 0.3.0-9.devel
- Resolves: rhbz#200694 (Moving "Han-Yin" <-> Zhu-Yin" option to AUX UI.)

* Fri Jun 01 2007 Caius Chance <cchance@redhat.com> - 0.3.0-8.devel
- Fixed bz#237916: [chewing] Candidate list (symbol) page change inaccracy.

* Fri Apr 20 2007 Caius Chance <cchance@redhat.com> - 0.3.0-7.fc7
- Fixed bz#237233: Up arrow on candidate list doesn't work.

* Fri Mar 09 2007 Caius Chance <cchance@redhat.com> - 0.3.0-6.devel
- Fixed bz231568: [chewing] Look up table is showing candidates of previous
  look-up.

* Tue Nov 21 2006 Caius Chance <cchance@redhat.com> - 0.3.0-5.fc7
- Fixed bz#216581: Ported the following bugfix:
- (bz#216337: Page Up / Page Down key doesn't when Chewing is activated.)
- (bz#209575: preedit buffer is not cleared when framework calls for
  instance reset.)

* Fri Sep 15 2006 Caius Chance <cchance@redhat.com> - 0.3.0-4.fc6
- Fixed bz#206232 - Shift_L + space doesn't work correctly

* Mon Sep 04 2006 Caius Chance <cchance@redhat.com> - 0.3.0-3.fc6
- Fixed bz#199353 - scim-chewing hangs for commit > 6 characters

* Wed Jul 19 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-2
- fix release

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-1.2.1.1
- rebuild

* Mon May 22 2006 Darshan Santani <dsantani@redhat.com>
- New source tarball added.
- Rebuild.

* Thu May 18 2006 Jens Petersen <petersen@redhat.com>
- configure with --disable-static
- exclude INSTALL from docs

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.2.7-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.2.7-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Aug 16 2005 Jens Petersen <petersen@redhat.com> - 0.2.7-1
- Initial build for Fedora Core
- cleanup spec file according to Fedora standard

* Fri Dec 31 2004 rabit <rabit@ipserv.org> 0.2.5-fc3
- update for 0.2.5. and fedora core 3

* Thu Oct 8 2004 rabit <rabit@ipserv.org> 0.2.4-fc2
- update for 0.2.4.

* Thu Oct 7 2004 rabit <rabit@ipserv.org> 0.2.3-fc2
- Initial build.
