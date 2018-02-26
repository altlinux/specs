%define pname synttree
Name: tetex-latex-%pname
Version: 1.4.1
Release: alt1.1
Summary: Typesetting syntactic trees for LaTeX
License: Latex Project Public License, 1.3a or later
Group: Publishing
URL: http://www.ctan.org/tex-archive/macros/latex/contrib/%pname
Source: %url-%version.tar
BuildArch: noarch
Requires: tetex-latex

# Automatically added by buildreq on Fri Jul 04 2008 (-bi)
BuildRequires: tetex-latex

%description 
The "%pname" package provides a simple way to typeset syntactic trees
as used in Chomsky's Generative Grammar.


%prep
%setup -n %pname-%version


%build
latex %pname.ins


%install
install -D -m 0644 {,%buildroot%_datadir/texmf/tex/latex/%pname/}%pname.sty


%files
%doc README
%_datadir/texmf/tex/latex/%pname


%changelog
* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.4.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-synttree

* Fri Jul 04 2008 Led <led@altlinux.ru> 1.4.1-alt1
- initial build
