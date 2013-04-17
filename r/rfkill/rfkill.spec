Name: rfkill
Version: 0.4
Release: alt1.qa1

Summary: A tool to use /dev/rfkill
License: BSD-style
Group: Networking/Other

Url: http://wireless.kernel.org/en/users/Documentation/rfkill

Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
rfkill is a small tool to query the state of the rfkill switches,
buttons and subsystem interfaces.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%doc README
%_sbindir/*
%_man8dir/*

%changelog
* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Apr 27 2010 Mykola Grechukh <gns@altlinux.ru> 0.4-alt1
- new version from upstream

* Thu Oct 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt1
- initial version
