Name: pfscalibration
Version: 1.5
Release: alt1

Summary: Photometric calibration of HDR and LDR cameras
License: GPLv2+
Group: Graphics

Url: http://www.mpi-inf.mpg.de/resources/hdr/calibration/pfs.html
Source: http://downloads.sourceforge.net/pfstools/pfscalibration-%version.tar.gz

# Automatically added by buildreq on Sat Mar 12 2011
BuildRequires: gcc-c++ libpfs-devel

%description
A photographic camera with a standard CCD sensor is able to acquire an image
with simultaneous dynamic range of not more than 1:1000. The basic idea to
create an image with a higher dynamic range is to combine multiple images with
different exposure settings, thus making use of available sequential dynamic
range.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Sat Mar 12 2011 Victor Forsiuk <force@altlinux.org> 1.5-alt1
- 1.5

* Fri Aug 22 2008 Victor Forsyuk <force@altlinux.org> 1.4-alt1
- 1.4

* Thu Jun 07 2007 Victor Forsyuk <force@altlinux.org> 1.3-alt1
- Initial build.
