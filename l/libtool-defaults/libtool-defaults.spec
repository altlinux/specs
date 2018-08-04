%set_compress_method none
%define libtool_version 2.4

Name: libtool-defaults
Version: 2.4.2
Release: alt6
Epoch: 3

Summary: %vendor setup for the GNU libtool
License: None
Group: System/Configuration/Other
BuildArch: noarch
Url: http://git.altlinux.org/gears/l/libtool-defaults.git

%description
This package provides default %summary.

%package -n libtool
Summary: %summary
Group: Development/Other
# Old versions of these packages used to provide alternatives
# that conflict with this package.
Conflicts: libtool_2.4 < 2.4.2-alt6
Conflicts: libtool_1.5 < 3:1.5.26-alt12
Conflicts: libtool_1.4 < 3:1.4.3-alt13

%description -n libtool
This package provides default %summary.

%install
mkdir -p %buildroot{%_bindir,%_datadir,%_infodir,%_man1dir}

for i in %_bindir/libtool{,ize}-default; do
	ln -rs %buildroot"${i/default/%libtool_version}" \
		%buildroot"$i"
done

for i in %_datadir/libtool %_infodir/libtool.info.xz %_man1dir/libtool.1.xz; do
	ln -rs %buildroot"${i/libtool/libtool-%libtool_version}" \
		%buildroot"$i"
done

for i in %_man1dir/libtoolize.1.xz; do
	ln -rs %buildroot"${i/libtoolize/libtoolize-%libtool_version}" \
		%buildroot"$i"
done

%add_findreq_skiplist %_infodir/*
%add_findreq_skiplist %_man1dir/*

%define _unpackaged_files_terminate_build 1

%files -n libtool
%_bindir/libtool-default
%_bindir/libtoolize-default
%_datadir/libtool
%_infodir/libtool.info.xz
%_man1dir/libtool.1.xz
%_man1dir/libtoolize.1.xz

%changelog
* Sat Aug 04 2018 Dmitry V. Levin <ldv@altlinux.org> 3:2.4.2-alt6
- Initial revision (replaces libtool alternatives).
