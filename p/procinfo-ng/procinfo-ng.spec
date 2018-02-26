Name: procinfo-ng
Version: 2.0.304
Release: alt1

Summary: A tool for gathering and displaying system information
License: GPLv2 and LGPLv2
Group: Monitoring

URL: http://procinfo-ng.sourceforge.net/
Source: http://downloads.sourceforge.net/procinfo-ng/%name-%version.tar.bz2
Patch: procinfo-ng-2.0.304-man.patch

# Automatically added by buildreq on Fri Dec 03 2010
BuildRequires: gcc-c++ libncurses-devel

%description
The %name command gets system data from the /proc directory (the kernel
filesystem), formats it and displays it on standard output. You can use
%name to acquire information about your system from the kernel as it is
running.

%prep
%setup
%patch -p1

%build
subst 's/$(LDFLAGS) procinfo.cpp/procinfo.cpp $(LDFLAGS)/' Makefile.in
%configure
%make_build

%install
%makeinstall_std
# We want to avoid file conflict with "old generation" :) procinfo:
mv %buildroot%_bindir/procinfo %buildroot%_bindir/%name
mv %buildroot%_man8dir/procinfo.8 %buildroot%_man8dir/%name.8

%files
%doc LICENSE.txt
%_bindir/*
%_man8dir/*

%changelog
* Fri Dec 03 2010 Victor Forsiuk <force@altlinux.org> 2.0.304-alt1
- Initial build.
