Name: kookish
Version: 0.1
Release: alt4

Summary: Set of scripts for building projects using cook
License: GPL
Group: Development/Other
Url: http://voins.program.ru/kookish
BuildArch: noarch

Requires: cook >= 2.24-alt1

#%package docs
#Summary: Documentation for kookish
#Group: Development/Other

Source: %url/%name-%version.tar.bz2

# Automatically added by buildreq on Tue Jan 25 2005 (-bi)
BuildRequires: cook

%description
Set of scripts for building projects using cook.

#%description docs

%prep
%setup -q

%install
cook -b main.cook install destdir=$RPM_BUILD_ROOT

%files
%_datadir/%name

%changelog
* Tue Jan 25 2005 Alexey Voinov <voins@altlinux.ru> 0.1-alt4
- description fixed
- buildreqs fixed

* Wed Jan 19 2005 Alexey Voinov <voins@altlinux.ru> 0.1-alt3
- new snapshot

* Mon Oct 11 2004 Alexey Voinov <voins@altlinux.ru> 0.1-alt2
- new snapshot.
- use own installation routine

* Tue Sep 21 2004 Alexey Voinov <voins@altlinux.ru> 0.1-alt1
- initial build
