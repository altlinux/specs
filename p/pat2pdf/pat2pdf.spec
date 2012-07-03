Name: pat2pdf
Version: 1.32
Release: alt1

Summary: Retrieve USPTO patents as TIFF and convert to PDF
License: GPL
Group: Office

Url: http://tothink.com/pat2pdf/
Source: %url/%name
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%description
This script connects to the USPTO patent database, retrieves the TIFF
patent images and converts them into a single pdf file using libtiff.

%prep
%build
%install
install -pDm755 %SOURCE0 %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Tue Jul 07 2009 Michael Shigorin <mike@altlinux.org> 1.32-alt1
- initial packaging
