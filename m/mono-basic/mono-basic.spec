
Name: mono-basic
Version: 2.10
Release: alt1
License: %lgpl2plus %mit
Url: http://www.mono-project.com/
Group: Development/Other
Summary: Visual Basic .NET support for Mono
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
Source: http://www.go-mono.com/sources/%name/%name-%version.tar

BuildPreReq: rpm-build-mono rpm-build-licenses
BuildRequires: mono-devel >= 1.2.5 mono-winforms
BuildRequires: /proc

%description
This package contains the Visual Basic .NET compiler and language
runtime. This allows you to compile and run VB.NET application and
assemblies.

%prep
%setup -q

%build
mkdir -p build/deps
mkdir -p class/lib/vbnc

./configure --prefix=/usr
make

%install
%make_install DESTDIR=%buildroot install

%files
%doc README
%_bindir/vbnc*
%_monodir/?.0/*
%_monogacdir/*
%_man1dir/*

%changelog
* Wed Oct 12 2011 Alexey Shabalin <shaba@altlinux.ru> 2.10-alt1
- 2.10

* Tue Nov 23 2010 Alexey Shabalin <shaba@altlinux.ru> 2.8-alt1
- 2.8

* Tue Mar 16 2010 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Dec 16 2009 Alexey Shabalin <shaba@altlinux.ru> 2.6-alt1
- 2.6

* Wed Jul 01 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- remove hack for build from git with empty dir (add in upstrem empty file)

* Mon Apr 13 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4-alt1
- 2.4
- add hack for build from git with empty dir

* Thu Jan 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1
- 2.2

* Tue Oct 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0 release

* Fri Sep 12 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.rc1
- 2.0 RC1

* Mon Sep 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre2
- 2.0 preview2

* Mon Aug 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt0.pre1
- 2.0 preview1

* Fri Mar 28 2008 Alexey Shabalin <shaba@altlinux.ru> 1.9-alt1
- 1.9

* Tue Jan 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- initial package for ALTLinux

