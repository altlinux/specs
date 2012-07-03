Name:		SNNS-Manual
Version:	4.2
Release:	alt2
Summary:	Printable documentation for Stuttgart Neural Network Simulator
Group:		Sciences/Computer science
License:	LGPL
Url:		http://www.ra.cs.uni-tuebingen.de/SNNS
Source0:	http://www.ra.cs.uni-tuebingen.de/downloads/SNNS/SNNSv%version.Manual.src.tar.gz
Patch:		SNNSv4.2.Manual.patch
Packager:	Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Mon Mar 01 2010
BuildRequires: fonts-type1-cm-super-pfb ghostscript-classic texlive-pictures

%description
Printable documentation for Stuttgart Neural Network Simulator

%prep
%setup -n userman
%patch -p1

%build
latex UserManual.tex < /dev/null || :
makeindex UserManual
bibtex UserManual
latex UserManual
latex UserManual
latex UserManual
dvips UserManual.dvi -o UserManual.ps
# this doesn't work in texlive
dvipdfm -o UserManual.pdf UserManual.dvi

%install
mkdir -p %buildroot

%files
%doc UserManual.pdf UserManual.ps UserManual.dvi README

%changelog
* Mon Mar 01 2010 Fr. Br. George <george@altlinux.ru> 4.2-alt2
- Use more accurate dependencies
- Enable PDF version

* Fri Oct 09 2009 Fr. Br. George <george@altlinux.ru> 4.2-alt1
- Initial build from scratch

