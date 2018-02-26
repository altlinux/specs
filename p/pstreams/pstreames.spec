Name: pstreams
Version: 0.5.2
Release: alt1

Summary: POSIX Process Control in C++
License: GPLv2
Group: Development/Other

Url: http://freshmeat.net/projects/pstreams/
Packager: Vladimir Scherbaev <vladimir at altlinux.org>

Source: %name-%version.tar.gz
Patch1: %name-%version-alt-make.patch

# Automatically added by buildreq on Sat Sep 13 2008
BuildRequires: doxygen

%description
PStreams allows you to run another program from your C++ application and to transfer data between the two programs, 
similar to shell pipelines. In the simplest case, a PStreams class is like a C++ wrapper for the POSIX.2 
functions popen(3) and pclose(3), using C++ IOStreams instead of C's stdio library. 
The library provides class templates in the style of the standard IOStreams that can be used with any standard-conforming C++ compiler on a POSIX platform.
The classes use a streambuf class that uses fork() and the exec family of functions to create a new process and to write/read data to/from the process. 

%prep
%setup -q
%patch1

%build
%make_build

%install
%make_install DESTDIR=%buildroot install
%__mkdir_p %buildroot
install -d %buildroot%_includedir/%name
install -v -m0644 pstream.h %buildroot%_includedir/%name

%files 
%doc AUTHORS ChangeLog COPYING.LIB Doxyfile INSTALL mainpage.html MANIFEST README
%_includedir/%name/*

%changelog
* Fri Sep 12 2008 Vladimir Scherbaev <vladimir@altlinux.org> 0.5.2-alt1
- Initial build


