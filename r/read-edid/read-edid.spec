Name: read-edid
Version: 3.0.2
Release: alt3
Group: System/Configuration/Other
License: GPL

Summary: Get monitor details

URL: http://polypux.org/projects/read-edid/

Source0: %name-%version.tar

BuildPreReq: rpm-macros-cmake
BuildRequires: libx86-devel cmake gcc-c++
ExcludeArch: armh aarch64 ppc64le

%description
This package will try to read the monitor details directly from the
monitor. The program get-edid asks a VBE BIOS for the EDID data. The
program parse-edid parses the data and prints out a human readable
summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%dir %_docdir/read-edid
%_docdir/read-edid/*
%_man1dir/*
%_bindir/*

%changelog
* Thu Dec 10 2020 Vladislav Zavjalov <slazav@altlinux.org> 3.0.2-alt3
- fix multiple definition error (for gcc-10)
- update ExcludeArch (libx86 is available only on i586 and x86_64)

* Sat Oct 20 2018 Vladislav Zavjalov <slazav@altlinux.org> 3.0.2-alt2
- fix segmentation fault in VBE mode (closes #35525)

* Thu Oct 11 2018 Vladislav Zavjalov <slazav@altlinux.org> 3.0.2-alt1
- v.3.0.2
- parse-edid: show product ID (patch by M.Fishkov)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Sep 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 2.0.0-alt2
- change Packager, rebuild with new libx86

* Tue Sep 23 2008 Alexey Gladkov <legion@altlinux.ru> 2.0.0-alt1
- New version (2.0.0).
- The lrmi code has been replaced by libx86 code.

* Tue Jul 17 2007 Alexey Gladkov <legion@altlinux.ru> 1.4.1-alt1
- First build for ALT Linux.
