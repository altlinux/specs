
Name: pegtl
Version: 1.3.1
Release: alt1%ubt

Group: System/Libraries
Summary: Parsing Expression Grammar Template Library
License: MIT
Url: https://github.com/ColinH/%name/

Source0: %name-%version.tar

# Automatically added by buildreq on Fri Aug 04 2017 (-bi)
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libstdc++-devel python-base python-modules python3 python3-base rpm-build-python3
#BuildRequires: gcc-c++ python-module-google python3-dev python3-module-zope ruby ruby-stdlibs
BuildRequires(pre): rpm-build-ubt
BuildRequires: make
#BuildRequires: gcc-c++

%description
The Parsing Expression Grammar Template Library (PEGTL) is a zero-dependency
C++11 header-only library for creating parsers according to a Parsing
Expression Grammar (PEG).

%package devel
Summary: Development files for %name
Group: Development/C++
Provides: PEGTL = %EVR
%description devel
The %name-devel package contains C++ header files for developing
applications that use %name.

%prep
%setup -q

#build
#export CXXFLAGS="%optflags"
#make CPPFLAGS="-pedantic %optflags" PEGTL_CPPFLAGS="-pedantic %optflags" CXXFLAGS="%optflags" PEGTL_CXXFLAGS="%optflags" compile

%install
install -d -m 0755 %buildroot/%_includedir/
find pegtl.hh pegtl/ -type f -exec install -D -p -m 0644 "{}" "%buildroot/%_includedir/{}" \;

%files devel
%doc README.md LICENSE
%_includedir/pegtl.hh
%_includedir/pegtl/

%changelog
* Fri Aug 04 2017 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1%ubt
- initial build
