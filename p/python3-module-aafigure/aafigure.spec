Name: python3-module-aafigure
Version: 0.6
Release: alt1
Url: https://pypi.org/project/aafigure
Summary: ASCII art to image conversion
Group: Development/Python3
License: BSD
Source: aafigure-%version.tar.gz
BuildArch: noarch

BuildREquires(pre): python3-devel

%description
The original idea was to parse ASCII art images, embedded in reST
documents and output an image. This would mean that simple illustrations
could be embedded as ASCII art in the reST source and still look nice
when converted to e.g. HTML.

aafigure can be used to write documents that contain drawings in plain
text documents and these drawings are converted to appropriate formats
for e.g. HTML or PDF versions of the same document.

Since then aafigure also grew into a standalone application providing
a command line tool for ASCII art to image conversion.

%prep
%setup -n aafigure-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/*
%_bindir/*

%changelog
* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 0.6-alt1
- Autobuild version bump to 0.6

* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Initial commit for ALT
