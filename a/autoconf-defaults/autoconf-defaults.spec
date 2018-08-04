%set_compress_method none
%define autoconf_version 2.60

Name: autoconf-defaults
Version: 2.69
Release: alt4
Epoch: 2

Summary: %vendor setup for the GNU Autoconf
License: None
Group: System/Configuration/Other
BuildArch: noarch
Url: http://git.altlinux.org/gears/a/autoconf-defaults.git

%description
This package provides default %summary.

%package -n autoconf
Summary: %summary
Group: Development/Other
# Old versions of these packages used to provide alternatives
# that conflict with this package.
Conflicts: autoconf_2.60 < 2:2.69-alt4
Conflicts: autoconf_2.50 < 2:2.59-alt12
Conflicts: autoconf_2.13 < 2:2.13-alt13

%description -n autoconf
This package provides default %summary.

%install
mkdir -p %buildroot{%_bindir,%_datadir,%_infodir,%_man1dir}

for i in %_bindir/{autoconf,autoheader,autom4te,autoreconf,autoscan,autoupdate,ifnames}-default; do
	ln -rs %buildroot"${i/default/%autoconf_version}" \
		%buildroot"$i"
done

for i in %_datadir/autoconf %_infodir/autoconf.info.xz; do
	ln -rs %buildroot"${i/autoconf/autoconf-%autoconf_version}" \
		%buildroot"$i"
done

for i in %_man1dir/{autoconf,autoheader,autom4te,autoreconf,autoscan,autoupdate,config.guess,config.sub,ifnames}.1.xz; do
	ln -rs %buildroot"${i/.1/-%autoconf_version.1}" \
		%buildroot"$i"
done

%add_findreq_skiplist %_infodir/*
%add_findreq_skiplist %_man1dir/*

%define _unpackaged_files_terminate_build 1

%files -n autoconf
%_bindir/autoconf-default
%_bindir/autoheader-default
%_bindir/autom4te-default
%_bindir/autoreconf-default
%_bindir/autoscan-default
%_bindir/autoupdate-default
%_bindir/ifnames-default
%_datadir/autoconf
%_infodir/autoconf.info.xz
%_man1dir/autoconf.1.xz
%_man1dir/autoheader.1.xz
%_man1dir/autom4te.1.xz
%_man1dir/autoreconf.1.xz
%_man1dir/autoscan.1.xz
%_man1dir/autoupdate.1.xz
%_man1dir/config.guess.1.xz
%_man1dir/config.sub.1.xz
%_man1dir/ifnames.1.xz

%changelog
* Sat Aug 04 2018 Dmitry V. Levin <ldv@altlinux.org> 2:2.69-alt4
- Initial revision (replaces autoconf alternatives).
