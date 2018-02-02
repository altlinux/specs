Name: mergerfs-tools
Version: 0.1
Release: alt1

Summary: Optional tools to help manage data in a mergerfs pool

Group: File tools
License: MIT
Url: https://github.com/trapexit/mergerfs-tools

Obsoletes: mergerfs-fsck
Provides: mergerfs-fsck = %version

# Source-git: https://github.com/trapexit/mergerfs-tools.git
Source: %name-%version.tar

BuildArch: noarch

%description
Optional tools to help manage data in a mergerfs pool.
 * mergerfs.ctl: A tool to make it easier to query and configure mergerfs at runtime
 * mergerfs.fsck: Provides permissions and ownership auditing and the ability to fix them
 * mergerfs.dedup: Will help identify and optionally remove duplicate files
 * mergerfs.balance: Rebalance files across drives by moving them from the most filled to the least filled
 * mergerfs.mktrash: Creates FreeDesktop.org Trash specification compatible directories on a mergerfs mount

%prep
%setup

%build

%install
make install INSTALLBINDIR=%buildroot%_bindir

%files
%_bindir/mergerfs.balance
%_bindir/mergerfs.ctl
%_bindir/mergerfs.dedup
%_bindir/mergerfs.dup
%_bindir/mergerfs.fsck
%_bindir/mergerfs.mktrash

%changelog
* Fri Feb 02 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
