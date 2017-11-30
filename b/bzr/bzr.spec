# vim: set ft=spec: -*- rpm-spec -*-

# check runs 'bzr selftest' that requires network to success
# export share_network=1 before gear-hsh
%def_without check

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: bzr
Version: 2.7.0
Release: %branch_release alt3.bzr20170317

Summary: Bazaar is a decentralized revision control system
License: %gpl2plus
Group: Development/Other

Url: http://bazaar-vcs.org
Packager: Anatoly Kitaykin <cetus@altlinux.ru>

Source: %name-%version.tar

Patch0: %name-%version.patch

%add_python_req_skip launchpadlib
%add_python_req_skip lazr

Conflicts: %name-doc < %version

BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu Aug 20 2009 (-bi)
BuildRequires: python-module-Pyrex python-modules-compiler python-modules-email python-modules-logging zlib-devel

%{?!__buildreqs:%{?!_without_check:%{?!_without_test:%{?!_disable_check:%{?!_disable_test:BuildRequires: python-module-docutils}}}}}
%{?!__buildreqs:%{?!_without_check:%{?!_without_test:%{?!_disable_check:%{?!_disable_test:BuildRequires: python-module-paramiko}}}}}
%{?!__buildreqs:%{?!_without_check:%{?!_without_test:%{?!_disable_check:%{?!_disable_test:BuildRequires: python-module-testtools}}}}}
%{?!__buildreqs:%{?!_without_check:%{?!_without_test:%{?!_disable_check:%{?!_disable_test:BuildRequires: python-module-python-subunit-tests}}}}}

%description
Bazaar is a distributed version control system that Just Works. While
many similar systems require you to adapt to their model of working,
Bazaar adapts to the workflows you want to use, and it takes only five
minutes to try it out. People have used it to version pretty much
anything: single-file projects, your /etc directory and even the
thousands of files and revisions in the source code for Launchpad,
MySQL and Mailman.

%package -n python-module-bzrlib-tests
Summary: Tools for testing Bazaar
Group: Development/Other

Requires: %name = %version-%release
Provides: bzr-selftest = %version-%release

%description -n python-module-bzrlib-tests
This package contain tools and test suites for testing Bazaar.

%package doc
Summary: %name documentation and examples
Group: Development/Other
BuildArch: noarch

Conflicts: %name < %version

%description doc
Bazaar is a decentralized revision control system. This
package contain documentation and examples for using Bazaar.

%define bzr_docdir %_docdir/%name-%version

%prep
%setup
%patch0 -p1

%build
%add_optflags -fno-strict-aliasing
%python_build

%install
#define _compress_method none
%python_install --install-data=%_datadir
install -dm0755 %buildroot%bzr_docdir
install -m0644 BRANCH.TODO INSTALL NEWS README TODO %buildroot%bzr_docdir
cp -a doc contrib %buildroot%bzr_docdir
# Hack! Need a subst in setup.py
mv %buildroot%_datadir/share/locale %buildroot%_datadir
%find_lang %name

%check
%make_build check

%files -f %name.lang
%_bindir/bzr
%_man1dir/bzr.*
%python_sitelibdir/*
%exclude %python_sitelibdir/bzrlib/tests
%exclude %python_sitelibdir/bzrlib/plugins/*/tests
%exclude %python_sitelibdir/bzrlib/util/tests
%bzr_docdir
%exclude %bzr_docdir/doc
%exclude %bzr_docdir/contrib
#%%_datadir/locale/*/LC_MESSAGES/bzr.mo

%files -n python-module-bzrlib-tests
%dir %python_sitelibdir/bzrlib
%dir %python_sitelibdir/bzrlib/plugins
%dir %python_sitelibdir/bzrlib/plugins/bash_completion
%dir %python_sitelibdir/bzrlib/plugins/changelog_merge
%dir %python_sitelibdir/bzrlib/plugins/grep
%dir %python_sitelibdir/bzrlib/plugins/launchpad
%dir %python_sitelibdir/bzrlib/plugins/netrc_credential_store
%dir %python_sitelibdir/bzrlib/plugins/news_merge
%dir %python_sitelibdir/bzrlib/plugins/po_merge
%dir %python_sitelibdir/bzrlib/plugins/weave_fmt
%dir %python_sitelibdir/bzrlib/util
%python_sitelibdir/bzrlib/tests
%python_sitelibdir/bzrlib/plugins/*/tests
%python_sitelibdir/bzrlib/util/tests
# bash_completion changelog_merge grep launchpad netrc_credential_store news_merge po_merge weave_fmt

%files doc
%dir %bzr_docdir
%bzr_docdir/doc
%bzr_docdir/contrib

%changelog
* Thu Nov 30 2017 Anatoly Kitaykin <cetus@altlinux.org> 2.7.0-alt3.bzr20170317
- Bugfix upgrade to trunk

* Wed Mar 02 2016 Anatoly Kitaykin <cetus@altlinux.org> 2.7.0-alt2
- Restored branch_release

* Mon Feb 29 2016 Anatoly Kitaykin <cetus@altlinux.org> 2.7.0-alt1
- 2.7.0 release

* Thu Oct 03 2013 Anatoly Kitaykin <cetus@altlinux.org> 2.6.0-alt2
- plugins and util tests also moved into bzrlib-tests
- find_langs policy applied

* Fri Aug 09 2013 Anatoly Kitaykin <cetus@altlinux.org> 2.6.0-alt1
- 2.6.0 release with typo fixes up to 2013-08-04

* Tue Oct 02 2012 Anatoly Kitaykin <cetus@altlinux.org> 2.5.1-alt1
- 2.5.1 release

* Tue Jul 03 2012 Anatoly Kitaykin <cetus@altlinux.org> 2.5.0-alt2
- fixed search for SSL CA certificates (Closes: 27138)

* Thu Mar 15 2012 Anatoly Kitaikin <cetus@altlinux.org> 2.5.0-alt1
- 2.5.0 release

* Sun Jan 01 2012 Anatoly Kitaikin <cetus@altlinux.org> 2.4.1-alt1
- 2.4.1 release

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.4-alt2.1
- Rebuild with Python-2.7

* Sat Oct 15 2011 Anatoly Kitaikin <cetus@altlinux.org> 2.3.4-alt2
- Corrections and ajustments

* Thu Sep 22 2011 Anatoly Kitaikin <cetus@altlinux.org> 2.3.4-alt1
- 2.3.4 release

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1.1
- Rebuilt for debuginfo

* Wed Aug 11 2010 Aleksey Avdeev <solo@altlinux.ru> 2.0.5-alt1
- 2.0.5 release
- Create %%name-doc and python-module-%%{name}lib-tests subpackages.
  (Closes: 23194)

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.1
- Rebuilt with python 2.6

* Tue Oct 13 2009 Aleksey Avdeev <solo@altlinux.ru> 2.0.0-alt1
- 2.0.0 release

* Sun Oct 11 2009 Aleksey Avdeev <solo@altlinux.ru> 1.17-alt1
- 1.17 release

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 1.10-alt2
- 1.10rc1 -> 1.10 release

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.10-alt1
- 1.9 release -> 1.10rc1

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.9-alt1
- 1.7.1 release -> 1.9 release
- buildreq

* Fri Oct 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Thu May 22 2008 Igor Zubkov <icesik@altlinux.org> 1.5-alt2
- 1.5rc1 -> 1.5 release

* Sat May 10 2008 Igor Zubkov <icesik@altlinux.org> 1.5-alt1
- 1.4 release -> 1.5rc1

* Fri May 02 2008 Igor Zubkov <icesik@altlinux.org> 1.4-alt3
- 1.4rc2 -> 1.4 release

* Wed Apr 23 2008 Igor Zubkov <icesik@altlinux.org> 1.4-alt2
- 1.4rc1 -> 1.4rc2

* Wed Apr 16 2008 Igor Zubkov <icesik@altlinux.org> 1.4-alt1
- 1.3.1 release -> 1.4rc1

* Tue Apr 15 2008 Igor Zubkov <icesik@altlinux.org> 1.3.1-alt1
- 1.3 release -> 1.3.1 release

* Fri Mar 21 2008 Igor Zubkov <icesik@altlinux.org> 1.3-alt2
- 1.3rc1 -> 1.3 release

* Sun Mar 16 2008 Igor Zubkov <icesik@altlinux.org> 1.3-alt1.rc1
- 1.2 release -> 1.3rc1

* Sun Feb 24 2008 Igor Zubkov <icesik@altlinux.org> 1.2-alt1
- 1.1 release -> 1.2 release

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 1.1-alt2.1
- Rebuilt with python-2.5.

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 1.1-alt2
- 1.1rc1 -> 1.1 release

* Sun Jan 06 2008 Igor Zubkov <icesik@altlinux.org> 1.1-alt1.rc1
- 1.0 -> 1.1rc1

* Tue Dec 18 2007 Igor Zubkov <icesik@altlinux.org> 1.0-alt2
- 1.0rc3 -> 1.0 release

* Tue Dec 18 2007 Igor Zubkov <icesik@altlinux.org> 1.0-alt1.rc3
- 1.0rc2 -> 1.0rc3

* Sun Dec 09 2007 Igor Zubkov <icesik@altlinux.org> 1.0-alt1.rc2
- 1.0rc1 -> 1.0rc2

* Sat Dec 01 2007 Igor Zubkov <icesik@altlinux.org> 1.0-alt1.rc1
- 0.92 -> 1.0rc1

* Tue Nov 13 2007 Igor Zubkov <icesik@altlinux.org> 0.92-alt2
- 0.92rc1 -> 0.92

* Tue Oct 30 2007 Igor Zubkov <icesik@altlinux.org> 0.92-alt1.rc1
- 0.91 -> 0.92rc1

* Wed Sep 26 2007 Igor Zubkov <icesik@altlinux.org> 0.91-alt1
- 0.90 -> 0.91

* Tue Sep 11 2007 Igor Zubkov <icesik@altlinux.org> 0.90-alt1
- 0.18 -> 0.90
- buildreq

* Wed Jul 18 2007 Igor Zubkov <icesik@altlinux.org> 0.18-alt1
- 0.14 -> 0.18
- move doc and contrib to bzr package (no more bzr-doc)
- buildreq

* Thu Mar 01 2007 Igor Zubkov <icesik@altlinux.org> 0.14-alt1
- 0.7 -> 0.14
- buildarch -> noarch
- buildreq

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.7-alt1.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Mon Apr 03 2006 Andriy Stepanov <stanv@altlinux.ru> 0.7-alt1
- Init build
