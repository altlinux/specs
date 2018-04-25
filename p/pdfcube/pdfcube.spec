Name:           pdfcube
Version:        0.0.5
Release:        alt4.svn20120708
Summary:        PDF presentation viewer with a spinning cube
Group:          Office
License:        GPL
URL:            http://code.100allora.it/pdfcube

# http://code.100allora.it/svn/pdfcube/trunk/
Source:        %name-%version.tar

BuildRequires: boost-program_options-devel gcc-c++ libGLUT-devel
BuildRequires: libgtkglext-devel libpoppler-glib-devel

%description
PDF Cube is an OpenGL API-based PDF viewer that adds a
compiz/Keynote-like spinning cube trasition effect to your PDF
presentations (including Latex, Beamer and Prosper). You can also zoom
on 5 predefined areas of any presentation page with a smooth zooming
effect.

%prep
%setup
rm -f m4/l*

%build
%autoreconf
%configure \
	--with-boost-program-options=boost_program_options-mt
%make_build

%install
%makeinstall_std

%files
%doc README ChangeLog COPYING AUTHORS
%_bindir/pdfcube

%changelog
* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.5-alt4.svn20120708
- Rebuilt with new boost.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.0.5-alt3.svn20120708.qa2
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.0.5-alt3.svn20120708.1
- rebuild with boost 1.57.0

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt3.svn20120708
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt2.svn20120708
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.svn20120708
- Version 0.0.5

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt2.svn20120218
- Rebuilt with Boost 1.49.0

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.svn20120218
- New snapshot

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.svn20111119
- Version 0.0.4

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt2
- Rebuilt with Boost 1.48.0

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.1.2
- Rebuilt with Boost 1.46.1 and for debuginfo

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1.1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.3-alt1.1
- rebuilt with new poppler

* Tue Dec 30 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.0.3-alt1
- new version

* Sat Oct 13 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.0.2-alt0.1.1
- Rebuilt due to libpoppler-glib.so.1 -> libpoppler-glib.so.2 soname change.

* Mon Jun 18 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.0.2-alt0.1
- first build

