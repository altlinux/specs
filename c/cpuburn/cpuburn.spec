Name: cpuburn
Version: 1.4a
Release: alt1

Summary: CPU testing utilities
License: GPL-2.0-only
Group: Monitoring
Url: http://pages.sbcglobal.net/redelm/
ExclusiveArch: %ix86 x86_64 %arm

# http://pages.sbcglobal.net/redelm/cpuburn_1_4_tar.gz
Source: cpuburn-%version.tar

Patch: cpuburn-1.4-deb-data.patch

%description
CPU testing utilities in optimized assembler for maximum loading P6
(Intel Pentium Pro, Pentium II, Celeron and Pentium III TM), AMD K6,
and P5 Pentium chips.

%prep
%setup -q
%patch -p1

%build
%ifarch %ix86 x86_64
%define cpulist P6 BX K6 K7 MMX P5
for n in %cpulist; do
	gcc -m32 -s -Wa,--noexecstack -no-pie -fno-PIE -nostdlib -o burn$n burn$n.S
done
%endif
%ifarch %arm
make -C ARM CC='gcc -s -Wa,--noexecstack -no-pie -fno-PIE'
%endif

%install
mkdir -p %buildroot%_bindir
%ifarch %ix86 x86_64
for n in %cpulist; do
	install -p -m755 burn$n %buildroot%_bindir/
done
%endif
%ifarch %arm
install -p -m755 ARM/burnCortexA8 %buildroot%_bindir/
%endif

%check
status=0
for f in %buildroot%_bindir/*; do
	time timeout 1 "$f" && status=1 || {
		[ $? -eq 124 ] ||
			status=1
	}
done
exit $status

%files
%_bindir/*
%ifarch %ix86 x86_64
%doc Design README
%endif
%ifarch %arm
%doc ARM/Design
%endif

%changelog
* Sun Dec 20 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4a-alt1
- 1.4 -> 1.4a.
- Enabled on %%armh.
- Fixed build when gcc is configured with --enable-default-pie.

* Tue Jan 23 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt5
- Mark utilities as not requiring executable stack.
- Merged asm fix from Debian cpuburn package.
- Fixed build on x86-64 platform.
- Updated URL, added Packager and ExclusiveArch tags.

* Fri Oct 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4-alt4
- rebuild with gcc3

* Tue Jun 11 2002 Michael Shigorin <mike@altlinux.ru> 1.4-alt3
- added missing burnK7 target

* Fri Feb 22 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt2
- Set strip method to "none".

* Tue Jul 31 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4-alt1
- 1.4

* Wed May 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.3-alt1
- Initial revision.
