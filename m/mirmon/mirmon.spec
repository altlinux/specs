Name: mirmon
Version: 2.11
Release: alt1

Summary: Monitor the state of mirrors
License: MIT
Group: Networking/Other
Url: http://www2.projects.science.uu.nl/ictbeta/mirmon/
BuildArch: noarch

# http://www2.projects.science.uu.nl/ictbeta/mirmon/mirmon-%version.tar.gz
Source: mirmon-%version.tar

%description
This packages contains a mirmon program -
an utility to monitor the state of mirrors.

%prep
%setup -q
sed -i 's,/sw/bin/,%_bindir/,g' mirmon

%install
mkdir -p %buildroot{%_bindir,%_datadir/%name,%_man1dir}
install -pm755 mirmon %buildroot%_bindir/
install -pm644 mirmon.1 %buildroot%_man1dir/
cp -a countries.list icons %buildroot%_datadir/%name/

%define _unpackaged_files_terminate_build 1

%files
%_bindir/%name
%_man1dir/%{name}.1*
%_datadir/%name
%doc *.txt

%changelog
* Wed Apr 06 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.11-alt1
- Updated to 2.11.

* Thu Sep 20 2007 Dmitry V. Levin <ldv@altlinux.org> 1.38-alt1
- Initial revision.
