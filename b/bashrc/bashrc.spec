Name: bashrc
Version: 1.0
Release: alt1
Summary: bashrc files for the GNU Bourne Again SHell (Bash)
Group: System/Configuration/Other
License: GPLv2+
BuildArch: noarch
Url: http://git.altlinux.org/gears/b/bashrc.git
Source0: bash_alias
Source1: bashrc

%description
This package provides %summary.

%install
install -pD -m755 %_sourcedir/bash_alias %buildroot%_sysconfdir/bashrc.d/alias.sh
install -p -m755 %_sourcedir/bashrc %buildroot%_sysconfdir/

%files
%config(noreplace) %_sysconfdir/bashrc*

%changelog
* Fri Aug 03 2018 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Moved bashrc files to a separate package.
