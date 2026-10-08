%define _unpackaged_files_terminate_build 1

Name: logtop
Version: 0.7
Release: alt2
Summary: Display real time statistics of whatever you want
License: BSD-2-Clause
Group: Text tools
Url: http://julienpalard.github.io/logtop/

# https://github.com/JulienPalard/logtop.git
Source: %name-%version.tar
Patch1: %name-%version-alt-build.patch

BuildRequires: libncurses-devel libncursesw-devel libuthash-devel

Requires: lib%name = %EVR

%description
logtop displays real-time count of strings received in standard input.
It's useful for some cases, like getting the IP flooding your server:
$ tail -f /var/log/apache2/access.log | cut -d ' ' -f1 | logtop

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
logtop displays real-time count of strings received in standard input.
It's useful for some cases, like getting the IP flooding your server:
$ tail -f /var/log/apache2/access.log | cut -d ' ' -f1 | logtop

This package contains shared library of %name.

%prep
%setup
%patch1 -p1
%build
%make_build all

%install
%makeinstall_std LIB_SUFFIX=%_libsuff

%files
%doc COPYRIGHT NCURSES_COPYRIGHT
%doc ChangeLog README.md examples
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so


%changelog
* Thu Oct 08 2026 Anton Farygin <rider@altlinux.org> 0.7-alt2
- Disabled unused Python bindings to fix build with Python 3.14.

* Tue Dec 19 2023 Grigory Ustinov <grenka@altlinux.org> 0.7-alt1.1
- NMU: Add build dependency on setuptools.

* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7-alt1
- Updated to upstream version 0.7.

* Thu Oct 31 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt3
- python2 -> python3

* Tue May 07 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.1-alt2.git20140901.2
- Fixed lib suffix handling.

* Tue Apr 02 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1.git20140901.2
- Rebuild with python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1.git20140901.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20140901.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri May 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20140901
- Initial build for Sisyphus

