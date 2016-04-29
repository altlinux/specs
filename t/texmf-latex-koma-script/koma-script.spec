%define srcName koma-script
Name: 	  texmf-latex-%srcName
Version:  3.19
Release:  alt1.a

Summary:  KOMA-Script is a bundle of versatile LaTeX classes and packages
License:  %lppl
Group:    Other
Url: 	  http://www.komascript.de/

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-texmf rpm-build-licenses
BuildRequires: texlive-latex-base

BuildArch:noarch

%description
KOMA-Script provides drop-in replacements for the LaTeX standard classes
article, report, and book. These KOMA-Script classes scrartcl, scrreprt,
and scrbook are much more configurable than the standard classes.

Additionally, KOMA-Script provides a completely new designed letter
class that is also very versatil. Predefined setting (letter class
options) are available, e.g., for German letters, US-American
letters, Swiss letters, French letters, and Japanese letters.

There are several additional packages in KOMA-Script that may be used
with other classes too, e.g.:
- scrbase (basic features of the KOMA-Script classes)
- tocbasic (features for tables of contents and creating more floats)
- scrdate (date functions)
- scrtime (current time)
- scrlayer (virtual layers)
- scrlayer-scrpage (page style configuration)
- typearea (semi-automatic typing area and margin setup)
- scrextend (extended features of the KOMA-Script classes)

%prep
%setup

%build

%install
mkdir -p %buildroot%_texmfmain
#ctanify --pkgname=%srcName --tdsdir=%buildroot/%_texmfmain *
cp -ar . %buildroot/%_texmfmain/

%files
%_texmfmain/tex/latex/*
%_texmfmain/source/latex/*
%_texmfmain/doc/latex/*

%changelog
* Fri Apr 29 2016 Denis Medvedev <nbr@altlinux.org> 3.19-alt1.a
Initial release
