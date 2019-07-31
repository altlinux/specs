Name:     definier
Version:  0.2
Release:  alt1

Summary:  A graphical interface for defining nrpe checks for check_timed_logs.pl
License:  GPLv2+
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/definier.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
A graphical interface for defining nrpe checks for check_timed_logs.pl. Check_timed_logs.pl is also included

%prep
%setup

%install
install -Dm 0644 definier %buildroot%_bindir/definier

%files
%_bindir/*
%doc *.md

%changelog
* Thu Jul 25 2019 Denis Medvedev <nbr@altlinux.org> 0.2-alt1
Initial release
