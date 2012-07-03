Name: rpm-build-pear
Version: 0.4
Release: alt2

Summary: RPM helper scripts for build PEAR packages

License: GPL
Group: Development/Other
Url: http://www.freesource.info/wiki/Altlinux/Policy/Pear

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://etersoft.ru/download/%name/%name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-php5 rpm-build-compat
Requires: rpm-build-php5 php5 php5-simplexml

%description
RPM helper scripts for build PEAR packages.
You can build PEAR rpm package with
pear make-rpm-spec <package> command from pear-PEAR_Command_Packaging package.
See %url for detailed PEAR packaging policy.

%prep
%setup -q

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/pear
install -D -m644 xml2changelog %buildroot/%php5_peardir/xml2changelog
install -D -m644 PHP-LICENSE-3.01 %buildroot/%php5_peardir/PHP-LICENSE-3.01

%files
%doc README
%_rpmmacrosdir/pear
%php5_peardir/xml2changelog
%php5_peardir/PHP-LICENSE-3.01

%changelog
* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- cleanup spec, move to build from git

* Mon Mar 24 2008 Denis Klimov <zver@altlinux.ru> 0.4-alt1
- Modify condition exist %%{pear_name}-%%{version} directory in macros file

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- new names for pear service macroses (see README)
- hide cd from install section in pear_install_std macros

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add rpm-build-php5 (build)requires
- change macros' names to RH compatible
- add php5, php5-simplexml requires

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
