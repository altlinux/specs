%define oname HIP
%define mwversion 1.46
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.1.0
Release: alt1

Summary: MediaWiki extension for Church Slavonic text in the HIP encoding

License: GPL-2.0-or-later
Group: Networking/WWW
Url: https://soulibre.ru/Mediawiki:HIP

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

Source: %oname-%version.tar

%description
The HIP extension adds the <hip> (inline) and <hiptext> (block) tags that
convert Church Slavonic text typed in the HIP encoding to the code points
of the Church Slavonic UCS fonts.

The fonts are not a part of the package: the site connects them itself
with @font-face and applies them to the .hip and .hiptext classes.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{runtest.php,runtest.sh,runtest2.sh,HIP1Tests.*,HIP2Tests.*}

%files -f %oname.files

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for Sisyphus
