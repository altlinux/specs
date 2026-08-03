%define _unpackaged_files_terminate_build 1
%define oname net.sf.teg

Name: teg
Version: 0.13.0
Release: alt1

Summary: Turn based strategy game
License: GPLv2
Group: Games/Other

Url: https://github.com/wfx/teg
Vcs: https://github.com/wfx/teg

Source0: %name-%version.tar
Source1: teg.desktop

Requires(pre):  GConf libGConf
Requires(post): GConf libGConf
Requires(preun): GConf libGConf

BuildRequires: gcc-c++ libstdc++-devel
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: libgoocanvas2-devel libgoocanvas2-gir-devel
BuildRequires: xmlto
BuildRequires: tidy
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: libxml2-devel
BuildRequires: libgnomeui-devel
BuildRequires: gettext gettext-tools
BuildRequires: gettext-tools libasprintf-devel
BuildRequires: perl(XML/Parser.pm)
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/desktop-file-install libgmock-devel libgtest-devel libreadline-devel

%description
Tenes Empanadas Graciela is a clone of Plan TA.ctico y EstratA.gico de la
Guerra, a turn based strategy game. Some rules are different.

%prep
%setup
for file in AUTHORS COPYING TODO PEOPLE ChangeLog; do
    iconv -f iso8859-1 -t utf-8 < $file > $file.$$
    mv -f $file.$$  $file
done
subst 's|stdc++fs|stdc++|' configure.ac

%build
./autogen.sh
%global optflags %optflags -fcommon
%configure
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/gconf/gconf.xml.defaults
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT/%_datadir/pixmaps/
mv -f $RPM_BUILD_ROOT/%_datadir/pixmaps/teg_icono.png $RPM_BUILD_ROOT/%_datadir/pixmaps/teg.png
rm -rf $RPM_BUILD_ROOT/%_datadir/gnome/apps/Games/teg.desktop
desktop-file-install \
  --dir=$RPM_BUILD_ROOT/%_datadir/applications %SOURCE1

pushd .
cd $RPM_BUILD_ROOT/%_datadir/locale
for a in *.gmo; do
    mv -f $a/LC_MESSAGES/teg@INSTOBJEXT@ $a/LC_MESSAGES/teg.mo
    mv -f $a `basename $a .gmo`
done
popd

%find_lang %name --all-name

%files -f %name.lang
%doc AUTHORS COPYING README.md TODO PEOPLE ChangeLog
%_bindir/%{name}*
%_datadir/GConf/gsettings/%name.convert
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/%oname.gschema.xml
%_datadir/gnome/help/%name
%_datadir/pixmaps/%name.png
%_datadir/%name

%changelog
* Mon Aug 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.13.0-alt1
- 0.12.0 -> 0.13.0
- add VCS
- spec cleanup

* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 0.12.0-alt1_2
- fixed build

* Thu Apr 15 2021 Igor Vlasenko <viy@altlinux.org> 0.12.0-alt1_1
- update to new release by fcimport

* Thu Apr 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_46
- update to new release by fcimport

* Sun Dec 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_42
- rebuild with readline7

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_40
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_39
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_37
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_36
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_35
- new version

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_32
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_31
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_30
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_29
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_28
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_27
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_27
- update to new release by fcimport

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_26
- updated by fcimport

* Wed Jul 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_25
- initial release by fcimport

