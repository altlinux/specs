# -*- rpm-spec -*-
# $Id: rtfm,v 1.3 2002/11/25 18:04:43 grigory Exp $

Name: rtfm
Version: 0.0.1
Release: alt2

Summary: Misc documentation for new users
License: GPL
Group: Books/Faqs
Url: ftp://ftp.altlinux.ru
Source0: %name-%version.sh
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Requires: /usr/bin/man /usr/bin/find

Provides: RTFM r.t.f.m R.T.F.M.
BuildArch: noarch

%description
R.T.F.M. - misc documentation for new users
make easy use of man. run rtfm <command> or
rtfm <command path>.

%install
mkdir -p %buildroot/{%_bindir,%_datadir}
install -m 0755 %SOURCE0 %buildroot%_bindir/%name
ln -s ./doc %buildroot%_datadir/%name
ln -s ./doc %buildroot%_datadir/RTFM

%files
%_datadir/*
%_bindir/%name

%changelog
* Mon Jan 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.0.1-alt2
- Minor spec cleanup.

* Mon Nov 25 2002 Grigory Milev <week@altlinux.ru> 0.0.1-alt1
- Initial build.


