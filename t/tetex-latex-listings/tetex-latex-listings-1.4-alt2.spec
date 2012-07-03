%define pname listings
Name: tetex-latex-%pname
Version: 1.4
Release: alt2.1
Summary: Typeset source code listings using LaTeX
License: LaTeX Project Public License 1.3 or later
Group: Publishing
URL: http://www.ctan.org/tex-archive/macros/latex/contrib/%pname
Source: %url-%version.tar
BuildArch: noarch
Requires: tetex-latex

BuildRequires: tetex-latex

%description 
The `%pname' package is a source code printer for LaTeX. You can
typeset stand alone files as well as listings with an environment
similar to `verbatim' as well as you can print code snippets using a
command similar to \verb'. Many parameters control the output and if
your preferred programming language isn't already supported, you can
make your own definition.


%prep
%setup -n %pname-%version


%build
%make_build


%install
install -d -m 0755 %buildroot%_datadir/texmf/tex/latex/%pname
install -m 0644 *.sty *.cfg %buildroot%_datadir/texmf/tex/latex/%pname/


%files
%doc README *.pdf
%_datadir/texmf/tex/latex/%pname


%changelog
* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.4-alt2.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-listings

* Wed Jul 09 2008 Led <led@altlinux.ru> 1.4-alt2
- added %pname.cfg (#10691)

* Fri Jul 04 2008 Led <led@altlinux.ru> 1.4-alt1
- 1.4
- fixed License (#16262)
- fixed %%files (#16264)

* Sun Aug 28 2005 Vladimir Lettiev <crux@altlinux.ru> 1.3-alt1
- Initial build for ALT Linux Sisyphus

