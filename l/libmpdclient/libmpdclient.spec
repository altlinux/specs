# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: libmpdclient
Version: 2.20
Release: alt1

Summary: MPD client library

License: BSD-like
Group: System/Libraries
Url: https://www.musicpd.org/
VCS: https://github.com/MusicPlayerDaemon/libmpdclient.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-vala
BuildRequires: meson libvala-devel
BuildRequires: doxygen fontconfig

%description
Library for Music Player Daemon client development.

%package devel
Summary: Header files for the MPD client library
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for MPD client library.

%package devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
Development documentation for %name.

%package vala
Summary: Vala language bindings for %name
Group: Development/Other
BuildArch: noarch
Requires: %name = %EVR

%description vala
This package provides Vala language bindings for %name.

%prep
%setup

%build
%meson -D documentation=true
%meson_build

%check
%meson_test

%install
%meson_install

%files
%doc README.rst COPYING AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/mpd/
%_pkgconfigdir/%name.pc

%files devel-docs
%_docdir/%name

%files vala
%_vapidir/*

%changelog
* Wed Nov 01 2023 Mikhail Tergoev <fidel@altlinux.org> 2.20-alt1
- Updated to upstream version 2.20.

* Mon Jul 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.19-alt1
- Updated to upstream version 2.19.

* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.15-alt1
- Updated to upstream version 2.15.

* Fri Sep 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13-alt1
- Updated to upstream version 2.13.

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt1.git20140711
- Version 2.10

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.5-alt1.1.qa1
- NMU: rebuilt for updated dependencies.

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Fixed build

* Sat Sep 17 2011 Slava Semushin <php-coder@altlinux.ru> 2.5-alt1
- Updated to 2.5

* Sat Jan 15 2011 Slava Semushin <php-coder@altlinux.ru> 2.4-alt1
- Updated to 2.4

* Sat Oct 30 2010 Slava Semushin <php-coder@altlinux.ru> 2.3-alt1
- Updated to 2.3
- Enable -Werror compiler flag
- Run make check

* Sun Jan 17 2010 Slava Semushin <php-coder@altlinux.ru> 2.1-alt1
- Initial build for ALT Linux Sisyphus (based on spec from PLD Linux)

* Sun Jan 17 2010 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: libmpdclient.spec,v $
Revision 1.2  2009/10/06 18:54:12  wiget
- rel 1

Revision 1.1  2009/10/06 18:47:31  wiget
- initial, based on libmpd.spec

