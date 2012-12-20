%def_enable shared
%def_enable static

%define bname ecap
%define lname lib%bname
Name: %{lname}0
Version: 0.0.3
Release: alt1
Summary: libecap library implements eCAP API in C++
License: BSD
Group: System/Legacy libraries
URL: http://www.e-cap.org/
Source: http://www.measurement-factory.com/tmp/%bname/%lname-%version.tar
Provides: %lname = %version-%release

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
Provides: %lname-devel = %version-%release
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release
Conflicts: %lname-devel > %version-%release

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
developing %lname applications.


%if_enabled static
%package devel-static
Summary: Libraries and header files for the libecap library
Group: Development/C++
Provides: %lname-devel-static = %version-%release
Requires: %lname-devel = %version-%release
Conflicts: %lname-devel-static > %version-%release

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

This package provides the static %lname library needed for developing static
%lname applications.
%endif


%prep
%setup -q -n %lname-%version

%build
%configure %{subst_enable shared} %{subst_enable static}
%make_build


%install
%makeinstall_std
install -d -m 0755 %buildroot%_docdir/%lname-%version
install -p -m 0644 LICENSE CREDITS NOTICE README %buildroot%_docdir/%lname-%version/


%if_enabled shared
%files
%doc %_docdir/%lname-%version
%_libdir/*.so.*
%endif


%files devel
%if_disabled shared
%doc %_docdir/%lname-%version
%else
%_libdir/*.so
%endif
%_includedir/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Thu Dec 20 2012 Led <led@altlinux.ru> 0.0.3-alt1
- initial build
