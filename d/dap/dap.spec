Name: dap
Version: 3.9
Release: alt1
Summary: A small statistics and graphics package based on C
Url: http://www.gnu.org/software/dap/
Group: Sciences/Mathematics
License: GPL
Source: %name-%version.tar.gz

%description
This directory and its subdirectories contain the source code for
Dap, which is a small statistics and graphics package based on C.
It provides core methods of data management, analysis, and graphics
that are commonly used in statistical consulting practice.  Anyone
familiar with the basic syntax of C programs can learn to use Dap
quickly and easily from the manual and the examples contained in
it; advanced features of C are not necessary, although they are
available.  (The manual contains a brief introduction to the C
syntax needed for Dap.)  Because Dap processes files one line at a
time, rather than reading entire files into memory, it can be, and
has been, used on data sets that have very many lines and/or very
many variables.

%package devel
Group: Development/C
Summary: Development environment for %name, %summary
%description devel
%summary

%prep
%setup

%build
%configure --with-pic
%make_build

%install
%makeinstall

%files
%doc AUTHORS INSTALL NEWS README TODO
%doc examples
%_infodir/%{name}*
%_bindir/*

%files devel
%_libdir/*.a
%_includedir/*

%changelog
* Sat Mar 22 2014 Fr. Br. George <george@altlinux.ru> 3.9-alt1
- Autobuild version bump to 3.9

* Sat Mar 22 2014 Fr. Br. George <george@altlinux.ru> 3.8-alt1
- Initial build for ALT

