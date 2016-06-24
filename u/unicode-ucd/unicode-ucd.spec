%define unicodedir %_datadir/unicode
%define ucddir %unicodedir/ucd

Name: unicode-ucd
Version: 9.0.0
Release: alt1

Summary: Unicode Character Database
Group: Development/Other
License: MIT
Url: http://www.unicode.org/ucd/

Source: http://www.unicode.org/Public/zipped/%version/UCD.zip
Source1: http://www.unicode.org/Public/%version/ucd/Unihan.zip
# http://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source2: http://www.unicode.org/copyright.html

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
* Fri Jun 24 2016 Yuri N. Sedunov <aris@altlinux.org> 9.0.0-alt1
- 9.0.0

* Tue Apr 05 2016 Yuri N. Sedunov <aris@altlinux.org> 8.0.0-alt1
- first build for sisyphus

