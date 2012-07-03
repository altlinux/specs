Name:		mozilla-common
Version:	1.0
Release:	alt1
Summary:	Mozilla common directories
Group:		System/Base
License:	GPL3
Packager:	Alexey Gladkov <legion@altlinux.ru>

%description
This package contains mozilla common directories.

%package devel
Summary:	Mozilla common directories
Group:		Development/Other

%description devel
Mozilla common directories

%install
mkdir -p %buildroot
cd %buildroot

mkdir -p \
	./%_rpmmacrosdir \
	./%_rpmlibdir \
	./%_libdir/mozilla/extensions \
	./%_datadir/mozilla/extensions/any

cat >./%_rpmmacrosdir/%name<<EOF
%%mozilla_arch_extdir	%%_libdir/mozilla/extensions
%%mozilla_noarch_extdir	%%_datadir/mozilla/extensions
%%mozilla_any_extdir	%%_datadir/mozilla/extensions/any
EOF

cat >./%_rpmlibdir/mozcommon.req.list<<EOF
%_datadir/mozilla	%name
%_libdir/mozilla	%name
EOF

%files
%_libdir/mozilla
%_datadir/mozilla

%files devel
%_rpmmacrosdir/%name
%_rpmlibdir/mozcommon.req.list

%changelog
* Wed Jan 11 2012 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- First build.

