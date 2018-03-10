Name: yaplc-rte-source
Version: 1.1.0
Release: alt1.20180208

Summary: YAPLC runtime environment project
License: GPLv3+
Group: Development/Other
Url: https://github.com/nucleron/RTE

Packager: Anton Midyukov <antohami@altlinux.org>

Source: yaplc-rte-source-%version.tar

Buildarch: noarch

%description
YAPLC/RTE can run user aplications made with YAPLC/IDE.
It runs on bare metal without any OS. It is small and portable.

%prep
%setup
rm -fr .gear

%build

%install
mkdir -p %buildroot%_prefix/src/yaplc-rte
cp -r * %buildroot%_prefix/src/yaplc-rte

%files
%_prefix/src/yaplc-rte

%changelog
* Sat Mar 10 2017 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1.20180208
- Initial build for ALT Sisyphus
