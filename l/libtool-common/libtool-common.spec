Name: libtool-common
Version: 0.2.3
Release: alt1

Summary: Wrapper and common files for different versions of libtool
Group: Development/Other
License: GPLv2+
Url: http://git.altlinux.org/gears/l/libtool-common.git

Conflicts: libtool < 3:1.4.2-alt1

Source: libtool_wrapper
Source1: libtool-ldconfig-dump.c

%description
This package contains files that provide co-existence of various
versions of GNU Libtool.

%prep
%setup -cT

%build
%__cc %optflags $(getconf LFS_CFLAGS) \
	%_sourcedir/libtool-ldconfig-dump.c -o libtool-ldconfig-dump

%install
install -pD -m755 %_sourcedir/libtool_wrapper \
	%buildroot%_bindir/libtool_wrapper
for f in libtool libtoolize; do
	ln -s libtool_wrapper "%buildroot%_bindir/$f"
done
install -pm755 libtool-ldconfig-dump %buildroot%_bindir/

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%files
%_bindir/*

%changelog
* Wed Dec 30 2020 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt1
- Simplified libtool_wrapper a bit.

* Sat Aug 04 2018 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt1
- Cleaned up libtool_wrapper.

* Thu Apr 18 2013 Dmitry V. Levin <ldv@altlinux.org> 0.2.1-alt1
- Built with LFS support enabled.

* Wed Apr 30 2008 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt3
- Fixed %%setup invocation.

* Sun Apr 08 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt2
- Cleaned up specfile.

* Mon Nov 29 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Implemented libtool-ldconfig-dump utility.

* Tue Aug 19 2003 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt2
- Updated package dependencies.

* Tue Aug 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.1-alt1
- Initial revision
