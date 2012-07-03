Name: libtool-common
Version: 0.2
Release: alt3

Summary: Wrapper and common files for different versions of libtool
Group: Development/Other
License: GPLv2+
Packager: Dmitry V. Levin <ldv@altlinux.org>

Conflicts: libtool < 3:1.4.2-alt1

Source: libtool_wrapper
Source1: libtool-ldconfig-dump.c

%description
This package contains files that provide co-existance of various
versions of GNU Libtool.

%prep
%setup -qcT

%build
%__cc %optflags %_sourcedir/libtool-ldconfig-dump.c -o libtool-ldconfig-dump

%install
install -pD -m755 %_sourcedir/libtool_wrapper \
	%buildroot%_bindir/libtool_wrapper
for f in libtool libtoolize; do
	ln -s libtool_wrapper "%buildroot%_bindir/$f"
done
install -pm755 libtool-ldconfig-dump %buildroot%_bindir/

%files
%_bindir/*

%changelog
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
