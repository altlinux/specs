%define unicodedir %_datadir/unicode
%define ucddir %unicodedir/ucd

Name: unicode-ucd
Version: 16.0.0
Release: alt1

Summary: Unicode Character Database
Group: Development/Other
License: MIT
Url: https://www.unicode.org/ucd/

Source: https://www.unicode.org/Public/zipped/%version/UCD.zip
Source1: https://www.unicode.org/Public/%version/ucd/Unihan.zip
# https://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source2: https://www.unicode.org/copyright.html

BuildArch: noarch

BuildRequires: unzip

%description
The Unicode Character Database (UCD) consists of a number of data files listing
Unicode character properties and related data. It also includes data files
containing test data for conformance to several important Unicode algorithms.

%prep
%setup -c -a1

grep -q "%version" ReadMe.txt || (echo "zip file seems not %version" ; exit 1)

%install
mkdir -p %buildroot%ucddir
cp -ar . %buildroot%ucddir
# gucharmap requires zipped Unihan for build
cp -p %SOURCE1 %buildroot%ucddir
cp -p %SOURCE2 .

%files
%dir %unicodedir
%ucddir/
%doc copyright.html

%changelog
* Wed Sep 11 2024 Yuri N. Sedunov <aris@altlinux.org> 16.0.0-alt1
- 16.0.0

* Mon Sep 04 2023 Yuri N. Sedunov <aris@altlinux.org> 15.1.0-alt1
- 15.1.0

* Thu Sep 22 2022 Yuri N. Sedunov <aris@altlinux.org> 15.0.0-alt1
- 15.0.0

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 14.0.0-alt1
- 14.0.0

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 13.0.0-alt1
- 13.0.0

* Sat May 11 2019 Yuri N. Sedunov <aris@altlinux.org> 12.1.0-alt1
- 12.1.0

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 12.0.0-alt1
- 12.0.0

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 11.0.0-alt1
- 11.0.0

* Wed Jun 21 2017 Yuri N. Sedunov <aris@altlinux.org> 10.0.0-alt1
- 10.0.0

* Fri Jun 24 2016 Yuri N. Sedunov <aris@altlinux.org> 9.0.0-alt1
- 9.0.0

* Tue Apr 05 2016 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt1
- first build for sisyphus

