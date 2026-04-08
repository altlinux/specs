%define _unpackaged_files_terminate_build 1

Name: altsign
Version: 0.3.0
Release: alt2

Summary: Submit files for signing to altsign-agent
License: GPL-2.0-or-later
URL: https://git.altlinux.org/gears/a/altsign.git
VCS: https://git.altlinux.org/gears/a/altsign.git
Group: Networking/Other

Source0: %name-%version.tar

BuildRequires: meson

%description
Altsign provides tools for signing kernel modules and PE binaries
via a remote alt-signer service over SSH.

This package contains the altsign client that sends files to an
altsign-agent session for signing. Designed to run inside a hasher
chroot with the session socket bind-mounted from the host.

%package -n altsign-agent
Summary: Daemon for remote code signing via alt-signer
Group: Networking/Other

%description -n altsign-agent
Local daemon that manages signing sessions and forwards requests
to a remote alt-signer service over SSH. Authorizes clients via
UNIX socket peer credentials. Use altsign-set to create sessions
and altsign to submit files for signing.

%package -n altsign-set
Summary: Create signing sessions for altsign-agent
Group: Networking/Other

%description -n altsign-set
Requests a signing session for a specific certificate from altsign-agent.
Prints the session socket path for use with altsign.

%package -n altsign-agent-module
Summary: SysV init service for kernel module signing
Group: Networking/Other
BuildArch: noarch
Requires: altsign-agent = %EVR

%description -n altsign-agent-module
Init script and configuration for running altsign-agent in kernel
module signing mode. Creates altsign-module user and altsign-module-admin
group for access control.

%package -n altsign-agent-pe
Summary: SysV init service for PE binary signing
Group: Networking/Other
BuildArch: noarch
Requires: altsign-agent = %EVR

%description -n altsign-agent-pe
Init script and configuration for running altsign-agent in PE binary
signing mode. Creates altsign-pe user and altsign-pe-admin group
for access control.

%prep
%setup -q

%build
%meson -Dinitddir=%_initddir -Dsysconfigdir=%_sysconfdir/sysconfig
%meson_build

%install
%meson_install

install -d %buildroot%_localstatedir/altsign-module
install -d %buildroot%_localstatedir/altsign-pe

mkdir -p %buildroot/run/altsign-module/session/sockdir
touch %buildroot/run/altsign-module/control.sock
touch %buildroot/run/altsign-module/session/sockdir/session.sock

mkdir -p %buildroot/run/altsign-pe/session/sockdir
touch %buildroot/run/altsign-pe/control.sock
touch %buildroot/run/altsign-pe/session/sockdir/session.sock

%check
%meson_test

%pre -n altsign-agent-module
getent group altsign-module >/dev/null || /usr/sbin/groupadd -r altsign-module
getent passwd altsign-module >/dev/null || \
    /usr/sbin/useradd -r -g altsign-module -d %_localstatedir/altsign-module \
        -c "ALT signer module agent user" altsign-module
getent group altsign-module-admin >/dev/null || /usr/sbin/groupadd -r altsign-module-admin

%pre -n altsign-agent-pe
getent group altsign-pe >/dev/null || /usr/sbin/groupadd -r altsign-pe
getent passwd altsign-pe >/dev/null || \
    /usr/sbin/useradd -r -g altsign-pe -d %_localstatedir/altsign-pe \
        -c "ALT signer PE agent user" altsign-pe
getent group altsign-pe-admin >/dev/null || /usr/sbin/groupadd -r altsign-pe-admin

%files -n altsign-agent
%doc LICENSE README.md ADMIN.md
%_bindir/altsign-agent
%_mandir/man8/altsign-agent.8*

%files -n altsign-set
%doc LICENSE README.md
%_bindir/altsign-set
%_mandir/man1/altsign-set.1*

%files
%doc LICENSE README.md
%_bindir/altsign
%_mandir/man1/altsign.1*

%files -n altsign-agent-module
%_initddir/altsign-agent-module
%config(noreplace) %_sysconfdir/sysconfig/altsign-agent-module
%attr(0700, altsign-module, root) %dir %_localstatedir/altsign-module
%ghost %dir %attr(0750, altsign-module, altsign-module-admin) /run/altsign-module/
%ghost %attr(0666, altsign-module, altsign-module) /run/altsign-module/control.sock
%ghost %dir %attr(0750, altsign-module, altsign-module) /run/altsign-module/session
%ghost %dir %attr(0755, altsign-module, altsign-module) /run/altsign-module/session/sockdir
%ghost %attr(0666, altsign-module, altsign-module) /run/altsign-module/session/sockdir/session.sock

%files -n altsign-agent-pe
%_initddir/altsign-agent-pe
%config(noreplace) %_sysconfdir/sysconfig/altsign-agent-pe
%attr(0700, altsign-pe, root) %dir %_localstatedir/altsign-pe
%ghost %dir %attr(0750, altsign-pe, altsign-pe-admin) /run/altsign-pe/
%ghost %attr(0666, altsign-pe, altsign-pe) /run/altsign-pe/control.sock
%ghost %dir %attr(0750, altsign-pe, altsign-pe) /run/altsign-pe/session
%ghost %dir %attr(0755, altsign-pe, altsign-pe) /run/altsign-pe/session/sockdir
%ghost %attr(0666, altsign-pe, altsign-pe) /run/altsign-pe/session/sockdir/session.sock

%changelog
* Wed Apr 08 2026 Egor Ignatov <egori@altlinux.org> 0.3.0-alt2
- Do not set /sbin/nologin shell for service users

* Mon Feb 09 2026 Egor Ignatov <egori@altlinux.org> 0.3.0-alt1
- Replaced signal handlers with signalfd+ppoll event loops
- Fixed multiple IPC security issues (fd leaks, heap over-read,
  SIGPIPE, SSH argument injection)

* Fri Feb 06 2026 Egor Ignatov <egori@altlinux.org> 0.2.0-alt2
- Added Requires: altsign-agent to -module and -pe subpackages
- Added ghost entries for runtime directories and sockets

* Tue Feb 03 2026 Egor Ignatov <egori@altlinux.org> 0.2.0-alt1
- Renamed project from alt-signer-client to altsign
- Binaries: alt-signer-proxy -> altsign-agent, alt-signer-sign -> altsign,
  alt-signer-set-cert -> altsign-set
- Source files: proxy.c/h -> altsign_agent.c/h,
  proxy_session.c -> altsign_agent_session.c, sign.c -> altsign.c,
  set-cert.c -> altsign_set.c
- Constants: PROXY_* -> AGENT_*
- Tests: proxy_*.sh -> agent_*.sh, ALT_SIGNER_*_BIN -> ALTSIGN_*_BIN
- Services: alt-signer-module -> altsign-agent-module,
  alt-signer-pe -> altsign-agent-pe
- Environment variables: ALT_SIGNER_* -> ALTSIGN_AGENT_*
- System users: alt-signer-* -> altsign-*
- Paths: /run/alt-signer-* -> /run/altsign-*

* Thu Mar 27 2025 Egor Ignatov <egori@altlinux.org> 0.1.0-alt1
- First build for ALT.
