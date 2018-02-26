Name: hlds-counterstrike-init
Version: 0.2
Release: alt1
Summary: HLDS CounterStrike initscript
License: GPL
Group: Networking/Other
URL: http://git.altlinux.org/people/thresh/packages/?p=hlds-counterstrike-init.git

Packager: Pavlov Konstantin <thresh@altlinux.ru>
Source1: hlds.init

BuildArch: noarch

Requires: screen
Requires: su
Requires: gawk
Requires: qstat

%description 
A modification of the CS Server startup script, to run the server
as a non-root user.

ORIGINAL AUTHORS :
Julien Escario ( pandemik@asylog.net )
&
Cedric Rochat ( crochat@younics.org )

ALTLinux fixes by Pavlov Konstantin ( thresh@altlinux.ru )

See the initscript itself for further details.

%install
mkdir -p %buildroot%_initdir

install -m755 %SOURCE1 %buildroot%_initdir/hlds

%pre
%_sbindir/groupadd -r -f _netgames 2>/dev/null ||:
%_sbindir/useradd -g _netgames -c 'Network games pseudouser' -d /dev/null -s '' -r _netgames 2>/dev/null ||:

%post
%post_service hlds

%preun
%preun_service hlds

%files
%_initdir/hlds

%changelog
* Sun Jan 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2-alt1
- Added qstat query check on status event.

* Sun Jan 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.1-alt1
- Initial packaging for ALT Linux.


