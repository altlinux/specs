Name: rpm-build-pecl
Version: 0.3
Release: alt1

Summary: RPM helper scripts for build PECL packages
License: GPL
Group: Development/Other

URL: http://www.altlinux.org/Pecl_Policy
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-php5 rpm-build-intro
Requires: rpm-build-php5 php5-devel php5-simplexml

%description
RPM helper scripts for build PECL packages.
You can build PECL rpm package with
peclr make-rpm-spec <package> command from pear-PEAR_Command_Packaging package.
See %url for detailed PECL packaging policy.

%prep
%setup

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/pecl

%files
%doc README
%_rpmmacrosdir/pecl

%changelog
* Wed Oct 27 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- update spec and files, fix docs
- fix url for ALT Policy

* Sat Mar 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- use %%* for args
- add php5-devel to requires

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
