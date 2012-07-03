Name: mirmon
Version: 1.38
Release: alt1

Summary: Monitor the state of mirrors
License: BSD-style
Group: Networking/Other
Url: http://people.cs.uu.nl/henkp/mirmon/
Packager: Dmitry V. Levin <ldv@altlinux.org>
BuildArch: noarch

# http://people.cs.uu.nl/henkp/mirmon/src/mirmon-%version.tar.gz
Source: mirmon-%version.tar

%description
This packages contains a mirmon program -
an utility to monitor the state of mirrors.

%prep
%setup -q
sed -i 's,/sw/bin/,%_bindir/,g' mirmon

%install
mkdir -p %buildroot{%_bindir,%_datadir/%name}
install -pm755 mirmon %buildroot%_bindir/
cp -a countries.list icons %buildroot%_datadir/%name/

%files
%_bindir/*
%_datadir/%name
%doc *.txt

%changelog
* Thu Sep 20 2007 Dmitry V. Levin <ldv@altlinux.org> 1.38-alt1
- Initial revision.

