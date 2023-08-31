Group: File tools
%define fedora 37
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# help2man is too old on rhel <= 6 to support some switches.
%if 0%{?fedora} || 0%{?rhel} >= 7
%bcond_without	man
%else
%bcond_with	man
%endif


Name:		fstransform
Version:	0.9.4
Release:	alt2_11
Summary:	Tool for in-place file-system conversion without backup

License:	GPLv3+
URL:		https://github.com/cosmos72/%{name}
Source0:	https://github.com/cosmos72/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	e2fsprogs-devel libe2fs-devel
BuildRequires:	gcc-c++
BuildRequires:	libcom_err-devel
BuildRequires:	zlib-devel

%if %{with man}
BuildRequires:	help2man
%endif # with man

Requires:	coreutils
Requires:	cfdisk eject fdisk getopt hwclock look lsblk msulogin rfkill setarch sfdisk shadow-change util-linux
Requires:	which
Source44: import.info

%description
fstransform is a tool to change a file-system from one format
to another, for example from jfs/xfs/reiser to ext2/ext3/ext4,
in-place and without the need for backup.


%prep
%setup -q


# Make sure Autotools files have proper timestamps.
/bin/touch aclocal.m4 configure Makefile.am Makefile.in


%build
%configure --disable-silent-rules
%make_build


%install
%makeinstall_std

%if %{with man}
# Create man-pages.
mkdir -p %{buildroot}%{_mandir}/man8
for f in %{buildroot}%{_sbindir}/* ; do
	n="$(echo ${f} | sed -e 's!^%{buildroot}%{_sbindir}/!!g')"
	%{_bindir}/help2man -N -s 8 --version-string='%{version}'	\
		--no-discard-stderr -o %{buildroot}%{_mandir}/man8/${n}.8 ${f}
done
%endif # with man


%check
%make_build check


%files
%doc doc/*
%doc ChangeLog
%doc README
%doc TODO
%doc --no-dereference AUTHORS
%doc --no-dereference COPYING
%if %{with man}
%{_mandir}/man8/fsattr.8*
%{_mandir}/man8/fsmount_kernel.8*
%{_mandir}/man8/fsmove.8*
%{_mandir}/man8/fsremap.8*
%{_mandir}/man8/%{name}.8*
%endif # with man
%{_sbindir}/fsattr
%{_sbindir}/fsmount_kernel
%{_sbindir}/fsmove
%{_sbindir}/fsremap
%{_sbindir}/%{name}


%changelog
* Thu Aug 31 2023 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt2_11
- moved to Sisyphus (feature #109461)

* Wed Feb 22 2023 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt2_10
- update to new release by fcimport

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt2_9
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt2_8
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt2_7
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt2_6
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_5
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_5
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_4
- update to new release by fcimport

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_3
- new version

