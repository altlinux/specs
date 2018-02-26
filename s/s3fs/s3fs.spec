Name: s3fs
Version: 0.0.191
Release: alt5

Summary: Amazon S3 filesystem using FUSE
Group: System/Kernel and hardware
License: GPL
Url: http://code.google.com/p/s3fs/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version.patch

Requires: fuse

# Automatically added by buildreq on Mon Mar 21 2011 (-bb)
BuildRequires: gcc-c++ libcurl-devel libfuse-devel libmpc libssl-devel libxml2-devel

%description
%summary

%prep
%setup
%patch0 -p1

%build
%make

%install
%makeinstall

%files
%_bindir/s3fs
%doc README

%changelog
* Mon Mar 21 2011 Denis Smirnov <mithraen@altlinux.ru> 0.0.191-alt5
- fix build

* Thu Feb 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.0.191-alt4
- repocop fix for specfile-macros-get_dep-is-deprecated

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.191-alt3
- rebuild with new openssl

* Sun Aug 29 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.191-alt2
- cleanup spec

* Fri Feb 12 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.191-alt1
- first build for Sisyphus
