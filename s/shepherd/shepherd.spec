%define _unpackaged_files_terminate_build 1

%def_with check

%define guile_sitedir %(guile-config info sitedir)
%define bash_completionsdir %_datadir/bash-completion/completions

Name: shepherd
Version: 0.10.5
Release: alt1

Summary: The GNU Shepherd
License: GPL-3.0+
Group: System/Configuration/Boot and Init
Url: https://www.gnu.org/software/shepherd/
Vcs: https://git.savannah.gnu.org/cgit/shepherd.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

Requires: guile-fibers
Conflicts: sysvinit
Conflicts: systemd-sysvinit

BuildRequires(pre): /proc
BuildRequires: guile-devel
BuildRequires: guile-fibers
BuildRequires: help2man
BuildRequires: texinfo

%description
The GNU Shepherd is a service manager written in Guile that looks after
the herd of daemons running on the system. It can be used as an "init"
system (PID 1) and also by unprivileged users to manage per-user
daemons-e.g., tor, privoxy, mcron. It supports several daemon startup
mechanisms, including inetd and systemd-style socket activation.
The GNU Shepherd is configured in Guile Scheme and can be extended in
the same language. It builds on a simple memory-safe and callback-free
programming model.

%prep
%setup
%autopatch0 -p1

%build
%autoreconf
%configure \
    --with-bash-completion-dir=%bash_completionsdir
%make_build

%install
%makeinstall_std
%find_lang %name

%check
%make_build check

%files -f %name.lang
%guile_ccachedir/shepherd*
%guile_sitedir/shepherd*
%_bindir/herd
%_bindir/shepherd
%_sbindir/halt
%_sbindir/reboot
%_sbindir/shutdown
%_libdir/shepherd
%_infodir/shepherd.info.*
%_man1dir/herd.*
%_man1dir/shepherd.*
%_man8dir/halt.*
%_man8dir/reboot.*
%bash_completionsdir/herd

%changelog
* Tue Jul 02 2024 Anton Zhukharev <ancieg@altlinux.org> 0.10.5-alt1
- Updated to 0.10.5.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 0.10.4-alt1
- Updated to 0.10.4.

* Tue Jan 09 2024 Anton Zhukharev <ancieg@altlinux.org> 0.10.3-alt1
- Updated to 0.10.3.

* Mon Jul 24 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.2-alt3
- Added %%runstatedir as /var/run/shepherd (for socket).

* Wed Jul 19 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.2-alt2
- Added guile-fibers requirement.

* Tue Jul 18 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.2-alt1
- Updated to 0.10.2.
- Packaged bash completions.

* Mon Jun 05 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.1-alt3
- Set conflict with systemd-sysvinit package.

* Sun Jun 04 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.1-alt2
- Set conflict with sysvinit package.

* Tue May 30 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.1-alt1
- New version.

* Fri May 26 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.0-alt1
- Initial build for ALT Sisyphus.

