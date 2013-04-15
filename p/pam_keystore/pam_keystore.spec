Name: pam_keystore
Version: 0.1.2
Release: alt1.svn1226.qa1

Summary: Store user password in kernel keystore 
License: %asl
Group: System/Libraries
Url: http://www.calculate-linux.ru
Source: %name-%version.tar
Source1: README.ALT.UTF8
Patch0: %name-%version-%release.patch 

Packager: Maxim Ivanov  <redbaron@altlinux.org>

BuildRequires: rpm-build-licenses
BuildRequires: pam-devel libkeyutils-devel

%description
PAM module to store user password in kernely key storage
It could be retrieved later from userspace using keyutils

%prep
%setup 
%patch0 -p1

%build
%make_build

%install
%makeinstall DESTDIR=%buildroot
mkdir -p %buildroot%_docdir/%name-%version/
cp %SOURCE1 %buildroot%_docdir/%name-%version/


%files
%doc %_docdir/*
/%_lib/security/*

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.2-alt1.svn1226.qa1
- NMU: rebuilt for debuginfo.

* Fri Apr 17 2009 Ivanov Maxim <redbaron@altlinux.org> 0.1.2-alt1.svn1226
- Initial build for Sisyphus 

