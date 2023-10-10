Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/mysql_config /usr/bin/unzip /usr/bin/xsltproc gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define python_binding 0
%define ruby_binding 0

Name:           tomoe
Version:        0.6.0
Release:        alt3_54
Summary:        Handwritten input system for Japanese and Chinese

License:        LGPL-2.1-or-later
URL:            http://tomoe.sourceforge.jp/
## stripped tarball is generated as follows:
# $ wget http://downloads.sourceforge.net/sourceforge/tomoe/%{name}-%{version}.tar.gz
# $ ./strip.sh %{name}-%{version}.tar.gz
Source0:        %{name}-stripped-%{version}.tar.gz
Source1:        strip.sh
Patch0:         tomoe-0.6.0-multiarch-conflict.patch
Patch1:         tomoe-0.6.0-bz502662.patch
Patch2:         tomoe-0.6.0-fixes-glib-includes.patch
Patch3:         tomoe-0.6.0-fixes-set-parse-error.patch
Patch4:         tomoe-strerror.patch

BuildRequires:  glib2-devel libgio libgio-devel, gettext-tools gtk-doc gtk-doc-mkpdf, libtool, intltool
BuildRequires:  perl(XML/Parser.pm), python3
%if %{python_binding}
BuildRequires:  python-module-pygobject-devel, python-devel, python-module-pygtk-devel
%endif
%if %{ruby_binding}
BuildRequires:  ruby-glib2-devel
%endif
Source44: import.info
## for extra dictionary backends
#BuildRequires:  mariadb-connector-c-devel, subversion-devel, hyperestraier-devel

%description
A program which does Japanese handwriting recognition.


%package devel
Group: Development/Other
Summary:    Tomoe development files
Requires:   %{name} = %{version}-%{release}

%description devel
The tomoe-devel package includes the header files for the tomoe package.
Install this package if you want to develop programs which use tomoe.


%prep
%setup -q
%patch0  -p0 -b .multiarch-conflict
%patch1  -p0 -b .bz502662
%patch2  -p1 -b .glib
%patch3  -p1 -b .compile
%patch4  -p1 -b .strerror

%build
./autogen.sh
%configure --disable-static --enable-gtk-doc
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

%if !%{ruby_binding}
rm -f $RPM_BUILD_ROOT%{_libdir}/ruby/site_ruby/*/tomoe.rb $RPM_BUILD_ROOT%{_libdir}/ruby/site_ruby/*/*-linux/*
%endif
chmod 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/xml2est.rb

# remove .la files
find ${RPM_BUILD_ROOT}%{_libdir} -name '*.la' | xargs rm

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO data/kanjidic*.html
%{_libdir}/libtomoe.so.*
%if %{python_binding}
%{_libdir}/python?.?/site-packages/tomoe.so
%endif
%{_libdir}/tomoe
%{_datadir}/tomoe
%dir %{_sysconfdir}/tomoe
%config(noreplace) %{_sysconfdir}/tomoe/config


%files devel
%{_libdir}/libtomoe.so
%{_includedir}/tomoe
%{_libdir}/pkgconfig/tomoe.pc
%{_datadir}/gtk-doc
%if %{python_binding}
%{_libdir}/pkgconfig/pytomoe.pc
%endif
%if %{ruby_binding}
%{_libdir}/ruby/site_ruby/1.8/tomoe.rb
%{_libdir}/ruby/site_ruby/1.8/*-linux/*
%endif

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt3_54
- update to new release by fcimport

* Thu Sep 29 2022 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt3_50
- to Sisyphus as zinnia dep

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt2_50
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt2_49
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt2_48
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt2_47
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_46
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_46
- update to new release by fcimport

* Tue Mar 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_44
- update to new release by fcimport

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_43
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_42
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_41
- update to new release by fcimport

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_40
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_39
- update to new release by fcimport

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_37
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_34
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_33
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_32
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_31
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_30
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_29
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_28
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_26
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_25
- initial fc import

