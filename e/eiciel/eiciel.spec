Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate pkgconfig(giomm-2.4) pkgconfig(gtkmm-2.4) pkgconfig(libgnome-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: eiciel
Version: 0.9.13.1
Release: alt1_1
Summary: Graphical editor for ACLs and xattr
License: GPLv2+
URL: http://rofi.roger-ferrer.org/eiciel
Source0: http://rofi.roger-ferrer.org/eiciel/files/eiciel-%{version}.tar.bz2

BuildRequires: gcc-c++
BuildRequires: libgnomeui-devel
BuildRequires: libacl-devel
BuildRequires: libnautilus-devel libnautilus-gir-devel
BuildRequires: libgtkmm3-devel
BuildRequires: desktop-file-utils

%global ext_dir %(eval "pkg-config --variable=extensiondir libnautilus-extension")

# don't "provide" a private shlib
%{echo 


}
Source44: import.info
%add_findprov_skiplist %{ext_dir}/.*\.so$

%description
Graphical editor for access control lists (ACLs) and extended attributes
(xattr), either as an extension within Nautilus, or as a standalone
utility.


%prep
%setup -q

sed -i -e 's!attr/xattr\.h!sys/xattr\.h!g' configure
[ "$(cksum ChangeLog|cut -d ' ' -f 1,2)" != "960335718 502" ] && exit -1

iconv -f ISO-8859-1 -t UTF-8 AUTHORS > foo ; mv foo AUTHORS


%build
%add_optflags -std=c++11
%configure --with-nautilus-extensions-dir=%{ext_dir} \
    --disable-static
V=1 make %{?_smp_mflags}


%install
%makeinstall_std
%find_lang %{name}

rm -f %{buildroot}%{ext_dir}/*.la

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc AUTHORS README
%doc --no-dereference COPYING
# ancient gettextize file only / recheck for new releases
#%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/gnome/help/%{name}/
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}*
%{ext_dir}/lib%{name}*.so
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*


%changelog
* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.9.13.1-alt1_1
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.13-alt1_1
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.12.1-alt2_8
- update to new release by fcimport

* Wed Apr 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.12.1-alt2_5
- to Sisyphus (closes: #35839)

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.12.1-alt1_5
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.12.1-alt1_4
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_5
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_4
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_3
- update to new release by fcimport

* Sat Oct 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_1
- new update

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_1
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.8.2-alt1_2
- update to new release by fcimport

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.2-alt1_1
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_10
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_9
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_8
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_7
- update to new release by fcimport

* Thu Dec 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_6
- fc import

