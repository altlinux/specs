Summary: documents for dstooltk
Name: dstool_tk-doc
Version: 2.0
Release: alt5
License: Custom
Group: Sciences/Mathematics
Packager: Igor Vlasenko <viy@altlinux.org>
BuildArch: noarch
Url: http://www.geom.uiuc.edu/software/dstool
Source0: dstooltk-doc_2.0.orig.tar.gz
Patch0: dstooltk-doc_2.0-3.diff.gz

# Automatically added by buildreq on Wed May 14 2008 (-bi)
BuildRequires: texlive-base-bin latex2html
BuildRequires: texmf(latex/float) 
#texmf(latex/bbm)
#packagereq: optimized out: fontconfig ghostscript-classic ghostscript-common libgpg-error netpbm perl-DBM tetex-core tetex-dvips tetex-latex xorg-x11-rgb

%description
dstooltk is a tool for the investigation of dynamical systems. This
 package contains documentation for dstool.  This concerns the tk
 front end.  There is also a package with an xview front end. The
 package and additional docs are dstool and dstool-doc.

%prep
%setup -n ds_doc
%patch0 -p1

%build
# results are included in tarball
# rebuild
rm -rf html/*
cd userman;  latex userman ;  latex userman; dvips -o userman.ps userman.dvi
rm userman.ps.gz
gzip -9 userman.ps
latex2html -dir ../html userman

%files
%doc debian/copyright
%doc html
%doc userman/userman.ps.gz

%changelog
* Mon Jan 04 2010 Igor Vlasenko <viy@altlinux.ru> 2.0-alt5
- fixed build

* Thu Aug 06 2009 Igor Vlasenko <viy@altlinux.org> 2.0-alt4
- updated build requires

* Fri Jul 24 2009 Igor Vlasenko <viy@altlinux.org> 2.0-alt3
- fixed latex dependencies

* Wed May 14 2008 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2
- refreshed buildreq

* Sat Oct 22 2005 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1
- first build

