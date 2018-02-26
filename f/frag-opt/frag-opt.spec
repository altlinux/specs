%def_disable static
%define shortname frag-opt

Name: %shortname
Version: 0.5.5
Release: alt3

License: LGPL
Url: http://personal.penny-craal.org/midianian/hack/
Packager: Pavlov Konstantin <thresh@altlinux.ru>
Summary: frag-opt is a re-entrant, portable command-line parsing library.
Group: System/Libraries
Source: %shortname-%version.tar.bz2

# Automatically added by buildreq on Mon Mar 14 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
frag-opt is a re-entrant, portable command-line parsing library.

%package -n lib%name
Summary: frag-opt commandline parsing library.
Group: Development/C++
Provides: frag-opt = %version-%release
Conflicts: frag-opt <= 0.5.4

%description -n lib%name
frag-opt is a re-entrant, portable command-line parsing library.

%package -n lib%name-devel
Summary: frag-opt development files.
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
frag-opt is a re-entrant, portable command-line parsing library.
The package contains the C headers and library to compile programs
based on frag-opt.

%if_enabled static
%package -n lib%name-devel-static
Summary: frag-opt static development files.
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel-static
frag-opt is a re-entrant, portable command-line parsing library.
The package contains static library to compile programs
based on frag-opt.
%endif

%prep
%setup -q -n %shortname-%version

%build
%configure \
		%{subst_enable static}

%make_build

%install

%make_install DESTDIR="%buildroot" install

%if_disabled static
%__rm -f %buildroot%_libdir/*.a
%endif

%files -n lib%name
%_libdir/*.so.*
%_man3dir/*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so

%if_enabled static
%files lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt3
- Rebuilt for soname set-versions

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.5.5-alt2
- Remove post/postun ldconfig calls.
- Fix URL.

* Fri Oct 07 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.5.5-alt1
- 0.5.5 release.
- Changed library name due to policy.
- Changed license tag to LGPL as it really is.

* Mon Mar 14 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.5.4-alt1
- 0.5.4 release.
