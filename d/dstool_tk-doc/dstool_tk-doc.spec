Summary: documents for dstooltk
Name: dstool_tk-doc
Version: 2.0
Release: alt6
License: Custom
Group: Sciences/Mathematics
Packager: Igor Vlasenko <viy@altlinux.org>
BuildArch: noarch
Url: http://www.geom.uiuc.edu/software/dstool
Source0: dstooltk-doc_2.0.orig.tar.gz
Patch0: dstooltk-doc_2.0-3.diff.gz

%if_with regen_html
BuildRequires: latex2html
%endif
BuildRequires: tex(latex) tex(float.sty) tex(dehypht.tex) tex(bbm.sty)
#texmf(latex/bbm)

%description
dstooltk is a tool for the investigation of dynamical systems. This
 package contains documentation for dstool.  This concerns the tk
 front end.  There is also a package with an xview front end. The
 package and additional docs are dstool and dstool-doc.

%prep
%setup -n ds_doc
%patch0 -p1

%build
cd userman;  latex userman ;  latex userman; dvips -o userman.ps userman.dvi
rm userman.ps.gz
gzip -9 userman.ps
cd ..
%if_with regen_html
# results are included in tarball
# rebuild
rm -rf html/*
latex2html -dir html userman
%endif

%files
%doc debian/copyright
%doc userman/userman.ps.gz
#if_with html
%doc html
#endif

%changelog
* Tue Jun 29 2021 Igor Vlasenko <viy@altlinux.org> 2.0-alt6
- resurrected in Sisyphus

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

