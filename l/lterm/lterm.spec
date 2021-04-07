Summary: The free terminal and multiprotocol client for Linux
Name: lterm
Version: 1.5.1
Release: alt2
License: GPLv2+
Group: Terminals
Url: http://lterm.sourceforge.net/
Source0: %name-%version.tar
Patch1: lterm-no-ssh_threads.patch

BuildRequires: libssl-devel libssh-devel libvte3-devel libgtk+3-devel rpm-build-xdg

%description
lterm is a vte-based terminal emulator for GNU/Linux systems. It is mainly used as SSH/Telnet client but can be very easily configured to use any other protocol. Furthermore it can be a usual terminal on local host.
Includes some features in order to ease user's work, avoid repetitive tasks and improve speed in operations, see a list below.
Available for Mac OS X (with XQuartz).

Features:

    Bookmarks
    Upload and download via SFTP
    Remote text files editing
    Remote files and directories management
    Color/style profiles management
    Expandable protocol set
    Session saving and recovery
    Tabs with activity alerts
    Password saving with encryption
    Customizable mouse behaviour
    Full screen mode

%prep
%setup
%patch1 -p2

%build
%autoreconf
%add_optflags -fcommon
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_xdgmimedir/*/%{name}*
%_datadir/%name
%doc ChangeLog NEWS AUTHORS TODO README

%changelog
* Wed Apr 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt2
- Fixed FTBFS with -fcommon.

* Sun Oct 28 2018 Terechkov Evgenii <evg@altlinux.org> 1.5.1-alt1
- 1.5.1
- Patch1 to avoid linking with libssh_threads (non-existent)

* Thu Jul 14 2016 Terechkov Evgenii <evg@altlinux.org> 1.3.2-alt1
- Initial build for ALT Linux Sisyphus
