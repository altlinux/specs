%define oname bar
Name: barcat
Version: 1.4
Release: alt0.1

Summary: portable Unix script for showing progress bars

License: BSD like
Url: http://www.theiling.de/projects/bar.html
Group: Text tools

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.theiling.de/downloads/%oname-%version-src.tar.bz2
BuildArch: noarch

%description
barcat is just like "cat", but displays an ASCII progress bar. Its
goal is to work on any Unix-like platform and to be directly usable
in installation scripts without needing compilation, so it is a pure
shell script.

%prep
%setup -q -n %oname-%version

%install
install -D %oname -m755 %buildroot%_bindir/%oname

%files
%doc COPYING README
%_bindir/*

%changelog
* Sun Feb 19 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt0.1
- initial build for ALT Linux Sisyphus

