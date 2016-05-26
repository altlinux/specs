Name: mosquito-hive
Version: 0.2
Release: alt1

Summary: rebuild a collection of packages in hasher

License: %gagpl3plus
Group: Development/Other
Url: http://git.altlinux.org/people/imz/public/mosquito-hive.git
Packager: Ivan Zakharyaschev <imz@altlinux.org>

Source: %name-%version.tar

Requires: hasher

BuildArch: noarch
BuildPreReq: rpm-build-licenses
# My scripts use it, and hence shell.req uses it:
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
install --preserve-timestamps -m 755 rebuild1.sh -t %buildroot%_datadir/%name/
install --preserve-timestamps -m 644 rebuild-functions.sh -t %buildroot%_datadir/%name/

# Executables to be run by the user:
mkdir -p %buildroot%_bindir
ln -s "$(relative %_datadir/%name/rebuild1.sh %_bindir/_)" -T %buildroot%_bindir/mosquito-rebuild1
install --preserve-timestamps -m 755 rebuild.sh -T %buildroot%_bindir/mosquito-rebuild

# For shell.req:
%global __spec_autodep_custom_pre export BASHOPTS=extglob

%files
%_bindir/*
%_datadir/%name
%doc README.md

%changelog
* Thu May 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1
- rebuild: take the list from stdin lines.
  (UI unified with my other scripts: pregirar.)

* Wed May 18 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus.
  (Only mosquito-rebuild is packaged; the rest is WIP.)


