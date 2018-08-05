%set_compress_method none
%define libtool_version 2.4

Name: libtool-defaults
Version: 2.4.2
Release: alt7
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
mkdir -p %buildroot{%_bindir,%_datadir,%_infodir}

for i in %_bindir/libtool{,ize}-default; do
	ln -rs %buildroot"${i/default/%libtool_version}" \
		%buildroot"$i"
done

for i in %_datadir/libtool %_infodir/libtool.info.xz; do
	ln -rs %buildroot"${i/libtool/libtool-%libtool_version}" \
		%buildroot"$i"
done

%add_findreq_skiplist %_infodir/*

%define _unpackaged_files_terminate_build 1

%files -n libtool
%_bindir/libtool-default
%_bindir/libtoolize-default
%_datadir/libtool
%_infodir/libtool.info.xz

%changelog
* Sun Aug 05 2018 Dmitry V. Levin <ldv@altlinux.org> 3:2.4.2-alt7
- Dropped symlinks to libtool manual pages in favour of man-pages package
  (ALT#35211).

* Sat Aug 04 2018 Dmitry V. Levin <ldv@altlinux.org> 3:2.4.2-alt6
- Initial revision (replaces libtool alternatives).
