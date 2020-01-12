%filter_from_requires /^python....inkex./d
%define name textext
%define version 0.4.4
%define release 2

Summary: Editable LaTeX objects for Inkscape
Name: 	 %{name}
Version: %{version}
Release: alt1_3
Source0: %{name}-%{version}.tar.lzma
License: BSD
Group: 	 Graphics
Url: 	 http://www.elisanet.fi/ptvirtan/software/textext/
BuildArch: noarch
Requires: inkscape >= 0.46 /usr/bin/latex texlive-latex-recommended python-module-lxml
# Earlier revisions of pstoedit were not compiled with plot-svg support:
Requires: pstoedit >= 3.45-5mdv2008.0
Source44: import.info
Patch33: textext-0.4.4-python2.6.patch

%description
Textext is an extension for Inkscape that allows one to insert text
typeset with LaTeX into one's graphics. Unlike similar extensions such
as Inklatex, Textext provides the ability to edit LaTeX objects after
creation.

%prep
%setup -q -c %{name}-%{version}
%patch33 -p0
sed -i 1s,python,python2, textext.py

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/inkscape/extensions

install -m 644 textext.inx %{buildroot}%{_datadir}/inkscape/extensions/
install -m 755 textext.py %{buildroot}%{_datadir}/inkscape/extensions/

%files
%{_datadir}/inkscape/extensions/textext.*


%changelog
* Sun Jan 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_3
- fixed build

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_2
- import from Mandriva 2011

