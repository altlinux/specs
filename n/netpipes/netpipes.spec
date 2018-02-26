Summary:	A set of command line utilities for network services access
Name:		netpipes
Version:	4.2
URL:		http://web.purplefrog.com/~thoth/netpipes/netpipes.html
Release:	alt1
Copyright:	GPL
Group:		Networking/Other
Source:		%name-%version.tar

%description
This package contains a set of command line utilities that can be used
to access other computers in a networked environment.

%prep
%setup -q

%build
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %buildroot/%_bindir %buildroot/%_mandir

%make	INSTROOT="%buildroot" \
	INSTBIN="%buildroot/%_bindir" \
	INSTMAN="%buildroot/%_mandir" \
		install

rm -f -- %buildroot/%_man1dir/ssl-auth.*

%files
%_bindir/*
%_man1dir/*
%doc COPYING README

%changelog
* Mon Jun 11 2007 Alexey Gladkov <legion@altlinux.ru> 4.2-alt1
- First build for ALT Linux

