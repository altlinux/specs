%define _unpackaged_files_terminate_build 1

Name: fwts
Version: 23.07.00
Release: alt1

Summary: Firmware Test Suite

# The ACPICA code is licensed under both GPLv2 and Intel-ACPI, a few
# files are licensed under the LGPL. Please see copyright file for details.
License: GPLv2 and LGPLv2 and (GPLv2 or Intel-ACPI)
Group: System/Base

Url: https://wiki.ubuntu.com/FirmwareTestSuite
#git: https://git.launchpad.net/fwts

Source0: %name-%version.tar

Patch1: 0001-fix-build-on-i586-arch.patch

BuildRequires: libgio-devel
BuildRequires: flex
BuildRequires: zlib-devel
BuildRequires: libbsd-devel
BuildRequires: bc

%description
Firmware Test Suite (FWTS) is a test suite that performs sanity checks on
Intel/AMD PC firmware. It is intended to identify BIOS and ACPI errors and if
appropriate it will try to explain the errors and give advice to help
workaround or fix firmware bugs. It is primarily intended to be a Linux-specific
firmware troubleshooting tool.

%prep

%setup
%autopatch -p1

# It is necessary to link the two libraries together, since they
# refer to each other's functions. Therefore, we will additionally
# create libraries for linking, in the future they will refer to
# the real ones in the directory /usr/lib64/fwts
cp -r src/lib src/lib_
cp -r src/libfwtsacpica src/libfwtsacpica_
sed -i "s|src/lib/Makefile|src/lib/Makefile\nsrc/lib_/Makefile|" configure.ac
sed -i "s|src/lib/src/Makefile|src/lib/src/Makefile\nsrc/lib_/src/Makefile|" configure.ac
sed -i "s|src/libfwtsacpica/Makefile|src/libfwtsacpica/Makefile\nsrc/libfwtsacpica_/Makefile|" configure.ac
sed -i "s|lib libfwtsacpica|lib_ libfwtsacpica_ lib libfwtsacpica|" src/Makefile.am
sed -i "s|libfwts_la_LIBADD =|libfwts_la_LIBADD = ../../../src/libfwtsiasl/.libs/libfwtsiasl.la ../../../src/libfwtsacpica_/.libs/libfwtsacpica.la |" src/lib/src/Makefile.am
sed -i "s|libfwtsacpica_la_LIBADD =|libfwtsacpica_la_LIBADD = ../../src/lib_/src/.libs/libfwts.la |" src/libfwtsacpica/Makefile.am

# Disable YACC
sed -i "s|AM_YFLAGS =|AM_YFLAGS = -Wno-yacc |" src/libfwtsiasl/Makefile.am

export LDFLAGS="$LDFLAGS -lz"
%autoreconf
%configure --disable-static

MAKE_VERSION_BUILD=$(make -v | head -1 | sed -E "s|GNU Make ||")
CONDITION=$(echo "$MAKE_VERSION_BUILD > 4.3" |bc -l)

if [[ $CONDITION == "1" ]];then
	make -j 1
else
	%make_build
fi

%install
%makeinstall_std

%check
%make_build check

%files
%doc README README_ACPICA.txt README_SOURCE.txt debian/copyright
%_bindir/fwts
%_bindir/kernelscan
%_datadir/fwts/
%_datadir/bash-completion/completions/fwts*
%_libdir/fwts/
%_man1dir/%name.1*
%_man1dir/%name-collect.1*
%_man1dir/%name-frontend-text.1*

%changelog
* Fri Jul 07 2023 Vasiliy Kovalev <kovalev@altlinux.org> 23.07.00-alt1
- 23.05.00 -> 23.07.00

* Mon May 29 2023 Vasiliy Kovalev <kovalev@altlinux.org> 23.05.00-alt1
- 22.11.00 -> 23.05.00

* Fri Dec 30 2022 Vasiliy Kovalev <kovalev@altlinux.org> 22.11.00-alt1
- 22.03.00 -> 22.11.00
- add support for single-thread build with make version 4.4
- bison: disable YACC
- fix undefined symbols in shared libraries:
  + libfwtsiasl libfwts libfwtsacpica
- add link with libz and disable static library

* Wed Apr 27 2022 Vasiliy Kovalev <kovalev@altlinux.org> 22.03.00-alt1
- Initial build for Sisyphus
