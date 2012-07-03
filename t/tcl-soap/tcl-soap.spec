# -*- rpm-spec -*-
# $Id: tcl-soap,v 1.3 2004/11/03 11:11:24 me Exp $

%define snapshot 20040923

%add_tcl_req_skip beepcore::log
%add_tcl_req_skip beepcore::mixer
%add_tcl_req_skip beepcore::peer

Name: tcl-soap
Version: 1.6.8
Release: alt0.2

Summary: Tcl commands for SOAP remote procedure calls
License: BSD
Group: Development/Tcl
URL: http://tclsoap.sourceforge.net/

%ifdef snapshot
Source: %name-%snapshot.tar.bz2
%else
Source: TclSOAP-%version.tar.bz2
%endif

Patch0: %name-1.6.7-alt-dom3.patch

BuildRequires: tcl-devel >= 8.4.0-alt1 rpm-build >= 4.0.4-alt41
BuildArch: noarch

%description
Provide support for building clients and servers for the
SOAP remote procedure call protocol from Tcl. SOAP is an 
XML based RPC mechanism which provides cross-platform
cross language compatability.

%prep
%setup -q %{?snapshot:-c}%{!?snapshot:-n tclsoap%version}
%patch -p1

%build
%__chmod +x ./configure
%configure

%install 
%makeinstall libdir=%buildroot%_tcldatadir

%files
%doc CHANGES LICENSE doc samples
%_tcldatadir/tclsoap%version

%changelog
* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.8-alt0.2
- rebuilt against new shiny tcl reqprov finder

* Thu Sep 23 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.8-alt0.1
- CVS snapshot @20040923 

* Wed Sep 22 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.7-alt0.2
- adopted for use with dom 3.0

* Tue May 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.7-alt0.1
- Initial build for %distribution

