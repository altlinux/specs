Name: textext
Version: 0.4.4
Release: alt3

Summary: Editable LaTeX objects for Inkscape
License: BSD
Group: Graphics
Url: http://www.elisanet.fi/ptvirtan/software/textext/

BuildArch: noarch

Source0: %name-%version.tar.lzma
Source44: import.info
Patch33: textext-0.4.4-python2.6.patch
Patch34: textext-0.4.4-port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-tools

%add_python3_req_skip inkex

Requires: inkscape >= 0.46 /usr/bin/latex texlive-latex-recommended python3-module-lxml
# Earlier revisions of pstoedit were not compiled with plot-svg support:
Requires: pstoedit >= 3.45-5mdv2008.0

%description
Textext is an extension for Inkscape that allows one to insert text
typeset with LaTeX into one's graphics. Unlike similar extensions such
as Inklatex, Textext provides the ability to edit LaTeX objects after
creation.

%prep
%setup -c %name-%version
%patch33 -p0
%patch34 -p1
sed -i 1s,python,python3, textext.py

$(find /usr/*/python%_python3_version/Tools/scripts/reindent.py) textext.py

%install
rm -rf %buildroot
mkdir -p %buildroot%_datadir/inkscape/extensions

install -m 644 textext.inx %buildroot%_datadir/inkscape/extensions/
install -m 755 textext.py %buildroot%_datadir/inkscape/extensions/

%files
%_datadir/inkscape/extensions/textext.*

%changelog
* Fri Jan 20 2023 Igor Vlasenko <viy@altlinux.org> 0.4.4-alt3
- fixed build

* Wed Mar 25 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.4-alt2
- Porting to python3.

* Sun Jan 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_3
- fixed build

* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_2
- import from Mandriva 2011

