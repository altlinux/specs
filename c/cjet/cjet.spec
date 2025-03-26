Summary: Cjet PCL emulation for Canon CaPSL printers

Name: cjet
Version: 0.8.9
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

License: GPL-2
Group: Publishing
URL: ftp://metalab.unc.edu/pub/Linux/system/printing/
Source: ftp://metalab.unc.edu/pub/Linux/system/printing/cjet089.tar
Patch0: cjet-add-include.patch

%description
CJET filters printer data from stdin to stdout, converting HP PCL (Printer
Command Language) commands to their CaPSL equivalents.
CaPSL is short for `Canon Printing Systems Language'.
Whereas PCL is a de-facto world-wide standard as a laser and inkjet printer
control language, CaPSL is limited to Canon laser printers.

%prep
%setup -q -n %{name}089
%patch -p0

%build
make OPT="%optflags"

%install
%__install -Dpm755 cjet %buildroot/%_bindir/cjet

%files
%doc README INSTALL COPYING TODO ChangeLog samples/
%_bindir/*

%changelog
* Wed Mar 26 2025 Andrew A. Vasilyev <andy@altlinux.org> 0.8.9-alt2
- NMU: fix FTBFS with gcc14

* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.8.9-alt1
- Initial build

