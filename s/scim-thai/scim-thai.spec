# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           scim-thai
Version:        0.1.3
Release:        alt1_5
Summary:        Thai Input Method Engine for SCIM

Group:          System/Libraries
License:        GPLv2+
URL:            http://linux.thai.net/projects/scim-thai
Source0:        ftp://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.gz
Patch0:         scim-thai-fixes-setup-dialog.patch

BuildRequires:  scim-devel, libthai-devel
%ifarch aarch64
BuildRequires:	autoconf
%endif
Requires:       scim
Source44: import.info

%description
SCIM-Thai is a SCIM IMEngine module for Thai, based on the libthai library.

Currently, it supports Ketmanee, TIS-820.2538, and Pattachote keybaord layouts
and can validate input sequences at 3 levels of strictness.

For applications that support surrounding text retrieval/deleting,
it also corrects invalid input sequences.


%prep
%setup -q
%patch0 -p1 -b .gtk2


%build
%ifarch aarch64
autoconf
%endif
%configure --disable-static
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/{IMEngine,SetupUI}/thai*.la
%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/scim-1.0/*/IMEngine/thai.so
%{_libdir}/scim-1.0/*/SetupUI/thai-imengine-setup.so
%{_datadir}/scim/icons/scim-thai.png


%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_5
- NMU (for oddity@): new version by fcimport

* Sat Oct 17 2015 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.1.1-alt2.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.1.1-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_12
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_11
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_10
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_9
- initial fc import

