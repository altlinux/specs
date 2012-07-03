# vim: set ft=spec : -*- rpm-spec -*-

Name: splat
Version: 1.2.3
Release: alt1

Summary: RF Signal Propagation, Loss, And Terrain Analysis Tool
Group: Sciences/Other
License: GPLv2
Url: http://www.qsl.net/kd2bd/splat.html

Packager: Sir Raorn <raorn@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Tue Aug 26 2008
BuildRequires: bzlib-devel gcc-c++ zlib-devel

%description
SPLAT! is an RF Signal Propagation, Loss, And Terrain analysis
tool for the spectrum between 20 MHz and 20 GHz.

%prep
%setup
%patch -p1

%build
%__cxx %optflags itm.cpp splat.cpp -o splat -lm -lbz2
pushd utils
  for utl in citydecoder srtm2sdf usgs2sdf fontdata bearing; do
    %__cc %optflags "$utl.c" -o "$utl" -lm -lbz2 -lz
  done
popd

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -p -m755 splat %buildroot%_bindir/splat
install -p -m644 docs/english/man/splat.man %buildroot%_man1dir/splat.1
pushd utils
  for utl in citydecoder srtm2sdf usgs2sdf fontdata bearing; do
    install -p -m755 "$utl" %buildroot%_bindir/"$utl"
  done
popd
cp utils/README README.utils

%files
%doc README README.utils sample_data docs/english/pdf/splat.pdf docs/english/text/splat.txt
%_bindir/*
%_man1dir/*.1*

%changelog
* Tue Aug 26 2008 Sir Raorn <raorn@altlinux.ru> 1.2.3-alt1
- Built for Sisyphus

