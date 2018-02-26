# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define datrie_version 0.2.3

Summary:  Thai language support routines
Name: libthai
Version: 0.1.14
Release: alt3_5
License: LGPLv2+
Group: System/Libraries
Source: ftp://linux.thai.net/pub/thailinux/software/libthai/libthai-%{version}.tar.gz
Source1: ftp://linux.thai.net/pub/thailinux/software/libthai/libdatrie-%{datrie_version}.tar.gz
Patch: libthai-libdatrie-static-build.patch
Patch1: libthai-0.1.9-doxygen-segfault.patch
Patch2: libthai-0.1.9-multilib.patch
URL: http://linux.thai.net

BuildRequires: doxygen
# we edit the Makefile.am's
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
Source44: import.info

%description
LibThai is a set of Thai language support routines aimed to ease
developers' tasks to incorporate Thai language support in their applications.
It includes important Thai-specific functions e.g. word breaking, input and
output methods as well as basic character and string supports.

%package devel
Summary:  Thai language support routines
Group: Development/C
Requires: libthai = %{version}-%{release}

%description devel
The libthai-devel package includes the header files and developer docs 
for the libthai package.

Install libthai-devel if you want to develop programs which will use
libthai.

%prep
%setup -q -n %{name}-%{version} -a 1
mv libdatrie-%{datrie_version} libdatrie
%patch -p1 -b .static-build
%patch1 -p1 -b .doxygen-segfault
%patch2 -p1 -b .multilib

%build

# libthai depends on this library called libdatrie.  libdatrie is a
# data-structure implementaiton that the author of libthai ripped out of it.
# However, since libthai is the only user of that code, there's no reason to
# 1) package it separately, 2) use it as a shared library.
# So, we compile it as a libtool convenience library and include in libthai.so,
# and use symbol hiding to hide them (and other internal symbols).
#
# The patch takes care of making datrie into a convenience lib and making sure
# libthai will include it (and hide its symbols), and the exports make sure
# libthai finds the uninstalled libdatrie.  We need to call automake, since
# the patch modifies a few Makefile.am's.

{
  pushd libdatrie
  mkdir m4
  autoreconf -i -f
  %configure
  make
  popd
}

export DATRIE_CFLAGS="-I$PWD/libdatrie"
export DATRIE_LIBS="$PWD/libdatrie/datrie/libdatrie.la"
export PATH="$PWD/libdatrie/tools:$PATH"

autoreconf -i -f

%configure --disable-static
make

%install

%makeinstall

# move installed doc files back to build directory to package them
# in the right place
mkdir installed-docs
mv $RPM_BUILD_ROOT%{_docdir}/libthai/* installed-docs
rmdir $RPM_BUILD_ROOT%{_docdir}/libthai

rm $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc README AUTHORS COPYING ChangeLog TODO
%{_libdir}/lib*.so.*
%{_datadir}/libthai

%files devel
%doc installed-docs/*
%{_includedir}/thai
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt3_5
- fixed build

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt2_5
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt2_4
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.14-alt1_4
- initial import by fcimport

