%set_verify_elf_method relaxed
%define _ruleuserdir %buildroot%_datadir/ruleuser

Name: ruleuser
Version: 1.1.0
Release: alt1
Summary: RuleUser - Management program.
Group: Networking/Remote access
License: GPLv2
Requires: python, python-module-pygtk, libgtkvnc, python-module-gtkvnc
Requires: sshfs-fuse, wol
Requires: coreutils, net-tools, glibc-utils, procps, nmap, xinput, xset
Requires: tightvnc, x11vnc, vlc
Obsoletes: RuleUser
AutoReqProv: no
BuildArch: noarch
Url: http://www.altlinux.org/LTSP
# DVCS: https://github.com/temaps/ruleuser
Source0: ruleuser.tar
Source1: ChangeLog.ru

%description
Management program for Linux terminal server and standalone clients.
Special for ALT Linux School.

%prep
%setup -n %name
cp %SOURCE1 .

%install
install -D -m 0644 ruleuser.desktop %buildroot%_desktopdir/ruleuser.desktop
install -D -m 0755 ruleuser %buildroot%_bindir/ruleuser

mkdir -p %_ruleuserdir
install -m 0644 *.py %_ruleuserdir

mkdir -p %_ruleuserdir/icons
install -m 0644 icons/* %_ruleuserdir/icons/

mkdir -p %_ruleuserdir/locale/ru/LC_MESSAGES/
install -m 0644 locale/ru/LC_MESSAGES/*.mo %_ruleuserdir/locale/ru/LC_MESSAGES/

install -D -m 0644 ruleuser-client %{_ruleuserdir}-client/ruleuser-client

%files
%doc ChangeLog.ru README LICENSE
%_bindir/ruleuser
%_datadir/ruleuser
%_desktopdir/ruleuser.desktop

%package -n ruleuser-client
Summary: RuleUser - Management program. Client side.
Group: Networking/Remote access
Requires: coreutils, net-tools, glibc-utils, procps, nmap, xinput, xset
Requires: tightvnc, x11vnc, vlc
BuildArch: noarch

%description -n ruleuser-client
Management program for Linux terminal server and standalone clients
Special for ALT Linux School.
Client side.

%files -n ruleuser-client
%_datadir/ruleuser-client/ruleuser-client

%changelog
* Fri May 26 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version (thanks Artem <tema@>)

* Wed May 29 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt5
- Initial import to Sisyphus
