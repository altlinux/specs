%def_enable shared
%def_enable static

%define bname ecap
Name: lib%bname
Version: 0.2.0
Release: alt3
Summary: libecap library implements eCAP API in C++
License: BSD
Group: System/Legacy libraries
URL: http://www.e-cap.org/
Source: http://www.measurement-factory.com/tmp/%bname/%name-%version.tar
Provides: %{name}2 = %version-%release

BuildRequires: gcc-c++

%description
eCAP is a software interface that allows a network application, such as an HTTP
proxy or an ICAP server, to outsource content analysis and adaptation to a
loadable module. For each applicable protocol message being processed, an
eCAP-enabled host application supplies the message details to the adaptation
module and gets back an adapted message, a "not interested" response, or a "block
this message now!" instruction. These exchanges often include message bodies.
The adaptation module can also exchange meta-information with the host
application to supply additional details such as configuration options, a reason
behind the decision to ignore a message, or a detected virus name.


%package devel
Summary: Libraries and header files for the libecap library
Group: Development/C++
Provides: %name-devel = %version-%release
Requires: %name%{?_disable_shared:-devel-static} = %version-%release
Conflicts: %{name}0-devel

%description devel
eCAP is a software interface that allows a network application, such as an HTTP
proxy or an ICAP server, to outsource content analysis and adaptation to a
loadable module. For each applicable protocol message being processed, an
eCAP-enabled host application supplies the message details to the adaptation
module and gets back an adapted message, a "not interested" response, or a "block
this message now!" instruction. These exchanges often include message bodies.
The adaptation module can also exchange meta-information with the host
application to supply additional details such as configuration options, a reason
behind the decision to ignore a message, or a detected virus name.

This package provides the library, include files, and other resources needed for
developing %name applications.


%if_enabled static
%package devel-static
Summary: Libraries and header files for the libecap library
Group: Development/C++
Provides: %name-devel-static = %version-%release
Requires: %name-devel = %version-%release
Conflicts: %{name}0-devel-static

%description devel-static
eCAP is a software interface that allows a network application, such as an HTTP
proxy or an ICAP server, to outsource content analysis and adaptation to a
loadable module. For each applicable protocol message being processed, an
eCAP-enabled host application supplies the message details to the adaptation
module and gets back an adapted message, a "not interested" response, or a "block
this message now!" instruction. These exchanges often include message bodies.
The adaptation module can also exchange meta-information with the host
application to supply additional details such as configuration options, a reason
behind the decision to ignore a message, or a detected virus name.

This package provides the static %name library needed for developing static
%name applications.
%endif


%prep
%setup -q

%build
%configure %{subst_enable shared} %{subst_enable static}
%make_build


%install
%makeinstall_std
install -d -m 0755 %buildroot%_docdir/%name-%version
install -p -m 0644 LICENSE CREDITS NOTICE README %buildroot%_docdir/%name-%version/


%if_enabled shared
%files
%doc %_docdir/%name-%version
%_libdir/*.so.*
%endif


%files devel
%_pkgconfigdir/*
%if_disabled shared
%doc %_docdir/%name-%version
%else
%_libdir/*.so
%endif
%_includedir/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Sun Oct 06 2013 Led <led@altlinux.ru> 0.2.0-alt3
- dropped wry fcimport'ed crap
- added subpackage with static library

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_4
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_2
- initial import by fcimport
