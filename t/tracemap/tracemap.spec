Name: tracemap
Version: 20080629
Release: alt1

Summary: Build graphical host trace map
License: Public domain
Group: Monitoring

Url: http://xgu.ru/wiki/tracemap
Source0: http://xgu.ru/downloads/tracemap.pl
Source1: http://xgu.ru/hg/tracemap/raw-file/0d498f80f832/xguru_fun
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

# Automatically added by buildreq on Fri Sep 10 2010 (-bi)
BuildRequires: libdb4-devel perl-Net-IP

%description
The script to generate pretty image showing how a host,
or a few, are getting routed to from our "viewpoint".
It will merge common trace parts in case there are many.

%prep

%build

%install
install -pDm755 %SOURCE0 %buildroot%_bindir/%name
install -pDm644 %SOURCE1 .

%files
%_bindir/*
%doc xguru_fun

%changelog
* Fri Sep 10 2010 Michael Shigorin <mike@altlinux.org> 20080629-alt1
- built for ALT Linux, finally
- thanks Igor Chubin for recommending his script
