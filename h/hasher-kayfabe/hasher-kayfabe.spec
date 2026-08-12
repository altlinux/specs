%global _unpackaged_files_terminate_build 1

Name: hasher-kayfabe
Version: 0.2.1
Release: alt1
Summary: Run hasher inside a rootless container
Group: Development/Other
License: GPL-2.0-or-later
VCS: https://altlinux.space/rider/hasher-kayfabe
Source0: %name-%version.tar

Requires: hasher
# kayfabe-privd mounts a writable cgroup2 over the read-only one podman gives a
# container. Without mount(8) it still starts, and the library fakes the one
# cgroup write hasher-priv insists on, with a warning and no per-job cgroup.
Requires: mount
# kayfabe-privd serialises its start sequence with flock; without it two
# concurrent builds race to start the daemon.
Requires: /usr/bin/flock

# Both of these are optional at runtime and neither belongs in the closure of a
# package whose whole purpose is a container image: the guard uses
# systemd-detect-virt when it is installed and reads the signals itself when it
# is not, and sudo is the wrapper's last resort for a host where the setuid
# helper was removed. The scanner cannot tell an optional call from a required
# one, so those two scripts are kept out of its way.
%filter_from_requires /^sudo$/d
%filter_from_requires /systemd-detect-virt/d

%description
hasher-priv refuses to work where it cannot see a real host: it compares its
namespaces with the caller's and dies when the kernel hides them behind a
missing CAP_SYS_PTRACE, it treats a read-only cgroupfs as fatal, and it creates
requested devices (/dev/kvm and the like) with mknod(), which no rootless
container may do.

This package answers each of those with what the process would have seen on a
host: its own namespaces, a writable descriptor, a bind mount of the container's
device node. hasher itself is not modified and not aware of any of it.

Installing shadows no hasher entry point: the wrapper takes over hsh and its
relatives only when kayfabe-activate is run, which is what a container image
does at build time. The package does install one privileged file, a setuid
helper that starts the daemon for a caller who has no other way to reach root;
it refuses to do anything on a system running an init that starts hasher-privd
itself, so on an ordinary host it is inert. The library is inert there as well:
every interception performs the real call first and only steps in where the
kernel refused it.

%prep
%setup

%build
%make_build CFLAGS="%optflags" CPPFLAGS="%optflags"

%install
%makeinstall_std libdir=%_libdir sbindir=%_sbindir libexecdir=%_libexecdir

%files
%doc README.md COPYING
%_sbindir/kayfabe-privd
%_sbindir/kayfabe-activate
%_sbindir/kayfabe-deactivate
%dir %_libexecdir/%name
%_libexecdir/%name/kayfabe-wrapper
%_libexecdir/%name/kayfabe-in-container
# Unreadable to everyone, runnable only by hasher's own group: it starts the
# daemon for a caller who has no other way to reach root, and does nothing else.
%attr(4710,root,hashman) %_libexecdir/%name/kayfabe-start
%_libexecdir/%name/profile.sh
%dir %_libdir/%name
%_libdir/%name/libkayfabe.so

%changelog
* Thu Aug 13 2026 Anton Farygin <rider@altlinux.org> 0.2.1-alt1
- fixed the installed scripts looking for each other in /usr/libexec while the
  package puts them in %_libexecdir, which made the packaged version unusable
- dropped the automatic dependencies on sudo and systemd-detect-virt, both of
  which are optional at runtime and unwanted in a container image
- fixed the container guard answering "host" wherever only the uid_map signal was left
- fixed a daemon whose socket file had been removed being taken for a running one,
  which left the container unable to build until it was restarted by hand
- the setuid helper now refuses a caller whose resource limits or nice value it
  cannot restore, rather than passing them on to the shared daemon

* Wed Aug 12 2026 Anton Farygin <rider@altlinux.org> 0.2.0-alt1
- activation, the wrappers and the setuid helper now refuse outside a container

* Wed Aug 12 2026 Anton Farygin <rider@altlinux.org> 0.1.0-alt1
- Initial build.
