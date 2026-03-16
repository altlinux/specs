Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 3

Name:           boswars
Version:        2.8
Release:        alt1_4
Summary:        Bos Wars is a futuristic real-time strategy game
License:        GPL-2.0-only
URL:            https://www.boswars.org/
Source0:        https://www.boswars.org/dist/releases/boswars-2.8-src.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}-48.png
Source3:        %{name}-128.png
Source4:        %{name}.appdata.xml
Source5:        %{name}.6
Patch1:		boswars-0001-Convert-to-UTF-8.patch
Patch2:		boswars-0002-fabricate.py-remove-deprecated-calls-to-os.stat_floa.patch
Patch3:		boswars-0003-build-detect-alternative-name-for-Lua-5.1-libs.patch
BuildRequires:	libSDL-devel
BuildRequires:	liblua5.1-devel
#BuildRequires:	compat-tolua++-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libGL-devel
BuildRequires:	libappstream-glib libappstream-glib-gir
BuildRequires:	libpng-devel libpng17-tools
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	python3
BuildRequires:	zlib-devel
Requires:       icon-theme-hicolor
Provides:	bundled(guichan)
Provides:	bundled(tolua++)
Source44: import.info

%description
Bos Wars is a futuristic real-time strategy game. It is possible to play
against human opponents over LAN, internet, or against the computer.
Bos Wars aims to create a completly original and fun open source RTS game.


%prep
%setup -q -n %{name}-%{version}-src
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i -e "s|-Wall -fsigned-char -D_GNU_SOURCE=1 -D_REENTRANT|%{optflags}|g" make.py
find campaigns engine maps -type f -executable -exec chmod -x {} ';'
# FIXME we want to use the system version of compat-tolua++
# rm engine/tolua/*.h engine/tolua/tolua_*.cpp


%build
/usr/bin/python3 make.py

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/languages
install -D -p -m 755 fbuild/release/boswars %{buildroot}%{_bindir}/%{name}
install -p -m 644 languages/*.po languages/*.pot \
  %{buildroot}%{_datadir}/%{name}/languages
cp -a campaigns graphics intro maps scripts sounds units patches \
  %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}
install -D -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -D -p -m 644 %{SOURCE3} \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -D -p -m 644 %{SOURCE4} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
install -D -p -m 644 %{SOURCE5} %{buildroot}%{_mandir}/man6/%{name}.6


%files
%doc README.txt CHANGELOG doc/*.html
%doc --no-dereference COPYRIGHT.txt LICENSE.txt doc/guichan-copyright.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*


%changelog
* Mon Mar 16 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.8-alt1_4
- NMU: fix FTBFS with zlib

* Tue Apr 08 2025 Igor Vlasenko <viy@altlinux.org> 2.8-alt1_3
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_24.svn160110
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_22.svn160110
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_21.svn160110
- update to new release by fcimport

* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_19.svn160110
- fixed build

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_14.svn160110
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_13.svn160110
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_11.svn160110
- update to new release by fcimport

* Fri Feb 10 2017 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_10.svn160110
- new version

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.6.1-alt1.1.qa1
- NMU: rebuilt for updated dependencies.

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1.1
- Rebuilt with libpng15

* Wed Jun 23 2010 Egor Glukhov <kaman@altlinux.org> 2.6.1-alt1
- 2.6.1 (specfile based on Fedora's)
