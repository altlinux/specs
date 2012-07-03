Name: diffpdf
Version: 2.1.1
Release: alt1
License: GPLv2
Summary: Visually compare two PDF files
Group: Publishing
Url: http://www.qtrac.eu/diffpdf.html
Source: %name-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: fontconfig libpoppler3-qt4 libqt4-core libqt4-devel libqt4-gui libqt4-xml libstdc++-devel
BuildRequires: gcc-c++ libpoppler-qt4-devel phonon-devel libpoppler-cpp-devel

%description
By default the comparison is of the text on each pair of pages, but
comparing the appearance of pages is also supported (for example, if a
diagram is changed or a paragraph reformatted). It is also possible to
compare particular pages or page ranges. For example, if there are two
versions of a PDF file, one with pages 1-12 and the other with pages
1-13 because of an extra page having been added as page 4, they can be
compared by specifying two page ranges, 1-12 for the first and 1-3, 5-13
for the second. This will make DiffPDF compare pages in the pairs (1,
1), (2, 2), (3, 3), (4, 5), (5, 6), and so on, to (12, 13).

%prep
%setup
cat >> README <<@@@

Although %name is commandline utility, it uses Qt4 much,
so one need a \$DISPLAY set properly to operate.
You can use %name without real X server hardware via xvfb like this:
$ xvfb-run %name <parameters>
@@@

# XXX Hack out missing cz translation
# sed -i '/_cz/d' resources.qrc

%build
lrelease-qt4 diffpdf.pro
qmake-qt4
%make


%install
install -D %name %buildroot%_bindir/%name
install -D %name.1 %buildroot%_man1dir/%name.1

%files
%doc README CHANGES
%_bindir/*
%_man1dir/*

%changelog
* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 2.1.1-alt1
- Autobuild version bump to 2.1.1

* Thu Apr 19 2012 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Autobuild version bump to 1.9.2
- Remove missing CZ translation

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Autobuild version bump to 1.8.0

* Tue Oct 11 2011 Fr. Br. George <george@altlinux.ru> 1.2.2-alt1
- Initial build from scratch

