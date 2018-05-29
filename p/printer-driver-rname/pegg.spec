%define rname pegg

Summary: CUPS printer drivers for Casio USB label printers
Name: printer-driver-rname
Version: 0.23
Release: alt1
License: GPLv2
Group: System/Configuration/Printing
Url: http://printer.konicaminolta.net/
# site is dead
Source: %rname-%version.tar
Source1: xbm2crw-0.4.tar
Source2: cups2pegg-0.21a.tar
Source3: pegg_el-0.11.tar
Patch1: cups-drivers-pegg-0.23-LDFLAGS.patch

BuildRequires: libusb-compat-devel
Requires: cups ImageMagick-tools

%description
CUPS printer drivers for Casio USB label printers.

This package contains CUPS drivers (PPD) for the following printers:

 o CASIO Computer CO. LTD. EL-700 EL-5000W
 o CASIO Computer CO. LTD. KL-P1000 KL-E11
 o CASIO Computer CO. LTD. KP-C10 KP-C50

%prep
%setup -c -T -n %rname-%version -a0 -a1 -a2 -a3
%patch1 -p1

# gunzip the man pages
find -name "*.1.gz" | xargs gunzip

%build
%make -C pegg-* CFLAGS="%optflags" LIB_PATH="%_libdir"
%make -C pegg_el-*/src CFLAGS="%optflags" LIB_PATH="%_libdir"

# Suppress logging in cups2pegg backend
perl -p -i -e "s:/var/log/cups/cups2pegg.log:/dev/null:" cups2pegg*/src/cups2pegg

# Fix PPD file
perl -p -i -e 's/^(\*ModelName:).*$/$1 "CASIO Computer CO. LTD. EL-700 EL-5000W"/' cups2pegg-*/src/ppd/casio_el.ppd
perl -p -i -e 's/^(\*ShortNickName:).*$/$1 "CASIO EL-700 EL-5000W"/' cups2pegg-*/src/ppd/casio_el.ppd
perl -p -i -e 's/^(\*ModelName:).*$/$1 "CASIO Computer CO. LTD. KL-P1000 KL-E11"/' cups2pegg-*/src/ppd/casio_kl.ppd
perl -p -i -e 's/^(\*ShortNickName:).*$/$1 "CASIO KL-P1000 KL-E11"/' cups2pegg-*/src/ppd/casio_kl.ppd
perl -p -i -e 's/: Letter/: 128_64/' cups2pegg-*/src/ppd/casio_kl.ppd
perl -p -i -e 's/^(\*ModelName:).*$/$1 "CASIO Computer CO. LTD. KP-C10 KP-C50"/' cups2pegg-*/src/ppd/casio_kp.ppd
perl -p -i -e 's/^(\*ShortNickName:).*$/$1 "CASIO KP-C10 KP-C50"/' cups2pegg-*/src/ppd/casio_kp.ppd
perl -p -i -e 's/: Letter/: 512_64/' cups2pegg-*/src/ppd/casio_kp.ppd

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir/cups/backend
install -d %buildroot%_datadir/cups/model/pegg
install -d %buildroot%_man1dir

install -m0755 pegg-*/pegg %buildroot%_bindir/
install -m0755 pegg_el-*/src/pegg_el %buildroot%_bindir/
install -m0755 xbm2crw*/xbm2crw %buildroot%_bindir/
install -m0755 cups2pegg*/src/cups2pegg %buildroot%_libdir/cups/backend/
install -m0644 pegg-*/pegg.1 %buildroot%_man1dir/
install -m0644 pegg_el-*/src/pegg_el.1 %buildroot%_man1dir/
install -m0644 cups2pegg-*/src/ppd/*.ppd* %buildroot%_datadir/cups/model/pegg/

rm -rf installed_docs
mkdir -p installed_docs/{pegg_el,xbm2crw,cups2pegg}
cp pegg_el-*/README pegg_el-*/TODO pegg_el-*/INSTALL installed_docs/pegg_el/
cp xbm2crw-*/README installed_docs/xbm2crw/
cp cups2pegg-*/*.png cups2pegg-*/*.html installed_docs/cups2pegg/

%files
%doc pegg-*/CHANGELOG pegg-*/README pegg-*/LICENSE pegg-*/INSTALL installed_docs/*
%_bindir/pegg
%_bindir/pegg_el
%_bindir/xbm2crw
%_libdir/cups/backend/cups2pegg
%dir %_datadir/cups/model/pegg
%_datadir/cups/model/pegg/*.ppd*
%_man1dir/pegg*.1*

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 0.23-alt1
- Initial build for ALT

