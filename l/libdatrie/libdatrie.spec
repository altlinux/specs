Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libdatrie
Version:        0.2.9
Release:        alt1_6
Summary:        Implementation of Double-Array structure for representing trie
License:        LGPLv2+
URL:            http://linux.thai.net/projects/datrie
Source0:        http://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
Patch0:         libdatrie-fixes-docs.patch
BuildRequires:  autoconf, automake, libtool
BuildRequires:  doxygen
Source44: import.info

%description
datrie is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with O(1) 
time complexity for searching. Comparably as efficient as hashing, trie also 
provides flexibility on incremental matching and key spelling manipulation. 
This makes it ideal for lexical analyzers, as well as spelling dictionaries.

Details of the implementation: http://linux.thai.net/~thep/datrie/datrie.html

%package        devel
Group: System/Libraries
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .docs

%build
autoreconf -f -i -v
#sed -i '/sys_lib_dlsearch_path_spec/s|/usr/lib |/usr/lib /usr/lib64|' configure
%configure --disable-static \
           --with-html-docdir=%{_docdir}/%{name}-devel
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std
rm -frv %{buildroot}%{_docdir}/%{name}
find %{buildroot} -name '*.*a' -delete -print

%check
LD_LIBRARY_PATH=../datrie/.libs make check

%files
%doc COPYING
%{_libdir}/libdatrie.so.*

%files devel
%doc AUTHORS ChangeLog NEWS README*
%{_includedir}/datrie/
%{_libdir}/libdatrie.so
%{_libdir}/pkgconfig/datrie-0.2.pc
%{_bindir}/trietool*
%{_mandir}/man1/trietool*
%{_docdir}/%{name}-devel/*.html
%{_docdir}/%{name}-devel/*.css
%{_docdir}/%{name}-devel/*.png
%{_docdir}/%{name}-devel/*.js

%changelog
* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.9-alt1_6
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.8-alt1_5
- new version

