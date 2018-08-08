%set_compress_method none
%define automake_version 1.14

Name: automake-defaults
Version: 1.14.1
Release: alt3
Epoch: 1

Summary: %vendor setup for the GNU Automake
License: None
Group: System/Configuration/Other
BuildArch: noarch
Url: http://git.altlinux.org/gears/a/automake-defaults.git

%description
This package provides default %summary.

%package -n automake
Summary: %summary
Group: Development/Other
# Old versions of these packages used to provide alternatives
# that conflict with this package.
Conflicts: automake_1.14 < 1.14.1-alt3
Conflicts: automake_1.11 < 1.11.6-alt7
Conflicts: automake_1.10 < 1:1.10.3-alt5
Conflicts: automake_1.9 < 1:1.9.6-alt7
Conflicts: automake_1.7 < 1:1.7.9-alt4
Conflicts: automake_1.6 < 1:1.6.3-alt10
Conflicts: automake_1.4 < 1:1.4p6-alt8

%description -n automake
This package provides default %summary.

%install
mkdir -p %buildroot{%_bindir,%_datadir,%_infodir,%_man1dir}

for i in %_bindir/{automake,aclocal}-default; do
	ln -rs %buildroot"${i/default/%automake_version}" \
		%buildroot"$i"
done

for i in %_datadir/automake %_infodir/automake.info.xz; do
	ln -rs %buildroot"${i/automake/automake-%automake_version}" \
		%buildroot"$i"
done

for i in %_man1dir/{automake,aclocal}.1.xz; do
	ln -rs %buildroot"${i/.1/-%automake_version.1}" \
		%buildroot"$i"
done

%add_findreq_skiplist %_infodir/*
%add_findreq_skiplist %_man1dir/*

%define _unpackaged_files_terminate_build 1

%files -n automake
%_bindir/automake-default
%_bindir/aclocal-default
%_datadir/automake
%_infodir/automake.info.xz
%_man1dir/automake.1.xz
%_man1dir/aclocal.1.xz

%changelog
* Wed Aug 08 2018 Dmitry V. Levin <ldv@altlinux.org> 1:1.14.1-alt3
- Initial revision (replaces automake alternatives).
