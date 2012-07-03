Name: imgdiff
Version: 1.0
Release: alt2

Packager: Vladislav Zavjalov <slazav@altlinux.org>

Source:%name-%version.tar

Summary: diff for images
License: GPL
Group: Graphics

Requires: libgtkmm2
BuildRequires: gcc-c++ libgtkmm2-devel

%description
diff for images

%prep
%setup
%build
%make_build
%install
%makeinstall
%files
%_bindir/*
%_mandir/man1/*

%changelog
* Tue Nov 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt2
- fix include

* Wed Jun 25 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- initial version


