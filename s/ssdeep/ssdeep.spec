Name: ssdeep
Version: 2.14.1
Release: alt1

Summary: Context Triggered Piecewise Hashing values
License: GPLv2+
Group: File tools

Url: http://ssdeep.sourceforge.net
Source: %name-%version.tar

BuildRequires: gcc-c++

%description
ssdeep is a program for computing and matching Context Triggered Piecewise
Hashing values. It is based on a spam detector called spamsum by Andrews
Trigdell

%package -n libfuzzy
License: GPLv2+
Group: System/Libraries
Summary: Library that provides %summary

%description -n libfuzzy
Library that provides %summary, used by %name

%package -n libfuzzy-devel
License: GPLv2+
Group: Development/C
Summary: API for libfuzzy

%description -n libfuzzy-devel
API for libfuzzy, %summary

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

rm -fv %buildroot%_libdir/*.a

%files
%doc README COPYING FILEFORMAT
%_bindir/*
%_man1dir/*

%files -n libfuzzy
%_libdir/*.so.*

%files -n libfuzzy-devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 2.14.1-alt1
- Build new version.

* Wed Oct 20 2021 Grigory Ustinov <grenka@altlinux.org> 2.13-alt2
- fixed FTBFS.

* Mon Apr 27 2015 Michael Shigorin <mike@altlinux.org> 2.13-alt1
- new version (watch file uupdate)

* Fri Oct 24 2014 Michael Shigorin <mike@altlinux.org> 2.12-alt1
- new version (watch file uupdate)

* Mon Sep 29 2014 Michael Shigorin <mike@altlinux.org> 2.11.1-alt1
- new version (watch file uupdate)

* Fri Sep 12 2014 Michael Shigorin <mike@altlinux.org> 2.11-alt1
- new version (watch file uupdate)

* Tue May 27 2014 Michael Shigorin <mike@altlinux.org> 2.10-alt1
- new version (watch file uupdate)
- spec cleanup

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.5-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jul 13 2010 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- New version

* Tue Jul 13 2010 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Initial build from SuSE

