%define _unpackaged_files_terminate_build 1

Name: memcache-top
Version: 0.6
Release: alt1.1
License: BSD
Group: Monitoring
Source: %name
URL: http://code.google.com/p/memcache-top/
Packager: Maxim Ivanov <redbaron@altlinux.org>

BuildRequires(pre): rpm-build-perl
Summary: top-like realtime stats from memcached
BuildArch: noarch
BuildRequires: perl-Term-ANSIColor

%description
It gives you the basic stats, and not too much else. (You can specify
thresholds, for instance, and it'll change color to red if you exceed
the thresholds. You can also choose the refresh/ sleep time, and whether
to show immediate (per second) stats, or lifetime stats. But it pretty
much all revolves around those stats.)

%prep
cp %SOURCE0 .

%install
install -D -m 755 %name  %buildroot%_bindir/%name


%files
%_bindir/*

%changelog
* Tue Nov 30 2010 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Nov 01 2009 Maxim Ivanov <redbaron at altlinux.org> 0.6-alt1
- Initial build for ALT Linux

