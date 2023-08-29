Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
BuildRequires: libtinfo-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Upstream changed its licensing to ASL 2.0 after releasing 0.9.18.
# I have decided to use the newest upstream code from September 2020 because
# in addition to many other fixes it fixes the build on Fedora.
%global commit0 dfe1ccb1055af99be0232a26520d247b5fe093bc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshotdate 20210601

%global libname libfoma

Name:           foma
Version:        0.10.0
Release:        alt1_0.7.%{snapshotdate}git%{shortcommit0}
Summary:        Xerox-compatible finite-state compiler

License:        Apache-2.0
URL:            https://github.com/mhulden/foma
Source0:        https://github.com/mhulden/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

# This patch is made after the OpenSUSE patch at
# https://build.opensuse.org/package/view_file/openSUSE:Factory/foma/foma-harden-build.patch?expand=1
#
# Foma does not use autotools, which complicates things a bit.
# CFLAGS, LDFLAGS and FLOOKUPLDFLAGS are edited with sed during the build so
# that the Fedora hardening switches are used. We can't, however, just
# add -pie to all of the linking phases with sed, because that would break
# the linker when building the shared library. For discussion on a similar
# issue, see https://lists.debian.org/debian-devel/2016/05/msg00302.html
Patch0:         foma-harden-build-fedora.patch

BuildRequires:  gcc zlib-devel readline-devel flex bison
Requires:       %{libname} = %{version}-%{release}
Source44: import.info

%description
Foma can be used for constructing finite-state automata and transducers.
It has support for many natural language processing applications such as
producing morphological analyzers. It is sufficiently generic to use for
a large number of purposes in addition to NLP. The foma interface is
similar to the Xerox xfst interface.

This package includes the foma command line tools.


%package -n     %{libname}
Group: Other
Summary:        The foma C library

%description -n %{libname}
Foma can be used for constructing finite-state automata and transducers.
It has support for many natural language processing applications such as
producing morphological analyzers. It is sufficiently generic to use for
a large number of purposes in addition to NLP. The foma interface is
similar to the Xerox xfst interface.

This package includes the foma C library.


%package -n     %{libname}-devel
Group: Other
Summary:        Development files for %{libname}
Requires:       %{libname} = %{version}-%{release}
Requires:       pkgconfig

%description -n %{libname}-devel
The libfoma-devel package contains libraries and header files for
developing applications that use libfoma.

%prep
%setup -q -n %{name}-%{commit0}
%patch0 -p1



%build
sed -i '/^CFLAGS/c\CFLAGS = %{optflags} -Wl,--as-needed -D_GNU_SOURCE -std=c99 -fvisibility=hidden -fPIC' foma/Makefile
sed -i '/^LDFLAGS/c\LDFLAGS = -lreadline -lz -ltinfo %{build_ldflags}' foma/Makefile
sed -i '/^FLOOKUPLDFLAGS/c\FLOOKUPLDFLAGS = libfoma.a -lz %{build_ldflags}' foma/Makefile
sed -i 's|echo "prefix=${prefix}"|echo "prefix=%{_prefix}"|' foma/Makefile

cd foma
%make_build


%install
sed -i '/^prefix/c\prefix = %{buildroot}%{_prefix}' foma/Makefile
sed -i '/^libdir/c\libdir = %{buildroot}%{_libdir}' foma/Makefile
cd foma
%makeinstall_std
# Remove static archive
find %{buildroot} -name '*.a' -exec rm -f {} ';'


%files
%{_bindir}/cgflookup
%{_bindir}/flookup
%{_bindir}/foma

%files -n %{libname}
%doc --no-dereference foma/COPYING
%doc foma/README
%{_libdir}/%{libname}.so.0
%{_libdir}/%{libname}.so.0.10.0

%files -n %{libname}-devel
%{_includedir}/*.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc


%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.10.0-alt1_0.7.20210601gitdfe1ccb
- update to new release by fcimport

* Sat Dec 18 2021 Igor Vlasenko <viy@altlinux.org> 0.10.0-alt1_0.2.20210601gitdfe1ccb
- update to new release by fcimport

* Sat Jul 24 2021 Igor Vlasenko <viy@altlinux.org> 0.10.0-alt1_0.1.20210601gitdfe1ccb
- new version

