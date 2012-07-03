Name: tcl-sasl
Version: 1.0
Release: alt1

Summary: Tcl bindings to SASL2 library
License: Distributable
Group: Development/Tcl
Url: http://beepcore-tcl.sourceforge.net/

Source: %name-%version-%release.tar

BuildRequires(pre): rpm-build-tcl >= 0.4-alt1
BuildRequires: libsasl2-devel tcl-devel >= 8.5.0

%description
%name in a Tcl bindings to SASL2 library

%prep
%setup
%teapatch

%build
aclocal
autoconf
%configure
make

%install
%makeinstall

%files
%doc doc/*.html
%_tcllibdir/*
%_tcldatadir/*

%changelog
* Sun Dec 28 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- updated to TEA 3.5 and current autotools

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt0.3
- fixed build for x86_64

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt0.2
- updated to TEA3.1

* Sat Jun 19 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt0.1
- initial build for %distribution
