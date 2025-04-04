%define _unpackaged_files_terminate_build 1
%global _libexecdir %prefix/libexec

Name: icmake
Version: 13.02.00
Release: alt1
Summary: A make utility using a C-like syntax
License: GPLv3
Group: Development/Tools
Url: https://gitlab.com/fbb-git/icmake
VCS: https://gitlab.com/fbb-git/icmake.git
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: gcc-c++

%description
Icmake (Intelligent C-like MAKE) is a hybrid between a make utility and a
shell script language, designed for software development and system
administration. Unlike traditional make, icmake uses a C-like scripting
language, giving developers more power and flexibility when defining build
rules or automating tasks.

It includes a compiler, executor, and utilities to support cross-platform
script execution. Icmake is especially useful for managing complex build
environments and packaging systems.

%package doc
Summary: Documentation for Icmake
Group: Development/Documentation
BuildArch: noarch

%description doc
Icmake (Intelligent C-like MAKE) is a hybrid between a make utility and a
shell script language, designed for software development and system
administration. Unlike traditional make, icmake uses a C-like scripting
language, giving developers more power and flexibility when defining build
rules or automating tasks.

It includes a compiler, executor, and utilities to support cross-platform
script execution. Icmake is especially useful for managing complex build
environments and packaging systems.

This package contains documentation for Icmake.

%prep
%setup
%patch0 -p1

%build
echo "/* created during rpmbuild */" >  %name/INSTALL.im
echo "#define BINDIR      \"%_bindir\"" >>  %name/INSTALL.im
echo "#define SKELDIR     \"%_datadir/%name\"" >>  %name/INSTALL.im
echo "#define MANDIR      \"%_mandir\"" >>  %name/INSTALL.im
echo "#define LIBDIR      \"%_libexecdir/%name\"" >>  %name/INSTALL.im
echo "#define CONFDIR     \"%_sysconfdir/%name\"" >>  %name/INSTALL.im
echo "#define DOCDIR      \"%_docdir/%name-%version\"" >>  %name/INSTALL.im
export ICMAKE_CPPSTD=--std=c++26
pushd %name
./prepare /
./buildlib /
./build all
popd

%install
pushd %name
./install all %buildroot
popd

%files
%_sysconfdir/*
%_bindir/*
%_libexecdir/%name
%_datadir/%name
%_man1dir/*
%_man7dir/*

%files doc
%_docdir/%name-%version

%changelog
* Fri Apr 04 2025 Anton Farygin <rider@altlinux.com> 13.02.00-alt1
- 13.01.00 -> 13.02.00
- updated summary and description

* Thu Apr 03 2025 Anton Farygin <rider@altlinux.com> 13.01.00-alt1
- 9.03.01 -> 13.01.00

* Wed Oct 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 9.03.01-alt1
- Updated to upstream version 9.03.01.

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.21.01-alt1.git20140120
- Version 7.21.01

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.21.00-alt1.git20130802
- Version 7.21.00

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.00-alt1.git20120722
- Version 7.19.00

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.16.00-alt1
- Initial build for Sisyphus

