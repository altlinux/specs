Name: mxk
Version: 1.10
Release: alt1

Summary: An evdev/uinput input mangling server
License: GPLv3+
Group: System/Configuration/Hardware
Url: http://welz.org.za/projects/mxk

Source: %name-%version.tar

BuildPreReq: groff-ps

%description
mxk is a reasonably sophisticated input rewriting server. It picks up
where conventional keyboard mappings reach their limits. mxk uses the
linux evdev/uinput infrastructure. This means that mxk runs entirely in
userspace, it doesn't require a special kernel driver or patch.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall etcdir=%buildroot%_sysconfdir

%files
%_sbindir/*
%_sysconfdir/%name/
%_man8dir/*
%doc README

%changelog
* Tue Sep 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1
- Version 1.10

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Apr 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.8-alt1
- 1.8

* Mon Mar 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.7-alt1
- initial build

