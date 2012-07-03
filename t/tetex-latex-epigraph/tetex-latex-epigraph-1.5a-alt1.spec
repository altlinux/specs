%define pname epigraph
Name: tetex-latex-%pname
Version: 1.5a
Release: alt1.1
Summary: Typesetting epigraphs for LaTeX
License: Latex Project Public License 1.3 or later
Group: Publishing
URL: http://www.ctan.org/tex-archive/macros/latex/contrib/%pname
Source: %url-%version.tar
BuildArch: noarch
Requires: tetex-latex

# Automatically added by buildreq on Fri Jul 04 2008 (-bi)
BuildRequires: tetex-latex

%description 
The %pname package is designed for typesetting epigraphs - the pithy
quotations often found at the start (or end) of a chapter. Both single
epigraphs and lists of epigraphs are catered for.

%prep
%setup -n %pname-%version


%build
latex %pname.ins


%install
install -D -m 0644 {,%buildroot%_datadir/texmf/tex/latex/%pname/}%pname.sty


%files
%doc README *.pdf
%_datadir/texmf/tex/latex/%pname


%changelog
* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.5a-alt1.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-epigraph

* Fri Jul 04 2008 Led <led@altlinux.ru> 1.5a-alt1
- initial build
