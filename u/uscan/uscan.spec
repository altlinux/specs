Name: uscan
Version: 0.1
Release: alt1

Packager: Avramenko Andrew <liks@altlinux.ru>
Summary: Utility to check watch files
Source0: uscan

License: %gpl2plus
Group: Development/Other

BuildArch: noarch

BuildPreReq: rpm-build-licenses perl-upstreamwatch
Requires: perl-upstreamwatch

%description
Prometeus project will provides interesting feature - comparison
with upstream version. Uscan is an utiliy for developers to check
if watch file works fine.

%prep

%build

%install
mkdir -p %buildroot%_bindir
install %SOURCE0 %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Mon Dec 10 2007 Avramenko Andrew <liks@altlinux.ru> 0.1-alt1
- First draft

