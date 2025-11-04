%define _unpackaged_files_terminate_build 1
%define lib_name esaxx

Name: %lib_name
Version: 20140203
Release: alt1

Summary: C++ enhanced suffix array template library
License: MIT
Group: Development/C++

Url: https://github.com/hillbig/esaxx
Vcs: https://github.com/hillbig/esaxx
Source: %name-%version.tar

%description
esaxx is a C++ template library supporting to build an enhanced suffix array
which is useful for various string algorithms. For an input text of length N,
esaxx builds a suffix tree in linear time using almost 20N bytes working space
(alphabet size independent).

In construction, esaxx first build a suffix array, and then compute the
inversed suffix array, and finally obtain the height array. By using a height
array, internal nodes in a suffix tree are enumerated in post-order.

It also provides the sample program to enumerate the statistics of all
substrings appeared in a text in linear time.

For a suffix array construction, I use sais.hxx, the induced sorting algorithm
implemented by Yuta Mori.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
Headers for building software that uses %name.

%prep
%setup

%install
mkdir -p %buildroot%_includedir/%lib_name
cp *.h *.hxx %buildroot%_includedir/%lib_name

%files -n lib%name-devel
%_includedir/%lib_name
%doc README

%changelog
* Thu Apr 17 2025 David Sultaniiazov <x1z53@altlinux.org> 20140203-alt1
- Initial build
