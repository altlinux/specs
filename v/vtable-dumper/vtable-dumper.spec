Name:		vtable-dumper
Version:	1.0
Release:	alt1
Group:		Development/Other
License:	GPLv2+
Source:		%version.tar.gz
Summary:	List content of virtual tables in a C++ shared library
URL:		https://github.com/lvc/vtable-dumper

# Automatically added by buildreq on Mon Sep 16 2013
BuildRequires: libelf-devel libstdc++-devel

%description
Vtable-Dumper - lists content of virtual tables in a C++ shared library.

It is intended for developers of software libraries and maintainers of
Linux distributions who are interested in ensuring backward binary
compatibility.

%prep
%setup

%build
%make

%install
# TODO this compiles the file again, but who cares?
%makeinstall

%files
%doc README
%_bindir/*

%changelog
* Mon Sep 16 2013 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Initial build from upstream

