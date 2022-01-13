%def_disable check
# XXX incorrect on i586 -DBUILD_UNIT_TESTS=1

Name:       libcuckoo
Version:    0.3
Release:    alt1
Summary:    A high-performance, compact hash table
URL:        https://github.com/efficient/libcuckoo
License:    Apache-2.0
Group:      Development/C++
Source:     %name-%version.tar.gz

# Automatically added by buildreq on Thu Jan 13 2022
# optimized out: cmake cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libsasl2-3 libstdc++-devel python3-base sh4
BuildRequires: ctest gcc-c++ python3

%description
%summary

%package devel
Summary:    %summary
Group:      Development/C++

%description devel
A high-performance, compact hash table that allows multiple concurrent
reader and writer threads

The Doxygen-generated documentation is available at the project page.

Authors: Manu Goyal, Bin Fan, Xiaozhou Li, David G. Andersen, and
Michael Kaminsky

For details about this algorithm and citations, please refer to our
papers in NSDI 2013 and EuroSys 2014. Some of the details of the hashing
algorithm have been improved since that work (e.g., the previous
algorithm in 1 serializes all writer threads, while our current
implementation supports multiple concurrent writers), however, and this
source code is now the definitive reference.

%prep
%setup

%build
%cmake -DBUILD_EXAMPLES=1 -DBUILD_TESTS=1 -DBUILD_UNIT_TESTS=1
%cmake_build

%install 
%cmake_install

%if_enabled check
%check
%make_build -C "%_cmake__builddir" test
%endif

%files devel
%doc examples libcuckoo-gdb-printers *.md
%_includedir/%name-c
%_includedir/%name
%_datadir/cmake/%name

%changelog
* Thu Jan 13 2022 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build for ALT
