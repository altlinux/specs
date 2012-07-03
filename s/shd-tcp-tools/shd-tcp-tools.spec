Name: shd-tcp-tools
Version: 0.05
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: shd-tcp-tools is a set of TCP network tools
License: MIT/X Consortium
Group: Networking/Other

URL: http://zakalwe.fi/~shd/foss/shd-tcp-tools/
Source: %url/%name-%version.tar.bz2

%description
shd-tcp-tools is a set of TCP network tools.

%prep
%setup

%build
./configure --package-prefix=%buildroot --prefix=/usr
%make_build CFLAGS="%optflags"

%install
%make install

%files
%_bindir/*
%doc ChangeLog.txt readme.txt

%changelog
* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 0.05-alt1
- 0.05

* Wed Aug 17 2005 Victor Forsyuk <force@altlinux.ru> 0.04-alt1
- Initial build.
