Name: yaplc_demos
Version: 2017.10.27
Release: alt1

Summary: DEMO project for PTA-2017 (Moscow)
License: MIT
Group: Development/Other
Url: https://github.com/nucleron/YAPLC_DEMOS

Packager: Anton Midyukov <antohami@altlinux.org>

Source: yaplc_demos-%version.tar

Buildarch: noarch

%description
DEMO project for PTA-2017 (Moscow)

%prep
%setup
rm -fr .gear

%build

%install
mkdir -p %buildroot%_docdir/YAPLC_DEMOS
cp -r * %buildroot%_docdir/YAPLC_DEMOS

%files
%_docdir/YAPLC_DEMOS

%changelog
* Sat Mar 10 2017 Anton Midyukov <antohami@altlinux.org> 2017.10.27-alt1
- Initial build for ALT Sisyphus
