Summary: PAM cached credentials module
Name: pam_ccreds
Version: 10
Release: alt1
Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

Source: ftp://ftp.padl.com/pub/%name-%version.tar
Url: http://www.padl.com/
License: GPL
Group: System/Base

BuildRequires: libssl-devel libpam0-devel libdb4-devel

%description
The pam_ccreds module provides a mechanism for caching
credentials when authenticating against a network
authentication service so that authentication can still
proceed when the service is down.

%prep
%setup

%build
%configure
make

%install
mkdir -p %buildroot/%{_lib}/security/

install pam_ccreds.so %buildroot/%{_lib}/security/


%files
/%{_lib}/security/pam_ccreds.so
%doc AUTHORS NEWS COPYING README ChangeLog

%changelog
* Mon Oct 08 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 10-alt1
- initial build for ALT Linux Sisyphus


