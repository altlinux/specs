# Upstream doesn't make releases.  We have to check the code out of git.
%define owner    tscrim
%define gittag   7b5a1f0039511326aeb616afb132a5065886b9d8
%define shorttag %(cut -b -7 <<< %gittag)
%define gitdate  20180227
%define soname 0

Name: coxeter3
Version: 3.1
Release: alt1
Summary: Combinatorial aspects of Coxeter group theory

License: GPL+
Group: Sciences/Mathematics
Url: https://github.com/%owner/coxeter

Source: %url/archive/%gittag/coxeter-%shorttag.tar.gz
# See https://github.com/tscrim/coxeter/pull/14
Source1: sage.h
Source2: sage.cpp
# Test files from the sagemath project
Source3: test.input
Source4: test.output.expected
# Store the runtime data in a more canonical place
Patch: coxeter-data.patch
# Build a shared library for use by sagemath
Patch1: coxeter-shared.patch

BuildRequires: gcc-c++ texlive-dist

%description
Coxeter is a program for the exploration of combinatorial issues related
to Coxeter groups and Hecke algebras, with a particular emphasis on the
computation of Kazhdan-lusztig polynomials and related questions.  It is
not a symbolic algebra system; rather, it is an interface for accessing
a direct C++ implementation of the concept of a Coxeter group.

%package -n lib%name-%soname
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name-%soname
This package contains a library that enables exploration of
combinatorial issues related to Coxeter groups and Hecke algebras, with
a particular emphasis on the computation of Kazhdan-lusztig polynomials
and related questions.

%package -n lib%name-devel
Summary: Header files and library links for coxeter
Group: Development/C++

%description -n lib%name-devel
Header files and library links for developing applications that use
the coxeter library.

%prep
%setup -n coxeter-%shorttag
%patch -p0
%patch1 -p0
cp -p %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 .

%build
%make_build optimize=true libdir=%_libdir \
  CXX=g++ CXXFLAGS="%optflags" LDFLAGS="$RPM_LD_FLAGS"
pdflatex INTRO.tex
pdflatex INTRO.tex

%install
# Install the library
mkdir -p %buildroot%_libdir
cp -a libcoxeter3.so* %buildroot%_libdir

# Install the header files
mkdir -p %buildroot%_includedir/coxeter
cp -p *.h *.hpp %buildroot%_includedir/coxeter

# Install the binary
mkdir -p %buildroot%_bindir
cp -p coxeter %buildroot%_bindir

# Install the runtime data
mkdir -p %buildroot%_datadir/coxeter
cp -a coxeter_matrices headers messages %buildroot%_datadir/coxeter

%check
LD_LIBRARY_PATH=$PWD ./coxeter < test.input > test.output
if ! diff test.output.expected test.output > /dev/null; then
  echo >&2 "Error testing coxeter on test.input:"
  diff -u test.output.expected test.output
  exit 1
fi

%files
%doc INTRO.pdf README
%_bindir/coxeter
%_datadir/coxeter/

%files -n lib%name-%soname
%_libdir/libcoxeter3.so.%{soname}*

%files -n lib%name-devel
%_includedir/coxeter/
%_libdir/libcoxeter3.so

%changelog
* Thu Nov 25 2021 Leontiy Volodin <lvol@altlinux.org> 3.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
