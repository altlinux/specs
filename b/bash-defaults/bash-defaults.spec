%set_compress_method none
%define bash_version 3

Name: bash-defaults
Version: 3.2.57
Release: alt4

Summary: %vendor setup for the GNU Bourne Again SHell (Bash)
License: None
Group: System/Configuration/Other
BuildArch: noarch

%description
This package provides default %summary.

%package -n sh
Summary: The GNU Bourne Again SHell (/bin/sh)
Group: Shells
Provides: /bin/sh, /usr/lib/bash

%description -n sh
This package provides default setup for the GNU Bourne Again SHell (/bin/sh).

%package -n bash
Summary: The GNU Bourne Again SHell (/bin/bash)
Group: Shells
Provides: /bin/bash
Requires: sh = %EVR

%description -n bash
This package provides default setup for the GNU Bourne Again SHell (/bin/bash).

%package -n bash-devel
Summary: Bash loadable builtins development files
Group: Development/Other
Requires: bash = %EVR

%description -n bash-devel
This package provides default setup for the GNU Bourne Again SHell (development files).

%install
mkdir -p %buildroot{/bin,/usr/lib/bash,%_bindir,%_includedir,%_infodir,%_man1dir}

for i in /bin/sh /bin/bash /bin/rbash %_bindir/bashbug %_includedir/bash; do
	ln -rs %buildroot"${i/sh/sh%bash_version}" %buildroot"$i"
done

for i in bash; do
	ln -s "$i"%bash_version.info.xz %buildroot%_infodir/"$i".info.xz
done

for i in sh bash rbash bashbug bash_builtins; do
	ln -s "${i/sh/sh%bash_version}".1.xz %buildroot%_man1dir/"$i".1.xz
done

# Those that conflict with real manpages from coreutils are not listed.
for i in \
	. : [ alias bg bind break builtin caller cd command compgen	\
	complete compopt continue declare dirs disown enable eval exec	\
	exit export fc fg getopts hash help history jobs let local	\
	logout mapfile popd pushd read readonly return set shift shopt	\
	source suspend times trap type typeset ulimit umask unalias	\
	unset wait							\
	; do
	ln -s bash_builtins.1.xz %buildroot%_man1dir/"$i".1.xz
done

%add_findreq_skiplist %_infodir/*
%add_findreq_skiplist %_man1dir/*

%files -n sh
/bin/sh
/usr/lib/bash

%files -n bash
/bin/bash
/bin/rbash
%_bindir/bashbug
%_infodir/*
%_man1dir/..1*
%_man1dir/*.1*

%files -n bash-devel
%_includedir/bash

%changelog
* Fri Aug 03 2018 Dmitry V. Levin <ldv@altlinux.org> 3.2.57-alt4
- sh: turned into setup package for /bin/sh.
- bash: turned into setup package for /bin/bash.
- bash-devel: turned into setup package for /usr/include/bash.
