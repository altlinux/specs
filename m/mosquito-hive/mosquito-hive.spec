Name: mosquito-hive
Version: 0.2.2
Release: alt1

Summary: rebuild a collection of packages in hasher

License: %gagpl3plus
Group: Development/Other
Url: http://git.altlinux.org/people/imz/packages/mosquito-hive.git
Packager: Ivan Zakharyaschev <imz@altlinux.org>

Source: %name-%version.tar

Requires: hasher
Requires: altlinux-repolist-utils

BuildArch: noarch
BuildPreReq: rpm-build-licenses
# My scripts use it, and hence shell.req uses it (could be detected by
# buildreq, but we should use the path forseeing a move between pkgs):
BuildPreReq: /bin/bash4

%description
Simple scripts to rebuild a collection of packages
in hasher.

The results are reported in a way similar to the beehive of ALT Sisyphus.
The build progress is reported in a way similar to girar of ALT Sisyphus.

Features:

* rebuild selected SRPMS (mosquito-rebuild)
** parallel builds, too
* get the list of SRPMS corresponding to a list of selected binary
  RPMS
** make the correspondence relations between src and bin pkg names,
  and between them and files (if src.list and bin.list are missing)
* diff between our results and the results of ALT Sisyphus beehive
  (based on the logs)

The features beyond the first bullet are WORK-IN-PROGRESS (not
packaged yet, but saved in Git).

%prep
%setup

%install
# Helpers:
mkdir -p %buildroot%_datadir/%name
install --preserve-timestamps -m 755 \
	rebuild{,1} \
	-t %buildroot%_datadir/%name/

# Executables to be run by the user
# (they need to be symlinks to the place where the helpers are):
mkdir -p %buildroot%_bindir
for f in rebuild; do
    ln -s "$(relative %_datadir/%name/"$f" %_bindir/_)" \
       -T %buildroot%_bindir/mosquito-"$f"
done

install --preserve-timestamps -m 755 \
	stripVerRel \
	-t %buildroot%_bindir/

%files
%_bindir/*
%_datadir/%name
%doc README.md

%changelog
* Thu Jan 17 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1
- rebuild1: use altlinux-repolist-utils (with limitations on SRPMDIR)
  instead of shell globs (not effective) to find the SRPM file.
- stripVerRel: new simple util.

* Fri May 27 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1
- hide rebuild1 (the handler for a single arg) from PATH, because a
  user gets nothing from it compared to mosquito-rebuild (many args).
- rebuild: show the command being run (to let the user know more).

* Thu May 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1
- rebuild: take the list from stdin lines.
  (UI unified with my other scripts: pregirar.)

* Wed May 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus.
  (Only mosquito-rebuild is packaged; the rest is WIP.)
