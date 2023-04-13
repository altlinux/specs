%define download_name stund

Name: stun
Version: 0.97
Release: alt3

Summary: Implements a simple Stun Client

License: Vovida Software License 1.0
Group: Communications
Url: http://sourceforge.net/projects/stun

# Source-url: http://downloads.sourceforge.net/%name/%download_name-%version.tgz
Source: %name-%version.tar
Patch: patch0.diff

BuildRequires: gcc-c++

%description
Implements a simple STUN client.
The STUN protocol (Simple Traversal of UDP through NATs) is described in the
IETF RFC 3489, available at http://www.ietf.org/rfc/rfc3489.txt

%package server
Group: Communications
Summary: Implements the Stun Server

%description server
Implements a simple STUN server.
The STUN protocol (Simple Traversal of UDP through NATs) is described in the
IETF RFC 3489, available at http://www.ietf.org/rfc/rfc3489.txt

%prep
%setup
%patch0 -p0

%build
%make_build

%install
install -D client %buildroot%_bindir/stun-client
install -D server %buildroot%_sbindir/stun-server

%files
%doc rfc3489.txt
%_bindir/stun-client

%files server
%doc readme.txt
%doc rfc3489.txt
%_sbindir/stun-server

%changelog
* Thu Apr 13 2023 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt3
- manual build for ALT Sisyphus

* Wed Feb 22 2023 Igor Vlasenko <viy@altlinux.org> 0.97-alt2_21
- update to new release by fcimport
...

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_9
- initial fc import

